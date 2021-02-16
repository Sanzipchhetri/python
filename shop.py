import smtplib
import email

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

cust = []
product = []
prodbuy = []
discount = 0
def main():
    while True:
        check = input("\nadd  customer :  A \t show customer : S \t Product Add : P \t Buy Product : B \n"
                      "check stock : C \t track cutomer type : T \t show inventory detail : I \n\nenter choice=> ")
        if check == 'q': 
            break
        if (check == 'A'):
            createcust()
        elif (check == 'S'):
            showcust()
        elif (check == 'P'):
            addProd()
            showProd()
        elif(check =='B'):
            buyprod()
        elif (check == 'C'):
            checkstock()
        elif(check=='T'):
            trackcustomertype()
        elif (check == 'I'):
            showinventory()
        else:
            print("thank u ")
def send_message():
    msg = MIMEMultipart()
    msg['From'] = 'Email@gmail.com'
    msg['To'] = "Email98@gmail.com"
    msg['Subject'] = '***Out of Stock***'
    body = "***Something goes wrong or Out of Stock***"
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()
    address_info = "Email@gmail.com"
    print(address_info, text)
    sender_email = "Email@gmail.com"
    sender_password = "Password"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    print("Login successful")
    server.sendmail(sender_email, address_info, text)
    print("Message sent")
    

def trackcustomertype():
    if(int(prodbuy[3]) >100): #prodbuy[3] is the amount
        print("customer is gold")
        discount = 0.5 #give 50% discount for gold customer
        prodbuy[4] = (float(prodbuy[4])*float(discount))+float(prodbuy[4])
        prodbuy.append(discount)
        prodbuy.append(prodbuy[4])
    elif(int(prodbuy[3]) >50 and int(prodbuy[3]) <100):
        print("customer is silver")
        discount = 0.3  # give 30% discount for gold customer
        prodbuy[4] = (float(prodbuy[4]) * float(discount)) + float(prodbuy[4])
        prodbuy.append(discount)
        prodbuy.append(prodbuy[4])
    elif (int(prodbuy[3]) > 25 and int(prodbuy[3]) < 50):
        print("customer is bronze")
        discount = 0.1  # give 10% discount for gold customer
        prodbuy[4] = (float(prodbuy[4]) * float(discount)) + float(prodbuy[4])
        prodbuy.append(discount)
        prodbuy.append(prodbuy[4])
    else:
        print("Normal Customer   no discount")
       

def showinventory():
    print(buyprod)
def checkstock():
    print("current stock is ")
    print(product)
    if(int(product[2])<5):
        send_message()
        

def buyprod():
    name = input("enter customer name ")
    prodbuy.append(name)
    size = input("enter product name  ")
    prodbuy.append(size)
    price = input("enter price ")
    prodbuy.append(price)
    amt = input("enter amount")
    prodbuy.append(amt)
    total = input("enter total")
    prodbuy.append(total)
def addProd():
    name = input("enter product name ")
    product.append(name)
    size = input("enter size ")
    product.append(size)
    price = input("enter price ")
    product.append(price)
def showProd():
    print("Product is ")
    print(product)
def createcust():
    name = input("enter name ")
    cust.append(name)
    phone = input("enter phone ")
    cust.append(phone)
    address = input("enter address ")
    cust.append(address)
    return cust
def showcust():
    print(cust)
main()
