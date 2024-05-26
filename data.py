import sys
import os
library_path = os.path.join(os.path.dirname(__file__), '.', 'Library')
sys.path.append(library_path)
library_path = os.path.join(os.path.dirname(__file__), '.', 'Algorithm')
sys.path.append(library_path)
from maze import maze
import DFS
import BFS
from aStar import aStar
from dijkstra import dijkstra

import csv
import random
import time

num_runs = 1

results_search = []
results_time = []
results_path = []

for _ in range(num_runs):
    row = 50
    col = 50
    m = maze(row, col)
    x = random.randint(1, row)
    y = random.randint(1, col)
    start = (x, y)
    endX = random.randint(1, row)
    endY = random.randint(1, col)
    m.CreateMaze(endX, endY, loopPercent=10.0)
    start_time = time.time()
    dSearch, dfsPath, dfwdPath = DFS.DFS(m, start)
    end_time = time.time()
    DFS_time = end_time - start_time
    start_time = time.time()
    bSearch, bfsPath, bfwdPath = BFS.BFS(m, start)
    end_time = time.time()
    BFS_time = end_time - start_time
    start_time = time.time()
    aSearch, aPath, afwdPath = aStar(m, start)
    end_time = time.time()
    AStar_time = end_time - start_time
    start_time = time.time()
    path,c, step=dijkstra(m,start)
    end_time = time.time()
    Dijkstra_time = end_time - start_time

    results_search.append([len(dSearch), len(bSearch), len(aSearch), step])
    results_time.append([DFS_time, BFS_time, AStar_time, Dijkstra_time])
    results_path.append([len(dfwdPath), len(bfwdPath), len(afwdPath), len(path)])

with open('results_search.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(results_search)

with open('results_time.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(results_time)

with open('results_path.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(results_path)