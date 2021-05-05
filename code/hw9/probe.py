# import getpass
from getpass import getuser
from pprint import pprint

def kodirovki():
    
    bb = b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'

    i = 0
    resa = ""
    resb = ""
    for b in bb:
        print(bin(b))
        i += 1
        if i== 1:
            resa = bin(b)[5:]
            print(resa)
        if i == 2:
            resb = bin(b)[4:]
            print(resb)
            a= str(resa)+str(resb)
            print("0b"+a)
            print()
            i = 0
        # print(str(resa), str(resb))

    be = bb.decode()
    print(be)
    print(be.encode())

def readFile():
    
    username = getuser()
    # file_name = "/home/"+username+"/Videos/skillboxPy/skillboxPyDev18/code/hw9/forRead.txt"
    # file_name = "/home/"+username+"/Desktop/cvMail"
    # file_name = "../forFileRead/read_me.txt"
    file_name = "somePath/someFile.txt"
    file = open(file_name, "r", encoding="utf8") # binary read --> r, rb
    file_content = file.read() # will return all drom file
    file.close()
    pprint(file_content)

# readFile()

def get_username_ubuntu():
    # import getpass
    username = getuser()
    print(username)


def write_file():
    file_name = "wr.txt" # if not exist --> creat automaticaly
    file = open(file_name, "a", encoding="utf8") # write = w, append mode = a
    file_content = "hello world\n"
    file.write(file_content)
    file.close()


def super_rw():
    file_name = "forRead.txt"
    file = open(file_name, mode="r+")
    file_content = "\nline to end \n"
    file.write("\nline to ennnnnnnd \n")
    file_content = file.read()
    file.write("\nline to enddddd \n")
    # file.write("\nasda\n")
    file.close()
    pprint(file_content)

if __name__ == "__main__":
    get_username_ubuntu()
    # readFile()
    # write_file()
    super_rw()