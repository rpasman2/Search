# search.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
# 
# Created by Michael Abir (abir2@illinois.edu) on 08/28/2018

"""
This is the main entry point for MP1. You should only modify code
within this file -- the unrevised staff files will be used for all other
files and classes when code is run, so be careful to not modify anything else.
"""
# Search should return the path and the number of states explored.
# The path should be a list of tuples in the form (row, col) that correspond
# to the positions of the path taken by your search algorithm.
# Number of states explored should be a number.
# maze is a Maze object based on the maze from the file specified by input filename
# searchMethod is the search method specified by --method flag (bfs,dfs,greedy,astar)

from collections import deque
import heapq

def getManhattanDistance(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def search(maze, searchMethod):
    return {
        "bfs": bfs(maze),
        "dfs": dfs(maze),
        "greedy": greedy(maze),
        "astar": astar(maze),
    }.get(searchMethod, [])
   

                
def bfs(maze):
    start = maze.getStart()
    if maze.isObjective(start[0], start[1]):
        return [start], 1
    frontier = deque([[start]])
    explored = []
    path = [start]
    while frontier:
        path = frontier.pop()
        node = path[-1]
        if not((node in explored)):
            explored.append(node)
        if maze.isObjective(node[0], node[1]):
            return path, len(explored)
        frontier_nodes = list(map(lambda x: x[-1], frontier))
        for child in maze.getNeighbors(node[0], node[1]):
            if child not in explored and child not in  frontier_nodes:
                newpath = list(path)
                newpath.append(child)
                frontier.appendleft(newpath)
                
    


def dfs(maze):
    # TODO: Write your code here
    # return path, num_states_explored
    start = maze.getStart()
    if maze.isObjective(start[0], start[1]):
        return [start], 1
    frontier = deque([[start]])
    explored = []
    path = [start]
    while frontier:
        path = frontier.pop()
        node = path[-1]
        if not((node in explored)):
            explored.append(node)
        if maze.isObjective(node[0], node[1]):
            return path, len(explored)
        frontier_nodes = list(map(lambda x: x[-1], frontier))
        for child in maze.getNeighbors(node[0], node[1]):
            if child not in explored and child not in  frontier_nodes:
                newpath = list(path)
                newpath.append(child)
                frontier.append(newpath)
                

                


def greedy(maze):
    # TODO: Write your code here
    # return path, num_states_explored
    start = maze.getStart()
    end = maze.getObjectives()[0]
    if maze.isObjective(start[0], start[1]):
        return [start], 1
    frontier = []
    explored = []
    path = [start]
    heapq.heappush(frontier, (getManhattanDistance(start,end), [start]))
    while frontier:
        path = heapq.heappop(frontier)[1]
        node = path[-1]
        print(node)
        if not((node in explored)):
            explored.append(node)
        if maze.isObjective(node[0], node[1]):
            return path, len(explored)
        frontier_nodes = list(map(lambda x: x[1][-1], frontier))
        for child in maze.getNeighbors(node[0], node[1]):
            dist = getManhattanDistance(child, end)
            if child not in explored and child not in  frontier_nodes:
                newpath = list(path)
                newpath.append(child)
                heapq.heappush(frontier, (dist, newpath))               



def astar(maze):
    # TODO: Write your code here
    # return path, num_states_explored
    start = maze.getStart()
    end = maze.getObjectives()[0]
    if maze.isObjective(start[0], start[1]):
        return [start], 1
    frontier = []
    explored = []
    path = [start]
    heapq.heappush(frontier, (getManhattanDistance(start,end), [start]))
    while frontier:
        path = heapq.heappop(frontier)[1]
        node = path[-1]
        print(node)
        if not((node in explored)):
            explored.append(node)
        if maze.isObjective(node[0], node[1]):
            return path, len(explored)
        frontier_nodes = list(map(lambda x: x[1][-1], frontier))
        for child in maze.getNeighbors(node[0], node[1]):
            dist = getManhattanDistance(child, end)
            if child not in explored and child not in  frontier_nodes:
                newpath = list(path)
                newpath.append(child)
                heapq.heappush(frontier, (dist + len(newpath), newpath))    
                
