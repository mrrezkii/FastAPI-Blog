from fastapi import FastAPI
from . import schemas
from . import models
from .database import engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post('/blog')
def create(request: schemas.Blog):
    return request