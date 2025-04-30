from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, String, Integer, Float, DateTime, JSON, ForeignKey
from datetime import datetime

# Created by nichervan essa
class Base(DeclarativeBase):
    pass
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    role = Column(String(100))
    username = Column(String(20))
    password = Column(String(100))


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    price = Column(Float)
    barcode = Column(String(30))
    stock = Column(Integer)
    image = Column(String(100), default="image.png")
    sales_quantity = Column(Integer, nullable=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category_name = Column(String(50))

    stock_entries = relationship("StockEntry", back_populates="product", cascade="all, delete")
    stock_exits = relationship("StockExit", back_populates="product", cascade="all, delete")

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    
    products = relationship("Product", backref="category", cascade="all, delete")


class StockEntry(Base):
    __tablename__ = "stock_entries"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    entry_date = Column(DateTime, default=datetime.now)
    report_id = Column(Integer, ForeignKey("sales_reports.id"), nullable=True)
    
    product = relationship("Product", back_populates="stock_entries")


class StockExit(Base):
    __tablename__ = "stock_exits"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    exit_date = Column(DateTime, default=datetime.now)
    report_id = Column(Integer, ForeignKey("sales_reports.id"), nullable=True)
    
    product = relationship("Product", back_populates="stock_exits")


class SalesReport(Base):
    __tablename__ = "sales_reports"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    date = Column(String(22))
    cashier = Column(String(50))
    employee = Column(String(40))
    
    sales = relationship("ProductSale", backref="sales_report", cascade="all, delete-orphan")
    stock_entries = relationship("StockEntry", backref="sales_report", cascade="all, delete-orphan")
    stock_exits = relationship("StockExit", backref="sales_report", cascade="all, delete-orphan")


class ProductSale(Base):
    __tablename__ = "product_sales"
    
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    time = Column(String(10), default="08:00")
    products = Column(JSON, nullable=False)
    total_items = Column(Integer)
    total_amount = Column(Float)
    report_id = Column(Integer, ForeignKey("sales_reports.id"))
    customer = Column(String(50))
    employee = Column(String(40))
    payment_method = Column(String(40))


class AccountProduct(Base):
    __tablename__ = "account_products"
    
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.now)
    items = Column(JSON, nullable=False)
    account_id = Column(Integer, ForeignKey('open_accounts.id'), nullable=False)
    
    account = relationship("OpenAccount", back_populates="products")


class OpenAccount(Base):
    __tablename__ = "open_accounts"
    
    id = Column(Integer, primary_key=True)
    customer_name = Column(String(100), nullable=False, unique=True)
    table_id = Column(Integer, ForeignKey('tables.id'), nullable=True)
    
    products = relationship("AccountProduct", back_populates="account", cascade="all, delete")
    table = relationship("Table", back_populates="open_accounts")


class StockReport(Base):
    __tablename__ = 'stock_reports'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    report_id = Column(Integer, nullable=False, unique=True)
    history = Column(JSON, nullable=False)


class Table(Base):
    __tablename__ = "tables"
    
    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False, unique=True)
    capacity = Column(Integer, nullable=False)
    status = Column(String(20), default="available")
    
    open_accounts = relationship("OpenAccount", back_populates="table", cascade="all, delete")


class PaymentMethod(Base):
    __tablename__ = "payment_methods"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(200))
    active = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.now)
class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True)
    customer_name = Column(String(100), nullable=False)
    phone_number = Column(String(20), nullable=True)
    total_amount = Column(Float, nullable=False)
    amount_paid = Column(Float, default=0.0)
    remaining_amount = Column(Float, nullable=False)
    status = Column(String(20), default="unpaid")  # unpaid / paid / partial
    created_at = Column(DateTime, default=datetime.now)

    products = relationship("LoanProduct", back_populates="loan", cascade="all, delete")


class LoanProduct(Base):
    __tablename__ = "loan_products"

    id = Column(Integer, primary_key=True)
    loan_id = Column(Integer, ForeignKey("loans.id"), nullable=False)
    product_name = Column(String(100), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    total_price = Column(Float, nullable=False)

    loan = relationship("Loan", back_populates="products")
# ---- Continue after your LoanProduct class ----

# Staff (Employees / Cashiers)
class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    role = Column(String(50), nullable=False)  # Admin, Cashier, Waiter, etc
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    phone = Column(String(20))
    email = Column(String(100))
    hire_date = Column(DateTime, default=datetime.now)
    active = Column(Integer, default=1)  # 1: active, 0: inactive

    shifts = relationship("Shift", back_populates="employee")
    expenses = relationship("Expense", back_populates="employee")


# Discounts Table
class Discount(Base):
    __tablename__ = "discounts"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    amount = Column(Float, nullable=False)  # Example: 5.0 or 10.0
    is_percentage = Column(Integer, default=0)  # 0: fixed amount, 1: percentage
    active = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.now)


# Taxes Table
class Tax(Base):
    __tablename__ = "taxes"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    percentage = Column(Float, nullable=False)
    active = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.now)


# Shift Management Table
class Shift(Base):
    __tablename__ = "shifts"

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    start_time = Column(DateTime, default=datetime.now)
    end_time = Column(DateTime, nullable=True)
    opening_cash = Column(Float, default=0.0)
    closing_cash = Column(Float, default=0.0)

    employee = relationship("Employee", back_populates="shifts")


# Receipt Table (One Receipt per Sale)
class Receipt(Base):
    __tablename__ = "receipts"

    id = Column(Integer, primary_key=True)
    sale_id = Column(Integer, ForeignKey("product_sales.id"), nullable=False)
    receipt_number = Column(String(50), unique=True, nullable=False)
    subtotal = Column(Float, nullable=False)
    tax = Column(Float, nullable=False)
    discount = Column(Float, nullable=True, default=0.0)
    total = Column(Float, nullable=False)
    paid = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    sale = relationship("ProductSale", back_populates="receipt")


# Link Receipt to ProductSale (extend ProductSale a little)
ProductSale.receipt = relationship("Receipt", back_populates="sale", uselist=False)


# Expenses Table
class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    amount = Column(Float, nullable=False)
    description = Column(String(200))
    date = Column(DateTime, default=datetime.now)
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=True)

    employee = relationship("Employee", back_populates="expenses") 