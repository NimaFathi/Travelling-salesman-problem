# Travelling-salesman-problem
TSP Problem using A*.<br>
In implementation I used addmissible heuristic:<br>
<b>H(x)</b> = distance between X and nearest unvisited city(Y) + Approximate distance to visit all unvisited city from X + distance from starting city to nearest unvisitded city(Y).<br>
because our heuristic is not consistant we need to do backtracking.<br>
to calculate H(x) and especially to calculate approximate distance to visit all cities we use minimum spanning tree and for that I implemented Kruskal algorithm.<br>
I also just used numpy to implement Astar without any Node or Graph class so that is very straight forward.

