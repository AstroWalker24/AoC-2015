from re import search

# 
# print(sum(1 for d in data if search(r"(..).*\1", d) and search(r"(.).\1", d)))

def findNice(text):
    data=text.splitlines()
    return (sum(1 for d in data if search(r"(..).*\1", d) and search(r"(.).\1", d)))


    




if __name__=="__main__":
    with open('inp.txt') as f:
        content=f.read()
        print(findNice(content))    