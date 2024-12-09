def floorCalc(code):
    floor=0
    for i in code:
        if i=="(":
            floor+=1
        elif i==")":
            floor-=1
        
    return floor



if __name__=="__main__":
    with open("inp.txt") as f:
        inp=f.read()
    print(floorCalc(inp))