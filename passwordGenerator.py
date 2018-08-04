'''

author : david gilbert
problem : random password generator

'''
import random as r

def passwordGenerator(length, capitalFlag = True, symbolFlag = True):
    
    #generate password
    

    r.seed();
    password = "";
    
    if(capitalFlag and symbolFlag) : #generate with capital letters and symbols
    
        char = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','1','2','3','4','5','6','7','8','9','0' , '~', '!', '@', '#', '$' ,'%', '&','*', '-', '+', '=', '?' ]

        temp = r.randrange(len(char));
        
        for x in range (0,length):
            temp = r.randrange(len(char));
            password += char[temp];
        
    
    elif(capitalFlag):  #generate with capital letters 
        
        char = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','1','2','3','4','5','6','7','8','9','0' ]

        temp = r.randrange(len(char));
        for x in range (0,length):
            temp = r.randrange(len(char));
            password += char[temp];
    
    elif(symbolFlag) : #generate with symbols
    
        char = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','1','2','3','4','5','6','7','8','9','0', '~', '!', '@', '#', '$' ,'%' , '&','*', '-', '+', '=' '?' ]
        temp = r.randrange(len(char));

        for x in range (0,length):
            temp = r.randrange(len(char));
            password += char[temp];        
    
    else : #generate without capital letters and symbols
    
        char = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m''1','2','3','4','5','6','7','8','9','0']
        temp = r.randrange(len(char));
        for x in range (0,length):
            temp = r.randrange(len(char));
            password += char[temp];    
    
    
    return password
    
    






###########
########### main function
###########
def main():

    #getting the setting/input for password
    length = input("how long do you you want your password ? ")
    
    #check input
    while not length.isdigit():  
        length = input("please enter an integer value ")
    
    capital = input("do you want capital letters ? *recommended* y/n ");
    
    if capital[0] == 'y' or capital[0] == 'Y':
        capitalFlag = True ;
    else :
        capitalFlag = False;
    
    symbol = input("do you want symbols ? *recommended* y/n ");
    
    if symbol[0] == 'y' or capital[0] == 'Y':
        symbolFlag = True;
    else :
        symbolFlag = False;
        
        
    password = passwordGenerator(int(length),capitalFlag,symbolFlag);


    print(password);
    
    

main();
