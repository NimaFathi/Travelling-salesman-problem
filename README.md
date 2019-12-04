# Travelling-salesman-problem
TSP Problem using A*.
In implementation I used addmissible heuristic:
<b>H(x)</b> = distance between X and nearest unvisited city(Y) + Approximate distance to visit all unvisited city from X + distance from starting city to nearest unvisitded city(Y).
because our heuristic is not consistant we need to do backtracking.
to calculate H(x) and especially to calculate approximate distance to visit all cities we use minimum spanning tree and for that I implemented Kruskal algorithm.
