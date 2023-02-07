#rsa
import random

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def coprime(phi):
    while True:
        e=random.randrange(2,phi)
        if gcd(phi,e)==1:
            return e
        
def priv(e,phi):
    d=0
    k=1
    while True:
        d=(phi*k+1)/e
        if d.is_integer():
            return int(d)
        k+=1

def modul(data,exp,n):
    return data**exp%(n)

def encrypt(data,e,n):
    cipher=[]
    for i in data:
        cipher.append(modul(ord(i),e,n))
    return cipher

def decrypt(data,e,n):
    cipher=[]
    for i in data:
        cipher.append(chr(modul(i,e,n)))
    return ''.join(cipher)

p=11
q=13
n=p*q
phi=(p-1)*(q-1)
e=coprime(phi)
d=priv(e,phi)

data=input("Enter the data: ")
enc=encrypt(data,e,n)

dec=decrypt(enc,d,n)
print(f'Entered data is: {data} \n The Encrypted Data is {enc} \n The Decrypted Data is {dec}')
