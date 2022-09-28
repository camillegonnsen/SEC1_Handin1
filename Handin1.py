
#Assignment 1.1
print("----Assignment 1.1----")
#Shared base
g = 666

#Shared prime
p = 6661

#Bob's public key
pk = 2227


#Alice's message
m = 2000


#Encryption:

#1. choose a random r (Alice's public key)
r = 35


def encrypt(message, privateKey):
    #2. compute Alice's public key: c1 = g^r mod p
    c_1 = (g**r) % p
    #3. compute the encrypted message: c2 = m * (pk^r mod p)
    c_2 = message * (privateKey**r % p)
    return (c_1,c_2)
    
c = encrypt(m, pk)
print("c =", c)

def decrypt(c, secretKey):
    #Unpacking tuple
    (c1,c2) = c
    #To decrypt we can use the formula c2/(g^(r^sk) mod p)
    #We know that c1 = g^r mod p and you can therefore replace g^r mod p with c1
    m = c2/((c1**secretKey) % p)
    return m

print("")
#Assignment 1.2
print("----Assignment 1.2----")

"""
We need to do a brute force to find Bob's secret key 

By using a for loop we can check every number with our public key formula 
and the number that gives us the message = 2000 will be our secret key
"""

def getSecretKey(publicKey):
    for i in range(1, p):
        if g**i % p == publicKey: return i

Bob_sk = getSecretKey(pk)
print("Bob's secret key =", Bob_sk)

print("")

#We can now decrypt the message using Bob's secret key
message = decrypt(c, Bob_sk)

print("Alice's secret message =", message)

print("")
#Assignment 1.3
print("----Assignment 1.3----")

#Mallory intercepting Alice's message 
def modifyMessage(c):
    c1, c2 = c
    #Modifying the encrypted message
    c2 = c2*3
    #Updating c
    c = (c1,c2)
    return c

interceptedC = modifyMessage(c)

interceptedMessage = decrypt(interceptedC, Bob_sk)

print("Alices secret  =", interceptedMessage)





