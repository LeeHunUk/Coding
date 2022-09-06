# 연습문제1. 앞 코드에서 노드 데이터가 특정 숫자인 노드 앞에
#           데이터를 추가하는 함수를 만들고, 테스트하기
# 단, tail에서부터 뒤로 이동하며, 특정 숫자인 노드를 찾는 방식

# 나만의 코드
class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new
    
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
    
    def prev_add(self, data, find):
        if self.tail == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.tail
            while node.data != find:
                node = node.prev
                if node == None:
                    answer = "값이 존재하지 않습니다."
                    return answer
            new = Node(data)        
            prev_node = node.prev
            prev_node.next = new
            new.prev = prev_node
            new.next = node
            node.prev = new

    def next_add(self, data, find):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.data != find:
                node = node.next
                if node == None:
                    answer = "값이 존재하지 않습니다."
                    return answer
            new = Node(data)
            next_node = node.next
            next_node.prev = new
            node.next = new
            new.prev = node
            new.next = next_node
            
            

            
double_linked_list1 = NodeMgmt(0)
for data in range(1, 10):
    double_linked_list1.insert(data)

double_linked_list1.desc()
print("====")
double_linked_list1.prev_add(1.5, 2)
double_linked_list1.desc()
print("====")

# 연습문제2. 앞 코드에서 노드 데이터가 특정 숫자인 노드 뒤에
#           데이터를 추가하는 함수를 만들고, 테스트하기
# 단, head에서부터 뒤로 이동하며, 특정 숫자인 노드를 찾는 방식
double_linked_list2 = NodeMgmt(0)
for data in range(1, 10):
    double_linked_list2.insert(data)

double_linked_list2.desc()
print("====")
double_linked_list2.next_add(1.7, 1)
double_linked_list2.desc()