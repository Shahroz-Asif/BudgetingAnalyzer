import pyodbc
from tkinter import *


con1 = pyodbc.connect((r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                       r'DBQ=D:\NED\Programming Fundamentals (CT-175)\Assignments\Database2.accdb;'))
cursor1 = con1.cursor()


def purchase_wrt_month():
    cursor1.execute(f"SELECT * FROM Purchases ORDER BY PurchaseYear DESC, PurchaseMonth DESC")
    data = cursor1.fetchall()
    print(data, "\t Purchase Table Entries")

    purchase_entry = data[0]
    print()
    print(purchase_entry, "\t Purchase Table Selected entry w.r.t the Product ID:")

    cursor1.execute(f"SELECT * FROM Product WHERE ProductID = {str(purchase_entry[1])}" )
    data2 = cursor1.fetchall()
    product_entry = data2[0]
    print()
    print(product_entry, "\t Product Table entry w.r.t ProductID")

    cursor1.execute(f"SELECT * FROM ProductType WHERE ProductName = '{str(product_entry[2])}'")
    data3 = cursor1.fetchall()
    producttype_entry = data3[0]
    print()
    print(producttype_entry, "\t Product Type entry w.r.t ProductName / ProductType")

# purchase_wrt_month()

def purchase_with_year():
    cursor1.execute(f"SELECT * FROM Purchases ORDER BY PurchaseYear DESC, PurchaseMonth DESC")
    data = cursor1.fetchall()
    print(data, "\t Purchase Table Entries")

    purchase_entry = data[0]
    print()
    print(purchase_entry, "\t Purchase Table Selected entry w.r.t the Product ID:")

    cursor1.execute(f"SELECT * FROM Product WHERE ProductID = {str(purchase_entry[1])}" )
    data2 = cursor1.fetchall()
    product_entry = data2[0]
    print()
    print(product_entry, "\t Product Table entry w.r.t ProductID")

    cursor1.execute(f"SELECT * FROM ProductType WHERE ProductName = '{str(product_entry[2])}'")
    data3 = cursor1.fetchall()
    product_type_entry = data3[0]
    print()
    print(product_type_entry, "\t Product Type entry w.r.t ProductName / ProductType")

    cursor1.execute(f"SELECT * FROM Salary WHERE Year = {str(purchase_entry[3])}")
    data4 = cursor1.fetchall()
    purchase_year_entry = data4[0]
    print()
    print(purchase_year_entry)

    cursor1.execute(f"SELECT * FROM Category WHERE CategoryName = '{str(product_type_entry[1])}'")
    data5 = cursor1.fetchall()
    product_category_entry = data5[0]
    print(product_category_entry)

# purchase_with_year()

def purchase_accordingto_year():
    cursor1.execute(f"SELECT * FROM Purchases WHERE PurchaseYear = 2021")
    data = cursor1.fetchall()
    print(data, "\t Purchase Table Entries of year 2021")

    purchase_entry = data[0]
    print()
    print(purchase_entry, "\t Purchase Table Selected entry w.r.t the Product ID:")

    cursor1.execute(f"SELECT * FROM Product WHERE ProductID = {str(purchase_entry[1])}" )
    data2 = cursor1.fetchall()
    product_entry = data2[0]
    print()
    print(product_entry, "\t Product Table entry w.r.t ProductID")

    cursor1.execute(f"SELECT * FROM ProductType WHERE ProductName = '{str(product_entry[2])}'")
    data3 = cursor1.fetchall()
    product_type_entry = data3[0]
    print()
    print(product_type_entry, "\t Product Type entry w.r.t ProductName / ProductType")

    cursor1.execute(f"SELECT * FROM Salary WHERE Year = {str(purchase_entry[3])}")
    data4 = cursor1.fetchall()
    purchase_year_entry = data4[0]
    print()
    print(purchase_year_entry, "\t Year & Salary entry w.r.t Year")

    cursor1.execute(f"SELECT * FROM Category WHERE CategoryName = '{str(product_type_entry[1])}'")
    data5 = cursor1.fetchall()
    product_category_entry = data5[0]
    print(product_category_entry, "\t Category Table Entry w.r.t Product category")

# purchase_accordingto_year()

def purchase_accordingto_category():
    cursor1.execute(f"SELECT * FROM ProductType WHERE CategoryName = 'Dairy' ")
    data = cursor1.fetchall()
    print(data, "\t All Product Type Table Entries of 'Dairy' Category")

    product_type_entry = data[0]
    print()
    print(product_type_entry, "\t Product Type Table Selected entry w.r.t the Category")

    cursor1.execute(f"SELECT * FROM Product WHERE ProductType = '{str(product_type_entry[0])}'")
    data2 = cursor1.fetchall()
    product_entry = data2[0]
    print()
    print(product_entry, "\t Product Table entry w.r.t the Product Type")

    cursor1.execute(f"SELECT * FROM Purchases WHERE ProductID = {str(product_entry[0])}")
    data3 = cursor1.fetchall()
    purchase_entry = data3[0]
    print()
    print(purchase_entry, "\t Purchase Table entry w.r.t the ProductID ")

    cursor1.execute(f"SELECT * FROM Salary WHERE Year = {str(purchase_entry[3])}")
    data4 = cursor1.fetchall()
    year_entry = data4[0]
    print()
    print(year_entry, "\t Salary & Year Table entry w.r.t the Purchase Year")

# purchase_accordingto_category()

def category_names():
    cursor1.execute(f"SELECT * FROM Category ORDER BY CategoryName")
    data = cursor1.fetchall()
    print(data, "\t All Category Table Entries")

# category_names()

def brand_and_cost():
    cursor1.execute(f"SELECT * FROM ProductType WHERE CategoryName = 'Dairy' ")
    data = cursor1.fetchall()
    product_type_entry = data[0]
    print(product_type_entry)

    cursor1.execute(f"SELECT * FROM Product WHERE ProductType = '{str(product_type_entry[0])}' ")
    data2 = cursor1.fetchall()
    product_entry = data2[0]
    print(product_entry[1], ", Rs.", product_entry[3])

# brand_and_cost()

def delete_entry(Purchase_ID):
    cursor1.execute(f"DELETE FROM Purchases WHERE PurchaseID = {Purchase_ID}")
    cursor1.execute(f"SELECT * FROM Purchases ORDER BY PurchaseYear DESC, PurchaseMonth DESC")
    data = cursor1.fetchall()
    print(data)

# delete_entry(4)

def new_entry(purchase_ID, product_ID, unit_amount, purchase_year, purchase_month, product_brand, salary, category_name, product_type):
    cursor1.execute(f" SELECT Year FROM Salary WHERE Year = {purchase_year}")
    data = cursor1.fetchall()
    print(data, f"Total entries of year: {purchase_year}")

    if data == []:
        cursor1.execute((f"INSERT INTO Purchases(PurchaseID, ProductID, UnitAmount, PurchaseYear, PurchaseMonth) VALUES"
                         f"({purchase_ID}, {product_ID}, {unit_amount}, {purchase_year}, {purchase_month})"))
        cursor1.commit()
        cursor1.execute(f"SELECT * FROM Purchases WHERE PurchaseYear = {purchase_year}")
        data2 = cursor1.fetchall()
        print(data2)

        cursor1.execute(f"INSERT INTO Salary(Year, Salary) VALUES {salary}, {purchase_year}")
        data4 = cursor1.commit()
        print(data4)

        cursor1.execute(f"INSERT INTO Product(ProductID, ProductBrand, ProductType) VALUES ({product_ID}, {product_brand}, {product_type})")
        data5 = cursor1.commit()
        print(data5)

        cursor1.execute(f"INSERT INTO ProductType(ProductName, CategoryName) VALUES ({product_brand}, {category_name}")
        data6 = cursor1.commit()
        print(data6)

        cursor1.execute(f"INSERT INTO Category(CategoryName) VALUES ({category_name})")
        cursor1.commit()

    else:
        cursor1.execute(f"UPDATE Purchases SET ProductID = {product_ID}, UnitAmount = {unit_amount}, PurchaseMonth = '{purchase_month}'"
                        f"WHERE PurchaseYear = {purchase_year}")
        cursor1.commit()

        cursor1.execute(f"SELECT * FROM Purchases WHERE PurchaseYear = {purchase_year}")
        data3 = cursor1.fetchall()
        print(data3, "done already")

        cursor1.execute(f"UPDATE Salary SET Salary = {salary} WHERE Year = {purchase_year}")
        cursor1.commit()

        cursor1.execute(f"UPDATE Product SET ProductBrand = {product_brand}, ProductType = {product_type} WHERE ProductID = {product_ID}")
        cursor1.commit()

        cursor1.execute(f"UPDATE ProductType SET CategoryName = {category_name} WHERE ProductName = {product_type}")
        cursor1.commit()

        cursor1.execute(f"UPDATE Category SET CategoryName = {category_name}")
        cursor1.commit()


