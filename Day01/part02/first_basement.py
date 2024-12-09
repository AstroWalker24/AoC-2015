def firstBasement(inp):
    floor=0
    j=0
    while j < len(inp):
        if inp[j]=="(":
            floor+=1
        elif inp[j]==")":
            floor-=1
        if floor==-1:
            return j+1
        j+=1

        
    





if __name__=="__main__":
    with open("inp.txt") as f:
        inp=f.read()

    print(firstBasement(inp))   