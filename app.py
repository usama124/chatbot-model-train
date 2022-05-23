import uvicorn
from fastapi import FastAPI, Depends
from route import train_route, root_router


# API description
description = "API for training models in background"


# FastAPI initialization and metadata for the documentation
app = FastAPI(
    root_path="/",
    title="Model Train API",
    description=description,
    version="0.5.0",
    contact={
        "name": "USAMA TAHIR",
        "email": "usamatahir717@gmail.com"
    }
)

app.include_router(root_router.router) # for root
app.include_router(train_route.router) # for login

#
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)