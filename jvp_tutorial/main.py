from fastapi import (
    FastAPI,
    Query,
    Path,
    Body,
    Cookie,
    Header,
    Form,
    status,
    File,
    UploadFile,
)
from enum import Enum
from typing import Optional, List, Literal, Union
from pydantic import BaseModel, Field, HttpUrl, EmailStr
from uuid import UUID
from datetime import datetime, time, timedelta

app = FastAPI()

# @app.get("/", description="This is our first route. ")
# async def base_get_root():
# return {"message" : "Hello World!"}
#
# @app.post("/")
# async def post():
# return {"messasge" : "Hello from the post route!"}
#
# @app.put("/")
# async def put():
# return {"message" : "Hello from the put route!"}
#
# @app.get("/user")
# async def list_user():
# return {"message" : "list user route"}
#
# @app.get("/users/me")
# async def get_current_user():
# return {"Message": "this is the current user"}
#
# @app.get("/user/{user_id}")
# async def get_item(user_id: str):
# return {"item_id" : user_id}
#
# class FoodEnum(str, Enum):
# fruits = "fruits"
# vegetables = "vegetables"
# dairy = "dairy"
#
# @app.get("/foods/{food_name}")
# async def get_food(food_name: FoodEnum):
# if food_name == FoodEnum.vegetables:
# return {"food_name": food_name, "message": "you are healthy"}
#
# if food_name.value == "fruits":
# return {
# "food_name": food_name,
# "message": "you are still healthy but like sweet things"
# }
# return {"food_name": food_name, "message": "I like chocolate milk"}
#
# fake_items_db = [{"item_name" : "Foo"}, {"item_name" : "Bar"}, {"item_name" : "Baz"}]
#
# @app.get("/items")
# async def list_items(skip: int = 0, limit: int = 10):
#    return fake_items_db[skip : skip + limit]
#
# @app.get("/items/{item_id}")
# async def get_item(item_id: str, sample_query_param: str, q: str | None = None, short: bool = False):
# item = {"item_id" : item_id, "sample_query_param" : sample_query_param}
# if q:
# item.update({"q" : q})
# if not short:
# item.update({"description" : "Pydantic!"})
# return item
#
# class Item(BaseModel):
# name: str
# description: Optional[str] = None # python < 3.10
# price: float
# tax: float | None = None # python > 3.10
#
# @app.post("/items")
# async def create_item(item: Item):
# item_dict = item.model_dump() # item.dict() is deprecated
# if item.tax:
# price_with_tax = item.price + item.tax
# item_dict.update({"price_with_tax" : price_with_tax})
# return item_dict
#
# @app.put("/items/{item_id}")
# async def create_item_with_put(item_id: int, item: Item, q: str | None = None):
# result = {"item_id": item_id, **item.model_dump()}
# if q:
# result.update({"q" : q})
# return result
#
# @app.get("/items")
# async def read_items(
# q: str
# | None = Query(
# None,
# min_length=3,
# max_length=10,
# title="Sample query string",
# description="This is a sample query string",
# alias="item-query"
# )
# ):
# results = {"items": [{"item_id": "Foo"}, {"item_id" : "Bar"}]}
# if q:
# results.update({"q": q})
# return results
#
# @app.get("/items_hidden")
# async def hidden_query_route(hidden_query: str | None = Query(None, include_in_schema=False)):
# if hidden_query:
# return {"hidden_query": hidden_query}
# return {"hidden_query": "Not found"}
#
# @app.get("/items_validation/{item_id}")
# async def read_items_validation(
# *, # if non-default params like q after default-set params like item_id we need *, or switch order of q and item_id
# item_id: int = Path(..., title="The ID of the item to get", gt=10, le=100),
# q: str = "default q",
# size: float = Query(..., gt=0, lt= 7.75)
# ):
# results = {"item_id": item_id}
# if q:
# results.update({"q": q})
# return results
#

""" 
Part 7 -> Body - Multiple Parameters
"""

# class Item(BaseModel):
# name: str
# description: str | None = None
# price: float
# tax: float | None = None
#
# class User(BaseModel):
# username: str
# full_name: str | None = None
#
# @app.put("/items/{item_id}")
# async def update_item(
# *,
# item_id: int = Path(..., title="The ID of the item to get", ge=0, le=150),
# q: str | None = None,
# item: Item = Body(...,  embed=True),
# user: User,
# importance: int = Body(...)
# ):
# results = {"item_id": item_id}
# if q:
# results.update({"q": q})
# if item:
# results.update({"item": item})
# if user:
#    results.update({"user": user})
# if importance:
#    results.update({"importance": importance})
# return results

"""
Part 8 -> Body - Fields
"""

# class Item(BaseModel):
# name: str
# description: str | None = Field(None, title = "The description of the item", max_length = 300)
# price: float = Field(..., gt=0, description="The price must be greater than zero.")
# tax: float | None = None
#
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item = Body(...)):
# results = {"item_id": item_id, "item": item}
# return results

"""
Part 9 -> Body - Nested Models
"""

# class Image(BaseModel):
# url: HttpUrl
# name: str
#
# class Item(BaseModel):
# name: str
# description: str | None = None
# price: float
# tax: float | None = None
# tags: set[str] = []
# image: list[Image] | None = None
#
# class Offer(BaseModel):
# name: str
# description: str | None = None
# price: float
# items: list[Item]
#
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
# results = {"item_id": item_id, "item": item}
# return results
#
# @app.post("/offers")
# async def create_offer(offer: Offer = Body(..., embed=True)):
# return offer
#
# @app.post("/images/multiple")
# async def create_multiple_images(images: list[Image] = Body(..., embed=True)):
# return images

"""
Part 10 - Declare Request Example Data
"""

# class Item(BaseModel):
#    name: str #= Field(..., example="Foo")
#    description: str | None = None #Field(None, example="A very nice item")
#    price: float #= Field(..., example=16.25)
#    tax: float | None = None #Field(None, example=1.67)
#
#    # class Config:
#        # schema_extra = {
#            # "example": {
#                # "name": "Foo",
#                # "description": "A very nice Item",
#                # "price": 16.25,
#                # "tax": 1.67,
#            # }
#        # }
#
# @app.put("/items/{item_id}")
# async def update_item(
#    item_id: int,
#    item: Item = Body(
#        ...,
#        example={
#            "name": "Foo",
#            "description": "A very nice Item",
#            "price": 16.25,
#            "tax": 1.67,
#        }
#    )):
#    results = {"item_id": item_id, "item": item}
#    return results

"""
Part 11 - Extra Data Types
"""

# @app.put("/items/{item_id}")
# async def read_items(
#    item_id: UUID,
#    start_date: datetime | None = Body(None),
#    end_date: datetime | None = Body(None),
#    repeat_at: time | None = Body(None),
#    process_after: timedelta | None = Body(None),
# ):
#    start_process = start_date + process_after
#    duration = end_date - start_process
#    return {
#        "item_id": item_id,
#        "start_date": start_date,
#        "end_date": end_date,
#        "repeat_at": repeat_at,
#        "process_after": process_after,
#        "start_process": start_process,
#        "duration": duration,
#        }
#

"""
Part 12 - Cookie and Header Parameters
"""


# @app.get("/items")
# async def read_items(
#    cookie_id: str | None = Cookie(None),
#    accept_encoding: str | None = Header(None),
#    sec_ch_va: str | None = Header(None),
#    user_agent: str | None = Header(None),
#    x_token: list[str] | None = Header(None),
# ):
#    return {
#        "cookie_id": cookie_id,
#        "Accept-Encoding": accept_encoding,
#        "sec-ch-va": sec_ch_va,
#        "User-Agent": user_agent,
#        "X-Token values": x_token,
#    }
#

"""
Part 13 - Response Model
"""


# class Item(BaseModel):
#    name: str
#    description: str | None = None
#    price: float
#    tax: float = 10.5
#    tags: list[str] = []
#
#
# items = {
#    "foo": {"name": "Foo", "price": 50.2},
#    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
#    "baz": {"name": "Baz", "description": None, "price": 58.2, "tax": 10.5, "tags": []},
# }
#
#
# @app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
# async def read_item(item_id: Literal["foo", "bar", "baz"]):
#    return items[item_id]
#
#
# @app.post("/items/", response_model=Item)
# async def create_item(item: Item):
#    return item
#
#
# @app.get(
#    "/items/{item_id}/name",
#    response_model=Item,
#    response_model_include={"name", "description"},
# )
# async def read_item_name(item_id: Literal["foo", "bar", "baz"]):
#    return items[item_id]
#
#
# @app.get("/item/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
# async def read_items_public_data(item_id: Literal["foo", "bar", "baz"]):
#    return items[item_id]
#
#
# class UserBase(BaseModel):
#    username: str
#    email: EmailStr
#    full_name: str | None = None
#
#
# class UserIn(UserBase):
#    password: str
#
#
# class UserOut(UserBase):
#    pass
#
#
# @app.post("/user/", response_model=UserOut)
# async def create_user(user: UserIn):
#    return user
#

"""
Part 14 - Extra Models
"""


# class UserBase(BaseModel):
#    username: str
#    email: EmailStr
#    full_name: str | None = None
#
#
# class UserIn(UserBase):
#    password: str
#
#
# class UserOut(UserBase):
#    pass
#
#
# class UserInDB(UserBase):
#    hashed_password: str
#
#
# def fake_password_hasher(raw_password: str):
#    return f"supersecret{raw_password}"
#
#
# def fake_save_user(user_in: UserIn):
#    hashed_password = fake_password_hasher(user_in.password)
#    user_in_db = UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
#    print("userin.dict", user_in.model_dump())
#    print("user 'saved'.")
#    return user_in_db
#
#
# @app.post("/user/", response_model=UserOut)
# async def create_user(user_in: UserIn):
#    user_saved = fake_save_user(user_in)
#    return user_saved
#
#
# class BaseItem(BaseModel):
#    description: str
#    type: str
#
#
# class CarItem(BaseItem):
#    type: str = "car"
#
#
# class PlaneItem(BaseItem):
#    type: str = "plane"
#    size: int
#
#
# items = {
#    "item1": {"description": "All my friends drive a low rider", "type": "car"},
#    "item2": {
#        "description": "Music is my aeroplane, it's my aeroplane",
#        "type": "plane",
#        "size": 5,
#    },
# }
#
#
# @app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
# async def read_item(item_id: Literal["item1", "item2"]):
#    return items[item_id]
#
#
# class ListItem(BaseModel):
#    name: str
#    description: str
#
#
# list_items = [
#    {"name": "Foo", "description": "There comes my hero"},
#    {"name": "Red", "description": "It's my aeroplane"},
# ]
#
#
# @app.get("/list_items/", response_model=list[ListItem])
# async def read_items():
#    return items
#
#
# @app.get("/arbitrary", response_model=dict[str, float])
# async def get_arbitrary():
#    return {"foo": 1, "bar": "hello"}
#

"""
Part 15 - Response Status Codes
"""


# @app.post("/items", status_code=status.HTTP_201_CREATED)
# async def create_item(name: str):
#    return {"name": name}
#
#
# @app.delete("/items/{pk}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_item(pk: str):
#    print("pk", pk)
#    return pk
#
#
# @app.get("/items/", status_code=status.HTTP_302_FOUND)
# async def read_items_redirect():
#    return {"hello": "world"}
#

"""
Part 16 - Form Fields
"""


# @app.post("/login/")
# async def login(username: str = Form(...), password: str = Form(...)):
#    print("password", password)
#    return {"username": username}
#
#
# @app.post("/login-json/")
# async def login_json(username: str = Body(...), password: str = Body(...)):
#    print("password", password)
#    return {"username": username}

"""
Part 17 - Request Files
"""


@app.post("/files/")
async def create_file(
    files: list[bytes] = File(..., description="A file read as bytes")
):
    if not files:
        return {"message": "no files sent"}
    return {"file-sizes": [len(file) for file in files]}


@app.post("/uploadfile/")
async def create_upload_file(
    file: UploadFile = File(..., description="A file read as UploadFile")
):
    if not file:
        return {"message": "No upload file sent"}
    return {"filename": file.filename}
