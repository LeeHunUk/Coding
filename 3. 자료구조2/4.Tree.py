"""
    $ 트리 구조
      - Node와 Branch를 이용해서, 사이클을 이루지 않도록 구성한 데이터 구조
      - 트리 중 이진 트리 형태의 구조로, 탐색(검색) 알고리즘 구현을 위해 많이 사용
"""

# 노드 클래스 만들기
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 이진 탐색 트리에 데이터 넣기
class NodeMgmt:
    def __init__(self, head):
        self.head = head
    
    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break
    
    # 이진 탐색 트리 탐색
    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False

head = Node(1)
BST = NodeMgmt(head)
BST.insert(2)
BST.insert(3)
BST.insert(0)
BST.insert(4)
BST.insert(8)

print(BST.search(8))
print(BST.search(-2))