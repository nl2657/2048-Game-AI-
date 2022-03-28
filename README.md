# 2048-Game-AI-Homework Assignment for Artificial Intelligence
AI that plays the 2048 game successfully (reaches around 4096)

I wrote the IntelligentAgent.py file which codes for a expectiminimax algorithm in order to sucessfully play the 2048 game. Program uses Alpha-beta pruning to eliminate irrelevant branches. Uses heuristic functions to predict best future move combinations.

The skeleton code includes the following files. 
   •Provided: GameManager.py. This is the driver program that loads your Computer AI and Player AI and
begins a game where they compete with each other. See below on how to execute this program.

   •Provided: Grid.py This module defines the Grid object, along with some useful operations: move(),
getAvailableCells(), insertTile(), and clone(), which you may use in your code. These are by no
means the most efficient methods available, so if you wish to strive for better performance, feel free to ignore
these and write your own helper methods in a separate file.

   •Provided: BaseAI.py This is the base class for any AI component. All AIs inherit from this module, and
implement the getMove() function, which takes a Grid object as parameter and returns a move (there are
different ”moves” for different AIs).

   •Provided: ComputerAI.py. This inherits from BaseAI. The getMove() function returns a computer
action that is a tuple (x, y) indicating the place you want to place a tile.

   •I wrote: IntelligentAgent.py. You will create this file. The IntelligentAgent class should inherit from
BaseAI. The getMove() function to implement must return a number that indicates the player’s action. In
particular, 0 stands for ”Up”, 1 stands for ”Down”, 2 stands for ”Left”, and 3 stands for ”Right”.
This is where your player-optimizing logic lives and is executed. Feel free to create submodules for this file to
use, and include any submodules in your submission.

    •Provided: BaseDisplayer.py and Displayer.py. These print the grid.

execute the game manager like so: $ python3 GameManager.py
