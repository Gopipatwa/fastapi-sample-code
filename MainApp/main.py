from typing import Optional
from fastapi import FastAPI
# for creating models and use post method we import pydantic BaseModel
from pydantic import BaseModel
import uvicorn


# Creating Instance FastAPI app CreateApp

app = FastAPI()


# Create Function
# use decorator to assign path 
# @app.get('/')
# def index():
#     return {"data":{"name":"Gopi"}}


# @app.get("/about")
# def about():
#     return {"data":"about Page"}

# pagination limit set data if data is very largwe
# @app.get('/blog/?skip=0&limit=10')
# @app.get('/blog?limit = 10&published=true')

# url = http://127.0.0.1:8000/blog?limit=10
# multiple parameter compare url = http://127.0.0.1:8000/blog?limit=20&published=false
@app.get('/blog')
# def index(limit,published:bool):

# default value set in sort sort:Optional[str]=None
def index(limit=10,published:bool=True,sort:Optional[str]=None):
# by default value set limit and published
    # return published
    if published:
        return {"data":f"{limit} Blog List from database"}
    else:
        return {"data":f"{limit} blogs from the db"}

@app.get('/blog/unpublished')
def unpublished():
    return {"data":"all unpublished blogs"}



@app.get('/blog/{id}')
def show(id:int):
# int,str,
# def show(id): by default get as strig id we can 
# define with type of parameter accept data like thid def show(id:int):
    # fetch blog with id = id
    return {"data":id}

@app.get("/blog/{id}/comments")
def comment(id):
    return {"data":{"comments":f"{id} hello world"}}





class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]
    name :str
    desc:Optional[str]=None


@app.post('/blog')
def create_blog(request:Blog):
    # return request
    return {"data":f"blog is created {request.title}"}

# For Running Application 
# main is filename and app is Fastapi app
# cmd-: uvicorn main:app --reload


# if __name__=="__main__":
#     uvicorn.run(app,host="127.0.0.1",port="9000")