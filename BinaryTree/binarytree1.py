class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(11)
root.left.left.left.left = Node(12)
root.left.left.left.left.left = Node(11)

    #                 1
    #                / \
    #               /   \
    #              2     3
    #             / \   / \
    #            /   \ /   \
    #           4    5 6    7   
    #          /
    #         /
    #        11
    #        /
    #       /
    #     12
    #     /
    #    /
    #   11