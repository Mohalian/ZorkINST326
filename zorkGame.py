import json
import pandas as pd
import re



with open("responses.json", "r", encoding="utf-8") as file:
    responses = json.load(file)
with open("actions.json", "r", encoding="utf-8") as file:
    actionAll = json.load(file)




class Player:
    """
    Contains and handles player data
    
    Attributes:
        pos: dictionary in form {"x": int, "y": int}, current coordinate 
            position of the player
        inventory: list of items the player is holding
    """
    def __init__(self, starting_pos, game_data):
        self.pos = starting_pos
        self.inventory = []
        self.game_data = game_data
        self.drank = False
        self.flashlight = False
        self.paintinglifted = False
        self.chestopen = False
        self.trapdooropen = False
        

    def updatePlayerPosition(self, choice):
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
    
        
        xLoc = self.pos.location[0]
        yLoc = self.pos.location[1]
        passed = False
        
        directions = {
            ("east", "right"):[xLoc+1,yLoc],
            ("west", "left"):[xLoc-1,yLoc],
            ("north", "up"):[xLoc,yLoc+1],
            ("south", "down"):[xLoc,yLoc-1] 
            
        }
        
        for cardinal, reg in directions:
            
            if cardinal in choice or reg in choice:
                
                xLoc = directions[(cardinal,reg)][0]
                yLoc = directions[(cardinal,reg)][1]
                
                
                self.pos = self.check_inBounds(xLoc, yLoc)
                if self.pos.location[0] != xLoc or self.pos.location[1] != yLoc\
                    or self.pos.keyName == "undergroundentrance":
                    print("Trap door not open")
                    return self.pos
                
        listPlaces = self.game_data.places
        
        
            
        for place in listPlaces:
            
            if len([name for name in place.name if name in choice]) >0:
                
                if max(abs(self.pos.location[0]-place.location[0]),\
                abs(self.pos.location[1]-place.location[1])) > 1:
                    break
                
                if place.keyName == "undergroundentrance" and self.trapdooropen == False:
                    print   
                return place    
                    
        print(responses["general"]["invalid_target"])
    
        return self.pos
    
    def check_inBounds(self,xLoc, yLoc):
        
        for place in self.game_data.places:
            if place.location == [xLoc, yLoc]:
                return place
        
        return self.pos
             
    def inventory_update(self, room,item_name, pick_drop):
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
        
        if pick_drop:
            for item in room.items:
                if item.name.lower() in item_name.aliases:
                    item_obj= item
                    break    
            if not item_obj:
                print(responses["items"]["item_not_here"])
                return
            room.items.remove(item_obj)
            self.inventory.append(item_obj)
            print(responses["items"]["pickup_success"])
            
        

        
class Item:
    
    def __init__(self, keyName ,name, aliases, portable, interactions, description, position):
        self.keyName = keyName
        self.name = name
        self.aliases = aliases
        self.portable = portable
        self.interactions = interactions
        self.description = description
        self.position = position

class Game:
    
    def __init__(self, boardsize=4):
        self.items = []
        with open("items.json", "r", encoding="utf-8") as item_file:
            item = json.load(item_file)
            for key, value in item.items():
                self.items.append(Item(key, value["screen_name"],\
                    value["aliases"], value["portable"]\
                , value["interactions"], value["description"], \
                    value["position"]))
                
        self.places = []
        with open("place.json", "r", encoding="utf-8") as places_file:
            places = json.load(places_file)
            for key, value in places.items():
                self.places.append(Places(key,value["location"], value["name"], \
                    value["description"], value["on-enter_text"]))
                
                
        self.currLoc = [0,0]
        self.boardsize = boardsize
    """
    def construct_gameboard(self, player):
       
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
        
        YBOUND = range(0,self.boardsize)
        XBOUND = range(0,self.boardsize)
        gameboard = pd.DataFrame(index=YBOUND,columns=XBOUND)
        for y in YBOUND:
            for x in XBOUND:
                gameboard.loc[y,x] = []
        
        for item in self.items:
            print(self.items[item])
            print(self.items[item]["position"])
            x = self.items[item]["position"][0]
            y = self.items[item]["position"][1]
            gameboard.loc[y,x].append(item)
        for place in self.places:
            x = self.places[place]["location"][0]
            y = self.places[place]["location"][1]
            gameboard.loc[y,x].append(place)
        x = player.pos["y"]
        y = player.pos["x"]
        gameboard.loc[y,x].append(player)
        
        return gameboard            
"""
class Places:
    def __init__(self, keyName,location, name, description, on_enter_text):
        self.keyName = keyName
        self.location = location
        self.name = name
        self.description = description
        self.on_enter_text = on_enter_text


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
            
def action(player, input, game):
    action_word = ""
    item_word = ""
    place_word = ""
    
    allCommands = "("
    for action, names in actionAll.items():
        for alias in names:
            allCommands += f"{alias}|" 
    
    allCommands = f"{allCommands[:-1]})"
    action_match = re.search(allCommands, input)
    
    if action_match:
        action_word = action_match.group(0)
        
    if (action_word in actionAll["go"]):
        
        player.updatePlayerPosition(input)
        print(responses["movement"]["moved"])
        return
    elif action_word in actionAll["inventory"]:
        
        toPrint = ""
        for item in player.inventory:
            toPrint += (f"{item.name}, ")
        
        print(toPrint[:-2])
    
    get_item = "("
    for item in game.items:
        
        for alias in item.aliases:
            get_item += f"{alias}|" 
    
    get_item = f"{get_item[:-1]})"
    item_word= re.search(get_item, input)
      
    if item_word:
        words = item_word.group(0)
    
    if item_word: 
        
        itemToUse = None
        for item in game.items:
        
           if words in item.aliases:
               itemToUse = item
               break
        
        if itemToUse == None:
            print(responses["items"]["nonexistent_item"])        
        if action_word in itemToUse.interactions:
            if action_word in actionAll["take"]:
                
                if itemToUse.keyName == "sorcerers_stone" and \
                    player.drank == False:
                        print(responses["items"]["sorcerers_stone_fail"])
                player.inventory_update(player.pos,itemToUse, action_word)
            
            elif action_word in actionAll["drink"]:
                player.inventory.pop(itemToUse)
                player.drank = True
            
            elif (action_word in actionAll["open"] or \
                action_word in actionAll["lift"]):
                
                if itemToUse.name[0] == "trap door":
                    player.trapdooropen = True
                    player.updatePlayerPosition("entrance")
                    
                elif itemToUse.name[0] == "painting":
                    if player.paintinglifted:
                        print(responses["items"]["painting_already_lifted"])
                        return
                    player.paintinglifted = True
                    print(responses["items"]["painting_lifted"])
                                   
           
            
        
              
def run():
    game = Game()
    player = Player(game.places[1], game)
    #gameboard = game.construct_gameboard(player)
    print("start game")
        
    keep_running = True
    
    while(keep_running):
        
        current_room = None
        
        for placeList in game.places:
            if placeList.location == [player.pos.location[0], \
                player.pos.location[1]]:
                current_room = placeList.name[0]
                
                print(f"[{current_room.upper()}]")
                print(placeList.on_enter_text)
        user_input = input("\nCommand> ").lower().strip()
        
        if user_input == "help" or user_input == "?":
            print("Possible actions include: look, go, take, drop, inventory, examine, use, open, close, talk, lift, drink, and climb")
        if user_input == "quit" or user_input == "q": #or win condition == True:
            keep_running = False
        else:
            action(player,user_input,game)


if __name__ == "__main__":
    run()
        
