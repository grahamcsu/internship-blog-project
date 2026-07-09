from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, select, insert, delete, update
import logging
import sqlite3
import json
import pandas as pd
import os
from schema.model import Article, ArticleCreate, ArticleUpdate, AuthorCreate
logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)
app=FastAPI()
engine = create_engine('sqlite:///articles.db')
metadata= MetaData()
articles = Table("article", metadata, autoload_with=engine)
authors = Table("author", metadata, autoload_with=engine)


@app.get("/api/articles/all")
def get_all_articles():
    with engine.connect() as conn:
        rows = conn.execute(select(articles)).all()
        return [dict(row._mapping) for row in rows]

@app.get("/api/articles/{ser_id}")
def search_article(ser_id:int):
    print(ser_id)
    with engine.connect() as conn:
        result=conn.execute(select(articles).where(articles.c["Id"]==ser_id)).first()
        if not result:
            raise HTTPException(status_code=404,detail='Not Found')
        return dict(result._mapping)

@app.post("/api/articles")
def add_article(payload:ArticleCreate):
    with engine.begin() as conn:
        author_check=conn.execute(select(authors).where(authors.c["Id"]==payload.author_id)).first()
        if not author_check:
            raise HTTPException(status_code=400,detail='Bad Request')
        result=conn.execute(
            insert(articles)
            .values({"Title":payload.title, "Content":payload.content, "AuthorId":payload.author_id})
            .returning(articles.c["Id"]))
        new_id=result.scalar_one()
        row=conn.execute(select(articles).where(articles.c["Id"]==new_id)).first()
        return dict(row._mapping)
    
@app.put("/api/articles/update")
def update_article(upd_id,payload:ArticleUpdate):
    with engine.connect() as conn:
        conn.execute(update(articles).where(articles.c["Id"]==upd_id).values({"Title":payload.title, "Content":payload.content}))
        conn.commit()

@app.delete("/api/articles/delete")
def delete_article(del_id:int):
    with engine.begin() as conn:
        try:
            conn.execute(delete(articles).where(articles.c["Id"]==del_id)).first()
        except:
            print('not a valid delete target')

@app.get("/api/authors/all")
def get_all_authors():
    with engine.connect() as conn:
        rows = conn.execute(select(authors)).all()
        return [dict(row._mapping) for row in rows]

@app.get("/api/authors/{ser_id}")
def search_author(ser_id:int):
    print(ser_id)
    with engine.begin() as conn:
        result=conn.execute(select(authors).where(authors.c["Id"]==ser_id)).first()
        if not result:
            raise HTTPException(status_code=404,detail='Not Found')
        return dict(result._mapping)

@app.post("/api/authors")
def add_author(payload:AuthorCreate):
    with engine.begin() as conn:
        result=conn.execute(
            insert(authors)
            .values({"FirstName":payload.firstname, "LastName":payload.lastname})
            .returning(authors.c["Id"]))
        new_id=result.scalar_one()
        row=conn.execute(select(authors).where(authors.c["Id"]==new_id)).first()
        return dict(row._mapping)
    
@app.delete("/api/authors/delete")
def delete_authors(del_id:int):
    with engine.begin() as conn:
        try:
            conn.execute(delete(articles).where(articles.c["AuthorId"]==del_id))
            conn.execute(delete(authors).where(authors.c["Id"]==del_id)).first()
        except:
            print('not a valid delete target')

# finish delete-- DONE
# same stuff but for author-- later
# create tables through python-- later

app.mount("/", StaticFiles(directory="static", html=True), name="static")