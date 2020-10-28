from bisect import insort

def sliding_window_median(lst, k):
    window = sorted(lst[:k])
    for num_to_remove, num in zip(lst, lst[k:]):
        print((window[k // 2] + window[~(k // 2)]) / 2.0)
        window.remove(num_to_remove)
        insort(window, num)



print(sliding_window_median([-1, 5, 13, 8, 2, 3, 3, 1], 3))