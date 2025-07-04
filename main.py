from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def index():
    return "hey this is my first api"

@app.get('/name')
def name():
    return {"name":"rahul Kumar parida"}

@app.get('/address')
def address():
    return {"address":{
        "at":"anji",
        "po":"sahaspura",
        "via":"Anantapur",
        "dist":"balasore"
    }}