
# def solveNQueens(n):

#     def put(x,y,mark):
#         dx=[-1,1,0,0,-1,-1,1,1]
#         dy = [0,0,-1,1,-1,1,-1,1]
#         mark[x][y]=1
#         for i in range(n):
#             for j in range(8):
#                 newx = x + i*dx[j]
#                 newy = y + i*dy[j]
#                 if newx>=0 and newx<n and newy>=0 and newy<n:
#                     mark[newx][newy]=1
#     def gen(k,n,location,mark,res):
#         if k==n:
#             res.append(location)
#             return
#         for i in range(n):
#             if mark[k][i]==0:
#                 tmpmark = mark
#                 location[k][i]='Q'
#                 put(k,i,mark)
#                 print(k,i,mark)
#                 gen(k+1,n,location,mark,res)
#                 mark = tmpmark
#                 location[k][i]='.'
#     res=[]
#     location=[['.' for _ in range(n)] for _ in range(n)]
#     mark = [[0 for _ in range(n)] for _ in range(n)]

#     gen(0,n,location,mark,res)
#     return res

# out = solveNQueens(4)
# print(out)

# def sort(s):
#     res=''
#     dic={}
#     for i in s:
#         if ord(i) in dic:
#             dic[ord(i)]+=1
#         else:
#             dic[ord(i)]=1
#     d = sorted(dic.keys())
#     for i in d:
#         res+=chr(i)
#         res+=str(dic[i])
#     return res

# out = sort('dddscfcsa')
# print(out)

def queen(n):
    d = [-1]*(n)

    def check(k,i):
        for j in range(k):
            if d[j]==i or abs(k-j)==abs(d[j]-i):
                return False
        return True
    
    def dfs(depth,value):
        if depth==n:
            res.append(value)
            return
        for i in range(n):
            if check(depth,i):
                d[depth] = i
                s = '.'*n
                dfs(depth+1,value+[s[:i]+'Q'+s[i+1:]])
    res = []
    dfs(0,[])
    return res
out = queen(4)
print(out)
