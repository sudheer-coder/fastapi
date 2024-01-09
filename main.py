from typing import List

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from models import SessionLocal, insurance_data, User
from schema import insurance_create, UserCreate, userGet

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/user/", response_model=UserCreate)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = User(**user.dict())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating insurance: {str(e)}")

@app.post("/insurance/", response_model=insurance_create)
def create_insurance(insurance: insurance_create, db: Session = Depends(get_db)):
    try:
        db_insurance = insurance_data(**insurance.dict())
        db.add(db_insurance)
        db.commit()
        db.refresh(db_insurance)
        return insurance
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating insurance: {str(e)}")

@app.get("/userget/{user_id}", response_model=userGet)
def get_user(user_id: int, db: Session = Depends(get_db)):
    try:
        userecord=db.query(User).filter(User.user_id == user_id).first()
        if userecord is None:
            raise HTTPException(status_code=404, detail=f"user not found")
        return userecord
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating insurance: {str(e)}")

@app.get("/insuranceget/{insu_id}", response_model=insurance_create)
def get_insurance(insu_id: int, db: Session = Depends(get_db)):
    try:
        insurancerecord=db.query(insurance_data).filter(insurance_data.policy_holder_id == insu_id).first()
        if insurancerecord is None:
            raise HTTPException(status_code=404, detail=f"user not found")
        return insurancerecord
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating insurance: {str(e)}")
@app.get("/insuranceall", response_model=List[insurance_create])
def get_all_insurance(db: Session = Depends(get_db)):
    try:
        insurancerecord=db.query(insurance_data).all()
        if insurancerecord is None:
            raise HTTPException(status_code=404, detail=f"user not found")
        return insurancerecord
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating insurance: {str(e)}")
@app.put("/insuranceupdate/{insu_id}", response_model=insurance_create)
def put_insurance(insu_id: int,insurance:insurance_create, db: Session = Depends(get_db)):
    try:
        insurancerecord=db.query(insurance_data).filter(insurance_data.policy_holder_id == insu_id).first()
        if insurancerecord is None:
            raise HTTPException(status_code=404, detail=f"user not found")
        else:
            for key, value in insurance.dict().items():
                setattr(insurancerecord, key, value)
            db.commit()
            db.refresh(insurancerecord)
            return insurance
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating insurance: {str(e)}")
@app.put("/userupdate/{user_id}", response_model=UserCreate)
def put_user(user_id: int,user:UserCreate, db: Session = Depends(get_db)):
    try:
        userecord=db.query(User).filter(User.user_id == user_id).first()
        if userecord is None:
            raise HTTPException(status_code=404, detail=f"user not found")
        else:
            for key, value in user.dict().items():
                setattr(userecord, key, value)
            db.commit()
            db.refresh(userecord)
            return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating insurance: {str(e)}")
@app.delete("/insurancedel/{insu_id}", response_model=str)
def del_insurance(insu_id: int,db: Session = Depends(get_db)):
    try:
        insurancerecord=db.query(insurance_data).filter(insurance_data.policy_holder_id == insu_id).first()
        if insurancerecord is None:
            raise HTTPException(status_code=404, detail=f"user not found")
        else:
            db.delete(insurancerecord)
            db.flush()
            db.commit()
            return "deleted"
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating insurance: {str(e)}")
@app.delete("/userdel/{user_id}", response_model=str)
def del_insurance(user_id: int,db: Session = Depends(get_db)):
    try:
        userecord=db.query(User).filter(User.user_id == user_id).first()
        if userecord is None:
            raise HTTPException(status_code=404, detail=f"user not found")
        else:
            db.delete(userecord)
            db.flush()
            db.commit()
            return "deleted"
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating insurance: {str(e)}")
