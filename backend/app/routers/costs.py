from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from .. import models, schemas
from ..services import allocation, excel_import
from ..dependencies import get_db

router = APIRouter()


@router.get("/", response_model=list[schemas.CostEntryOut])
def list_costs(db: Session = Depends(get_db)):
    return db.query(models.CostEntry).all()


@router.post("/import-excel", response_model=list[schemas.CostEntryOut])
def import_costs_from_excel(
    file: UploadFile = File(...), db: Session = Depends(get_db)
):
    """Import cost entries from an uploaded Excel file."""
    df = excel_import.load_spend_from_excel(file.file)
    entries = allocation.allocate_costs(df)
    for entry in entries:
        db.add(entry)
    db.commit()
    for entry in entries:
        db.refresh(entry)
    return entries
