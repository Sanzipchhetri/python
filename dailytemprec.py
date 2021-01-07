def temperaturecategory(temperature):

    templength=len(temperature)

    tempdetails=[]

    category=[]

    categoryday=""

    categorytemp=""

    for i in range(templength):

        sums=0

        hot=0

        pleasant=0

        normal=0

        cold=0

        length=len(temperature[i])

        for j in range(len(temperature[i])):

            if temperature[i][j] >50:

                categoryday='A'

                categorytemp="Very Hot"

                hot=hot+1

            elif temperature[i][j] >40 and temperature[i][j] <=50:

                categoryday='B'

                categorytemp="Pleasant day"

                pleasant=pleasant+1

            elif temperature[i][j] >25 and temperature[i][j] <=40:

                categoryday='C'

                categorytemp="Normal day"

                normal=normal+1

            elif temperature[i][j] <=25:

                categoryday='D'

                categorytemp="Very cold"

                cold=cold+1

            sums=sums+temperature[i][j]

            category.append([categorytemp,categoryday])

        average=float(sums/(length))

        tempdetails.append([hot,pleasant,normal,cold,average])

    return tempdetails,category

    

 

def result(temperature,infolist,tempdetails,category):

    count=0

    wheather=["Hot","Pleasant","Normal","Cold"]

    dayscategory=["A","B","C","D"]

    print("\n\t\tDaily Temperature Report\n")

    count=0

    for i in range(len(infolist)):

        print(f"\nCustomer[{count}]: {infolist[i][0]}\t\tAddress: {infolist[i][1]} \n")

        for j in range(len(temperature[i])):

            countemp=j+1

            

            print(f"Temperature day[{countemp}]= {temperature[i][j]} Celsius {category[count][0]}   {category[count][1]} Category Day")

            count=count+1

        print(f"\nThe average temp for {countemp}= {tempdetails[i][-1]} Celsius")

        for k in range(len(tempdetails[i])-1):

            print("Number of %s days = %d day/s"%(wheather[k],tempdetails[i][k]))

        print("\n\t\tDays category")

        for l in range(len(tempdetails[i])-1):

            print(f"Number of {dayscategory[l]} category days= {tempdetails[i][l]} day/s")

 

def informations():

    print("\n\n\n\n\n\t\t\tTemperature Record System[TRS]\n\t\t\tSunway company pvt. ltd\n\t\t\tMaitidevi Kathmandu")

    count=int(input("\n\nEnter how many customers wanted to record data: "))

    infolist=[]

    temperature=[[] for i in range(count)]

    for i in range(0,count):

        name=input("Enter the name of the %d customer that wanted to record the temperature: "%(i+1))

        address=input("Enter the address of %d customer: "%(i+1))

        numberofdays=int(input("Enter how many days %d customer wanted to record temperature? "%(i+1)))

        infolist.append([name,address])

        print("Please Enter %d days Temperature Reading"%numberofdays)

        for j in range(0,numberofdays):

            intemp=float(input("Temperature Day[%d]= "%(j+1)))

            temperature[i].append(intemp)

    tempdetails,category=temperaturecategory(temperature)

    result(temperature,infolist,tempdetails,category)

if __name__ == "__main__":
    informations()
