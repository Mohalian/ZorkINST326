import json

def updatePlayerPostion(choice, player_pos, boardSize):
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
    xLoc = player_pos["x"]
    yLoc = player_pos["y"]
    
    while keepLoop:
        
        if "move" not in choice:
            print("Not a movement command")
            return player_pos
    
        if "move north" in choice:
        
            yLoc = player_pos["y"]+1
            
    
        elif "move south" in choice:
        
            yLoc = player_pos["y"]-1
            
    
        elif "move west" in choice:
        
            xLoc = player_pos["x"]-1
            
    
        elif "move east" in choice:
        
            xLoc = player_pos["x"]+1
    
        else:
            choice = input("Movement command is move + (North, South, East, \
                        West): ").lower()
            continue  
      
        if xLoc >= boardSize or xLoc < 0 or yLoc >= boardSize or yLoc < 0:
            
            choice = input("You've been blocked by thick trees, \
                           find another command: ").lower()
            continue
        
        player_pos["x"] = xLoc
        player_pos["y"] = yLoc
        keepLoop = False
    
    return player_pos
        
        
    
def inventory_update(player, room, item_word, file, pick_drop):
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

    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    item_word = item_word.lower()
    item_name = None
    item_obj == None
    for key, value in data.items():
        if item_word == key or item_word in value:
            item_name = key
            break
    if not item_name:
        print(f"I don't understand what '{item_word}' is.")
        return
    
    if pick_drop:
        for item in room.items:
            if item.name.lower() == item_name:
                item_obj= item
                break    
        if not item_obj:
            print("That item isn't here.")
            return
        room.items.remove(item_obj)
        player.inventory.append(item_obj)
        print("Taken!")
        
    else:
        for item in player.inventory:
            if item.name == item_name:
                item_obj = item
                break
        if not item_obj:
            print("You don't have that.")
            return
        player.inventory.remove(item_obj)
        room.items.append(item_obj)
        print("Dropped!")                