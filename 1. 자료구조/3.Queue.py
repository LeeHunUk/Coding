# 큐 구조
# : 가장 먼저 넣은 데이터를 가장 먼저 꺼낼 수 있는 구조
# : FIFO 선입선출 | 스택과 꺼내는 순서는 반대

# 큐 만들기
import queue

# 가장 일반적인 큐 자료 규조
data_queue = queue.Queue() 
data_queue.put("Coding")
data_queue.put(1)

print(data_queue.qsize(), data_queue.get(), data_queue.get(), data_queue.qsize())
print("===========")

# Lifo 큐
lifo_queue = queue.LifoQueue()
lifo_queue.put("Coding")
lifo_queue.put(1)

print(lifo_queue.qsize(), lifo_queue.get(), lifo_queue.get(), lifo_queue.qsize())
print("===========")

# Priority 큐
priority_queue = queue.PriorityQueue()
priority_queue.put((10,"Korea"))
priority_queue.put((5, 1))
priority_queue.put((15, "China"))

priority_queue.put((15, "Japen"))

print(priority_queue.qsize(), priority_queue.get(), priority_queue.get(),priority_queue.qsize())
print(priority_queue.get(), priority_queue.qsize())

# 멀티 태스킹을 위한 프로세스 스케쥴링 방식을 구현하기 위해 많이 사용됨