def permute(array, permutation):
    for i in range(len(array)):
        element = array[i]
        # which place to put element
        p = permutation[i]
        while p != i:
            # put element to array[p] and previous of array[p] assign to element
            array[p], element = element, array[p]
            # put p to permutation[p], previous of permutation[p] assign to p
            # p and element are ready to permute them
            permutation[p], p = p, permutation[p]

        array[i] = element
        permutation[i] = p
    return array


print(permute( ["a", "b", "c", "d"], [3, 0, 2, 1]))