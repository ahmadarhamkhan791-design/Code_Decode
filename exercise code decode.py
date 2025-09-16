'''1                                                                                                                                                         '''
def secret():
    try:
        a =int(input("Entre your choice : \n1. code-- \n2.decode-- \nif you want want change your input into code press 1 otherwise press 2 for decoding : "))
        value =input("Entre your input: ")
        if a==1 and len(value)<3:
            print(value[::-1])
        elif a==1 and len(value)>=3:
            print("art"+value[1::]+value[0]+"uni")
        elif a==2 and len(value)<3:
            print(value[::-1])
        elif a==2 and len(value)>=3:
            print(value[0:1:2]+value[3:-4:1])
    finally:
        print("This is our coding decoding program")
    
secret()

