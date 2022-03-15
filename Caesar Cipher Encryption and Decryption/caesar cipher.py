def encrypt(text,st):
    result=""
    for i in range(len(text)):
        char=text[i]
        if(char.isupper()):
            result+=chr((ord(char)+st-65)%26+65)
        else:
            result+=chr((ord(char)+st-97)%26+97)
    return result

def decrypt(result,st):
    decrypt=""
    for i in range(len(result)):
        char=result[i]
        if(char.isupper()):
            decrypt+=chr((ord(char)-st-65)%26+65)
        else:
            decrypt+=chr((ord(char)-st-97)%26+97)
    return decrypt

text=input()
st=int(input())
res=encrypt(text,st)
res2=res.upper()
print("Cipher is:" +res2)
print("Decrypted message:" +decrypt(res,st))

