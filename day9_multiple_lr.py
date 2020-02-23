# Enter your code here. Read input from STDIN. Print output to STDOUT

def calc_minors_matrix(mat):
    pass

def calc_cofactors_matrix(minors):
    pass

def calc_adjugate_matrix(cofactors):
    pass

def calc_determinant(mat):
    pass

def scalar_multiplication(n, mat):
    ans = []
    for i in range(len(mat)):
        ans.append([n * j for j in mat[i]])

def inverse_calc(mat):
    if len(mat) == len(mat[0]):
        minors = calc_minors_matrix(mat)
        cofactors = calc_cofactors_matrix(minors)
        adj = calc_adjugate_matrix(cofactors)
        det = calc_determinant(mat)
        return scalar_multiplication(1/det, adj)
    else:
        return -1




m, n = [int(i) for i in input().split()]

dataset = [[0 for j in range(n)] for i in range(m+1)]

x = [[1 for j in range(m + 1)] for i in range(n)]

y = [[0 for j in range(1)] for i in range(n)]


    
for i in range(n):
    inp = [float(j) for j in input().split()]
    for k in range(0, m):
        x[i][k+1] = inp[k]
    y[i][0] = inp[m]

q = int(input())

feature_sets = [[float(j) for j in input().split()] for i in range(q)]

