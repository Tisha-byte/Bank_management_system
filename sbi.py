import pymysql as sql
c=sql.connect(host="localhost",user="root",password="password",database="sbi_bank")
con=c.cursor()
def CreateAccount():
    acc_num = int(input("enter account number: "))
    n = input("enter account holder name: ")
    type = input("enter type of account(Saving/Current): ")
    amt = int(input("enter minimum deposit balance 500<amount<2000: "))
    mob = int(input("enter mobile number: "))
    q = "insert into bank values('%d','%s','%s','%d',%d)"%(acc_num,n,type,amt,mob)
    r = con.execute(q)
    if(r>0):
        print("Account Created")
    else:
        print("Account Not Created")
    c.commit()
#CreateAccount()

def Closeaccount():
    acc_num=int(input("enter account number:  "))
    q="delete from bank where account_num='%s'"%(acc_num)
    r = con.execute(q)
    if (r > 0):
        print("Account Closed")
    else:
        print("Account Not Closed")
    c.commit()
#Closeaccount()
def show_account_holder():
    qur="select account_holder,Amount from bank"
    con.execute(qur)
    r=con.fetchall()
    for data in r:
        print(data)
#show_account_holder()
def Balance_enc():
    acc_num = int(input("enter account number whose balance you want to check: "))
    qur = "select * from bank where account_num='%d'"%(acc_num)
    con.execute(qur)
    for data in con.fetchall():
        print(data[0], " ", data[1], " ", data[2], " ", data[3], "\n")
#Balance_enc()
def deposit():
    a = 0
    acc_num = int(input("enter account number: "))
    amount = int(input("enter amount you want to deposit: "))
    qur = "select Amount from bank where account_num='%d'" % (acc_num)
    con.execute(qur)
    for data in con.fetchall():
        a = data[0]



    total_Amount = a + amount
    qur1 = "update bank set Amount='%d'where account_num='%d'" % (total_Amount, acc_num)
    r = con.execute(qur1)
    if (r > 0):
        print("Balance deposited: ", total_Amount)
    else:
        print("Balance not deposited")
    c.commit()
def withdraw():

    a=0
    acc_num = int(input("enter account number: "))
    amount = int(input("enter amount you want to withdraw : "))
    qur = "select Amount from bank where account_num='%d'"%(acc_num)
    con.execute(qur)
    for data in con.fetchall():
          a = data[0]
    if(a < amount):
        print("Insufficient balance")
    else:
        total_Amount =  a - amount
        qur1 = "update bank set Amount='%d'where account_num='%d'"%(total_Amount,acc_num)
        r=con.execute(qur1)
        if(r>0):
          print("Balance Withdrawed: ", total_Amount)
        else:
          print("Balance not Withdrawed")
        c.commit()
#withdraw()
def Modify():
    acc_num = int(input("enter account number: "))
    p = int(input("enter new Mobile number: "))

    q = "update bank set mobile_num='%d'where account_num='%d'"%(p, acc_num)
    r = con.execute(q)
    if (r > 0):
        print("Account Modify")
    else:
        print("Account Not Modify")
    c.commit()
#Modify()
while(True):
    print("************* BANK MANAGEMENT SYSTEM ************* \n")
    print("*********WELCOME IN STATE BANK OF INDIA***********\n")
    print("MAIN MENU:\n1. Create account\n2. Deposit amount\n3. Withdraw amount\n4. Balance enquiry\n5. All account holder list\n6. Close account\n7. Modify Account\n8. Exit\n")
    x=int(input("Enter your choice:"))
    if(x==1):
        CreateAccount()
    elif(x==2):
        deposit()
    elif(x==3):
        withdraw()
    elif(x==4):
        Balance_enc()
    elif(x==5):
        show_account_holder()
    elif(x==6):
        Closeaccount()
    elif(x==7):
        Modify()
    else:
        break







