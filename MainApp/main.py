from fastapi import FastAPI


# CreateApp
app = FastAPI()


# Create Function
# use decorator to assign path 
@app.get('/')
def index():
    return {"data":{"name":"Gopi"}}


@app.get("/about")
def about():
    return {"data":"about Page"}


# For Running Application 
# main is filename and app is Fastapi app
# cmd-: uvicorn main:app --reload
