def housesRobo(inp):
    houses = set()  
    santa_coordinates = [0, 0]
    robot_coordinates = [0, 0]
    
   
    houses.add(tuple(santa_coordinates))
    
    for i, direction in enumerate(inp.strip()):  
        if i % 2 == 0:
            current = santa_coordinates
        else:
            current = robot_coordinates
        
        # Move based on the direction
        if direction == "^":
            current[1] += 1
        elif direction == "v":
            current[1] -= 1
        elif direction == ">":
            current[0] += 1
        elif direction == "<":
            current[0] -= 1
        
        # Add the new position to the set of visited houses
        houses.add(tuple(current))
    
    return len(houses)  # Return the number of unique houses


if __name__ == "__main__":
    with open("inp.txt") as f:
        inp = f.read()
        print(housesRobo(inp))
