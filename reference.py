reference/placeholder

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import logging
import os
from schema.model import Article
logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)
app=FastAPI()
entries=["static/entry1.txt","static/entry2.txt","static/entry3.txt"]
@app.get("/api/grab/")
def grab_entry():
      final_msg=""
      for i in range(len(entries)):
          with open(entries[i], "r") as file:
            final_msg=final_msg+str(file.read()+"\n")
      return {"message":final_msg}

@app.get("/articles/{article_name}")
def get_article(article_name):
    logger.info(article_name)
    first_match = next(
    (name for name in os.listdir('static') if article_name in name),
        None
    )
    with open("static/"+str(first_match), "r") as file:
        file_text=str(file.read()+"\n")
    logger.info(first_match)
    return {"message":file_text}

@app.get("/search")
def search_articles(query):
    for i in os.listdir('static'):
        if i.endswith(".txt"):
            with open("static/"+i) as file:
                file_text=file.read()
                if query in file_text:
                    return{"message":True}
    return{"message":False}

@app.post("/article/create")
def create_article(article:Article):
    with open(f"static/{article.title}.txt", 'w') as file:
        file.write(article.content)
    return{"message":'success'}


app.mount("/", StaticFiles(directory="static", html=True), name="static")

