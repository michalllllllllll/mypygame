'''
Caesar Cipher is a cryptographic algorithm where we shift letters by a given 
key.
e.g. Message = "abcde"
key = 5
encrypted message = "fghij"
'''
# 65-90 : A-Z; 97 - 122: a - z
# print(chr(65)) #chr(int) - this gives you an ASCII character of a given number
# print(ord(" ")) #ord(str)- this gives you number associated with an ASCII character
'''
def encrypt(msg:str,key:int ):#the key can be from 1-25
    emsg = ""
    for i in range(len(msg)):
        e = ord(msg[i])
        if e < 65 or e >90:#here we check if the character is in fact A-Z
            #in this case simply leave the character as is
            pass
        else:
            e = e + key
            if e > 90:#this is because we want to only work with alphabets
                e = e - 26# -90 + 64

        emsg += chr(e)
    return emsg

print(encrypt("kyzj zj aljk r kvjk kf jvv zw pfl riv rscv kf kf wzxliv zk flk nyrk kyv rtklrc dvjjrxv zk. kyv uzwwztlckp zj fecp xfzex kf zetivrjv wifd yviv fe.",5))#should return "FGHCDE"
'''
def decrypt(msg:str,key:int ):
    emsg = ""
    for i in range(len(msg)):
        e = ord(msg[i])
        if e < 97 or e > 122 :
            pass
        else:
            e = e - key
            if e < 97:
                e = e + 26

        emsg += chr(e)
    return emsg



x = 0
a = 0
while x >= 0 and x < 26:
    print(a, ". ", decrypt("ldqx bgqhrslzr!",x))
    x += 1
    a += 1

#first message key is 17
#second key is 3
#third key is 9
#fourth is 11
#fifth key is 10
#key is 25!!!!!
