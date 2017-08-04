# ReadMe

This project is a console interface for selecting and executing bash commands

*Works only in Linux based systems (including Mac)*

Provided example looks like this:  
![image 1](http://thephisics101.eu/images/image-1.png)

# Structure

The `nodes` variable is the one that holds the information about the display and execution

## Selectable

`Selectable` is the parent class of `Option` and `Node`

### Option

**`Option(name, command)`**

`name` sets the display name for the option

`command` sets the command which will be executed

### Node

Nodes can hold other nodes and options

**`Node(name)`**

`name` sets the display name of the node  

**`Node.add_children(*args)`**

`*args` are the nodes and options, can be chained

# Controls

<kbd>⭡</kbd> and <kbd>⭣</kbd> to navigate between `Selectable`s

<kbd>⭠</kbd> and <kbd>⭢</kbd> to navigate between `Node`s

<kbd>⮠</kbd> to select current `Option`

<kbd>Ctrl</kbd>+<kbd>C</kbd> to exit without selecting

<kbd>h</kbd> to show the help menu

# Running

This programm can be run with python 3

`python3 main.py`
