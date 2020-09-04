# Decorators

@instance.get()
@instance.post()
@instance.put()
@instance.delete()
@instance.options()
@instance.head()
@instance.patch()
@instance.trace()


# Minimal program
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
# Minimal program

# endpoint with parameter
# Checkout with http://127.0.0.1:8000/items/
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

# you can also use pedantic types
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

