from LSBSteg1 import *
from cryptography.fernet import Fernet
import cv2
def encode():
    fi=input("Enter the name of file to be Encrypted:>> ")
    global e
    global p
    with open(fi,'r+') as f:
        rea=f.read()
    def encrypt():
        #encrytion code
        import random
        a=rea
        x=0
        #a='ben 123_'
        j=['1','2','3','4','5','6','7','8','9','0']
        o=''#indexing'
        global e
        e=[]#split with index numbers
        r=[]
        for i in a:
            q=str(i)
            s=str(x)
            x=x+1
            p=s+"/"+q
            e.append(p)
            r.append(p)

        random.shuffle(e)
        #print(str(e))
    def writefile():
        global w
        w=input("Enter the name of File:- ")
        with open(w,'w+') as x:
            x.write(str(e))
            #y=x.read()
            #print(y)
    def hash():
        # Python program to find MD5 hash value of a file
        import hashlib
             
        filename = fi
        with open(filename,"rb") as f:
            bytes = f.read() # read file as bytes
            readable_hash = hashlib.md5(bytes).hexdigest();
                #print(readable_hash)
            return readable_hash
    global h
    h=hash()
    def append():
        with open(w,'a') as x:
            ha='\n'+h
            f=x.write(ha)
            x.close()
    def encode2():
    #encoding
        with open(w,'r') as f:
            rea1=f.read()
        x=input("Enter Image Name:- ")
        steg = LSBSteg(cv2.imread(x))
        #print(type(steg))
        img_encoded = steg.encode_text(rea1)
        global y
        y=input("Enter New Image Name:- ")
        cv2.imwrite(y, img_encoded)
    global p
    global fernet
    def password():
        global p
        p=input("Enter Password:- ")
        filename = y
        finalpassword = p+"|"+filename


        # generate a key for encryption and decryption
        # You can use fernet to generate
        # the key or use random key generator
        # here I'm using fernet to generate key

        key = Fernet.generate_key()

        # Instance the Fernet class with the key

        global fernet
        fernet = Fernet(key)

        # then use the Fernet class instance
        # to encrypt the string string must
        # be encoded to byte string before encryption
        encMessage = fernet.encrypt(finalpassword.encode())

        print("Original String: ", finalpassword)
        print("Encrypted String: ", encMessage)
    hash()
    encrypt()
    writefile()
    append()
    encode2()
    password()
#print('&&',e)
def decode():
    fid='encryptedfile.txt'
    def decrypt():
    #decrytion code
        with open(fid,'r+') as ab:
            r=ab.read()
            #print('%%%%',r)
        a=e
        #print('$$',a)
        b=len(a)
        c=[]
        f=[]
        z=[]
        r=''
        for i in a:
            s=i.split("/")
            c.append(s)
            f.append(s[0])
        #print(f)
        l=len(f)
        for i in range(l):
            for j in c:
                if j[0]==str(i):
                    z.append(j[1])
        
        #print(z)
        with open(fid,'w+') as de:
            de.truncate()
            for i in z:
                if i=="\n":
                    de.write("\n")
                else:
                    de.write(i)
        #for i in c:
         #   d=i[1]
          #  f.append(d)

        #for i in f:
         #   r=r+i
        #print(r)
    def removelastline1():
    #remove last line from a text line in python
        fd=open(fid,"r")
        d=fd.read()
        #print('*****',d)
        fd.close()
        m=d.split("\n")
        #print('^^^^',m)
        global ha
        ha=m[-1]
        s="\n".join(m[:-1])
        #print(s)
        fd=open(fid,"w+")
        for i in range(len(s)):
            fd.write(s[i])
        fd.close()
    def hash1():
        # Python program to find MD5 hash value of a file
        import hashlib
             
        filename = 'sample.txt'
        with open(filename,"rb") as f:
            bytes = f.read() # read file as bytes
            readable_hash = hashlib.md5(bytes).hexdigest();
                #print(readable_hash)
            return readable_hash
    global h1
    h1=hash1()
    def verify():
        if ha==h1:
            print('******************')
            print("\n \nHash Verified")
            print('******************')
        else:
            print("Hash Not verified")
    def decode2():
        ima=input("Enter Image name:- ")
    #decoding
        im = cv2.imread(ima)
        steg = LSBSteg(im)
        global t
        t=steg.decode_text()
        #print("Text value:",t)
        with open(fid,'w+') as f:
            f.write(t)
    def password1():
        import matplotlib.pyplot as plt
        import matplotlib.image as mpimg
        setpassword = p
        userpassword = input("Enter Password:")
        if setpassword==userpassword:
            img = mpimg.imread('image.jpg')
            imgplot = plt.imshow(img)
            plt.show()
            decode2()
            removelastline1()
            decrypt()
            hash1()
            verify()
        else:
            print("Invalid Password")
    def aesdecrypt():
        f=input("Enter value:")
        decMessage = fernet.decrypt(f).decode()
        d=decMessage.split("|")
        print("decrypted string: ",decMessage)
        print("Password ",d[0])
        print("Filename ",d[1])
    aesdecrypt()
    password1()
def main():
    while True:
        print("1.Encode")
        print("2.Decode")
        print("0.Exit")
        a=input("Enter >>")
        if a=='1':
            print("*******ENCODE*******")
            encode()
        elif a=='2':
            print("*******DECODE*******")
            decode()
        elif a=='0':
            break
        else:
            print("Wrong value")
main()
