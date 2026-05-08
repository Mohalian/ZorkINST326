import json
import pandas as pd
import re
import time


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
    def __init__(self, starting_pos, game):
        self.pos = starting_pos
        self.inventory = []
        self.game = game
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
       choice: command entered by the user to move
       
       
    Side effects:
        Changes self.pos and prints to console

    Returns: 
        self.pos: the new position of the player (Place object)
    """
    
        
        xLoc, yLoc = self.pos.location
      
       
        
        directions = {
            ("east", "right"):[xLoc+1,yLoc],
            ("west", "left"):[xLoc-1,yLoc],
            ("north", "forward"):[xLoc,yLoc+1],
            ("south", "back"):[xLoc,yLoc-1] 
            
        }
        
        for cardinal, reg in directions:
            
            if cardinal in choice or reg in choice:
                
                xLoc = directions[(cardinal,reg)][0]
                yLoc = directions[(cardinal,reg)][1]
                
                self.pos,changed = self.check_inBounds(xLoc, yLoc)
                if changed == True:
                    
                    return self.pos
                else:
                    scroll_print(responses["movement"]["blocked"], 
                                 self.game.skip_scroll)
                    return self.pos
            
        listPlaces = self.game.places
    
        for place in listPlaces:
            
            if len([name for name in place.name if name in choice]) > 0:
                
              
                if max(abs(self.pos.location[0]-place.location[0]),\
                abs(self.pos.location[1]-place.location[1])) > 1 and \
                    (place.keyName not in ["undergroundentrance", "kitchen"] \
                    and self.pos.keyName not in ["undergroundentrance", "kitchen"]):
                    
                    break
                
                return place    
                
                
                
            
                    
        scroll_print(responses["general"]["invalid_target"], self.game.skip_scroll)
    
        return self.pos
    
    def check_inBounds(self,xLoc, yLoc):
        """
        This function just helps with updatePlayerPosition to see if the user
        can move to that spot
    
        Args:
        choice: command entered by the user to move
       
       
        Side effects:
            Changes self.pos and prints to console

        Returns: 
            self.pos: the new position of the player (Place object)
            True or False -> used to print an error message if false
        
        
        """
        
        
        for place in self.game.places:
            if place.location == [xLoc, yLoc]:
                return place,True
        
        return self.pos,False
            
class Item:
    """
    A class to hold the specific features of an item
    
    Attributes:
    keyName(string): key of the item
    name(str): screen name of the item
    aliases(list of str): all the usable names of the item
    portable(bool): can the item be move
    interactions(list of str): all the actions the item can take
    description(str): Describes the item
    position(list of int): an X coordinate and y coordinate to represent
    the position of the item 
    
    """
    
    def __init__(self, keyName ,name, aliases, portable, interactions, \
        description, position):
        """
        Initializes the attributes of the item class
        
        Args:
        KeyName(string): key of the item
        name(str): screen name of the item
        aliases(list of str): all the usable names of the item
        portable(bool): can the item be move
        interactions(list of str): all the actions the item can take
        description(str): Describes the item
        position(list of int): an X coordinate and y coordinate to represent
        the position of the item 
        
        Side Effects:
        Changes all the attributes
        
        """
        
        self.keyName = keyName
        self.name = name
        self.aliases = aliases
        self.portable = portable
        self.interactions = interactions
        self.description = description
        self.position = position

class Game:
    """
    This class loads the items and place files and is used to hold all the 
    features the user can take an action of
    
    Attributes:
    items(list of Item object): has a list of all Item objects
    places(list of Place object): has a list of all Place objects
    currLoc([int,int]): X and Y coordinate the game starts on
    boardSize(int): represents the map size
    skip_scroll(bool): Option to keep text printing out over time

    
    
    """
    
    def __init__(self, boardsize=4):
        """
        Initializes the attributes of Game class
        
        Args:
        Boardsize(int + optional): Added to make stronger constraints to the map
        
        Side Effects:
        Changes all attributes
        Opens a file
        
        """
        
        
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
        self.skip_scroll = False
    
class Places:
    """
    A class to hold the specific features of an Place
    
    Attributes:
    keyName(string): key of the item
    Location(list of int): an X coordinate and y coordinate to represent
    the position of the place
    name(list of str):  all the findable names of the place
    description(str): Describes the place
    on_enter_text(str): The text that pops up when you enter a location
     
    
    """
    
    
    def __init__(self, keyName,location, name, description, on_enter_text):
        """
        Initializes the attributes of the Place class
        
        Args:
        keyName(string): key of the item
        Location(list of int): an X coordinate and y coordinate to represent
        the position of the place
        name(list of str):  all the findable names of the place
        description(str): Describes the place
        on_enter_text(str): The text that pops up when you enter a location 
        
        Side Effects:
        Changes all the attributes
        
        """
        
        
        
        self.keyName = keyName
        self.location = location
        self.name = name
        self.description = description
        self.on_enter_text = on_enter_text



def Regex(toIter, input):
    """
    Use regular expression to search if an action is in the input
    
    Args:
    toIter(list of dict): represents all the actions available
    input(str): the 
    
    
    """
    
    allCommands = "("
    for action, names in toIter.items():
        for alias in names:
            allCommands += f"{re.escape(alias)}|"
            
    allCommands = f"{allCommands[:-1]})"
    return re.search(allCommands, input)


    
    
def look(player_pos, game, choice):
    """
    Shows what objects are at the player's current or nearby coordinate
    
    Args:
        player_pos: player's current coordinate position in dictionary form
            {"x":int, "y":int}
        game: game class
        direction: optional string, specified direction in command
        
    Side effects:
        prints messages using scroll_print function depending on choice
        
    """
    xLoc = player_pos.location[0]
    yLoc = player_pos.location[1]
    
    item_count = 0
    choice = choice.split()
    if len(choice) == 1:
        direction = None
    elif len(choice) == 2:
        direction = choice[1]
    else:
        scroll_print("Invalid Input", game.skip_scroll)
    
    directions = {
        ("east", "right"):(xLoc+1,yLoc),
        ("west", "left"):(xLoc-1,yLoc),
        ("north", "up"):(xLoc,yLoc+1),
        ("south", "down"):(xLoc,yLoc-1) 
         }
    
    if direction != None:
        for key in directions:
            if direction in key:
                xLoc, yLoc = directions[key]
    for item in game.items:
        if item.position == [xLoc,yLoc]:
            item_count += 1
            if direction == None:
                if ((item.name == "sorcerer's stone") or 
                (item.name == "flashlight") or 
                (item.name == "diamond egg")):
                    scroll_print(f"There is something else here...",
                                 game.skip_scroll)
                else:
                    scroll_print(f"There is a {item.name} here.",
                                 game.skip_scroll)
            else:
                if ((item.name == "sorcerer's stone") or 
                (item.name == "flashlight") or 
                (item.name == "diamond egg")):
                    scroll_print(f"There is something else there...",
                                 game.skip_scroll)
                else:
                    scroll_print(f"There is a {item.name} there.",
                                 game.skip_scroll)
    if item_count == 0:
        if direction == None:
            scroll_print("There is nothing here.",
                         game.skip_scroll)
        else:
            scroll_print("There is nothing there.",
                         game.skip_scroll)
            
def action(player, input, game):
    
    """
    Handles what actions to do for every input of the player, extracting the action and item word
    from input and handling different actions with responses based on conditionals of the game.
    
    Args:
        player: Player class instance
        input: (str) Player's input
        game: Game class instance
        
    Side effects:
        Prints responses based on the action and condition of the action.
        Adds from inventory and removes (purple drink) from player inventory.
        Changes player attributes such as player.drank or player.trapdooropen
        
    
    """
    
    action_word = ""
    item_word = ""
    place_word = ""
    

    action_match = Regex(actionAll, input)
    
    if action_match:
        action_word = action_match.group(0)
        
    else:
        scroll_print(responses["general"]["invalid_target"],
                     game.skip_scroll)
        return 
    
    if (action_word in actionAll["go"]):
        
        player.pos = player.updatePlayerPosition(input)
        if player.pos.keyName == "churchbasement" and player.flashlight == True:
            scroll_print(player.pos.on_enter_text,
                         game.skip_scroll)
            scroll_print(responses["items"]["basement_visible"],
                         game.skip_scroll)
            return
        
        return
    
    elif (action_word in actionAll["look"]):
        look(player.pos, game, input)
        return
    
    elif action_word in actionAll["inventory"]:
        
        toPrint = ""
        for item in player.inventory:
            toPrint += (f"{item.name}, ")
        
        if len(player.inventory) == 0:
            scroll_print("Nothing in the inventory", game.skip_scroll)
        else:
            scroll_print(toPrint[:-2], game.skip_scroll)
        return
    
    get_item = "("
    for item in game.items:
        
        for alias in item.aliases:
            get_item += f"{re.escape(alias)}|" 
    
    get_item = f"{get_item[:-1]})"
    item_word= re.search(get_item, input)
      
    if item_word:
        words = item_word.group(0)
    else:
        scroll_print(responses["general"]["invalid_target"], game.skip_scroll)
        return
        
    if item_word: 
        
        itemToUse = None
        for item in game.items:
        
           if words in item.aliases:
               itemToUse = item
               break
        
        if itemToUse == None:
            scroll_print(responses["items"]["nonexistent_item"], 
                         game.skip_scroll)
            
        found = [key for key in itemToUse.interactions \
            if action_word in actionAll[key]]
    
        
                       
        if len(found) > 0:
            
            if action_word in actionAll["take"]:
                
                if itemToUse in player.inventory:
                    scroll_print(responses["items"]["already_have"], 
                                 game.skip_scroll)
                    return
                    
                if itemToUse.keyName == "sorcerers_stone" and \
                    player.drank == False:
                        scroll_print(responses["items"]["sorcerers_stone_fail"],
                                     game.skip_scroll)
                        return

                if itemToUse.position == player.pos.location:
                    
                    if itemToUse.keyName in ["diamondegg", "flashlight"] and \
                        player.chestopen == False:
                        return
                        
                    player.inventory.append(itemToUse)
                    scroll_print(responses["items"]["pickup_success"],
                                game.skip_scroll)
                    return
                else:
                    scroll_print(responses["general"]["invalid_target"], game.skip_scroll)
                    return
            
            elif action_word in actionAll["drink"]:
                
                if itemToUse in player.inventory:
                    scroll_print("Delicious", game.skip_scroll)
                    player.inventory.remove(itemToUse)
                    player.drank = True
                    return
                
                else:
                    scroll_print("Need to take before you drink",
                                 game.skip_scroll)
                    return
            
            elif action_word in actionAll["use"]:
                player.flashlight = True
                scroll_print(responses["items"]["flashlight_on"],
                             game.skip_scroll)
                
                if(player.pos.keyName == "churchbasement"):
                    scroll_print(responses["items"]["basement_visible"],
                                 game.skip_scroll)
                return
                
            elif (action_word in actionAll["open"] or \
                action_word in actionAll["lift"]):
                
                if itemToUse.keyName == "trapdoor":
                    
                    player.trapdooropen = True
                    if player.pos.keyName == "kitchen":
                        player.pos = \
                            player.updatePlayerPosition("undergroundentrance")
                    elif player.pos.keyName == "undergroundentrance":
                        player.pos = player.updatePlayerPosition("kitchen")
                    
                    return    
                
                elif itemToUse.keyName == "chest":
                    if player.chestopen == True:
                        scroll_print(responses["items"]["chest_already_open"],
                                     game.skip_scroll)
                        return
                    
                    scroll_print(responses["items"]["chest_opened"],
                                 game.skip_scroll)
                    player.chestopen = True
                    return
                    
                    
                        
                elif itemToUse.keyName == "painting":
                    if player.flashlight == False:
                        scroll_print("Can't find it in the darkness", 
                                     game.skip_scroll)
                        return
                    elif player.paintinglifted:
                        scroll_print(responses["items"]
                                     ["painting_already_lifted"], 
                                     game.skip_scroll)
                        return
                    player.paintinglifted = True
                    scroll_print(responses["items"]["painting_lifted"], 
                                 game.skip_scroll)
                    return
                
        else:
               
            scroll_print("You can't perform that action", game.skip_scroll)
                                   
           
def win(player, game):
    inventory_item_name = [i.keyName for i in player.inventory]
    if "diamondegg" in inventory_item_name and "sorcerers_stone" in inventory_item_name:
        scroll_print(responses["items"]["win"], game.skip_scroll)
        return True
    else: 
        return False
     
        
              
def run():
    """
    Actually runs the game and has the power to end it based on input, 
    gets an input every turn, and gives help messages if the player asks for it. Also
    makes sure it doesn't keep printing place description messages, only if player
    enters room for the first time

    Side effects:
        Prints/Doesn't print messages based on if it's the first time entering room
        Runs/ends the actual game (all the functions)
        Creates game and player instance
        Prints help message if asked

    """
    game = Game()
    player = Player(game.places[1], game)
    #gameboard = game.construct_gameboard(player)
    scroll_print("start game", game.skip_scroll)
    current_room = None
        
    keep_running = True
    lastRoom = None
    
    while(keep_running):
        
        if win(player, game):
            break
        
        
        
        for placeList in game.places:
            
            if placeList.location == [player.pos.location[0], \
                player.pos.location[1]]:
                current_room = placeList.name[0]
                
                if not(lastRoom == current_room):
                    
                    scroll_print(f"[{current_room.upper()}]", game.skip_scroll)
                    scroll_print(placeList.on_enter_text, game.skip_scroll)
                    lastRoom = current_room
                    
        user_input = input("\nCommand> ").lower().strip()
        
        
        if user_input == "help" or user_input == "?":
            scroll_print("""Possible actions include: look, go, take, drop, 
                         inventory, examine, use, open, close, talk, lift, 
                         drink, and climb""", game.skip_scroll)
        if user_input == "quit" or user_input == "q": #or win condition == True:
            keep_running = False
        elif user_input == "skip":
            game.skip_scroll = True
        else:
            action(player,user_input,game)
        
def scroll_print(to_print, skip_scroll):
    text = str(to_print)
    for c in text:
        print(c, end='', flush = True)
        if(not skip_scroll):
            time.sleep(0.02)
    print()    


if __name__ == "__main__":
    run()
        
