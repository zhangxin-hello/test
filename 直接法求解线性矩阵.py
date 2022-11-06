import numpy as np

#输入：n，矩阵array。
#输出：转换为上三角的矩阵array：
def get_array(n, array):
    #i表示对于每一列的操作：
    for i in range(0,n):
        #找出对应那行元素[p,i]不是零的行p(注意：要从i开始):
        for p in range(i,n):
            if array[p,i] > 1e-5:
                break
            else:
                p=p+1
        #若不存在，则p==n:
        if p == n:
            return "no"
        #若存在，交换p,i两行（若p==i,则跳过此步骤）：
        if p != i:
            temp = array[j,:]
            array[j,:] = array[i,:]
            array[i,:] = temp
        #j表示对余下每一行的操作：
        for j in range(i+1,n):
            m = array[j,i]/array[i,i]
            array[j,:] = array[j,:] + (-1)*m*array[i,:]
    
    return array

#输入：n，上三角的矩阵。
#输出：解x（一维数组） or “无解信息”：
def get_result(n,array):
    if array[n-1,n-1] == 0 or array=='no':
        return "no unique solution exists."

#使用一维数组储存解x的集合：
    x = np.zeros(n)
    x[n-1] = array[n-1,n]/array[n-1,n-1]

#计算得x[:(n-2)]得值：
    for i in range(n-1,0,-1):
        x[i-1] = (array[i-1,n] - sum(x[i:n]*array[i-1,i:n])) /array[i-1,i-1]
    
    return x

#输入：n,矩阵。
#输出：解x（一维数组） or “无解信息”
def solution_array(array):
    lenth = len(array)
    #array_return 为上三角矩阵：
    array_return = get_array(lenth,array)
    result  = get_result(lenth,array_return)

    return result

def main():
    # array = np.array([
    #               [1,1,0,3,4],
    #               [2,1,-1,1,1],
    #               [3,-1,-1,2,-3],
    #               [-1,2,3,-1,4],
    #               ])
    array = np.array([
        [1,0,1,2],
        [1,1,1,4],
        [1,1,0,3],
    ])
    result = solution_array(array)
    # n = len(array)
    # temp = get_array(n,array)

    # result = get_result(n,temp)
    print(f"result: {result}.")

main()
