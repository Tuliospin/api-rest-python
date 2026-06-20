from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.item import ItemCreate, ItemOut, ItemUpdate
from app.services import item_service
from app.core.deps import get_current_user
from app.db.session import get_db
from app.models.user import User

router = APIRouter()


@router.get("/", response_model=List[ItemOut])
def list_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return item_service.get_all(db, current_user.id, skip, limit)


@router.post("/", response_model=ItemOut, status_code=201)
def create_item(
    item_in: ItemCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return item_service.create(db, item_in, current_user.id)


@router.get("/{item_id}", response_model=ItemOut)
def get_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    item = item_service.get_by_id(db, item_id, current_user.id)
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return item


@router.put("/{item_id}", response_model=ItemOut)
def update_item(
    item_id: int,
    item_in: ItemUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    item = item_service.get_by_id(db, item_id, current_user.id)
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return item_service.update(db, item, item_in)


@router.delete("/{item_id}", status_code=204)
def delete_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    item = item_service.get_by_id(db, item_id, current_user.id)
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    item_service.delete(db, item)
