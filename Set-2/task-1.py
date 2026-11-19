class Node:
    def __init__(self, claim_id):
        self.claim_id = claim_id
        self.left = None
        self.right = None
class ClaimBST:
    def __init__(self):
        self.root = None

    def insert(self, claim_id):
        if self.root is None:
            self.root = Node(claim_id)
            return True
        current = self.root
        while True:
            if claim_id == current.claim_id:
                return False
            if claim_id < current.claim_id:
                if current.left is None:
                    current.left = Node(claim_id)
                    return True
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(claim_id)
                    return True
                current = current.right
    def search(self, claim_id):
        current = self.root
        while current is not None:
            if claim_id == current.claim_id:
                return True
            current = current.left if claim_id < current.claim_id else current.right
        return False

    def inorder(self):
        result = []
        def visit(node):
            if node is not None:
                visit(node.left)
                result.append(node.claim_id)
                visit(node.right)
        visit(self.root)
        return result

    def preorder(self):
        result = []
        def visit(node):
            if node is not None:
                result.append(node.claim_id)
                visit(node.left)
                visit(node.right)
        visit(self.root)
        return result
    def postorder(self):
        result = []
        def visit(node):
            if node is not None:
                visit(node.left)
                visit(node.right)
                result.append(node.claim_id)
        visit(self.root)
        return result
if __name__ == "__main__":
    tree = ClaimBST()
    for claim_id in [1050, 1025, 1075, 1010, 1040, 1060, 1090, 1030, 1045, 1080]:
        tree.insert(claim_id)
    print("Inorder (sorted):", tree.inorder())
    print("Preorder:", tree.preorder())
    print("Postorder:", tree.postorder())
    print("Search 1040:", tree.search(1040))
    print("Search 9999:", tree.search(9999))
    print("Insert duplicate 1040:", tree.insert(1040))
