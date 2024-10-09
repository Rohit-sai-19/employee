from sqlalchemy.orm import Session
import models
import schemas
from hash import Hash
from fastapi import HTTPException,status
from datetime import datetime 

def create_emp(request: schemas.Emp, db: Session):
    new_emp = models.Emp(
        first_name=request.first_name,
        last_name=request.last_name,
        email_id=request.email_id
    )
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp

def get_emp_by_id(id: int, db: Session):
    emp = db.query(models.Emp).filter(models.Emp.id == id).first()
    if not emp:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with id {id} not available"
        )
    return emp

def get_all_employees(db: Session):
    employees = db.query(models.Emp).all()
    return employees

def delete_emp(id: int, db: Session):
    del_emp = db.query(models.Emp).filter(models.Emp.id == id).first()
    if not del_emp:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with id {id} not found"
        )
    db.delete(del_emp)
    db.commit()

def update_emp(id: int, request: schemas.Emp, db: Session):
    emp_to_update = db.query(models.Emp).filter(models.Emp.id == id).first()
    if not emp_to_update:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with id {id} not found"
        )
    emp_to_update.first_name = request.first_name
    emp_to_update.last_name = request.last_name
    emp_to_update.email_id = request.email_id
    db.commit()
    db.refresh(emp_to_update)
    return emp_to_update

def login(id: int, db: Session):
    # Logic to handle employee login
    emp_to_login = db.query(models.Emp).filter(models.Emp.id == id).first()
    if not emp_to_login:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with id {id} not found"
        )
    # Implement your login logic, such as updating the login timestamp
    emp_to_login.login = datetime.utcnow().isoformat()
    db.commit()
    return {"message": "Employee logged in successfully"}

def logout(id: int, db: Session):
    # Logic to handle employee logout
    emp_to_logout = db.query(models.Emp).filter(models.Emp.id == id).first()
    if not emp_to_logout:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with id {id} not found"
        )
    # Implement your logout logic, such as updating the logout timestamp
    emp_to_logout.logout = datetime.utcnow().isoformat()
    db.commit()
    return {"message": "Employee logged out successfully"}

def emp_info(request: schemas.EmpLog, db: Session):
    new_emp_log = models.EmpLog(
        email_id=request.email_id,
        password=Hash.bcrypt(request.password)
    )
    db.add(new_emp_log)
    db.commit()
    db.refresh(new_emp_log)
    return new_emp_log
