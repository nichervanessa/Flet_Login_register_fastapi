from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import Employee,Expense,StockEntry,StockExit,Receipt,SalesReport,StockReport,Table,Tax,User,OpenAccount,PaymentMethod,Product,ProductSale,LoanProduct,AccountProduct,Shift,Discount,Loan,Category,Base
from Schema_server import EmployeeBase,UserLogin,EmployeeCreate,EmployeeRead,ExpenseBase,ExpenseCreate,ExpenseRead,StockEntryBase,StockEntryCreate,StockEntryRead,StockExitBase,StockExitCreate,StockExitRead,ReceiptBase,ReceiptCreate,ReceiptRead,TaxRead,LoanRead,UserRead,SalesReportBase,SalesReportCreate,SalesReportRead,ShiftRead,StockReportBase,StockReportCreate,StockReportRead,TableRead,ProductRead,CategoryRead,DiscountRead,LoanProductRead,OpenAccountRead,ProductSaleRead,PaymentMethodRead,AccountProductRead,TableBase,TableCreate,TaxBase,TaxCreate,UserBase,UserCreate,OpenAccountBase,OpenAccountCreate


def get_user(db:Session,name:str,role:str,username:str):
    user_info=db.query(User).filter(User.name==name,User.role==role,User.username==username).first()
    if user_info is None:
        raise HTTPException(status_code=404,detail="User not found")
    return user_info

def get_wallets(db=Session,skip:int=0,limit:int=50):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(user: UserCreate,db:Session):
    db_user=User(username=user.username,password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def login_user(user: UserLogin,db:Session):
    user_info=get_user(db,user.username)
    user_password=user.password

    get_password=db.query(User).filter(User.password==user_password).first()
    if user_info is None:
        raise HTTPException(status_code=404,detail="User not found")
    elif get_password is None:
        raise HTTPException(status_code=401,detail="Invalid password")
    return user_info