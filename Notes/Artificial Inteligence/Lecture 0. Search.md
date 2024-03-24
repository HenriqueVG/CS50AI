#cs50 #harvard #ai #course #python #introduction #search

-------------
# Search

[[Search problems]] involve an agent that is given an initial state and a goal state, and it returns a solution of how to get from the former to the latter. A navigator app uses a typical search process, where the agent (the thinking part of the program) receives as input your current location and your desired destination, and, based on a search algorithm, returns a suggested path. However, there are many other forms of search problems, like puzzles or mazes.

![[15Puzzle.png]]

Finding a solution to a 15 puzzle would require the use of a search algorithm.

- ### Agent 
	An entity that perceives its environment and acts upon that environment. In a navigator app, for example, the agent would be a representation of a car that needs to decide on which actions to take to arrive at the destination. 

- ### State
	A configuration of an agent in its environment. For example, in a [15 puzzle](https://en.wikipedia.org/wiki/15_puzzle), state is any one way that all the numbers are arranged on the board. ^8f6117
	- #### Initial State
		The state from which the search algorithm starts. In a navigator app, that would be the current location. ^343f56

- ### Actions
	 Choices that can be made in a state. More precisely, actions can be defined as a function. Upon receiving state `s` as input, `Actions(s)` returns as output the set of actions that can be executed in state `s`. For example, in a _15 puzzle_, the actions of a given state are the ways you can slide squares in the current configuration (4 if the empty square is in the middle, 3 if next to a side, 2 if in the corner).
 ^fb9f0a
- ### Transition Model
    A description of what state results from performing any applicable action in any state. More precisely, the transition model can be defined as a function. Upon receiving state `s` and action `a` as input, `Results(s, a)` returns the state resulting from performing action `a` in state `s`. For example, given a certain configuration of a _15 puzzle_ (state `s`), moving a square in any direction (action `a`) will bring to a new configuration of the puzzle (the new state).

- ### State Space
    The set of all states reachable from the initial state by any sequence of actions. For example, in a 15 puzzle, the state space consists of all the 16!/2 configurations on the board that can be reached from any initial state. The state space can be visualized as a directed graph with states, represented as nodes, and actions, represented as arrows between nodes.
    
![[15PuzzleState.png]]

- ### Goal Test
    The condition that determines whether a given state is a goal state. For example, in a navigator app, the goal test would be whether the current location of the agent (the representation of the car) is at the destination. If it is — problem solved. If it’s not — we continue searching.
     ^e514c9
- ### Path Cost
    A numerical cost associated with a given path. For example, a navigator app does not simply bring you to your goal; it does so while minimizing the path cost, finding the fastest way possible for you to get to your goal state. ^444e3b

-------------
# Solving Search Problems

- **Solution**
	A sequence of actions that leads from the [[#^343f56|initial state]] to the goal state.
	- **Optimal Solution**
        A solution that has the lowest [[#^444e3b|path cost]] among all solutions.

In a search process, data is often stored in a **_node_**, a data structure that contains the following data:
- A _[[#^8f6117|state]]_
- Its _parent node_, through which the current node was generated
- The _[[#^fb9f0a|action]]_ that was applied to the state of the parent to get to the current node
- The _path cost_ from the initial state to this node

_Nodes_ contain information that makes them very useful for the purposes of [[search algorithms]]. They contain a _state_, which can be checked using the _[[#^e514c9|goal test]]_ to see if it is the final state. If it is, the node’s _path cost_ can be compared to other nodes’ _path costs_, which allows choosing the _optimal solution_. Once the node is chosen, by virtue of storing the _parent node_ and the _action_ that led from the _parent_ to the current node, it is possible to trace back every step of the way from the _initial state_ to this node, and this sequence of actions is the _solution_.

However, _nodes_ are simply a [[data structure]]— they don’t search, they hold information. To actually search, we use the **[[frontier]]**, the mechanism that “manages” the _nodes_. The _frontier_ starts by containing an initial state and an empty set of explored items, and then repeats the following actions until a solution is reached:
```
Repeat:
	1. If the frontier is empty,
	       - Stop.There is no solution to the problem.
	2. Remove a node from the frontier. This is the node that will be considered.
	3. If the node contains the goal state,
			- Return the solution. Stop.
Else: 
	 - Expand the node (find all the new nodes that could be reached from this node), and add resulting nodes to the frontier;
	- Add the current node to the explored set.
```

## [[Depth-First Search]]
In the previous description of the _frontier_, one thing went unmentioned. At stage 1 in the pseudocode above, which node should be removed? This choice has implications on the quality of the solution and how fast it is achieved. There are multiple ways to go about the question of which nodes should be considered first, two of which can be represented by the data structures of **stack** (in _depth-first_ search) and **queue** (in _breadth-first search_; and [here is a cute cartoon demonstration](https://www.youtube.com/watch?v=2wM6_PuBIxY) (of the difference between the two).

We start with the _depth-first_ search (_DFS_) approach.

A _depth-first_ search algorithm exhausts each one direction before trying another direction. In these cases, the frontier is managed as a _stack_ data structure. The catchphrase you need to remember here is <mark style="background: #FF5582A6;">“last-in first-out. After nodes are being added to the frontier, the first node to remove and consider is the last one to be added. This results in a search algorithm that goes as deep as possible in the first direction that gets in its way while leaving all other directions for later.</mark>

> [!Example]
> Take a situation where you are looking for your keys. In a _depth-first_ search approach, if you choose to start with searching in your pants, you’d first go through every single pocket, emptying each pocket and going through the contents carefully. You will stop searching in your pants and start searching elsewhere only once you will have completely exhausted the search in every single pocket of your pants.

- Pros:
    - At best, this algorithm is the fastest. If it “lucks out” and always chooses the right path to the solution (by chance), then _depth-first_ search takes the least possible time to get to a solution.
- Cons:
    - It is possible that the found solution is not optimal.
    - At worst, this algorithm will explore every possible path before finding the solution, thus taking the longest possible time before reaching the solution.

Code example:
```python
# Define the function that removes a node from the frontier and returns it
def remove(self):
	# Terminate the search if the frontier is empty, because this means that there is no solution
	if self.empty():
		raise Exception("empty frontrier")
	else:
		# Save the last item in the list (which is the newest node added)
		node = self.frontier[-1]
		# Save all the items on the list besides the last node (i.e. removing the last node)
		self.frontier = self.frontier[:-1]
		return node
```

## [[Breadth-First Search]]

The opposite of _depth-first_ search would be _breadth-first_ search (_BFS_).

A _breadth-first_ search algorithm will follow multiple directions at the same time, taking one step in each possible direction before taking the second step in each direction. In this case, the frontier is managed as a _queue_ data structure. The catchphrase you need to remember here is <mark style="background: #FF5582A6;">"first-in first-out.” In this case, all the new nodes add up in line, and nodes are being considered based on which one was added first (first come first served!). This results in a search algorithm that takes one step in each possible direction before taking a second step in any one direction.</mark>

> [!Example]
> Suppose you are in a situation where you are looking for your keys. In this case, if you start with your pants, you will look in your right pocket. After this, instead of looking at your left pocket, you will take a look in one drawer. Then on the table. And so on, in every location you can think of. Only after you will have exhausted all the locations will you go back to your pants and search in the next pocket.

- Pros:
    - This algorithm is guaranteed to find the optimal solution.
- Cons:
    - This algorithm is almost guaranteed to take longer than the minimal time to run.
    - At worst, this algorithm takes the longest possible time to run.

Code Example:
```python
# Define the function that removes a node from the frontier and returns it.
    def remove(self):
    	  # Terminate the search if the frontier is empty, because this means that there is no solution.
        if self.empty():
            raise Exception("empty frontier")
        else:
            # Save the oldest item on the list (which was the first one to be added)
            node = self.frontier[0]
            # Save all the items on the list besides the first one (i.e. removing the first node)
            self.frontier = self.frontier[1:]
            return node
```

