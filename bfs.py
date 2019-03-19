def initvisited(graph):
    diction = {}
    for y in range (len(graph)):
        for x in range (len(graph[y])):
            diction[(x,y)] = 0 
    return diction   

def initbefore(graph):
    diction = {}
    for y in range (len(graph)):
        for x in range (len(graph[y])):
            diction[(x,y)] = (-1, -1) 
    return diction     

def bfs(graph, visited, before, x, y, x_food, y_food):
    queue = [(x, y)]
    temp = (x, y)
    visited[temp] = 1
    node = queue.pop(0) 
    while True:
        if (visited[(node[0] + 1, node[1])] == 0 and graph[node[0]+1][node[1]]!=1 and graph[node[0]+1][node[1]]!=3):
            visited[(node[0]+1, node[1])] = 1
            queue.append((node[0] + 1, node[1]))
            before[(node[0] + 1, node[1])] = node

        if (visited[(node[0] - 1, node[1])] == 0 and graph[node[0]-1][node[1]]!=1 and graph[node[0]-1][node[1]]!=3):
            visited[(node[0]-1, node[1])] = 1
            queue.append((node[0] - 1, node[1]))
            before[(node[0] - 1, node[1])] = node

        if (visited[(node[0], node[1] + 1)] == 0 and graph[node[0]][node[1] + 1]!=1 and graph[node[0]][node[1]+1]!=3):
            visited[(node[0], node[1]+1)] = 1
            queue.append((node[0], node[1]+1))
            before[(node[0], node[1]+1)] = node

        if (visited[(node[0], node[1] - 1)] == 0 and graph[node[0]][node[1] - 1]!=1 and graph[node[0]][node[1]-1]!=3):
            visited[(node[0], node[1]-1)] = 1
            queue.append((node[0], node[1]-1))
            before[(node[0], node[1]-1)] = node

        if len(queue) == 0:
            break
        else:
            node = queue.pop(0)

        if node == (x_food, y_food):
            break

def path(before, x, y, x_food, y_food):
    result = []
    if(before[(x_food, y_food)] == (-1, -1)):
        return result
    temp = (x_food, y_food)
    result.append((x_food, y_food))
    while(before[temp]!=(x,y)):
        result.append(before[temp])
        temp = before[temp]
    result.append((x,y))
    result.reverse()
    return result   


def returnPath(x, y, x_f, y_f):
    f = open("map1.txt", 'r')
    firstline = f.readline()
    matrix = f.readlines()
    graph = []
    for line in matrix:
        temp = [int(value) for value in line.split()]
        graph.append(temp)
    f.close()

    visited = initvisited(graph)
    before = initbefore(graph)

    bfs(graph, visited, before, x, y, x_f, y_f)
    result = path(before, x, y, x_f,y_f)
    # print(result)
    return result

# f = open("map1.txt", 'r')
# firstline = f.readline()
# matrix = f.readlines()
# graph = []
# for line in matrix:
#     temp = [int(value) for value in line.split()]
#     graph.append(temp)
# f.close()

# x_pacman = 0
# y_pacman = 0
# x_food = 0
# y_food = 0
# for y in range (len(graph)):
#     for x in range (len(graph[y])):
#         character = graph[x][y]
#         if character == 5:
#             x_pacman = x
#             y_pacman = y

#         if character == 2:
#             x_food = x
#             y_food = y 
# print(x_pacman, y_pacman)
# visited = {}
# before = {}
# visited = initvisited(graph)
# before = initbefore(graph)

# bfs(graph, visited, before, x_pacman, y_pacman, x_food, y_food)
# result = path(before, x_pacman, y_pacman, x_food, y_food)
# print(result)

# print(path)
# for y in range (len(graph)):
#     for x in range (len(graph[y])):
#         if(dict[(x,y)] == 0):
#             print(graph[x][y], end=" ")
#     print("")

# queue = [(6,8)]
# queue.append((1,2))
# queue.append((5,2))
# queue.append((3,4))
# node = queue.pop(0)
