import numpy as np

def matrix(key):
    matrix=list(key)
    alphabets=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for e in alphabets:
        if e not in key:
            matrix.append(e)
    matrix=np.array(matrix)
    matrix=matrix.reshape(5,5)
    return matrix

def digraph(plaintext):
    if len(plaintext)%2==1:
        plaintext+="Z"
    pt=[plaintext[i:i+2] for i in range(0,len(plaintext),2)]
    temp=[]
    for i in pt:
        if(i[0]==i[1]):
            temp.append(i[0]+'Z')
        else:
            temp.append(i)
    return temp

def position(key_matrix,letter):
    x=y=0
    for i in range(5):
        for j in range(5):
            if(key_matrix==letter):
                x=i
                y=j
    return x,y

def encrypt(message,key_matrix):
    cipher=[]
    for e in message:
        p1,q1=position(key_matrix,e[0])
        p2,q2=position(key_matrix,e[1])
        if p1==p2:
            if q1==4:
                q1=-1
            if q2==4:
                q2=-1
            cipher.append(key_matrix[p1][q1+1])
            cipher.append(key_matrix[p1][q2+1])
        elif q1==q2:
            if p1==4:
                p1=-1
            if p2==4:
                p2=-1
            cipher.append(key_matrix[p1+1][q1])
            cipher.append(key_matrix[p2+1][q2])
        else:
            cipher.append(key_matrix[p1][q2])
            cipher.append(key_matrix[p2][q1])
    return cipher

key=input("Enter key:")
message=input("Enter message")
digraph=digraph(message)
print("Break into",digraph)
a=matrix(key)
print("Matrix\n",a)
print("Cipher:","".join(encrypt(digraph,a)))



    