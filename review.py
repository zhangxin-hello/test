import numpy as np

def solution_array(array):
    n = len(array)
    #i表示对于每一列的操作：
    for i in range(0,n-1):
        #找出对应那行元素[p,i]不是零的行p(注意：要从i开始):
        for p in range(i,n):
            if (abs(array[p,i])) > 1e-5:
                break
            else:
                p=p+1
        #若不存在，则p==n:
        if p == n:
            return "no unique solution exists."
        #若存在，交换p,i两行（若p==i,则跳过此步骤）：
        if p != i:
            temp = array[j,:]
            array[j,:] = array[i,:]
            array[i,:] = temp
        #j表示对余下每一行的操作：
        for j in range(i+1,n):
            m = array[j,i]/array[i,i]
            array[j,:] = array[j,:] + (-1)*m*array[i,:]
    
    if abs(array[n-1,n-1]) <1e-5:
        return "no unique solution exists."

    #使用一维数组储存解x的集合：
    x = np.zeros(n)
    x[n-1] = array[n-1,n]/array[n-1,n-1]

    #计算得x[:(n-2)]的值：
    for i in range(n-1,0,-1):
        x[i-1] = (array[i-1,n] - sum(x[i:n]*array[i-1,i:n])) /array[i-1,i-1]
    
    return x

def main():
    # array = np.array([
    #     [1,0,1,2],
    #     [1,1,1,4],
    #     [1,1,0,3],
    # ])

    array = np.array([[1.,1,0,3,4],[2,1,-1,1,1],[3,-1,-1,2,-3],[-1,2,3,-1,4]])

    result = solution_array(array)
    print(result)

main()