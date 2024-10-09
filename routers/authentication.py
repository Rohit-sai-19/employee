from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import database, models, token,schemas,jwt_utils
from hash import Hash
from datetime import timedelta

router = APIRouter(tags=['Authentication'])

@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session=Depends(database.get_db)):
    user = db.query(models.EmpLog).filter(models.EmpLog.email_id == request.username ).first()
    if not user :
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="invalid credentials")
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="invalid password")
    
    access_token = jwt_utils.create_access_token(
        data={"sub": user.email_id})
    return {"access_token":access_token, "token_type":"bearer"}