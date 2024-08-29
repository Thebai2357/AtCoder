def i():
    return int(input())
def ii():  # 数値受け取り 複数対応
    return map(int,input().split())
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(ii()) for _ in range(N)] if N!= 0 else list(ii())
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

N,M = ii()
AB = ai(M)

class UnionFind():
    def __init__(self,n):
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n

    def root(self,x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]
    def issame(self,x,y):
        return self.root(x) == self.root(y)
    
    def unite(self,x,y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx,ry=ry,rx
        self.par[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry]
        return True
    
    def size(self,x):
        return self.siz[self.root(x)]

uf = UnionFind[N]
print(uf)
