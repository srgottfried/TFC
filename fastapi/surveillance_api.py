from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Metadata(BaseModel):
    user: str
    date: str
    url: str
    title: Optional[str]
    description: Optional[str]
    area: Optional[str]
    type: Optional[str]
    sector: Optional[str]


metadata_db = []


@app.get("/")
async def root():
    return metadata_db


@app.post("/")
async def root(metadata: Metadata):
    if not url_is_present(metadata.url):
        metadata_db.append(metadata)
        return {"info": "OK"}
    else:
        return {"error": "URL already exists in DB"}


def url_is_present(url: str) -> bool:
    slot = list(filter(lambda metadata: metadata.url == url, metadata_db))
    return slot != []
