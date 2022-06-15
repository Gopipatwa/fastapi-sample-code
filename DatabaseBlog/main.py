from fastapi import FastAPI
import models
from Database import enigne
from routers import blog,user,authentication

# run app using cmd like uvicorn main:app --reload

app = FastAPI()

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
models.Base.metadata.create_all(enigne)
# is a valid pydantic field type   if not create instance with pydantic BaseModel
