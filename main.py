from sanic import Sanic
from sanic.response import text

app = Sanic("Burgerbot")

@app.get("/")
async def hello_world(req):
    return text("<p>Hello, World!</p>")

@app.post("/hit")
async def hit(req):
    print("I was hit")
    print(req.body)
    return text("Ok")
