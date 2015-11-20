# search_problem

Finding Paths
_______________________________

It can run on your terminal with command in following.

**DFS Finding Paths**

python pacman.py -l tinyMaze -p SearchAgent  ---- This command use tinyMaze as the map for searching.

python pacman.py -l mediumMaze -p SearchAgent ---- This use mediumMaze.

python pacman.py -l bigMaze -z .5 -p SearchAgent ---- This is for bigMaze.

_____________________________________________________

**BFS Finding Paths**

python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs ----- This command use mediumMaze as the map for searching

python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5 ----- This use bigMaze

If Pacman moves too slowly for you, try the option --frameTime 0 after any command.

_____________________________________________________


















________________________________________________________

The Pacman board will show an overlay of the states explored, 
and the order in which they were explored (brighter red means earlier exploration).
