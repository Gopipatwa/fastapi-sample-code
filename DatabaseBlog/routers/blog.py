from fastapi import APIRouter,Depends,status,Response,HTTPException
from fastapi.encoders import jsonable_encoder
from oauth2 import get_current_user
import Schemasdb
from typing import List
import Database,models
from sqlalchemy.orm import Session
from repository import blog


get_db = Database.get_db

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"],
)



@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request:Schemasdb.Blog,db:Session=Depends(get_db),get_current_user:Schemasdb.Users=Depends(get_current_user)):
    return blog.create(request,db)

@router.get('/',response_model=List[Schemasdb.ShowBlog])
def Get_All(db:Session = Depends(get_db),get_current_user:Schemasdb.Users=Depends(get_current_user)):
    return blog.get_all(db)

@router.get('/{id}',response_model=Schemasdb.ShowBlog)
def get(id,response:Response,db:Session = Depends(get_db),get_current_user:Schemasdb.Users=Depends(get_current_user)):
    return blog.get_piese(id,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int,db:Session = Depends(get_db),get_current_user:Schemasdb.Users=Depends(get_current_user)):
    return blog.destroy(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int,response:Response,request:Schemasdb.Blog,db:Session = Depends(get_db),get_current_user:Schemasdb.Users=Depends(get_current_user)):
    return blog.update(id,request,db)

