class Node:
    def __init__(self, code):
        self.code = code
        self.left = None
        self.right = None


class HubBST:
    def __init__(self):
        self.root = None

    def insert(self, code):
        def add(node, value):
            if node is None:
                return Node(value)
            if value < node.code:
                node.left = add(node.left, value)
            elif value > node.code:
                node.right = add(node.right, value)
            return node
        self.root = add(self.root, code)

    def search(self, code):
        current = self.root
        while current:
            if code == current.code:
                return True
            current = current.left if code < current.code else current.right
        return False

    def height(self):
        def measure(node):
            if node is None:
                return -1
            return 1 + max(measure(node.left), measure(node.right))
        return measure(self.root)

    def inorder(self):
        def walk(node):
            return walk(node.left) + [node.code] + walk(node.right) if node else []
        return walk(self.root)

    def preorder(self):
        def walk(node):
            return [node.code] + walk(node.left) + walk(node.right) if node else []
        return walk(self.root)

    def postorder(self):
        def walk(node):
            return walk(node.left) + walk(node.right) + [node.code] if node else []
        return walk(self.root)


if __name__ == "__main__":
    codes = ["HYD", "DEL", "MUM", "BLR", "GOA", "KOL", "PUN", "AMD", "CHE", "JAI"]
    tree = HubBST()
    for code in codes:
        tree.insert(code)
    sorted_tree = HubBST()
    for code in sorted(codes):
        sorted_tree.insert(code)
    print("Insertion order:", codes)
    print("Search CHE:", tree.search("CHE"))
    print("Search LKO:", tree.search("LKO"))
    print("Inorder:", tree.inorder())
    print("Preorder:", tree.preorder())
    print("Postorder:", tree.postorder())
    print("Tree height (edges):", tree.height())
    print("Sorted-input height (edges):", sorted_tree.height())
