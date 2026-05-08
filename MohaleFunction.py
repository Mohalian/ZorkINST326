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
                
                self.pos,changed = self.check_inBounds(xLoc, yLoc)
                if changed == True:
                    
                    
                    return self.pos
                
        listPlaces = self.game_data.places
        
        
            
        for place in listPlaces:
            
            if len([name for name in place.name if name in choice]) >0:
                
              
                if max(abs(self.pos.location[0]-place.location[0]),\
                abs(self.pos.location[1]-place.location[1])) > 1:
                    
                    break
                
                if place.keyName == "undergroundentrance" and self.trapdooropen == False:
                    print("Trap door not open")
                    return self.pos
                
                return place    
                    
        print(responses["general"]["invalid_target"])
    
        return self.pos
    
    def check_inBounds(self,xLoc, yLoc):
        
        for place in self.game_data.places:
            if place.location == [xLoc, yLoc]:
                return place,True
        
        return self.pos,False
            
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



def Regex(toIter, input):
    
    allCommands = "("
    for action, names in toIter.items():
        for alias in names:
            allCommands += f"{alias}|"
            
    allCommands = f"{allCommands[:-1]})"
    return re.search(allCommands, input)


    print(responses["general"]["invalid_target"])
def look(player_pos, game_data, choice):
    """
    Shows what objects are at the player's current or nearby coordinate
    
    Args:
        player_pos: player's current coordinate position in dictionary form
            {"x":int, "y":int}
        game_data: game class
        direction: optional string, specified direction in command
        
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
        print("Invalid Input")
    
    directions = {
        ("east", "right"):(xLoc+1,yLoc),
        ("west", "left"):(xLoc-1,yLoc),
        ("north", "up"):(xLoc,yLoc+1),
        ("south", "down"):(xLoc,yLoc-1) 
         }
    
    for key in directions:
        if direction in key:
            xLoc, yLoc = directions[key]
    for item in game_data.items:
        if item.position == [xLoc,yLoc]:
            item_count += 1
            if direction == None:
                if ((item.name == "sorcerer's stone") or 
                (item.name == "flashlight") or 
                (item.name == "diamond egg")):
                    print(f"There is something else here...")
                else:
                    print(f"There is a {item.name} here.")
            else:
                if ((item.name == "sorcerer's stone") or 
                (item.name == "flashlight") or 
                (item.name == "diamond egg")):
                    print(f"There is something else there...")
                else:
                    print(f"There is a {item.name} there.")
    if item_count == 0:
        if direction == None:
            print("There is nothing here.")
        else:
            print("There is nothing there.")
            
def action(player, input, game):
    
    
    action_word = ""
    item_word = ""
    place_word = ""
    

    action_match = Regex(actionAll, input)
    
    if action_match:
        action_word = action_match.group(0)
        
    else:
        print(responses["general"]["invalid_target"])
        return 
    
    if (action_word in actionAll["go"]):
        
        player.pos = player.updatePlayerPosition(input)
        print(responses["movement"]["moved"])
        return
    
    elif (action_word in actionAll["look"]):
        look(player.pos, game, input)
        return
    
    elif action_word in actionAll["inventory"]:
        
        toPrint = ""
        for item in player.inventory:
            toPrint += (f"{item.name}, ")
        
        
        print(toPrint[:-2])
        return
    
    get_item = "("
    for item in game.items:
        
        for alias in item.aliases:
            get_item += f"{alias}|" 
    
    get_item = f"{get_item[:-1]})"
    item_word= re.search(get_item, input)
      
    if item_word:
        words = item_word.group(0)
    else:
        print(responses["general"]["invalid_target"])
        return
        
    if item_word: 
        
        itemToUse = None
        for item in game.items:
        
           if words in item.aliases:
               itemToUse = item
               break
        
        if itemToUse == None:
            print(responses["items"]["nonexistent_item"])        
        if action_word in itemToUse.interactions or action_word in actionAll.values:
            
            if action_word in actionAll["take"]:
                
                if itemToUse in player.inventory:
                    print(responses["items"]["already_have"])
                    return
                    
                if itemToUse.keyName == "sorcerers_stone" and \
                    player.drank == False:
                        print(responses["items"]["sorcerers_stone_fail"])
                        return
                player.inventory.append(itemToUse)
                print(responses["items"]["pickup_success"])
            
            elif action_word in actionAll["drink"]:
                
                if itemToUse in player.inventory:
                    print("Delicious")
                    player.inventory.remove(itemToUse)
                    player.drank = True
                
                else:
                    print(responses["items"]["item_not_here"])
            
            elif action_word in actionAll["use"]:
                player.flashlight = True
                print(responses["items"]["flashlight_on"])
                
            elif (action_word in actionAll["open"] or \
                action_word in actionAll["lift"]):
                
                if itemToUse.keyName == "trapdoor":
                    
                    player.trapdooropen = True
                    if player.pos.keyName == "kitchen":
                        player.pos = player.updatePlayerPosition("entrance")
                    elif player.pos.keyName == "entrance":
                        player.pos = player.updatePlayerPosition("kitchen")
                        
                
                elif itemToUse.keyName == "chest":
                    if player.chestopen == True:
                        print(responses["items"]["chest_already_open"])
                        return
                    
                    print(responses["items"]["chest_opened"])
                    player.chestopen = True
                   
                    
                        
                elif itemToUse.keyName == "painting":
                    if player.flashlight == False:
                        print("Can't find it in the darkness")
                        return
                    elif player.paintinglifted:
                        print(responses["items"]["painting_already_lifted"])
                        return
                    player.paintinglifted = True
                    print(responses["items"]["painting_lifted"])
    
                                   
           
def win(player):
    inventory_item_name = [i.keyName for i in player.inventory]
    if "diamondegg" in inventory_item_name and "sorcerers_stone" in inventory_item_name:
        print(responses["items"]["win"])
        return True
    else: False
     
        
              
def run():
    game = Game()
    player = Player(game.places[1], game)
    #gameboard = game.construct_gameboard(player)
    print("start game")
    current_room = None
        
    keep_running = True
    lastRoom = None
    
    while(keep_running):
        
        if win(player):
            break
        
        
        
        for placeList in game.places:
            
            if placeList.location == [player.pos.location[0], \
                player.pos.location[1]]:
                current_room = placeList.name[0]
                
                if not(lastRoom == current_room):
                    
                    print(f"[{current_room.upper()}]")
                    print(placeList.on_enter_text)
                    lastRoom = current_room
                    
        user_input = input("\nCommand> ").lower().strip()
        
        
        if user_input == "help" or user_input == "?":
            print("Possible actions include: look, go, take, drop, inventory, examine, use, open, close, talk, lift, drink, and climb")
        if user_input == "quit" or user_input == "q": #or win condition == True:
            keep_running = False
        else:
            action(player,user_input,game)
        
        


if __name__ == "__main__":
    run()
        
