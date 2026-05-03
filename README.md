# 📦 Inventory Management System  

A **console-based Inventory Management System** developed in Python as part of the **CSC1024 Programming Principles Group Project**.

---

## 📖 Overview  

This project simulates a simple inventory system for small businesses, allowing users to manage:

- Products  
- Suppliers  
- Orders  
- Inventory levels  
- Reports  

The system uses **text files as a database**, demonstrating fundamental programming concepts such as file handling, modular design, and data processing.

---

## Features  

### Product Management  
- Add new products  
- Update product details  
- View product list  

### Supplier Management  
- Add suppliers  
- View supplier information  

### Order Management  
- Place product orders (auto stock deduction)  
- Place supplier orders  

### Inventory Tracking  
- View inventory in table format  
- Detect low stock items (< 5 units)  

### Reporting System  
- Product sales report  
- Supplier order summary  
- Low stock report  

---

## Concepts Demonstrated  

- Functions & modular programming  
- File handling (`.txt` storage)  
- Input validation  
- Loops & conditionals  
- Dictionaries (data aggregation)  
- CLI-based system design  

---

### 🧩 Core Modules  

| Module   | Description                          |
|----------|--------------------------------------|
| Product  | Add, update, display products        |
| Supplier | Manage supplier data                 |
| Orders   | Handle product & supplier orders     |
| Inventory| Track stock levels                   |
| Reports  | Generate sales & order reports       |

---

## 🔧 Key Functions  

### Utility  
- `getInput()` → Validates user input  
- `getQuantity()` → Ensures numeric input  
- `checkFile()` → Checks file existence  
- `replaceLine()` → Updates file records  

### Product  
- `addProduct()`  
- `updateProduct()`  
- `showProducts()`  

### Supplier  
- `addSupplier()`  
- `showSuppliers()`  

### Orders  
- `addProductOrder()`  
- `addSupplierOrder()`  
- `addOrder()`  

### Reports  
- `productSales()`  
- `supplierOrder()`  
- `lowStock()`  

### System  
- `menu()`  
- `main()`  

