from sqlalchemy.orm import Session
from models.material import Material
from schemas.material import MaterialCreate

def create_material(db: Session, material_data: MaterialCreate, class_id: int):
    db_material = Material(**material_data.dict(), class_id=class_id)
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material

def get_material(db: Session, material_id: int):
    return db.query(Material).filter(Material.id == material_id).first()
