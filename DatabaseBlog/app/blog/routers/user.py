from fastapi import APIRouter,Depends,status,Response,HTTPException
from fastapi.encoders import jsonable_encoder
from blog import Schemasdb
from typing import List
from blog import Database
# from Hashing import Hash
from sqlalchemy.orm import Session
from blog.repository import user


get_db = Database.get_db
router = APIRouter(
    prefix="/user",
    tags=["Users"],
)


@router.post('/',status_code=status.HTTP_201_CREATED,response_model=Schemasdb.ShowUsers)
def create_user(request:Schemasdb.Users,db:Session = Depends(get_db)):
    return user.create(request,db)

@router.get("/{id}",status_code=status.HTTP_202_ACCEPTED,response_model=Schemasdb.ShowUsers)
def get_user(id:int,response:Response,db:Session = Depends(get_db)):
    return user.get_user(id,db)