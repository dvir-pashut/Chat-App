from flask import Flask, render_template, redirect, url_for, request
import os.path
from datetime import datetime
import dbconnection
import time
# To pring the server HOSTNAME
import socket

app = Flask(__name__)
hostname = socket.gethostname()
#return main index page
@app.route("/")
def home():
    return render_template("index.html",hostname=hostname)


#return room index page
@app.route("/<room>")
def roomMsg(room):
     print(f"Host Name is: {hostname}")
     return render_template("index.html",hostname=hostname)

#Get Spesific room message and post
@app.route("/api/chat/<room>", methods=["POST", "GET"])
def getMessages(room):
    if request.method == "POST":
        #Gets data from The Post Request, Create a simple format with date
        user = request.form["username"]
        message = request.form["msg"]
        now = datetime.now()
        #Formatting the message and sending it to post to the DB
        date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        current_message = f"[{date_time_str}] {user}: {message}"
        dbconnection.post_message(f"room{room}",current_message)
        return redirect(url_for("getMessages",room=room))
    #GET request    
    else:
        result = dbconnection.get_messages(f"room{room}")
        return result



if __name__ == "__main__":
    # try:
    #     dbconnection.DB_INITIALIZATION()
    # except:
    #     time.sleep(15)
    #     dbconnection.DB_INITIALIZATION()
    app.run(host='0.0.0.0')
