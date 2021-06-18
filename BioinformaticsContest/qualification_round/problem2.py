from tqdm import tqdm
import concurrent.futures as cf

# Problem 2: Metabolite Annotation

def find_best_j_k(s, m, a):
    result = {'combo': '', 'delta': float('inf')}
    for j in range(0, len(m)):
        for k in range(0, len(a)):
            mass = m[j] + a[k]
            if mass > 0:
                delta = abs(s - mass)
                if delta < result['delta']:
                    result['delta'] = delta
                    result['combo'] = f'{j+1} {k+1}'
    return result

def annotate_metabolites(case):
    results = []
    l = len(case['s'])
    with tqdm(total=l, desc='Signals: ') as pbar:
        with cf.ProcessPoolExecutor(max_workers=7) as executor:
            futures = [executor.submit(find_best_j_k, case['s'][i], case['m'], case['a']) for i in range(0, l)]
            for future in cf.as_completed(futures):
                res = future.result()
                results.append(f'{res["combo"]}')
                pbar.update(1)
    return results


# zug zug exponential attempt ---------------------------------
# def annotate_metabolites(case):
#     results = []
#     for i in range(0, len(case['s'])):
#         result = {'combo': '', 'delta': float('inf')}
#         for j in range(0, len(case['m'])):
#             for k in range(0, len(case['a'])):
#                 mass = case['m'][j] + case['a'][k]
#                 if mass > 0:
#                     delta = abs(case['s'][i] - mass)
#                     if delta < result['delta']:
#                         result['delta'] = delta
#                         result['combo'] = f'{j+1} {k+1}'
#         results.append(f'{result["combo"]}')
#     return results
# ----------------------------------------------------------------

# flawed gradient descent attempt --------------------------------
# def test_combo(s, j, k):
#     if j and k and j+k > 0:
#         return abs(s-(j+k))
#     else:
#         return float('inf')

# def decend_gradient(s, m, a):
#     j,k = 0,0
#     done = False
#     while not done:
#         options = {
#             'current_square': test_combo(s, m[j], a[k]),
#             'step_right': float('inf'),
#             'step_down': float('inf'),
#             'step_diag': float('inf'),
#             }
#         space_to_right = j < len(m)-1
#         space_to_down = k < len(a)-1
#         if space_to_right:
#             options['step_right'] = test_combo(s, m[j+1], a[k])
#         if space_to_down:
#             options['step_down'] = test_combo(s, m[j], a[k+1])
#         if space_to_right and space_to_down:
#             options['step_diag']=  test_combo(s, m[j+1], a[k+1])

#         option = min(options, key=options.get)
#         if option == 'current_square':
#             return [option, m[j], a[k]]
#         elif option == 'step_right':
#             j += 1
#         elif option == 'step_down':
#             k += 1
#         elif option == 'step_diag':
#             j += 1
#             k += 1

# def annotate_metabolites(case):
#     sorted_m = sorted(case['m'], reverse=True)
#     sorted_m_2 = sorted(case['m'])
#     sorted_a = sorted(case['a'], reverse=True)

#     results = []
#     for i in range(0, len(case['s'])):
#         choice_1 = decend_gradient(case['s'][i], sorted_m, sorted_a,)
#         choice_2 = decend_gradient(case['s'][i], sorted_m_2, sorted_a,)
#         if choice_1[0] > choice_2[0]:
#             m_j = choice_1[1]
#             a_k = choice_1[2]
#         else:
#             m_j = choice_2[1]
#             a_k = choice_2[2]
#         j = case['m'].index(m_j) + 1
#         k = case['a'].index(a_k) + 1
#         results.append(f'{j} {k}')
#     return results

# multithreadded option
# def annotate_metabolites(case):
#     sorted_m = sorted(case['m'], reverse=True)
#     sorted_m_2 = sorted(case['m'])
#     sorted_a = sorted(case['a'], reverse=True)

#     results = []
#     with cf.ThreadPoolExecutor() as executor:
#         futures = [executor.submit(decend_gradient, case['s'][i], sorted_m, sorted_a) for i in range(0, len(case['s']))]
#         for future in list(tqdm(cf.as_completed(futures), total = len(futures))):
#             res = future.result()
#             m_j = res[1]
#             a_k = res[2]
#             j = case['m'].index(m_j) + 1
#             k = case['a'].index(a_k) + 1
#             results.append(f'{j} {k}')
#     return results
# -------------------------------------------------------------------------

