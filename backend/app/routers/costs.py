from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import models, schemas
from ..dependencies import get_db

router = APIRouter()


@router.get("/", response_model=list[schemas.CostEntryOut])
def list_costs(db: Session = Depends(get_db)):
    return db.query(models.CostEntry).all()
