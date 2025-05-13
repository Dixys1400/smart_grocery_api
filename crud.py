from sqlalchemy.orm import Session
import models, schemas
from datetime import datetime


def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(
        name=item.name,
        category=item.category,
        purchased=False
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items(db: Session):
    return db.query(models.Item).order_by(models.Item.added_at.desc()).all()

def update_item(db: Session, item_id, item: schemas.ItemUpdate):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not db_item:
        return None
    for key, value in item.dict(exclude_unset=True).items():
        setattr(db_item, key, value)
        if key == "purchased" and value:
            db_item.purchase_count += 1
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_item(db: Session, item_id: int):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
    return item

def get_suggested_items(db: Session):
    return db.query(models.Item).filter(models.Item.purchased == False).order_by(models.Item.purchase_count.desc()).limit(5).all()
