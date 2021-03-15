from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# import socket

app = FastAPI()

# from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware
# # proxy_ip = socket.gethostbyname("*")
# app.add_middleware(ProxyHeadersMiddleware, trusted_hosts="*")

from sample_sheets import main

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/moviepicks")
async def root():
    values = main()
    print(values)
    return {"data": values}
