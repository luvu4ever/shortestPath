from agent import *
from COLOR import *
from maze import maze
from textLabel import textLabel

def RCW():
    global direction
    k=list(direction.keys())
    v=list(direction.values())
    v_rotated=[v[-1]]+v[:-1]
    direction=dict(zip(k,v_rotated))

def RCCW():
    global direction
    k=list(direction.keys())
    v=list(direction.values())
    v_rotated=v[1:]+[v[0]]
    direction=dict(zip(k,v_rotated))

def moveForward(cell):
    if direction['forward']==3:
        return (cell[0],cell[1]+1),3
    if direction['forward']==0:
        return (cell[0],cell[1]-1),0
    if direction['forward']==1:
        return (cell[0]-1,cell[1]),1
    if direction['forward']==2:
        return (cell[0]+1,cell[1]),2

def wallFollower(m, goal=(1,1)):
    global direction
    direction={'forward':1,'left':0,'back':2,'right':3}
    currCell=(m.rows,m.cols)
    path=[]
    while True:
        if currCell== goal:
            break
        if m.maze_map[currCell][direction['left']]==0:
            if m.maze_map[currCell][direction['forward']]==0:
                RCW()
            else:
                currCell,d=moveForward(currCell)
        else:
            RCCW()
            currCell,d=moveForward(currCell)
        path.append(currCell)
    # path2=path
    # while 'EW' in path2 or 'WE' in path2 or 'NS' in path2 or 'SN' in path2:
    #     path2=path2.replace('EW','')
    #     path2=path2.replace('WE','')
    #     path2=path2.replace('NS','')
    #     path2=path2.replace('SN','')
    return path
        


if __name__=='__main__':
    myMaze=maze(10,10)
    myMaze.CreateMaze(loopPercent=1)
    goal = (4,4)
    b=agent(myMaze, goal = goal, color=COLOR.yellow)
    path=wallFollower(myMaze, goal)
    # myMaze.tracePath({a:path})
    myMaze.tracePath({b:path})

    print(path)
    myMaze.run()