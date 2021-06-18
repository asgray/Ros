# Problem 3: Diagnosis
from numpy import array
from tqdm import tqdm
import concurrent.futures as cf

class Node:
    def __init__(self, index, info_content, parent):
        self.children = []
        self.index = index
        self.info_content = info_content
        self.parent = parent
    
    def PrintTree(self):
        print(f'{self.index}: {self.info_content}')
        if self.children:
            for child in self.children:
                child.PrintTree()
    
    def Insert(self, node):
        if node.parent == self.index:
            node.parent = self
            self.children.append(node)
        else:
            for child in self.children:
                child.Insert(node)
    
    def FindParents(self):
        path = [self.index]
        if self.parent is None:
            return [self.index]
        else:
            path += self.parent.FindParents()
            return path

# try to build tree bottom up using map
def build_tree(parents, ic_content):
    root = Node(1, 5, None)
    node_map = {1: root}
    with tqdm(total=len(parents), desc='Building Tree: ') as pbar:
        for i in range(0, len(parents)):
            parent = parents[i]
            new_node = Node(i+2, ic_content[i+1], parent)
            node_map[i+2] = new_node
            node_map[parent].Insert(new_node)
            pbar.update(1)
    return root, node_map

# strip nodes recovered in path from instance
def find_node_path(node_map, instance):
    total_nodes = set()
    for node in instance:
        if node not in total_nodes:
            parents = node_map[node].FindParents()
            for parent in parents:
                total_nodes.add(parent)
    # ic_vals = []
    # for node in total_nodes:
    #     ic_vals.append(node_map[node].index)
    # return sorted(ic_vals, reverse=True)
    return sorted(list(total_nodes), reverse=True)

def process_node_matrix(node_map, instances):
    matrix = []
    with tqdm(total=len(instances), desc='Finding Paths: ') as pbar:
        with cf.ProcessPoolExecutor(max_workers=7) as executor:
            futures = [executor.submit(find_node_path, node_map, instance) for instance in instances]
            for future in cf.as_completed(futures):
                res = future.result()
                matrix.append(res)
                pbar.update(1)
    
    final_matrix = array([[0]*len(node_map)]*len(instances))
    with tqdm(total=len(instances), desc='Finalizing Matrix: ') as pbar:
        for i in range(0, len(matrix)):
            for node in matrix[i]:
                final_matrix[i][node-1] = node_map[node].info_content
            final_matrix[i] = final_matrix[i][::-1]
            pbar.update(1)
    return final_matrix

def id_disease(disease_matrix, patient):
    for j in range(0, len(patient)):
        for i in range(0, len(disease_matrix)):
            ic_val = disease_matrix[i][j]
            if ic_val > 0 and ic_val in patient:
                return i+1
                