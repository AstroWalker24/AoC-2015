def sphericalHouses(inp):
    visited_coordinates=[[0,0]]
    current_coordinate=[0,0]
    houses=1
    for char in inp:
        if char=="^":
            current_coordinate[1]+=1
            if current_coordinate not in visited_coordinates:
                visited_coordinates.append(current_coordinate.copy())
                houses+=1
        elif char=="v":
            current_coordinate[1]-=1
            if current_coordinate not in visited_coordinates:
                visited_coordinates.append(current_coordinate.copy())
                houses+=1
        elif char==">":
            current_coordinate[0]+=1
            if current_coordinate not in visited_coordinates:
                visited_coordinates.append(current_coordinate.copy())
                houses+=1
        elif char=="<":
            current_coordinate[0]-=1
            if current_coordinate not in visited_coordinates:
                visited_coordinates.append(current_coordinate.copy())
                houses+=1

    return houses 

        

if __name__=="__main__":
    with open("inp.txt") as f:
        inp=f.read()
        print(sphericalHouses(inp))