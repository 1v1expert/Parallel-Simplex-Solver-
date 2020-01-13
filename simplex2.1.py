A = []
A_nums = []
basis = []
file = open("input.txt")
for j in file:
    j = j.split()
    # print(j)
    if j[0] != "func":
        A.append([float(j[-2])])
        A[-1] +=(list(map(float,j[:-2])))
        A_nums.append(j[-1])
    else:
        break
j=file.readline().rstrip().split()
func_max = list(map(float,j[:-1]))
num_func = j[-1]
n = len(A)
func_max = [0] + func_max
if num_func == "max":
    for s in range(len(func_max)):
        func_max[s] = -func_max[s]
A.append(func_max)
print(A)
for j in range(n):
    if A_nums[j] != "less":
        for l in range(n+1):
            if l != j:
                A[l].append(0)
            else:
                A[l].append(-1)
    for l in range(n + 1):
        if l != j:
            A[l].append(0)
        else:
            A[l].append(1)
k = int(file.readline())
file.close()
lens = len(A[0])

def diff_cur(ind1,ind2,f_ind,e_ind,cof):
    for j in range(f_ind,e_ind+1):
        A[ind1][j] = A[ind1][j]/cof

def diff_another(ind2,ind0,ind1,f_ind,e_ind,cof):
    line1 = A[ind0][f_ind:e_ind+1]
    for s in range(len(line1)):
        line1[s] *= cof
    for s in range(len(line1)):
        A[ind1][s+f_ind] += line1[s]

def multi_diff_another(ind2,ind0,f_ind,e_ind,coefs):
    for j in range(n + 1):
        if j != ind_coeff:
            diff_another(ind2, ind0, j, f_ind, e_ind,coefs[j])
    