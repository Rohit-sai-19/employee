from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
import schemas, database,oauth2
from repository import emp  # Make sure to create a repository module for your logic
from oauth2 import get_current_user
router = APIRouter(tags=['Employee'])

get_db = database.get_db

@router.post("/create", response_model=schemas.Emp)
def create_emp(request: schemas.Emp, db: Session = Depends(get_db),current_user : schemas.EmpLog= Depends(get_current_user)):
    return emp.create_emp(request, db)

@router.get('/employee/all', status_code=status.HTTP_200_OK)
def get_all_employees(db: Session = Depends(get_db),current_user : schemas.EmpLog= Depends(get_current_user)):
    return emp.get_all_employees(db)

@router.get('/employee/{id}', status_code=status.HTTP_200_OK)
def get_emp_by_id(id: int, db: Session = Depends(get_db),current_user : schemas.EmpLog= Depends(get_current_user)):
    return emp.get_emp_by_id(id, db)

@router.delete('/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_emp(id: int, db: Session = Depends(get_db),current_user : schemas.EmpLog= Depends(get_current_user)):
    return emp.delete_emp(id, db)

@router.put('/update/{id}', status_code=status.HTTP_204_NO_CONTENT)
def update_emp(id: int, request: schemas.Emp, db: Session = Depends(get_db),current_user : schemas.EmpLog= Depends(get_current_user)):
    return emp.update_emp(id, request, db)

@router.put('/login/{id}', status_code=status.HTTP_204_NO_CONTENT)
def login(id: int, db: Session = Depends(get_db),current_user : schemas.EmpLog= Depends(get_current_user)):
    return emp.login(id, db)

@router.put('/logout/{id}', status_code=status.HTTP_204_NO_CONTENT)
def logout(id: int, db: Session = Depends(get_db),current_user : schemas.EmpLog= Depends(get_current_user)):
    return emp.logout(id, db)

@router.post('/emp_info/', response_model=schemas.EmpLog, status_code=status.HTTP_201_CREATED)
def create_emp_info(request: schemas.EmpLog, db: Session = Depends(get_db),current_user : schemas.EmpLog= Depends(get_current_user)):
    return emp.emp_info(request, db)
