def knows(A, B):
    return True

def findCelebrity(n, matrix):
    st = []
    for i in range(n):
        st.append(i)

    A = st.pop()
    B = st.pop()

    while len(st) > 1:
        if knows(A, B):
            A = st.pop()
        else:
            B = st.pop()

    C = st.pop()
    if knows(C, B):
        C = B
    if knows(C, A):
        C = A

    for i in range(n):
        if C != i and (knows(C,i) or not knows(i, C)):
            return -1
    return C





