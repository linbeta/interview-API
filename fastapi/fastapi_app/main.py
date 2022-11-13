from fastapi import FastAPI
from .routers import example
import uvicorn


app = FastAPI()
# incluse router example
app.include_router(example.router)


@app.get("/")
def root():
    return "Welcome! please visit http://127.0.0.1:8000/docs for this API documentation. :)"

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
