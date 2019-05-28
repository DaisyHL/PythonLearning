# -*- coding: utf-8 -*-
"""
Created on Tue May 28 2019

@author: YangYang
"""

"""
将一串数组以“Z 形”放入 n 个桶中
(第一列正着放，第二列倒着放)
例：
数组：[1, 2, 3, 4, 5, 6, 7]，将其放入 3 个桶中
输出：
[
    [1, 6, 7],
    [2, 5],
    [3, 4],
]
"""
# 方法一
def ListZ(data,step):
    #补充矩阵
    for i in range(step):
        if len(data) % step != 0:
            data.append(None)
            
    # 翻转偶数列
    for i in range(0,len(data),step):
        if (i/step) % 2 != 0:        
            data[i:i+step] = data[i+step-1:i-1:-1]   
            
    # 重新排列数组
    Zdata = []  
    for i in range(step):    
        data_ramp = [data[j] for j in range(i,len(data),step)]
        if None in data_ramp:
            data_ramp.remove(None)
        Zdata.append(data_ramp)
    return Zdata

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
step = 4
Zdata = ListZ(data,step)
print(Zdata)


'''    
# 根据step重新排列数据
data_step = [data[i:i+step] for i in range(0,len(data),step)]   
'''          

# 方法二
def split_bucket(array, n):
    buckets = [[] for _ in range(n)]
    for i ,num in enumerate(array):
        if (i // n) % 2 == 0:
            bucket = buckets[i % n]
        else:
            bucket = buckets[-(i % n) - 1]
        bucket.append(num)
    return buckets
if __name__ == '__main__':
    print(split_bucket([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],4))
