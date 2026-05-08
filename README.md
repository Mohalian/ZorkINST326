### TO DO:  
- Add optional conditions to allow for things like keys or a flashlight to be held/used to go between places (like the kitchen and the underground) (IMPORTANT!)
- Allow for aliases to be used to refer to actions/items (should be relatively simple to add to existing functions)
- Add a drop item function
- Create a win condition <---Main emphasis here
- Finish action function <---Main emphasis here
- Fill out below:

  - An explanation of the purpose of each file in your repository.
    
    **MohaleFunction.py: This holds the code for the game to be run
    responses.json: Used in MohaleFunction to automate responses to certain actions that the user takes
    actions.json: Used in MohaleFunction to represent all actions that can be taken by the user
    items.json: Used in MohaleFunction to represent all items that are available in the game
    places.json: Used in MohaleFunction to represent all the places the user can go in the game**
    
  - Clear instructions on how to run your program from the command line. You do not need to explain how to run the program on Windows and on MacOS; 
  just pick one. If your program takes command-line arguments, please document the command-line interface (which arguments are required? which are 
  optional, if any? what data types are you looking for? are there a specific format for data files? etc.)

**Run it in a Python code runner(Visual Studio -> type python3 MohaleFunction.py) and make sure to import the MohaleFunction.py and all json files into the same folder along with the same names as seen in the repository. We do not use any command line arguments**
  
  - Clear instructions on how to use your program and/or interpret the output of the program. Anything the user might encounter while using your 
  program that a random person on the street would not find self-explanatory needs to be explained in your instructions.
  
  - An annotated bibliography of all sources you used to develop your project, including sources of data, sources of background information about
  your project topic, and sources about Python programming that informed specific aspects of your code. For each source, explain how you used the 
  source. You do not need to cite any INST 326 course materials.

**Reference**

Zork I. (n.d.). Retrieved May 8, 2026, from http://retinal.dehy.de/docs/doku.php?id=miscellaneous:games:zork_i

Zork I Map. (n.d.). Untitled. Retrieved May 8, 2026, from https://www.mocagh.org/infocom/zork-map-front.pdf

ZORK I: The Great Underground Empire. (n.d.). MIT. Retrieved May 8, 2026, from https://web.mit.edu/marleigh/www/portfolio/Files/zork/transcript.html

Zork I: The Great Underground Empire/Walkthrough. (n.d.). STRATEGYWIKI. Retrieved May 8, 2026, from https://strategywiki.org/wiki/Zork_I:_The_Great_Underground_Empire/Walkthrough
  
  - Attribution: in order to evaluate whether each member has made a substantial, original contribution to the project, please provide a table like 
  the one below, with a separate row for each method or function.

| Function/Method | Author | Technique |
| -------- | ------ | --------- |
| Game.\_\_init\_\_ | Andrew | with statement |
| look() | Andrew | f-strings |
| updatePlayerPosition() | Jai | max(), sequence unpacking |
| Regex() | Thomas | regular expression |
| win() | Thomas | list comprehension |

