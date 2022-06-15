from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from blog import Schemasdb,models
from blog import JWTtoken
from blog.Database import get_db
from fastapi.security import OAuth2PasswordRequestForm
from blog.Hashing import Hash
router = APIRouter(
    tags=['Authentication']
)

@router.post("/login")
def login(request:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(get_db)):
    print(request.username)
    user = db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"username {request.username} is not exists in database or Invalid Credentials")
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"Incorrect Password")
    
    # access_token_expires = timedelta(minutes=ACC)
    access_token = JWTtoken.create_access_token(data={"sub":user.email})
    return {"access_token":access_token,"token_type":"bearer"}