from sqlalchemy.orm import Session
from blog import models
from fastapi import HTTPException,status
from blog.Hashing import Hash
from blog import Schemasdb


def create(request:Schemasdb.Users,db:Session):
    new_user = models.User(name = request.name,email=request.email,password = Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(id,db:Session):
    user = db.query(models.User).filter(models.User.id==id).first()
    print(user)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Not found this id {id} user in database table")
    return user