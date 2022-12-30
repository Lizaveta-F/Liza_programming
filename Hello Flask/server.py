from flask import Flask,render_template
import requests


app=Flask(__name__)

@app.route("/<name>")
def hello_name(name):
    response = requests.get(url=f"https://api.genderize.io?name={name}")
    response2 = requests.get(url=f"https://agify.io?name={name}")
    gender = response.json()["gender"]
    age = response2.json()["age"]
    
    return render_template("home.html",name=name,gender=gender)




if __name__=="__main__":
    app.run(debug=True)
    