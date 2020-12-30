def showMenu():
    print ("1) Area of rectangle")
    print ("2) Area of triangle")
    print ("3) Area of square")
    print ("4) exit") 
    data=int(input("Enter your choice: "))
    return data
data = showMenu()
while data!=3:
    user=showMenu()
    if data==1:
        h=float(input("Enter the height:"))
        w=float(input("Enter the weidth: "))
        area=h*w
        print("Area of rectangle is ",area)
    elif data==2:
            a = float(input("enter the lenght"))
            b = float(input("enter the breadth"))
            c = float(input("Enter the weidth"))
            s = (a + b + c) / 2
            area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
            print('The area of the triangle is ',area)
    elif data==3:
                s=float(input("Enter the area of side:"))
                Area=s*s
                print("Area of square:",Area)
    elif data==4:
                print("Exiting")

