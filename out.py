from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import hello
import mysql.connector

app = Flask(__name__)

#Supposed to track the stage of the game
class stage:
    i = 1



@app.route("/sms",methods=['GET','POST'])

def sms_reply():
    
    phone = request.values.get('From', None)
    body = request.values.get('Body', None)
    
    print(body)
    print(phone)
    
    #Code for Stages
    hello.stage(stage.i,phone,body)
    
    resp = MessagingResponse()
    
    #hello.send("Test", phone)
    #resp.message("Hewwo Back " + phone)
    
    return str(resp)


##if __name__ == "__main__":
##    app.run(debug=True)
app.run(debug=True)