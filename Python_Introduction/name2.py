#this is a program that will get a name and add "is cool" to the end

def coolify(name):
    return name + "is cool"

def __main():
    myname = input("please type in your name : ")
    myname = coolify(myname)
    print(myname)
    
