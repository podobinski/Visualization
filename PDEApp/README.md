# Partial Differential Equation App
This app visualizes, how different PDE Solvers solve different PDEs. The user can interactively change stepwidth (in time and space) and initial condition. One can also choose from 2 different solvers (explicit Euler, implicit Euler, implicit midpoint rule) and 2 different PDEs (Heat transport and wave equation) as well as from an implicit and an explicit solver for each PDE.

## Running
Enter 
```
$ bokeh-server --script run_app.py
```
in bash to run the app. Then enter
```
http://localhost:5006/bokeh/pde
```
in your browser to use the app in it.

##ToDos
- [x] publish this to the internet
- [ ] Add "PLAY" button for continuous time.
- [ ] Add code for embedding.