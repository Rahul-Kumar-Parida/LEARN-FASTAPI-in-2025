from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app=FastAPI()

"""
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

   
@app.get('/blogs/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}

@app.get('/blogs/{id}')
def show(id: int):
    return {'blogs': {'blog': id}}


 """

#Query Parameter

@app.get('/blogs')
def show(limit=10,published: bool=True, sort:Optional[str]=None):

    if published:
        return {'data': f"{limit} published blogs fetch from db"}
    else:
        return {'data': f"Total 1000 blogs fetch from db"}
    

@app.get('/blogs/{id}/comments')
def comments(id,limit=10):

    return {'data':{'2','1'}}


class Blog(BaseModel):
    title:str
    body: str
    published:Optional[bool]

@app.post('/blog')
def create_blog(request : Blog):

    return {'data':f"blog is created as title: {request.title} and body : {request.body}  and published :{request.published}"}


#if you want to use the localhost then use it

# if __name__=="__main__":
#     uvicorn.run(app, host='127.0.0.1', port=9000)
