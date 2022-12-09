from flask import Flask, render_template, redirect, url_for, request
import os.path
from datetime import datetime
import dbconnection

app = Flask(__name__)

#return main index page
@app.route("/")
def home():
    return render_template("index.html")

#return room index page
@app.route("/<room>")
def roomMsg(room):
     return render_template("index.html")

#Get Spesific room message and post
@app.route("/api/chat/<room>", methods=["POST", "GET"])
def getMessages(room):
    if request.method == "POST":
        #Gets data from The Post Request, Create a simple format with date
        user = request.form["username"]
        message = request.form["msg"]
        now = datetime.now()
        date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        current_message = f"[{date_time_str}] {user}: {message}"
        #Check if file exists
        if os.path.isfile(f"rooms/{room}.txt"):
            with open(f"rooms/{room}.txt",'a') as file:
                file.write(f"{current_message}\n")
        else:
            with open(f"rooms/{room}.txt",'w') as file:
                file.write(f"{current_message}\n")
        return redirect(url_for("getMessages",room=room))
    #GET request    
    else:
        # if os.path.isfile(f"rooms/{room}.txt"):
        #     with open(f"rooms/{room}.txt") as file:
        #         content = ""
        #         for line in file:
        #             content += f"{line}"
        #         return content
        result = dbconnection.get_messages(room)
        return result
        
        # else:
        #     return "No Chat Yet - You Welcome To send The First Message"



if __name__ == "__main__":
    app.run(host='0.0.0.0')
