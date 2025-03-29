import heapq
import math

class Node:
    def __init__(self, id, a, b, c, d, price):
        self.id = id
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.price = price
    
    def __repr__(self):
        return f"id: {self.id} : {self.a} {self.b} {self.c} {self.d} {self.price}"
    
    def l2_distance(self):
        return math.sqrt((self.a - BASE.a) ** 2 +
                         (self.b - BASE.b) ** 2 +
                         (self.c - BASE.c) ** 2 +
                         (self.d - BASE.d) ** 2)

    def __lt__(self, other):
        return self.l2_distance() < other.l2_distance()

BASE = Node(-1, 6, 200, 5, 30, -1)

nodes = [
    Node(1, 2, 200, 4, 27, 30000),
    Node(2, 5, 150, 3, 35, 20000),
    Node(3, 3, 180, 4, 25, 25000),
    Node(4, 1, 230, 2, 10, 21000),
    Node(5, 5, 180, 5, 40, 38000),
    Node(6, 4, 210, 3, 30, 31000)
]

pq = []
for node in nodes:
    heapq.heappush(pq, node)

price = 0
weight = 0

for _ in range(5):
    now = heapq.heappop(pq)
    print(now)
    temp_weight = math.exp(-now.l2_distance())
    print(f"tempWeight : {temp_weight}")
    price += temp_weight * now.price
    weight += temp_weight

print(f"price : {price / weight}")
