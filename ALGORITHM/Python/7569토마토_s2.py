from collections import deque

def bfs() :
    while q :
        k,i,j = q.popleft()
        for l in range(6) :
            nk,ni,nj = k + dk[l], i + di[l], j + dj[l]
            if -1 < nk < h and -1 < ni < n and -1 < nj < m :
                if a[nk][ni][nj] == 0:# and check[nk][ni][nj] == -1 :
                    q.append((nk,ni,nj))
                    a[nk][ni][nj] = a[k][i][j] + 1

m,n,h = map(int,input().split())
a = [ [ list(map(int,input().split())) for _ in range(n) ] for _ in range(h) ]
di = [0,0,0,0,1,-1]
dj = [0,0,1,-1,0,0]
dk = [1,-1,0,0,0,0]
q = deque()

for k in range(h) :
    for i in range(n) :
        for j in range(m) :
            if a[k][i][j] == 1 :
                q.append((k,i,j))

bfs()
t = 0
for k in range(h) :
    for i in range(n) :
        for j in range(m) :
            if a[k][i][j] == 0:
                print(-1)
                exit()
            if t < a[k][i][j]:
                t = a[k][i][j]
print(t-1)