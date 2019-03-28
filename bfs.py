def initvisited(graph):
    diction = {}
    for x in range (len(graph)):
        for y in range (len(graph[x])):
            diction[(x,y)] = 0 
    return diction   

def initlevel(graph):
    diction = {}
    for x in range (len(graph)):
        for y in range (len(graph[x])):
            diction[(x,y)] = 0 
    return diction   


def initbefore(graph):
    diction = {}
    for x in range (len(graph)):
        for y in range (len(graph[x])):
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

def checkwallaround(graph, x, y):
    numWallAround = 0
    if (graph[x+1][y]==1 or graph[x+1][y]==3):
        numWallAround+=1

    if (graph[x-1][y]==1 or graph[x-1][y]==3):
        numWallAround+=1

    if (graph[x][y+1]==1 or graph[x][y+1]==3):
        numWallAround+=1

    if (graph[x][y-1]==1 or graph[x][y-1]==3):
        numWallAround+=1

    if(numWallAround == 4):
        return False
    else:
        return True

def smellFood(graph, visited, level, x, y):
    stack = [(x, y)]
    temp = (x, y)
    visited[temp] = 1
    level[temp] = 0
    node = stack.pop(len(stack) - 1) 
    while True:
        t = level[node]
        if t < 4:
            if (visited[(node[0] + 1, node[1])] == 0 and graph[node[0]+1][node[1]]!=1 and graph[node[0]+1][node[1]]!=3):
                visited[(node[0]+1, node[1])] = 1
                stack.append((node[0] + 1, node[1]))
                level[(node[0] + 1, node[1])] = level[node] + 1

            if (visited[(node[0] - 1, node[1])] == 0 and graph[node[0]-1][node[1]]!=1 and graph[node[0]-1][node[1]]!=3):
                visited[(node[0]-1, node[1])] = 1
                stack.append((node[0] - 1, node[1]))
                level[(node[0] - 1, node[1])] = level[node] + 1

            if (visited[(node[0], node[1] + 1)] == 0 and graph[node[0]][node[1] + 1]!=1 and graph[node[0]][node[1]+1]!=3):
                visited[(node[0], node[1]+1)] = 1
                stack.append((node[0], node[1]+1))
                level[(node[0], node[1]+1)] = level[node] + 1

            if (visited[(node[0], node[1] - 1)] == 0 and graph[node[0]][node[1] - 1]!=1 and graph[node[0]][node[1]-1]!=3):
                visited[(node[0], node[1]-1)] = 1
                stack.append((node[0], node[1]-1))
                level[(node[0], node[1]-1)] = level[node] + 1

        if len(stack) == 0:
            return False
        
        else:
            node = stack.pop(len(stack) - 1)

        if graph[node[0]][node[1]] == 2:
            return True

def DFSforLevel3(graph, visited, before, x, y, final):
    stack = [(x, y)]
    temp = (x, y)
    visited[temp] = 1
    node = stack.pop(len(stack) - 1)
    f = node 
    while True:
        print(node)
        flag = 0
        if (visited[(node[0] + 1, node[1])] == 0 and graph[node[0]+1][node[1]]!=1 and graph[node[0]+1][node[1]]!=3):
            visited[(node[0]+1, node[1])] = 1
            tempV = initvisited(graph)
            tempL = initlevel(graph)
            if (smellFood(graph, tempV, tempL, node[0] + 1, node[1])):
                stack.append((node[0] + 1, node[1]))
                before[(node[0] + 1, node[1])] = node
                flag+=1

        if (visited[(node[0] - 1, node[1])] == 0 and graph[node[0]-1][node[1]]!=1 and graph[node[0]-1][node[1]]!=3):
            visited[(node[0]-1, node[1])] = 1
            tempV = initvisited(graph)
            tempL = initlevel(graph)
            if (smellFood(graph, tempV, tempL, node[0] - 1, node[1])):
                stack.append((node[0] - 1, node[1]))
                before[(node[0] - 1, node[1])] = node
                flag+=1

        if (visited[(node[0], node[1] + 1)] == 0 and graph[node[0]][node[1] + 1]!=1 and graph[node[0]][node[1]+1]!=3):
            visited[(node[0], node[1]+1)] = 1
            tempV = initvisited(graph)
            tempL = initlevel(graph)
            if (smellFood(graph, tempV, tempL, node[0], node[1] + 1)):
                stack.append((node[0], node[1]+1))
                before[(node[0], node[1]+1)] = node
                print(3)
                flag+=1

        if (visited[(node[0], node[1] - 1)] == 0 and graph[node[0]][node[1] - 1]!=1 and graph[node[0]][node[1]-1]!=3):
            visited[(node[0], node[1]-1)] = 1
            tempV = initvisited(graph)
            tempL = initlevel(graph)
            if (smellFood(graph, tempV, tempL, node[0], node[1] - 1)):
                stack.append((node[0], node[1]-1))
                before[(node[0], node[1]-1)] = node
                flag+=1

        if len(stack) == 0 or flag == 0:
            break
        else:
            print(stack)
            node = stack.pop(len(stack) - 1)
            f = node

    final.append(f)

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

def pathLevel3(before, x, y, final):
    result = []
    if(final == (x,y)):
        return result 
    temp = final
    print(temp)
    result.append(temp)
    while(before[temp] != (x, y)):
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
# for x in range (len(graph)):
#     for y in range (len(graph[x])):
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
# level = {}
# final = []
# visited = initvisited(graph)
# before = initbefore(graph)
# level = initlevel(graph)

# DFSforLevel3(graph, visited, before, x_pacman, y_pacman, final)
# finalPoint = final[0]
# solution = pathLevel3(before, x_pacman, y_pacman, finalPoint)

# print(solution)







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
