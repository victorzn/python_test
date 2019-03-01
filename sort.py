def swap(arr,i,j):
    arr[i],arr[j] = arr[j],arr[i]
#################### 冒泡排序 ##############################
def bubble(arr):
    if len(arr)<2:
        return arr
    for i in range(1,len(arr)):
        for j in range(len(arr)-i):
            if arr[j]>arr[j+1]:
                swap(arr,j,j+1)
    return arr
a = [1,3,5,2,4,6]
out = bubble(a)
print(out)
################### 选择排序 ################################hhh
def select(arr):
    if len(arr)<2:
        return arr
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                swap(arr,i,j)
    return arr
a = [1,3,5,2,4,6]
out = select(a)
print(out)
################# 插入排序 ###################################
def insert(arr):
    for i in range(1,len(arr)):
        p = i-1
        cur = arr[i]
        while p>=0 and arr[p]>cur:
            arr[p+1] = arr[p]
            p-=1
        arr[p+1]=cur
    return arr
a = [1,3,5,2,4,6]
out = insert(a)
print(out)
##################### 归并排序 ################################
def merge(left,right):
    res=[]
    while left and right:
        if left[0]<right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    if left:
        res+=left
    if right:
        res+=right
    return res
def mergesort(arr):
    if len(arr)<2:
        return arr
    mid = len(arr)//2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left,right)
a = [1,3,5,2,4,6]
out = mergesort(a)
print(out)
################################ 快速排序 #################################
def partition(arr,left,right):
    index = left
    id = left+1
    i = id
    while i<=right:
        if arr[i]<arr[index]:
            swap(arr,i,id)
            id+=1
        i+=1
    swap(arr,index,id-1)
    return id-1
def quicksort(arr,left,right):
    if left<right:
        pid = partition(arr,left,right)
        quicksort(arr,left,pid-1)
        quicksort(arr,pid+1,right)
    return arr
a = [1,3,5,2,4,6]
out = quicksort(a,0,len(a)-1)
print(out)
############################# 堆排序 #######################################
def build(arr):
    for i in range(len(arr)//2,-1,-1):
        heap(arr,i)
def heap(arr,i):
    left = 2*i+1
    right = 2*i+2
    lar = i
    if left<arrl and arr[left]>arr[lar]:
        lar = left
    if right<arrl and arr[right]>arr[lar]:
        lar = right
    if lar!=i:
        swap(arr,i,lar)
        heap(arr,lar)
def heapsort(arr):
    global arrl
    arrl = len(arr)
    build(arr)
    for i in range(len(arr)-1,0,-1):
        swap(arr,0,i)
        arrl-=1
        heap(arr,0)
    return arr
a = [1,3,5,2,4,6]
out = heapsort(a)
print(out)
################################### 寻找中位数 ####################################
def heapadjust(arr,parent):
    child = 2*parent+1
    while child<len(arr):
        if child+1<len(arr):
            if arr[child+1]>arr[child]:
                child+=1
        if arr[parent]>=arr[child]:
            break
        swap(arr,parent,child)
        parent,child = child,2*child+1
def find(nums):
    if len(nums)<2:
        return nums[0]
    if len(nums)==2:
        return sum(nums)/2
    mid = len(nums)//2
    heap = nums[:mid+1]
    for i in range(len(heap)//2,-1,-1):
        heapadjust(heap,i)
    for j in range(mid+1,len(nums)):
        if nums[j]>=heap[0]:
            continue
        else:
            heap[0]=nums[j]
            heapadjust(heap,0)
    if len(nums)%2==0:
        return (heap[0]+max(heap[1],heap[2]))/2
    else:
        return heap[0]
a = [10,32,3,5,20,4,6]
out = find(a)
print(out)
#############################  堆排序2 ###################################
def heapadjust2(arr,parent):
    child = 2*parent+1
    while child<arrll:
        if child+1<arrll:
            if arr[child+1]>arr[child]:
                child+=1
        if arr[parent]>=arr[child]:
            break
        swap(arr,parent,child)
        parent,child = child,2*child+1
def hs(arr):
    global arrll
    arrll = len(arr)
    for i in range(len(arr)//2,-1,-1):
        heapadjust2(arr,i)
    for j in range(len(arr)-1,0,-1):
        swap(arr,0,j)
        arrll-=1
        heapadjust2(arr,0)
    return arr
a = [1,3,5,2,4,6]
out = hs(a)
print(out)
################################# 希尔排序 #####################################
def shellsort(arr):
    if len(arr)<2:
        return arr
    gap = 1
    while gap<len(arr)/3:
        gap = gap*3+1
    while gap>0:
        for i in range(gap,len(arr)):
            cur = arr[i]
            j = i-gap
            while j>=0 and arr[j]>cur:
                arr[j+gap] = arr[j]
                j-=gap
            arr[j+gap] = cur
        gap//=3
    return arr
a = [1,3,5,2,4,6]
out = shellsort(a)
print(out)
################################# 计数排序 #####################################
def countsort(arr,maxValue):
    bucketLen = maxValue+1
    bucket = [0]*bucketLen
    sid = 0
    for i in arr:
        bucket[i]+=1
    for j in range(bucketLen):
        while bucket[j]>0:
            arr[sid]=j
            sid+=1
            bucket[j]-=1
    return arr
a = [1,3,5,2,4,6,]
out = countsort(a,140)
print(out)

################################# 基数排序 #####################################
def radixsort(arr):
    buck=[[]]
    digit = 0
    while len(buck[0])!=len(arr):
        buck = [[] for _ in range(10)]
        for i in range(len(arr)):
            num = (arr[i]//(10**digit))%10
            buck[num].append(arr[i])
        arr=[]
        for i in range(10):
            arr+=buck[i]
        digit+=1
    return arr
a = [1,3,235,32,24,6]
out = radixsort(a)
print(out)

    



