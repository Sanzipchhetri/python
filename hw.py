string=input("Enter the string:")
print(string)
vowel=0
for i in string:
    if(i=="a" or i=="e" or i=="o" or i=="u" or i=="i"):
        vowel=vowel+1
    print("total number of vowel are",vowel)
    for i in range(2,vowel):
        if (vowel%i!=0):
            print("it is prime number.")
        else:
            print("It is not prime number:")
            for i in range(1,10):
                print(vowel,'x',i,'=',vowel*i)
                
