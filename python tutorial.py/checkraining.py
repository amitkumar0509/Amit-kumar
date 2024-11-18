check=input("IS RAINING?")
print(check)
if(check=='yes'):
        print( input("have umbrella?"))
        if 'yes':
                print("go outside")
        if 'no':
                print("wait a while...")
                print(input("Is raining outside?"))
                if 'no':
                        print("Go outside")
                else:
                        print("wait a while...")
       
        
elif(check=='no'):
        print("go outside!!")
        
print("THE END")

    