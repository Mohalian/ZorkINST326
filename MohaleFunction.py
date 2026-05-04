import json
import pandas as pd
import re

with open("responses.json", "r", encoding="utf-8") as file:
    responses = json.load(file)
    

class Player:
    """
    Contains and handles player data
    
    Attributes:
        pos: dictionary in form {"x": int, "y": int}, current coordinate 
            position of the player
        inventory: list of items the player is holding
    """
    def __init__(self, starting_pos):
        self.pos = starting_pos
        self.subplace = "frontofdoor"
        self.inventory = []
        

    def updatePlayerPostion(self, choice, boardSize):
        """
    This function changes the player position and makes sure the user enters a
    valid movement command
    
     Args:
       choice: command entered by the user, has to have the specific command
       move + a direction(string)
       player_pos: Contains the x and y loc of the player(dict, keys either "x"
       or "y")
       boardSize: the size of the playable map(int)
       
    Side effects:
        Changes player_pos

    Returns: 
        player_pos: the new position of the player (dict)
    """
    
        keepLoop = True
        xLoc = self.pos["x"]
        yLoc = self.pos["y"]
    
        while keepLoop:
        
            if "move" not in choice:
                print("Not a movement command")
                return self.pos
    
            if "move north" in choice:
        
                yLoc = self.pos["y"]-1
            
    
            elif "move south" in choice:
        
                yLoc = self.pos["y"]+1
            
    
            elif "move west" in choice:
        
                xLoc = self.pos["x"]-1
            
    
            elif "move east" in choice:
        
                xLoc = self.pos["x"]+1
    
            else:
                choice = input("Movement command is move + (North, South, East, \
                        West): ").lower()
                continue  
      
            if xLoc >= boardSize or xLoc < 0 or yLoc >= boardSize or yLoc < 0:
            
                choice = input("You've been blocked by thick trees, \
                           find another command: ").lower()
                continue
        
            self.pos["x"] = xLoc
            self.pos["y"] = yLoc
            keepLoop = False
    
        return self.pos
        
    def inventory_update(self, player, room, item_word, pick_drop):
        """
        Appends item objects into player's inventory list and removes from room's
        items list (pickup)or removes from player inventory and appends to room's
        item list (drop)
        
        Args:
            player: Player class instance
            room: Room class instance
            item_word: (str) inputted item word
            file: (filepath) filepath to item words dictionary
            pick_drop: (boolean) True if picking up, False if dropping
            
        Side effects:
            removes/appends to player's inventory attribute list
            removes/appends to room's items attribute list
            prints error, dropped, or picked up messages
            
        """
        with open("items.json", "r", encoding="utf-8") as f:
            item = json.load(f)
        item_word = item_word.lower()
        item_name = None
        item_obj = None
        for key, value in item:
            if item_word == key or item_word in value["aliases"]:
                item_name = key
                break
        if not item_name:
            print(responses["items"]["nonexistentitem"])
            return
        
        if pick_drop:
            for item in room.items:
                if item.name.lower() == item_name:
                    item_obj= item
                    break    
            if not item_obj:
                print(responses["items"]["item_not_here"])
                return
            room.items.remove(item_obj)
            player.inventory.append(item_obj)
            print(responses["items"]["pickup_success"])
            
        else:
            for item in player.inventory:
                if item.name == item_name:
                    item_obj = item
                    break
            if not item_obj:
                print(responses["items"]["dropped_fail"])
                return
            player.inventory.remove(item_obj)
            room.items.append(item_obj)
            print(responses["items"]["dropped"])


    # Integrate the following existing functions into this class?
    # def updatePlayerPosition(self, choice, boardsize):
    
    # def inventoryUpdate(self, item_word, file, pick_drop):
  
class Item:
    
    def __init__(self, name, aliases, portable, interactions, description, position):
        self.name = name
        self.aliases = aliases
        self.portable = portable
        self.interactions = interactions
        self.description = description
        self.position = position

class Place:
    
    def __init__(self, name, onentertext, description, position):
        self.name = name
        self.onentertext = onentertext
        self.description = description
        self.position = position
        
class Game:
    
    def __init__(self):
        with open("items.json", "r", encoding="utf-8") as itemfile:
            self.items = {}
            item_dict = json.load(itemfile)
            for key, value in item_dict.items():
                self.items[key] = Item(key, value["aliases"], value["portable"], value["interactions"], value["description"], value["position"])
                
        with open("place.json", "r", encoding="utf-8") as placefile:
            self.places = {}
            place_dict = json.load(placefile)
            for key, value in place_dict.items():
                self.places[key] = Place(key, value["on-enter_text"], value["description"], value["location"])
                

           
                



def can_interact(target_actions, player_action, item=None):
    """
    Checks if a player's interaction with a target object is valid or not
    
    Args:
        allowed_actions: tuple of tuples in form (action_taken, req_item=None)
            where each item is a string, represents the actions allowed to be
            taken on the target object, and the required item to do so
        player_action: string of what the player is attempting to do
        item: optional string of the item to be used with the action
        
    Side Effects:
        Prints a message to console if an item is needed/used to perform an
        action, or if the action cannot be completed
        
    Returns:
        True if the player action is valid and can occur, False if it is not
    
    """
    
    for action in target_actions:
        
        if player_action == action[0]:
            
            if action[1] == item and item != None:
                print(f"You used the {action[1]}.")
                return True
            
            elif action[1] == None:
                return True
            
            elif action[1] != item and item != None:
                print(f"Wrong item, you need a {action[1]} to do that.")
                return False
            
            elif action[1] != item:
                print(f"You need a {action[1]} to do that.")
                return False                
            
    print("You can't do that.")
    return False       

def get_player_input(input, objects, actions):
    """
    Takes an input as a string and parses through to find an action and an
    object that will be used later.

    Args:
        input: (str) Users input of an action and an object
        objects: (list) List of acceptable objects as strings
        actions: (list) List of acceptable actions as strings

    Side effects:
        prints "Invalid input" if user's input is not at least two words
        prints "Invalid action" if first word is not in action list
        prints "Couldn't find item" if none of the other words are in the
        object list
    Returns:
        verb(str), object(str) tuple of selected action and object as strings
    """
    words = input.lower().strip().split(" ")
    if len(words) < 2:
        print("Invalid input")
        return None, None
    verb = words[0]
    if not verb in actions:
        print("Invalid action")
    for i in range(1, len(words)):
        if words[i] in objects:
            return verb, words[i]
    print("Couldn't find item")
    return None, None

def construct_gameboard(player, items, places, boardSize=5):
    """
    Takes a board size and a json dictionary of in-game objects and creates a 
    coordinate map of the objects that can be traversed by the player
    
    Args:
        player: a player object
        items: a list of item objects (from the game.items attribute)
        places: a list of place objects (from the game.places attribute)
    Returns:
        gameboard: a pandas data frame representing the coordinate map, where
            columns represent the x-axis and rows represent the y-axis flipped. 
            Each cell is a list with every object it contains at that position, 
            and can include the player
    """
    YBOUND = range(0,boardSize)
    XBOUND = range(0,boardSize)
    gameboard = pd.DataFrame(index=YBOUND,columns=XBOUND)
    for y in YBOUND:
        for x in XBOUND:
            gameboard.loc[y,x] = []
    
    for item, val in items.items():
        x = item.position[0]
        y = item.position[1]
        gameboard.loc[y,x].append(item)
    for place in places:
        x = place.position[0]
        y = place.position[1]
        gameboard.loc[y,x].append(place)
    x = player.pos["y"]
    y = player.pos["x"]
    gameboard.loc[y,x].append(place)
    
    return gameboard

def get_player_pos(player, gameboard):
    """
    Checks the players current position
    
    Args:
        player: class object representing the player on the gameboard
        gameboard: dataframe as a coordinate grid
        
    Returns:
        The players current coordinate position as a tuple, if it is not found
        on the gameboard then it returns None
    """
    boardSize = len(gameboard.columns)
    for y in range(0,boardSize):
        for x in range(0, boardSize):
            if player in gameboard.loc[y,x]:
                return {"x":x,"y":y}
    return None

def look(player_pos, gameboard, direction=None):
    """
    Shows what objects are at the player's current or nearby coordinate
    
    Args:
        player_pos: player's current coordinate position in dictionary form
            {"x":int, "y":int}
        gameboard: gameboard dataframe
        direction: optional string, specified direction in command
        
    """
    x = player_pos["x"]
    y = player_pos["y"]
    
    if direction == "north":
        y -= 1
    if direction == "south":
        y += 1
    if direction == "west":
        x -= 1
    if direction == "east":
        x += 1
    
    if len(gameboard.loc[y,x]) > 1:
        for object in gameboard.loc[y,x]:
            if (isinstance(object, Player) == False) and direction == None:
                print(f"There is a {object.name} here.")
            elif (isinstance(object, Player) == False):
                print(f"There is a {object.name} there.")
    else:
        if direction == None:
            print("There is nothing here")
        else: 
            print("There is nothing there")
            
def action(player, input, gameboard, gameclass):
    action_word = ""
    item_word = ""
    place_word = ""
    action_match = re.search(r"(move|go|drink|take|drop)", input)
    if action_match:
        action_word = action_match
        
    if (action_word == "move" or action_word == "go"):
        place_word = re.search(r"(east, west, north, south)")
        if place_word:
            player.updatePlayerPostion(place_word, player.pos)
            print(responses["movement"]["moved"])
    
    item_word = re.search(r"(purple\sdrink|trapdoor)", input)
    if item_word: 
        if item_word == "purple drink":
            if action_word == "take":
                x,y = gameclass.items["purpledrink"].position

                gameboard.loc[y,x].remove(gameclass.items["purpledrink"])
                player.inventory.append(gameclass.items["purpledrink"])
                print("Took Purple drink.")
            
            
            
def run():
    
    player = Player({"x": 0, "y": 0})
    print("start game")
    
    with open("place.json", "r") as f:
        places = json.load(f)
        
    with open("actions.json", "r", encoding="utf-8") as f:
        actions = json.load(f)
        
    with open("items.json", "r", encoding="utf-8") as f:
        items = json.load(f)
        
    keep_running = True
    
    while(keep_running):
        
        current_room = None
        
        for name, data in places.items():
            if data["location"] == [player.pos["x"], player.pos["y"]]:
                current_room = name
                print(f"[{name.upper()}]")
                print(data["on-enter_text"])
        user_input = input("\nCommand> ").lower().strip()
        if user_input == "quit" or user_input == "q":
            keep_running = False
        else:
            action(player,user_input,places,Game())


if __name__ == "__main__":
    run()
        
    


if __name__ == "__main__":
    run()
