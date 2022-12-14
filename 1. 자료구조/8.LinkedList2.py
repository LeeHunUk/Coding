# 객체지향 프로그래밍으로 링크드 리스트 구현하기
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


linkedlist1 = NodeMgmt(0)
linkedlist1.desc()
print("============")

for data in range(1, 10):
    linkedlist1.add(data)
linkedlist1.desc()
print("================")

linkedlist1.delete(0)
linkedlist1.delete(3)
linkedlist1.desc()