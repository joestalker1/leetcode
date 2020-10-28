def longest_contiguous_history(user1, user2):
    matrix = [[None for _ in range(len(user2) + 1)] for _ in range(len(user1) + 1)]

    for i in range(len(user1) + 1):
        matrix[i][0] = []

    for j in range(len(user2) + 1):
        matrix[0][j] = []

    # Populate the matrix with longest common subarrays between histories
    for i in range(1, len(user1) + 1):
        for j in range(1, len(user2) + 1):
            if user1[i - 1] == user2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + [user1[i - 1]]
            else:
                matrix[i][j] = []

    # Go ahead and find the longest contiguous common subarray
    longest_result = []
    for i in range(len(user1) + 1):
        for j in range(len(user2) + 1):
            if len(matrix[i][j]) > len(longest_result):
                longest_result = matrix[i][j]
    return longest_result



print(longest_contiguous_history(user1 = ['/home', '/register', '/login', '/user', '/one', '/two'], user2 = ['/home', '/red', '/login', '/user', '/one', '/pink']))