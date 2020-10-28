
from twilio.rest import Client
import mysql.connector
import threading #kill timer
#import foo

GM = "+15192228170"
#Tokens for Twilio
account_sid = 'ACaac1efae2287878f8482161bbba5c1a9'
auth_token = '18620312c75b2c747fcd385d20c01ab5'
print("Tokens Added")
  
#SQL Connection
mydb = mysql.connector.connect(user='among', password='password',
                              host='127.0.0.1',
                              database='AMONGUS',
                              use_pure=False)
if (mydb):
    print(mydb)
    print("Connection successful!") #Success
else:
    print("Connection unsuccessful!") #Not Success

cursor1 = mydb.cursor(buffered=True)
cursor2 = mydb.cursor()

sql = "SELECT * FROM Colour;"
cursor1.execute(sql)

def detGM():
    print("w")
#Stage 1: Setup
def setup(phone,mess):
    if phone == '12':
        print("GM Texting")
    else:
        print("Player?")
        #Check if already in Player Table
        sql = "SELECT * FROM Player WHERE strPhone = '" + phone + "';"
        cursor1.execute(sql)
        result1 = cursor1.rowcount
        if result1 == 0:
            #Check if colour exists...
            sql = "SELECT * FROM Colour WHERE strColour = '" + mess + "';"
            cursor1.execute(sql)
            result1 = cursor1.rowcount
            if result1 != 0:
                sql = "SELECT intColID FROM Colour WHERE strColour = '" + mess + "';"
                cursor1.execute(sql)
                result1 = cursor1.fetchone()
                result = str(result1[0])
                print(result)
                sql = "INSERT INTO Player(strPhone,intColID) VALUES ('" + phone +"', " + result + ");"
                cursor1.execute(sql)
                print("Registered number " + phone + " as colour ID " + result)
            else:
                print("Wut?")
            
        else:
            print("Already Registered!")
            message = "You're already registered! Please wait for the game to begin!"
            send(message,phone)

def send(message,phone):

    client = Client(account_sid,auth_token)

    client.messages.create(
            to=phone,
            from_='+12892030618',
            body= message
            )

#stage(): Determine the stage, to allow for the proper action to be taken
    #i: The current stage, sent from the Flask SMS App
def stage(i,phone,mess):
    message = mess.upper()
    if i == 1:
        #Stage 1: Setup
        setup(phone,message)
        
    
        
        
