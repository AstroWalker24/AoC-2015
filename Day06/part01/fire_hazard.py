def countOns(matrix):
    count=0
    for i in range(1000):
        for j in range(1000):
            if matrix[i][j]==1:
                count+=1
            
    return count

def toggleSwitches(instructions):
    # declaring the globals 
    grid=[]

    # filling all the values of the grid with null(000)
    for i in range(1000):
        grid.append([0]*1000)

    # trim the extra spaces off from the instructions 
    instructions=instructions.strip()
    

    # instructions can be either turn off or turn on or toggle 
    instruction_set=instructions.split('\n')

    for instruction in instruction_set:
        # split the instruction into words 
        words=instruction.split(" ")
        if words[0]=='toggle':
            start_coordinate=words[1].split(',')
            end_coordinate=words[3].split(',')

            for i in range(int(start_coordinate[0]),int(end_coordinate[0])+1):
                for j in range(int(start_coordinate[1]),int(end_coordinate[1])+1):
                    if grid[i][j]==0:
                        grid[i][j]=1
                    else:
                        grid[i][j]=0

        elif words[0] == 'turn' and words[1]=='on':
            # retreive the coordinates 
            start_coordinate=words[2].split(',')
            end_coordinate=words[4].split(',')

            for i in range(int(start_coordinate[0]),int(end_coordinate[0])+1):
                for j in range(int(start_coordinate[1]),int(end_coordinate[1])+1):
                    grid[i][j]=1

        elif words[0] == 'turn' and words[1]=='off':
            start_coordinate=words[2].split(',')
            end_coordinate=words[4].split(',')

            for i in range(int(start_coordinate[0]),int(end_coordinate[0])+1):
                for j in range(int(start_coordinate[1]),int(end_coordinate[1])+1):
                    grid[i][j]=0
            
        else:
            print("Invalid Instruction")
            return -1
        
    return countOns(grid)




if __name__=="__main__":
    # read the inp from the file 
    with open('inp.txt') as f:
        content=f.read()
        print(toggleSwitches(content))