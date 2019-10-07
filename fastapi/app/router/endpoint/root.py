import logging
# logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["Root"])
async def read_root():
    logging.info('request read_root')
    return {"Hello": "World"}


@router.get("/items/{item_id}", tags=["Root"])
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}