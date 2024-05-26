from agent import *
from COLOR import *
from maze import maze
from collections import deque
from textLabel import textLabel

def recursiveBacktracking(m, start=None):
    if start is None:
        start = (m.rows, m.cols)
    visited = [start]
    stack = [start]
    backtrackPath = {}
    searchedPath = []
    while len(stack) > 0:
        currCell = stack[-1]
        searchedPath.append(currCell)
        if currCell == m._goal:
            break
        poss = 0
        for d in range(4):
            if m.maze_map[currCell][d] == True:
                dx = m.delta()[0]
                dy = m.delta()[1]
                child = (currCell[0] + dx[d], currCell[1] + dy[d])
                if child in visited:
                    continue
                poss += 1
                visited.append(child)
                stack.append(child)
                backtrackPath[child] = currCell
                break
        if poss > 1:
            m.markCells.append(currCell)
        if poss == 0:
            stack.pop()
    # fwdPath = {}
    # cell = m._goal
    # while cell != start:
    #     fwdPath[backtrackPath[cell]] = cell
    #     cell = backtrackPath[cell]
    return searchedPath

if __name__ == '__main__':
    m = maze(10, 10)
    m.CreateMaze(2, 4)

    path1 = recursiveBacktracking(m, (5, 1))

    a = agent(m, 5, 1, goal=(2, 4), footprints=True, color=COLOR.green)
    # b = agent(m, 5, 1, goal=(2, 4), footprints=True, color = COLOR.yellow)
    m.tracePath({a: path1}, showMarked=True)
    # m.tracePath({b: path2})
    # l3 = textLabel(m, 'Recursive Backtracking Path Length', len(path) + 1)
    m.run()