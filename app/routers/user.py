from fastapi import APIRouter


router_2 = APIRouter(prefix='/user', tags=['user'])

@router_2.get("/")
async def all_users():
    pass

@router_2.get("/user_id")
async def user_by_id():
    pass

@router_2.post("/create")
async def create_user():
    pass

@router_2.put("/update")
async def update_user():
    pass

@router_2.delete("/delete")
async def delete_user():
    pass

