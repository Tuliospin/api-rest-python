from sqlalchemy.orm import Session
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate


def get_all(db: Session, owner_id: int, skip: int = 0, limit: int = 100):
    return db.query(Item).filter(Item.owner_id == owner_id).offset(skip).limit(limit).all()


def get_by_id(db: Session, item_id: int, owner_id: int):
    return db.query(Item).filter(Item.id == item_id, Item.owner_id == owner_id).first()


def create(db: Session, item_in: ItemCreate, owner_id: int):
    item = Item(**item_in.dict(), owner_id=owner_id)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update(db: Session, item: Item, item_in: ItemUpdate):
    for field, value in item_in.dict(exclude_unset=True).items():
        setattr(item, field, value)
    db.commit()
    db.refresh(item)
    return item


def delete(db: Session, item: Item):
    db.delete(item)
    db.commit()
