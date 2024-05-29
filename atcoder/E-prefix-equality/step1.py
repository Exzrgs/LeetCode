"""
xorは順番によらないから、要素が同じであればほとんどの場合同じになる
"""

from random import randrange

num_elements = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

num_to_random = dict()
for num in a:
    num_to_random[num] = randrange(1 << 60)
for num in b:
    num_to_random[num] = randrange(1 << 60)

a_index_to_hash = [0] * (num_elements + 1)
a_seen = set()
b_index_to_hash = [0] * (num_elements + 1)
b_seen = set()
for i in range(1, num_elements + 1):
    a_index_to_hash[i] = a_index_to_hash[i - 1]
    if a[i - 1] not in a_seen:
        a_index_to_hash[i] ^= num_to_random[a[i - 1]]
        a_seen.add(a[i - 1])
    b_index_to_hash[i] = b_index_to_hash[i - 1]
    if b[i - 1] not in b_seen:
        b_index_to_hash[i] ^= num_to_random[b[i - 1]]
        b_seen.add(b[i - 1])

num_queries = int(input())
for _ in range(num_queries):
    x, y = map(int, input().split())
    
    if a_index_to_hash[x] == b_index_to_hash[y]:
        print("Yes")
    else:
        print("No")
