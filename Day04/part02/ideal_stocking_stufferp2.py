import hashlib 


def findHash(string):
    encoded_string= string.encode('utf-8')
    md5_hash = hashlib.md5(encoded_string)
    hex_digest = md5_hash.hexdigest()
    return hex_digest


def findNumber(prefix):
    # starting from 1
    start=1
    while True:
        string=prefix+str(start)
        hash_string=findHash(string)
        if hash_string[0:6]=="000000":
            return start
        start+=1




if __name__=="__main__":
    prefix="ckczppom"
    print(findNumber(prefix))








