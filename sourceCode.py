import random as ran
import pyperclip

##
## Made by mlody4ever
## 

def menu():
    print('''


    Welcome to password generator made in python!

    1. Generate Password
    2. Exit
    
    ''')
    menNav = input('>> ')
    if menNav == '1':
        generate()
    elif menNav == '2':
        quit()
    else:
        menu()


def generate():
    sChars = ['-','+','=','_','*','%','$','.','~','#','!',':',';'] # define Character and Special Characters
    Chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0','1','2','3','4','5','6','7','8','9']
    length = 32  # Password length
    password = '0'
    for i in range(0,length,1):  #loop to make password
        if ran.randint(0,1) == 0:
            if ran.randint(0,1) == 0:  #lower or upper character?
                password += Chars[ran.randint(0, len(Chars)-1)].upper()
            else:
                password += Chars[ran.randint(0, len(Chars)-1)].lower()
        else:
            password += sChars[ran.randint(0, len(sChars)-1)]
    
    print('Your Password: ',password)
    menNav = input('Would you like to save your password and copy it to copyboard? (Y/N) ').lower()
    if menNav == 'y':
        pyperclip.copy(password)  #copy password
        file = open('passwords.txt','a', encoding='UTF-8')  #open file and append password to it
        file.write(password+'\n')
        file.close()
        print('Saved and copied!')
        menu()
    else:
        menu()



menu()