from agent import agent
from maze import maze
from textLabel import textLabel
from queue import PriorityQueue

def h(cell1,cell2):
    x1,y1=cell1
    x2,y2=cell2

    return abs(x1-x2) + abs(y1-y2)
def aStar(m):
    start=(m.rows,m.cols)
    g_score={cell:float('inf') for cell in m.grid}
    g_score[start]=0
    f_score={cell:float('inf') for cell in m.grid}
    f_score[start]=h(start,(1,1))

    open=PriorityQueue()
    open.put((h(start,(1,1)),h(start,(1,1)),start))
    aPath={}
    while not open.empty():
        currCell=open.get()[2]
        if currCell==(1,1):
            break
        for d in range(4):
            if m.maze_map[currCell][d]==True:
                dx = [0, -1, 1, 0]
                dy = [-1, 0 ,0, 1]
                child=(currCell[0] + dx[d], currCell[1] + dy[d])

                temp_g_score=g_score[currCell]+1
                temp_f_score=temp_g_score+h(child,(1,1))

                if temp_f_score < f_score[child]:
                    g_score[child]= temp_g_score
                    f_score[child]= temp_f_score
                    open.put((temp_f_score,h(child,(1,1)),child))
                    aPath[child]=currCell
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[aPath[cell]]=cell
        cell=aPath[cell]
    return fwdPath

if __name__=='__main__':
    m=maze(10,10)
    m.CreateMaze()
    path=aStar(m)

    a=agent(m,footprints=True)
    m.tracePath({a:path})
    l=textLabel(m,'A Star Path Length',len(path)+1)

    m.run()