import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Abhinav@18",database="dbs")
cur=mydb.cursor()
def risk():
    s="select Account_key,month(Transaction_Date),sum(Transaction_Amount) from customer_transaction where Transaction_type='INN' GROUP BY month(Transaction_Date)"
    cur.execute(s)
    res=cur.fetchall()
    print("input transactions")
    for i in res:
        if i[2]>1000:
            print(i[0],"highrisk")
    print("\n")
    a="select Account_key,month(Transaction_Date),sum(Transaction_Amount) from customer_transaction where Transaction_type='OUT' GROUP BY month(Transaction_Date)"
    cur.execute(a)
    r=cur.fetchall()
    print("out transaction")
    for i in r:
        if i[2]>800:
            print(i[0],"highrisk")
    print("\n")
    b="select Account_key,sum(Transaction_Amount) from customer_transaction  GROUP BY day(Transaction_Date)"
    cur.execute(b)
    bb=cur.fetchall()
    print("per day transactions")
    for i in bb:
        if i[1]>20:
            print(i[0],"highrisk")

    
risk()