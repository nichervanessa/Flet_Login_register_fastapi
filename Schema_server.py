from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from datetime import datetime

# -------------------- User --------------------
class UserBase(BaseModel):
    name: str
    role: str
    username: str

class UserCreate(UserBase):
    password: str
class UserLogin(UserBase):
    password:str
class UserRead(UserBase):
    id: int
    name:str
    role:str
    username: str


    class Config:
        orm_mode = True

# -------------------- Category --------------------
class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase): pass

class CategoryRead(CategoryBase):
    id: int
    class Config:
        orm_mode = True

# -------------------- Product --------------------
class ProductBase(BaseModel):
    title: str
    price: float
    barcode: str
    stock: int
    image: Optional[str] = "image.png"
    sales_quantity: Optional[int] = None
    category_id: int
    category_name: Optional[str] = None

class ProductCreate(ProductBase): pass

class ProductRead(ProductBase):
    id: int
    class Config:
        orm_mode = True

# -------------------- StockEntry --------------------
class StockEntryBase(BaseModel):
    name: Optional[str]
    product_id: int
    quantity: int
    report_id: Optional[int] = None

class StockEntryCreate(StockEntryBase): pass

class StockEntryRead(StockEntryBase):
    id: int
    entry_date: datetime
    class Config:
        orm_mode = True

# -------------------- StockExit --------------------
class StockExitBase(BaseModel):
    name: str
    product_id: int
    quantity: int
    report_id: Optional[int] = None

class StockExitCreate(StockExitBase): pass

class StockExitRead(StockExitBase):
    id: int
    exit_date: datetime
    class Config:
        orm_mode = True

# -------------------- SalesReport --------------------
class SalesReportBase(BaseModel):
    name: str
    date: str
    cashier: str
    employee: str

class SalesReportCreate(SalesReportBase): pass

class SalesReportRead(SalesReportBase):
    id: int
    class Config:
        orm_mode = True

# -------------------- ProductSale --------------------
class ProductSaleBase(BaseModel):
    date: datetime
    time: str = "08:00"
    products: Dict
    total_items: int
    total_amount: float
    report_id: Optional[int]
    customer: str
    employee: str
    payment_method: str

class ProductSaleCreate(ProductSaleBase): pass

class ProductSaleRead(ProductSaleBase):
    id: int
    class Config:
        orm_mode = True

# -------------------- AccountProduct --------------------
class AccountProductBase(BaseModel):
    items: Dict
    account_id: int

class AccountProductCreate(AccountProductBase): pass

class AccountProductRead(AccountProductBase):
    id: int
    date: datetime
    class Config:
        orm_mode = True

# -------------------- OpenAccount --------------------
class OpenAccountBase(BaseModel):
    customer_name: str
    table_id: Optional[int]

class OpenAccountCreate(OpenAccountBase): pass

class OpenAccountRead(OpenAccountBase):
    id: int
    class Config:
        orm_mode = True

# -------------------- StockReport --------------------
class StockReportBase(BaseModel):
    report_id: int
    history: Dict

class StockReportCreate(StockReportBase): pass

class StockReportRead(StockReportBase):
    id: int
    class Config:
        orm_mode = True

# -------------------- Table --------------------
class TableBase(BaseModel):
    number: int
    capacity: int
    status: str = "available"

class TableCreate(TableBase): pass

class TableRead(TableBase):
    id: int
    class Config:
        orm_mode = True

# -------------------- PaymentMethod --------------------
class PaymentMethodBase(BaseModel):
    name: str
    description: Optional[str]
    active: int = 1

class PaymentMethodCreate(PaymentMethodBase): pass

class PaymentMethodRead(PaymentMethodBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True

# -------------------- LoanProduct --------------------
class LoanProductBase(BaseModel):
    loan_id: int
    product_name: str
    quantity: int
    price: float
    total_price: float

class LoanProductCreate(LoanProductBase): pass

class LoanProductRead(LoanProductBase):
    id: int
    class Config:
        orm_mode = True

# -------------------- Loan --------------------
class LoanBase(BaseModel):
    customer_name: str
    phone_number: Optional[str]
    total_amount: float
    amount_paid: float = 0.0
    remaining_amount: float
    status: str = "unpaid"

class LoanCreate(LoanBase): pass

class LoanRead(LoanBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True

# -------------------- Employee --------------------
class EmployeeBase(BaseModel):
    name: str
    role: str
    username: str
    password: str
    phone: Optional[str]
    email: Optional[str]

class EmployeeCreate(EmployeeBase): pass

class EmployeeRead(EmployeeBase):
    id: int
    hire_date: datetime
    active: int
    class Config:
        orm_mode = True

# -------------------- Discount --------------------
class DiscountBase(BaseModel):
    name: str
    amount: float
    is_percentage: int = 0
    active: int = 1

class DiscountCreate(DiscountBase): pass

class DiscountRead(DiscountBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True

# -------------------- Tax --------------------
class TaxBase(BaseModel):
    name: str
    percentage: float
    active: int = 1

class TaxCreate(TaxBase): pass

class TaxRead(TaxBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True

# -------------------- Shift --------------------
class ShiftBase(BaseModel):
    employee_id: int
    start_time: Optional[datetime]
    end_time: Optional[datetime]
    opening_cash: float = 0.0
    closing_cash: float = 0.0

class ShiftCreate(ShiftBase): pass

class ShiftRead(ShiftBase):
    id: int
    class Config:
        orm_mode = True

# -------------------- Receipt --------------------
class ReceiptBase(BaseModel):
    sale_id: int
    receipt_number: str
    subtotal: float
    tax: float
    discount: float = 0.0
    total: float
    paid: float

class ReceiptCreate(ReceiptBase): pass

class ReceiptRead(ReceiptBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True

# -------------------- Expense --------------------
class ExpenseBase(BaseModel):
    title: str
    amount: float
    description: Optional[str]
    employee_id: Optional[int]

class ExpenseCreate(ExpenseBase): pass

class ExpenseRead(ExpenseBase):
    id: int
    date: datetime
    class Config:
        orm_mode = True
