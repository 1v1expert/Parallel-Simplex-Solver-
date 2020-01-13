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

