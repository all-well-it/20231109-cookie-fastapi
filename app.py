from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import starlette.status as status
import uuid

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["content-disposition"]
)


@app.post("/redirect")
async def root(d: dict):
    print('d', d)
    token = '-'.join([str(uuid.uuid4()) for i in range(10)])
    return {"token": token}

