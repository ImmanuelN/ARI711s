from pyamaze import maze, agent, textLabel
from queue import PriorityQueue

#hearistic function that implements the manhattan distance
def heuristic(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1 - x2) + abs(y1 - y2)

#Cost function to add a cost based on the directions moved E = Left, W = Right, S = Down, N = Up
def cost_function(d):
    # Assign cost based on direction
    if d == 'E' or d == 'W':
        # Higher cost for moving east or west
        return 2
    elif d == 'S' or d == 'N':
        # Lower cost for moving south or north
        return 1
    else:
        # Default cost for other actions (should not happen)
        return 1
    
def getFullCost(fullCost):
    return fullCost

#A star Implementation
def aStar(m):
    start = (m.rows, m.cols)
    g_score = {cell: float('inf') for cell in m.grid}
    g_score[start] = 0
    f_score = {cell: float('inf') for cell in m.grid}
    f_score[start] = heuristic(start, (1, 1))

    open = PriorityQueue()
    open.put((heuristic(start, (1, 1)), start))
    aPath = {}
    fullCost = 0
    while not open.empty():
        _, currCell = open.get()
        if currCell == (1, 1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])
    
                
                temp_g_score = g_score[currCell] + 1
                temp_f_score = temp_g_score + heuristic(childCell, (1, 1)) + cost_function(d)

                if temp_f_score < f_score[childCell]:
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_f_score
                    open.put((temp_f_score, childCell))
                    aPath[childCell] = currCell
                    fullCost += cost_function(d)
                    

    fwdPath = {}
    cell = (1, 1)
    while cell != start:
        fwdPath[aPath[cell]] = cell
        cell = aPath[cell]
    return fwdPath, fullCost

if __name__ == '__main__':
    m = maze(10, 20)
    m.CreateMaze()
    path, fullCost = aStar(m)

    a = agent(m, footprints=True)
    m.tracePath({a: path})
    l = textLabel(m, 'A Star Path Length', len(path) + 1)
    i = textLabel(m, 'Manhattan Distance' , heuristic((1, 1), (m.rows, m.cols))+1)
    j = textLabel(m, 'Total Movement Cost for A* is ', fullCost)
    print("All States in the Grid: \n",m.grid)
    
    m.run()
