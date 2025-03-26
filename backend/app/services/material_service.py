from sqlalchemy.orm import Session
from db.models import Material  # Corregida importación
from schemas.material import MaterialCreate
from fastapi import HTTPException

def create_material(db: Session, material_data: MaterialCreate, class_id: int):
    db_material = Material(**material_data.dict(), class_id=class_id)
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material

def get_material(db: Session, material_id: int):
    material = db.query(Material).filter(Material.id == material_id).first()
    if not material:
        raise HTTPException(status_code=404, detail="Material not found")
    return material

def delete_material(db: Session, material_id: int):
    material = get_material(db, material_id)
    db.delete(material)
    db.commit()
    return {"message": "Material deleted successfully"}
