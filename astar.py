from pyamaze import maze, textLabel

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


if __name__ == '__main__':
    m = maze(10, 20)
    m.CreateMaze()
    
    i = textLabel(m, 'Manhattan Distance' , heuristic((1, 1), (m.rows, m.cols))+1)
    print("All States in the Grid: \n",m.grid)
    
    m.run()