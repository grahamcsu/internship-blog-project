from pydantic import BaseModel

class Article(BaseModel):
    title:str
    content:str

class ArticleCreate(BaseModel):
    title:str
    content:str
    author_id:int

class ArticleUpdate(BaseModel):
    title:str
    content:str

class AuthorCreate(BaseModel):
    firstname:str
    lastname:str