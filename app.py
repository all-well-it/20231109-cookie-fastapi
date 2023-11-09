from fastapi import FastAPI, Request, HTTPException, status, Response
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
from fastapi import Cookie

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["content-disposition"]
)


@app.get("/cookie")
def root(response: Response):
    response.set_cookie(
        key="fakesession",
        value="fake-cookie-session-value",
        domain="localhost"
    )
    return {"message": "Come to the dark side, we have cookies"}


@app.get("/cookie-test")
def root(fakesession: Annotated[str | None, Cookie()] = None):
    print(fakesession)
    return {"message": "done"}


