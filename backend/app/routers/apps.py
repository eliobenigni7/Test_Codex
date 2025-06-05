from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import models, schemas
from ..dependencies import get_db

router = APIRouter()


@router.get("/", response_model=list[schemas.ApplicationOut])
def list_apps(db: Session = Depends(get_db)):
    return db.query(models.Application).all()


@router.post("/", response_model=schemas.ApplicationOut)
def create_app(app: schemas.ApplicationCreate, db: Session = Depends(get_db)):
    db_app = models.Application(**app.dict())
    db.add(db_app)
    db.commit()
    db.refresh(db_app)
    return db_app
