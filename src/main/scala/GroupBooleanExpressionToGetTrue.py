def split(expression):
    operands, operators = [], []

    for value in expression:
        if value in {'T', 'F'}:
            operands.append(value)
        else:
            operators.append(value)

    return operands, operators

def solve(expression):
    operands, operators = split(expression)

    n = len(operands)
    # all true and false variables: from i to j expression
    T = [[0 for _ in range(n)] for _ in range(n)]
    F = [[0 for _ in range(n)] for _ in range(n)]
    # if operands[i][i] is one variable's value
    for i in range(n):
        if operands[i] == 'T':
            T[i][i] = 1
            F[i][i] = 0
        else:
            T[i][i] = 0
            F[i][i] = 1
    # [i,i + gap] is split point : left and right subexpressions.
    for gap in range(1, n):
        for i in range(n - gap):
            j = i + gap
            # for every expression [i+k],[k+1,j] we evaluate count of true expressions
            # k is split point.(i,k) operation (k+1,j)
            for k in range(i, j):
                # evaluate total number of false and true variables
                all_options = (T[i][k] + F[i][k]) * (T[k+1][j] + F[k+1][j])
                # if k is split point, let's evaluate left subexpression <> right subexpression
                if operators[k] == '&':
                    # if it's and, number is product of left and right true variables
                    T[i][j] += T[i][k] * T[k+1][j]
                    # the rest is false
                    F[i][j] += (all_options - T[i][j])

                elif operators[k] == '|':
                    # evaluate false expressions.
                    F[i][j] += F[i][k] * F[k+1][j]
                    # the rest is true result
                    T[i][j] += (all_options - F[i][j])

                elif operators[k] == '^':
                    # if xor then true * false + false * true
                    T[i][j] += F[i][k] * T[k+1][j] + T[i][k] * F[k+1][j]
                    F[i][j] += T[i][k] * T[k+1][j] + F[i][k] * F[k+1][j]
    # return total number
    return T[0][n - 1]

print(solve(['F', '|', 'T', '&', 'T']))