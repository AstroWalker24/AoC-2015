def getPaper(inp):
    inp=inp.split('\n')
    total=0

    for i in inp:

        if not i.strip():  
            continue
        l,w,h=str(i).split('x')

        # calculating  the l*w 
        lw=int(l)*int(w)
        # calculating the w*h
        wh=int(w)*int(h)
        # calculating the h*l
        hl=int(h)*int(l)

        # calculating the smallest side 
        small=min(lw,wh,hl)

        # calculating the total paper required 
        total+=2*(lw+wh+hl)+small

        
    return total



if __name__=="__main__":
    with open('inp.txt') as f:
        inp=f.read()

        print(getPaper(inp))