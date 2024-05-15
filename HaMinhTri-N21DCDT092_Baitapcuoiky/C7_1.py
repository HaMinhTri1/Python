class DoThi:
    def __init__(self, so_dinh):
        self.so_dinh = so_dinh
        self.ds_ke = [[] for _ in range(so_dinh)]

    def them_canh(self, u, v):
        self.ds_ke[u].append(v)
        self.ds_ke[v].append(u)

    def dfs(self, u, visited):
        visited[u] = True
        for v in self.ds_ke[u]:
            if not visited[v]:
                self.dfs(v, visited)

    def LienThong(self):
        visited = [False] * self.so_dinh
        self.dfs(0, visited)
        return all(visited)

# Sử dụng ví dụ:
dt = DoThi(5)
dt.them_canh(0, 3)
dt.them_canh(1, 2)
dt.them_canh(3, 4)

if dt.LienThong():
    print("Đồ thị là liên thông.")
else:
    print("Đồ thị không liên thông.")
