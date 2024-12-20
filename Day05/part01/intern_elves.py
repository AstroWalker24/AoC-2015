def findNice(text):
    # defining globals 
    vowels = ['a','e','i','o','u']


    # storing every string in an array
    strings = text.split('\n')
    niceStrings=0
    for string in strings:
        # check for the first rule : containing at least three vowels
        counter=0
        for char in string:
            if char in vowels:
                counter+=1
        if counter<3:
            # not a nice string , break the loop here 
            continue 

        # if the case 1 is passed, check for the second rule: containing at least one letter that appears twice in a row 
        flag=False 
        for i in range(len(string)-1):
            if string[i]==string[i+1]:
                flag=True
                break 

        if flag==False:
            # not a nice string, break the loop here 
            continue

        # if case 1 and 2 are passed, check for the final case, the string should not contain any of the following strings: ab,cd,pq,xy
        if 'ab' in string or 'cd' in string or 'pq' in string or 'xy' in string:
            # not a nice string, break the loop here 
            continue

        niceStrings+=1

    return niceStrings 





if __name__=="__main__":
    with open('inp.txt') as f:
        content=f.read()
        print(findNice(content))