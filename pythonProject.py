#==================================CODE=======================================
from PIL import Image
import string
from random import *
"""
def login(username, password):
    k = key()
    encrypt(password, k)
   
def setUp():
    u = input("What would you like your username to be?  We will make sure your username is unique so your account stays secure.")
    pw = input("What would you like you password to be?")
    k = key()
    encrypt(pw, k)
    #check database for identical usernames: link to sql script??
    
    #once new info is guaranteed unique, the info is entered (via sql) into database, and the pw will be encrypted.  The user should be taken to the next page where they can select and image and filters to apply.

    
def key():
    min_char = 8
    max_char = 20
    allchar = string.ascii_letters + string.punctuation + string.digits
    key = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
    return key

def encryptXOR(pw, key):
    #encrypt binary pw with XOR logic:
    xorPWArr = []
    while len(xorPWArr) > len(key):
        digitsLeft = len(xorPWArr) - len(key)
        key += key[:digitsLeft]      
    for k in range(0,len(pw)):
        current = ""
        for i in range(0,len(key[k])):
            xkey = key[k]
            xpw = pw[k]
            if(xpw[i] == xkey[i]):
                current += "0"
            else:
                current += "1"
        xpw = current
        xorPWArr.append(xpw)
    #print("xor binary pw: \t",xorPWArr)
    
    encryptNOT(xorPWArr, key)

def encrypt(password, theKey):
    #pw is a string; convert to bin and change least important digit w xor logic and with a key!! thats randomly generated for each user
    binKey = []
    binPW = []
    #print("the key is: ",theKey)
    #print("the pw is: ",password)
    
    #convert pw into binary
    for n in range(0, len(password)):
        binary = str(bin(ord(password[n])))[2:]
        if len(binary) == 7:
            binPW.append(binary) 
    
    #convert key into binary:
    for n in range(0, len(theKey)):
        theBinary = str(bin(ord(theKey[n])))[2:]
        while(len(theBinary) < 7):
            theBinary = "0" + theBinary
        binKey.append(theBinary)
   
    def string_hex(string):
        return ':'.join(format(ord(c), 'x') for c in string)
    p = string_hex(password)
    k = string_hex(theKey)
    print(p,k)
    def hex_string(hexa):
        hexgen = (hexa[i:i+2] for i in range(0, len(hexa), 2))
        return ''.join(chr(eval('0x'+n)) for n in hexgen)
    p2 = hex_string(p)
    k2 = hex_string(k)
    def string_bin(string):
        return ':'.join(format(ord(c), 'b') for c in string)
    p3 = string_bin(p2)
    k3 = string_bin(k3)
    def bin_string(binary):
        bingen = (binary[i:i+7] for i in range(0, len(binary), 7))
        return ''.join(chr(eval('0b'+n)) for n in bingen) 
    p4 = bin_string(p3)
    k4 = bin_string(k3)    
    #set binKeyArray to the same length as bin password:
    while len(p4) > len(k4):
        digitsLeft = len(p4) - len(k4)
        k4 += k4[:digitsLeft]  

    #print("bin pw: \t",binPW)
    #print("binKey: \t",binKey)
    encryptXOR(p4, k4)
def encryptNOT(xpw, xkey):  
    #print("xpw: ",xpw,"xkey: ",xkey)
    #encrypt binary pw with NOT logic:
    notPWArr = []
    while len(notPWArr) > len(xkey):
        digitsLeft = len(notPWArr) - len(xkey)
        xkey += xkey[:digitsLeft]      
    for k in range(0,len(xpw)):
        current = ""
        for i in range(0,len(xkey[k])):
            nkey = xkey[k]
            npw = xpw[k]
            if(npw[i] == nkey[i]):
                current += "0"
            else:
                current += "1"
        npw = current
        notPWArr.append(npw)
    #print("not binary pw: \t",notPWArr)
    login(notPWArr, xkey)    


def decryptXOR(thePW, theKey):
    #decrypt the xor pw with exor logic
    exorPWArr = []
    for m in range(0,len(thePW)):
        current = ""
        for i in range(0,len(theKey[m])):
            exorKey = theKey[m]
            exorPw = theKey[m]
            if(exorPw[i] == "1" and exorPw[i] == exorKey[i]):
                current += "1"
            else:
                current += "0"
        exorPW = current
        exorPWArr.append(current)
    return exorPWArr
    #print("decrypted:\t",exorPWArr)

    
def decryptNOT(npw, nkey):   
    #decrypt the exor pw with NOT logic
    nnotPWArr = []
    #print("npw: ",npw,"nkey: ",nkey)
   
    while len(npw) > len(nkey):
        digitsLeft = len(nnotPWArr) - len(nkey)
        nkey += nkey[:digitsLeft]      
    for m in range(0,len(npw)):
        current = ""
        for i in range(0,len(nkey[m])):
            nnotKey = nkey[m]
            nnotPw = npw[m]
            if(nnotPw[i] == "1"):
                current += "0"
            else:
                current += "1"
        nnotPW = current
        nnotPWArr.append(current)
    #print("decrypted:\t",nnotPWArr)
    decryptXOR(nnotPWArr, nkey)
"""
#le interface
#button = tk.button(parent, option=value, etc)
#https://www.python-course.eu/tkinter_buttons.php
#https://stackoverflow.com/questions/20865010/how-do-i-create-an-input-box-with-python
from tkinter import *
root = Tk()
root.title("PicEdit")
root.configure(background="pink")
width = 400
height = 280
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
#==============================VARIABLES======================================
USERNAME = StringVar()
PASSWORD = StringVar()
    
    
#==============================METHODS========================================
import mysql.connector
    
def Database():
    print("database method")
    global conn, cursor
    conn = mysql.connector.connect(user = "sql9246944", password = "ShYAzlPRzu", host = "sql9.freesqldatabase.com", database = "sql9246944")
    cursor = conn.cursor(buffered = True)
    #cursor.execute("CREATE TABLE IF NOT EXISTS `User` (mem_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, file TEXT)")       
           
    
def Login(event=None):
    #print("1")
    Second()
def Second():
    print(USERNAME.get(), PASSWORD.get())
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.configure(text="Please complete the required field!", fg="red")
    else:
        print("else")
        cursor.execute("SELECT * FROM User WHERE username = '"+USERNAME.get()+"' AND pwd = '"+PASSWORD.get()+"'")
        wow = cursor.fetchone()
        print(wow)
        if wow is not None:
            lbl_text.configure(text="Login Successful", fg="green")
            u = USERNAME.get()
            p = PASSWORD.get()
            USERNAME.set("")
            PASSWORD.set("")
            login(u,p)
        else:
            lbl_text.configure(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")   
        
        
     
def HomeWindow():
    global Home
    root.withdraw()
    Home = Toplevel()
    Home.title("PicEditor")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.resizable(0, 0)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    lbl_home = Label(Home, text="Welcome!", font=('times new roman', 20)).pack()
    btn_back = Button(Home, text='Back', command=Back).pack(pady=20, fill=X)
     
def Back():
    Home.destroy()
    root.deiconify()
#==============================FRAMES=========================================
Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Top.configure(background="pink")
Form = Frame(root, height=200)
Form.pack(side=TOP, pady=20)
Form.configure(background="pink")
     
#==============================LABELS=========================================
lbl_title = Label(Top, text = "Login Here :)", font=('arial', 15))
lbl_title.configure(background="pink")
lbl_title.pack(fill=X)
lbl_username = Label(Form, text = "Username:", font=('arial', 14), bd=15)
lbl_username.grid(row=0, sticky="e")
lbl_username.configure(background="pink")
lbl_password = Label(Form, text = "Password:", font=('arial', 14), bd=15)
lbl_password.grid(row=1, sticky="e")
lbl_password.configure(background="pink")
lbl_text = Label(Form)
lbl_text.configure(background="pink")
lbl_text.grid(row=2, columnspan=2)
     
#==============================ENTRY WIDGETS==================================
username = Entry(Form, textvariable=USERNAME, font=(14))
username.grid(row=0, column=1)
#username.configure(background="light green")
password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
password.grid(row=1, column=1)
#password.configure(background="light green")
     
#==============================BUTTON WIDGETS=================================
btn_login = Button(Form, text="Login", width=45, command=Login)
btn_login.grid(pady=25, row=3, columnspan=2)
#btn_login.bind('<Return>', Login)
btn_login.configure(background="light green")
    
    
#==============================INITIALIATION==================================
if __name__ == '__main__':
    Database()
    root.mainloop()
    cursor.close()
    conn.close()    
        


#-----img editing-----
#from (https://www.blog.pythonlibrary.org/2017/10/11/convert-a-photo-to-black-and-white-in-python/):
def grayscale(inputPath, outputPath):
    pic = open(inputPath,"rb")
    pixelData = pic.read()
    byteData = bytearray(pixelData)   

    for x in range(35, len(byteData)):
        if x > len(byteData) - 3:
                    break
        red = byteData[x]
        green = byteData[x+1]
        blue = byteData[x+2]
        red = int((red+green+blue)/3)
        green = int((red+green+blue)/3)
        blue = int((red+green+blue)/3)
        byteData[x] = red
        byteData[x+1] = green
        byteData[x+2] = blue
        picture = open(outputPath,"wb")
        picture.write(byteData)     
    
def invert(inputPath, outputPath):
    pic = open(inputPath,"rb")
    pixelData = pic.read()
    byteData = bytearray(pixelData)
    #print(byteData[0])
    #for bmp file: should seee /x42 as the starting hex pair
    for x in range(35, len(byteData)):
        byteData[x] = abs(255-byteData[x])
        #print(byteData[x],"x: ",x)

    picture = open(outputPath,"wb")
    picture.write(byteData)


def allRed(inputPath, outputPath):
    pic = open(imgPath,"rb")
    pixelData = pic.read()
    byteData = bytearray(pixelData)
    #print(byteData[0])
    #for bmp file: should seee /x42 as the starting hex pair
    for x in range(35, len(byteData),3):
        if x > len(byteData):
            break
        byteData[x] = 255 #sets each red value to 255
        
    picture = open(outputPath,"wb")
    picture.write(byteData)
    
    return picture


def sepiaPalette(color):
    palette = []
    r, g, b = color
    for i in range(255):
        palette.extend((r*i/255,g*i/255, b*i/255))
    return palette

def sepia(inputPath, outputPath):
    original = open(inputPath)
    """
    whitish = (255,240,192)
    sepia = make_sepia_palette(whitish)
    """
    #convert original to grayscale:
    bw = original.convert('L')
    
    #add sepia toning
    bw.putpalette(sepia)
    
    #convert to rgb:
    sepiaImg = bw.convert('RGB')
    
    sepiaImg.save(outputPath)
    
#allRed("wonderWomanCover.bmp","wonder.bmp")
#grayscale("wonderWomanCover.bmp","wonder.bmp")
#invert("wonderWomanCover.bmp","wonder.bmp")


haveAccount = input("Answer 'true' if you have an account, 'false' if you do not.")
if haveAccount == 'true':
    username = input("What is your username?")
    password = input("Now enter your password: ")
    #login(username, password)
else:
    setUp()




        
    
                   
    
    
    
    
   