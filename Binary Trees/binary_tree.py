class BinaryTree:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return f"BinaryTree({self.val})"

    def insert(self, val):
        if self.val is None:
            self.val = val
            return

        if self.val > val:
            if self.left is None:
                self.left = BinaryTree(val)  # 'val' will take the position, and self.left for it will again become None
            else:
                self.left.insert(val)  # recursive call to left branch

        elif self.val < val:  # everything is the same as in the left branch
            if self.right is None:
                self.right = BinaryTree(val)
            else:
                self.right.insert(val)

        else:
            raise ValueError(f"Val {val} already exists")

    def bfs(self):  # Breadth-first search
        res = []

        queue: list = [self]

        while queue:
            node = queue.pop(0)
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return res

    def dfs(self):  # Depth-first search
        pass

    def print_hierarchy(self, _dir="root", _level=0):
        print(f"[{_dir}] #{_level} = {self.val} | left = {self.left} | right = {self.right}")
        if self.left is not None:
            self.left.print_hierarchy("left", _level + 1)
        if self.right is not None:
            self.right.print_hierarchy("right", _level + 1)


tree = BinaryTree()

tree.insert(6)
tree.insert(1)
tree.insert(8)
tree.insert(5)
tree.insert(10)

tree.print_hierarchy()

result_bfs = tree.bfs()
print("BFS:", result_bfs)
