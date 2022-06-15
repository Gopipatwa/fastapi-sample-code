from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from blog import models
from blog.oauth2 import get_current_user
from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from blog import Schemasdb

def get_all(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request:Schemasdb.Blog,db:Session):
    print(request)
    new_blog =models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(id:int,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
    
    blog.delete(synchronize_session=False)
    db.commit()
    return {"detail":f"Deleted {id} blog "}


def update(id:int,request:Schemasdb.Blog,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    
    if not blog.first():
        print(jsonable_encoder(request))
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
    # db.query(models.Blog).filter(models.Blog.id==id).update(request)
    # blog.update({"title":request.title,"body":request.body})
    blog.update(jsonable_encoder(request))
    db.commit()
    
    return {
        "detail":{
            "message":f"updated {id}"
        }
    }

def get_piese(id:int,db:Session):
    piese = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not piese:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with this id {id} is not available")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"details":f"Blog with this id {id} is not available"}
    return piese