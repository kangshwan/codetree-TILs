import sys
input = sys.stdin.readline
N = int(input())
hashmap = {}
for _ in range(N):
    command = input().split()
    if command[0] == 'add':
        k, v = map(int, command[1:])
        hashmap[k] = v
    elif command[0] == 'find':
        k = int(command[1])
        if k in hashmap:
            print(hashmap[k])
        else:
            print('None')
    elif command[0] == 'remove':
        k = int(command[1])
        hashmap.pop(k)