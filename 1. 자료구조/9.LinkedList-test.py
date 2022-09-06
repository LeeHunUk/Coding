class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    # 추가
    def add(self, data):
        if self.head =="":
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    # 조회
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    # 삭제
    def delete(self, data):
        if self.head =="":
            print("해당 값을 가진 노드가 없습니다.")
            return
        
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                else:
                    node = node.next
    
    # 나만의 찾기
    def find_node(self, data):
        node = self.head
        while node.next:
            if node.next.data == data:
                print(f"데이터 값이 {node.next.data}인 값은 {node.next}")
                break
            else:
                node = node.next
    
    # 실제 답안
    def search_node(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next



# 연습문제 1. 위 코드에서 노드 데이터가 2인 노드 삭제
linkedlist1 = NodeMgmt(0)
for data in range(1, 10):
    linkedlist1.add(data)

linkedlist1.delete(2)
linkedlist1.desc()
print("==============")

# 연습문제 2. 위 코드에서 노드 데이터가 특정 숫자인 노드를 찾는 함수 만들기 및 테스트
linkedlist2 = NodeMgmt(0)
for data in range(1, 10):
    linkedlist2.add(data)

linkedlist2.desc()
linkedlist2.find_node(4)

print(linkedlist2.search_node(4))