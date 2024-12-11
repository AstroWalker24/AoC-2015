def getRibbon(inp):
    inp=inp.split('\n')
    total=0
    for i in inp:
        if not i.strip():
            continue 
        l,w,h=str(i).split('x')

        # calculating the ribbon needed for the bow
        bow=int(l)*int(w)*int(h)

        # calculating the smallest side 
        array=[int(l),int(w),int(h)]
        array.remove(max(array))

        perimeter = 2*(array[0]+array[1])
        
            

        # calcula ting the total ribbon required
        total+=bow+perimeter

    return total




if __name__=="__main__":
    with open('inp.txt') as f :
        inp=f.read()
        print(getRibbon(inp))