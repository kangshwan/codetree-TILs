array = []
N = int(input())
for i in range(N):
    command = input().split()
    if command[0] == 'push_back':
        array.append(int(command[1]))
    if command[0] == 'pop_back':
        array.pop()
    if command[0] == 'size':
        print(len(array))
    if command[0] == 'get':
        print(array[int(command[1])-1])