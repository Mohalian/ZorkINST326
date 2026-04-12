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
        