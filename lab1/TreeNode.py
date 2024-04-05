class TreeNode:
    data = -1
    children = []

    def __init__(self, data, children):
        self.data = data
        self.children = children

    def __lt__(self, other):
        return self.data < other.data

    def __gt__(self, other):
        return self.data > other.data
