import math
import numpy as np

N = 10000
tol = 1e-3

def Jacobi(array,b):
    n = len(array)
    k = 0
    x0 = np.zeros(n)
    x  = np.zeros(n)
    w  = 0.5

    while(k<=N):
        for i in range(n):
            #普通迭代：
            #sum1 = sum(array[i,0:n]*x0[0:n])
            #Gauss-Seidel 迭代改进：
            # sum2 = sum(array[i,0:i]*x[0:i])+sum(array[i,i:n]*x0[i:n])
            # x[i] = (-1*sum2+array[i,i]*x0[i]+b[i]) /array[i,i]
            #松弛法：
            temp = b[i]-sum(array[i,0:i]* x[0:i])- sum(array[i,(i+1):n]* x[(i+1):n])
            x[i] = (1-w) *x0[i] + w* temp /array[i,i]
                
        if np.max(abs(x-x0)) < tol:
            print('x is ok.')
            return x
        k = k+1
        x0 =x.copy()

    if k == N+1:
        print(f"the time is over {N}.")


def main():
    array1 = np.array([
       [4,3,0],
       [3,4,-1],
       [0,-1,4],
    ])
    #注意b = np.array([6,25,-11,15])
    #与b = np.array([[6,25,-11,15]])是不同维数的矩阵
    b1 = np.array([24,30,-24])

    array2 = np.array([
        [1,1,1],
        [2,-1,2],
        [3,2,1],
    ])
    b2 =np.array([2,-2,6])

    result = Jacobi(array1,b1)

    print(result)

main()
