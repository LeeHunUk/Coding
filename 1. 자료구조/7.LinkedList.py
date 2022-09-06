"""
 $ 링크드 리스트(연결 리스트)
   - 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 데이터 구조

 $ 기본 구조와 용어
   - 노드 : 데이터 저장 단위로 구성
   - 포인터 : 노드 안에서 다음이나 이전의 노드와 연결 정보를 가지고 있는 공간
 $ 장점
   - 미리 데이터 공간을 할당하지 않아도 됨
 $ 단점
   - 연결을 위한 별도 데이터 공간이 필요하므로, 저장공간 효율이 높지 않음
   - 연결 정보를 찾는 시간이 필요하므로 접근 속도 가 느림
   - 중간 데이터 삭제시, 앞뒤 데이터의 연결을 재구성해야 하는 부가적인 작업 필요
"""

# Node 구현
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# 연결하기
node1 = Node(1)
# node2 = Node(2)
# node1.next = node2
head = node1

# 데이터 추가하기
def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)

for index in range(2, 10):
    add(index)

# 데이터 출력하기
node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)
print("=========")

# 중간데이터 추가
node3 = Node(1.5)
node = head
search =True
while search:
    if node.data == 1:
        search = False
    else:
        node = node.next

node_next = node.next
node.next = node3
node3.next = node_next

node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)
print("=========")