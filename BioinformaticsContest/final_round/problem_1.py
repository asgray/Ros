import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def plot_distro(pos_array, neg_array):
    
    plt.scatter(pos_array, np.zeros_like(pos_array), c='green')
    plt.scatter(neg_array, np.zeros_like(neg_array), c='red', s=1)
    plt.show()