
from time import time
from faker import Faker

from fastapi import FastAPI,Request
from fastapi.responses import RedirectResponse
app = FastAPI()
faker = Faker()
@app.get("/")
async def read_root(request: Request):
   return RedirectResponse(f"{request.url}docs")
@app.get("/name")
async def get_fake_name():
   return{"Name":faker.name(), "Timestamp":time()}
@app.get("/address")
async def get_fake_address():
   return{"Address":faker.address(), "Timestamp":time()}
@app.get("/email")
async def get_fake_email():
   return{"Email":faker.email(), "Timestamp":time()}

@app.get("/all")
async def get_all_data():
   return{
      "Name":faker.name(),
      "Address":faker.address(),
      "Email":faker.email(),
      "Timestamp":time()
   }

