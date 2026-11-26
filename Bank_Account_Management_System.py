import mysql.connector
class Banking:
    def __init__(self):
        try:
            self.con=mysql.connector.connect(user='root',password='root',host='localhost',database='bank_management')
            print(self.con)
        except:
            print('Connection failed')

    def create(self,customer_name,account_type,phone,balance):
        try:
            cursor=self.con.cursor()
            query='insert into accounts(customer_name,account_type,phone,balance)values(%s,%s,%s,%s)'
            data=(customer_name,account_type,phone,balance)
            cursor.execute(query,data)
            self.con.commit()
            print('Account Created Successfully')
        except:
            print('Failed to create account')

    def view(self):
        try:
            cursor = self.con.cursor()
            query = 'select * from accounts order by balance desc'
            cursor.execute(query,)
            records = cursor.fetchall()
            if records:
                for row in records:
                    print(row)
            else:
                print('no record')
        except:
            print('There are no accounts')



    def search(self,account_id):
        try:
            cursor=self.con.cursor()
            query='select * from accounts where account_id=%s'
            data=(account_id,)
            cursor.execute(query,data)
            record=cursor.fetchone()
            if record:
                print(record)
            else:
                print("record not found")
        except:
            print("Failed to Search the account")

    def deposit(self,account_id):
        try:
            cursor=self.con.cursor()
            amount=int(input('Enter the amount'))
            query='update accounts set balance=balance+%s where account_id=%s'
            data=(amount,account_id)
            cursor.execute(query,data)
            self.con.commit()
            if cursor.rowcount>0:
                print("Amount deposited successfully")
            else:
                print("Account not found")
        except:
            print("Failed to deposit")


    def withdraw(self,account_id):
        try:
            cursor=self.con.cursor()
            amount=int(input('Enter the amount:'))
            if amount<=0:
                print('invalid amount')
                return
            query='update accounts set balance=balance-%s where account_id=%s and balance>=%s'
            data=(amount,account_id,amount)
            cursor.execute(query,data)
            self.con.commit()
            if cursor.rowcount>0:
                print("Amount withdraw successfull")
            else:
                print("Insufficient balance")
        except:
            print('Account not found')

    def delete(self,account_id):
        try:
            cursor=self.con.cursor()
            query='delete from accounts where account_id=%s'
            data=(account_id,)
            cursor.execute(query,data)
            self.con.commit()
            if cursor.rowcount>0:
                print("Account deleted successfully")
            else:
                print("Failed to delete")
        except:
            print("Account not found")


    def summary(self):
        try:
            cursor=self.con.cursor()
            query='select count(*),sum(balance),avg(balance) from accounts'
            cursor.execute(query)
            t,s,a=cursor.fetchone()
            print('Total number of accounts:',t)
            print('Total balance:',s)
            print('Average balance:',a)
            query='select account_type, count(*) from accounts group by account_type'
            cursor.execute(query)
            type=cursor.fetchall()
            print('Account types:',type)
        except:
            print('No accounts found')


b=Banking()
while(1):
    print('1.Create Account')
    print('2.View All Accounts')
    print('3.Search Account')
    print('4.Deposit Account')
    print('5.Withdraw Account')
    print('6.Delete Account')
    print('7.Account Summary')
    print('8.Exit')

    ch=int(input('Enter your choice:'))

    if ch==1:
        c=input('Enter customer name:')
        a=input('Enter account type:')
        p=int(input('Enter phone number:'))
        ba=int(input('Enter balance:'))
        b.create(c,a,p,ba)

    elif ch==2:
        b.view()
    elif ch==3:
        id=int(input('Enter account_id:'))
        b.search(id)
    elif ch==4:
        id=int(input('Enter account_id:'))
        b.deposit(id)
    elif ch==5:
        id=int(input('Enter account_id:'))
        b.withdraw(id)
    elif ch==6:
        id=int(input('Enter account_id:'))
        b.delete(id)
    elif ch==7:
        b.summary()
    elif ch==8:
        exit()
    else:
        print('Invalid Choice')