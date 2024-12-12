from fastapi import FastAPI

from .database import Base,engine
from .routers import router
#Initialize FastAPI
app = FastAPI()

Base.metadata.create_all(bind=engine)

#Rwgister Router
app.include_router(router=router, prefix="/api",tags=["todos"])