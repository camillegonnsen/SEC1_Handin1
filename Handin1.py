
#Assignment 1.1

#Shared base
g = 666
print("g =", g)
#Shared prime
p = 6661
print("p =", p)
#Bob's public key
pk = 2227
print("pk =", pk)

#Bob's message
m = 2000
"""
Encryption:
1. choose a random r (Alice's pk)
"""

r = 35
print("r =", r)

def encrypt(message, privateKey):
    #3. compute c1 = g^r
    c_1 = (g**r)%p
    #compute c2 = m · (pk^r mod p)
    c_2 = message * (privateKey**r % p)
    return (c_1,c_2)
    
c = encrypt(m, pk)
print("c =", c)

def decrypt(c, secretKey):
    c1,c2 = c
    m = c2/((c1**secretKey) % p)
    return m

#Assignment 1.2
"""
We need to do a brute force to find Bob's secret key 

By using a for loop we can check every number with our public key function 
and the number that gives us the message = 2000 with be our secret key
"""

def getSecretKey():
    for i in range(1, p):
        if g**i % p == pk: return i

Bob_sk = getSecretKey()
print("sk =", Bob_sk)


message = decrypt(c, Bob_sk)

print("Alice's secret message =", message)

#Assignment 1.3
def modifyMessage(c):
    c1, c2 = c
    c2 = c2*3
    c = (c1,c2)
    return c

newC = modifyMessage(c)

newMessage = decrypt(newC, Bob_sk)

print("After Bob's decryption =", newMessage)





