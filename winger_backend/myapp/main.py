from fastapi import FastAPI
from myapp.auth import auth
from myapp.users import users
from myapp.schools import schools

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(schools.router, prefix="/schools", tags=["Schools"])
