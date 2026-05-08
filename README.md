
  - An explanation of the purpose of each file in your repository.  
    
    **MohaleFunction.py: This holds the code for the game to be run**  
    **responses.json: Used in MohaleFunction to automate responses to certain actions that the user takes**    
    **actions.json: Used in MohaleFunction to represent all actions that can be taken by the user**  
    **items.json: Used in MohaleFunction to represent all items that are available in the game**  
    **places.json: Used in MohaleFunction to represent all the places the user can go in the game**  

**Run it in a Python code runner(Visual Studio -> type python3 MohaleFunction.py) and make sure to import the MohaleFunction.py and all json files into the same folder along with the same names as seen in the repository. We do not use any command line arguments**
  
  - Clear instructions on how to use your program and/or interpret the output of the program. Anything the user might encounter while using your 
  program that a random person on the street would not find self-explanatory needs to be explained in your instructions.

**Objective of the game:**
The main goal of the game is to explore the map, taking and using items in the quest to collect two main items. To win the game, you need to take the diamond egg and the sorcerer's stone

**Movement:**
The player can move by using either the name of a nearby location or a cardinal direction(north, west,etc)/(left,right, forward, back)

The specific movement commands are "go", "walk", "move", "run". There is a special case location (kitchen and underground entrance) that can only be moved back and forth using the "open trapdoor" command

**Items:**
You can use the look command to see any items in the room or a hint of a potentially hidden one. There are many ways you can interact with an item, such as "take", "get", "grab", "pick" for any item that can be picked, "open" or "lift" for a specific item that can be opened, "use" or "turn on" for items such as the flashlight which can be used, or even "drink" an item. 

You can check what items you have taken by using the "inventory", "inv" commands

**Help or end game:**
You can end the game by typing "q" or "quit" and you can get a hint by typing in "?" or "help" which will list some helpful actions you can take

**Sample:**

Move right --> moves to the room on the right if possible

turn on flashlight --> Turns on flashlight

open chest --> opens chest

walk to living room --> moves player to living room if possible

**Annotated Bibliography**

Python re.escape() method. (n.d.). Tutorial Point. Retrieved May 8, 2026, from https://www.tutorialspoint.com/python/python_re_escape_method.htm

**Used this source to figure out how the re.escape command works so I can use it to handle cases where the input has a space/special keys**

Zork I. (n.d.). Retrieved May 8, 2026, from http://retinal.dehy.de/docs/doku.php?id=miscellaneous:games:zork_i

**Research on the background of the game and the specific objectives and tasks that occur in the game**

Zork I Map. (n.d.). Untitled. Retrieved May 8, 2026, from https://www.mocagh.org/infocom/zork-map-front.pdf

**Used to base our own map layout to be similar to the original Zork game.**
ZORK I: The Great Underground Empire. (n.d.). MIT. Retrieved May 8, 2026, from https://web.mit.edu/marleigh/www/portfolio/Files/zork/transcript.html

**Shows the actions and what a live run-through of Zork would look like. We based the actions and movement on this transcript.**

Zork I: The Great Underground Empire/Walkthrough. (n.d.). STRATEGYWIKI. Retrieved May 8, 2026, from https://strategywiki.org/wiki/Zork_I:_The_Great_Underground_Empire/Walkthrough

**We based our game progression and the necessities to win on this walkthrough.**  

BD103. (2020, December 7). A simple function that scrolls text to the Python console. GithubGist. Retrieved May 8, 2026, from https://gist.github.com/BD103/f89ef60a57aedd68394b38b8f22584d5  

**We used this function to make text printed to the console appear one character at a time, and added an optional flag set through the Game class to disable it**  

Python Software Foundation. (2000). time — Time access and conversions — Python 3.7.2 documentation. Python.org. Retrieved May 8, 2026, from https://docs.python.org/3/library/time.html  

**This was used both in the text scroll and to measure the time it takes for the player to beat the game, using time.sleep() and time.time().**

###  

| Function/Method | Author | Technique |
| -------- | ------ | --------- |
| Game.\_\_init\_\_ | Andrew | with statement |
| look() | Andrew | f-strings |
| updatePlayerPosition() | Jai | max(), sequence unpacking |
| Regex() | Thomas | regular expression |
| win() | Thomas | list comprehension |
| action() | Jai | N/A |

