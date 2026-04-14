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