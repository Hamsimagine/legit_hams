from fastapi import FastAPI, Depends, HTTPException # type: ignore
from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from pydantic import BaseModel
from typing import List

# Database setup
DATABASE_URL = "sqlite:/https://github.com/Hamsimagine/legit_hams.git"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# SQLAlchemy models
class SmartFarmData(Base):
    __tablename__ = ""
    
    id = Column(Integer, primary_key=True, index=True)
    level = Column(Float, nullable=False)
    flowtoday = Column(Float, nullable=False)
    pompa = Column(Float, nullable=False)
    listrik = Column(Float, nullable=False)
    rellay = Column(Float, nullable=False)

# Pydantic models
class SmartFarmDataCreate(BaseModel):
    level: float
    flowtoday: float
    pompa: float
    listrik: float
    rellay: float

class SmartFarmDataResponse(SmartFarmDataCreate):
    id: int

    class Config:
        from_attributes = True  # Pydantic V2

# FastAPI setup
app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create database tables (if not created already)
Base.metadata.create_all(bind=engine)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Flow Meter IoT"}

# Endpoint to fetch all data
@app.get("/data/", response_model=List[SmartFarmDataResponse])
def read_all_smartfarm_data(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    data = db.query(SmartFarmData).offset(skip).limit(limit).all()
    return data

# Endpoint to fetch data by ID
@app.get("/data/{data_id}", response_model=SmartFarmDataResponse)
def read_smartfarm_data(data_id: int, db: Session = Depends(get_db)):
    db_data = db.query(SmartFarmData).filter(SmartFarmData.id == data_id).first()
    if db_data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return db_data

# Endpoint to update data by ID
@app.put("/data/{data_id}", response_model=SmartFarmDataResponse)
def update_smartfarm_data(data_id: int, data: SmartFarmDataCreate, db: Session = Depends(get_db)):
    db_data = db.query(SmartFarmData).filter(SmartFarmData.id == data_id).first()
    if db_data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    # Update data
    db_data.level = data.level
    db_data.flowtoday = data.flowtoday
    db_data.pompa = data.pompa
    db_data.listrik = data.listrik
    db_data.rellay = data.rellay

    db.commit()
    db.refresh(db_data)
    return db_data
