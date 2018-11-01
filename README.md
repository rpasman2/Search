# Search

Basic Pathfinding

I consider the problem of finding the shortest path from a given start state while eating one or more dots or "food pellets."  The maze layout is given in a simple text format, where '%' stands for walls, 'P' for the starting position, and '.' for the dot(s) (see sample maze file). All step costs are equal to one.
I implement the state representation, transition model, and goal test needed for solving the problem in the general case of multiple dots. I also implement a unified top-level search routine that can work with all of the following search strategies.

Depth-first search
Breadth-first search
Greedy best-first search
A* search (using manhattan distance)
