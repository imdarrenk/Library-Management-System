#Inventory Management System
from datetime import datetime
import os

def replaceLine(fileName,lineNum,text):
    lines = open(fileName,'r').readlines()
    lines[lineNum]=text
    out=open(fileName,'w')
    out.writelines(lines)
    out.close

def getInput(text):
    while True:  # Run an infinite loop until valid input is received
        value = input(f'Enter {text}: ').strip()  # Use .strip() to remove extra spaces
        if value:  # If value is not empty
            return value
        else:
            print('Invalid input. Please enter a valid input.')

def getQuantity(type,text):
    try:
        value=type(input(f'Enter {text}: '))
        return value
    except ValueError:
        print('Enter a valid number for the quantity.')
        return getQuantity(type,text)

def printHeader(htitle):
    title=htitle
    titleLen=len(title)

    print('='*60)
    space=int((60-titleLen)/2)
    print(' '*space,title,' '*space)
    print('='*60)

def checkFile(fileName):
    # Check if the file exists and its size is 0 bytes
    return os.path.exists(fileName) and os.path.getsize(fileName) > 0

def loopFunc(func):
      output=func()
      choice= input("Do you wish to repeat the function? (Yes or No)").strip().lower()
      if choice == 'yes':
        return loopFunc(func)
      else:
          return output

def showProducts():
    fileCheck = checkFile('products.txt')

    if fileCheck:
        print('\nProduct List')
        with open('products.txt','r') as f:
            lines = f.readlines()  # Read all lines into a list
            for line in lines:
                productInfo=line.strip().split(',#')
                print(f'Product ID : {productInfo[0]}\nName       : {productInfo[1]}\nDescription: {productInfo[2]}\nPrice      : {productInfo[3]}\nQuantity   : {productInfo[4]}\n')
    else:
        print('There is no products entered in our database yet.\nPlease enter product details first.')
        return True

def showSuppliers():
    fileCheck=checkFile('suppliers.txt')

    if fileCheck:
        print('\nSupplier List')
        with open('suppliers.txt','r') as f:
            lines = f.readlines()  # Read all lines into a list
            for line in lines:
                supplierInfo = line.strip().split(',#')
                print(f'Supplier ID    : {supplierInfo[0]}\nName           : {supplierInfo[1]}\nContact Details: {supplierInfo[2]}\n')
    else:
        print('There is no supplier details entered in our database yet\nPlease enter supplier detials first.')
        return True

def addProduct():
    print('Add a New Product\n')
    productId= getInput('Product ID')
    productName= getInput('Product Name')
    productDescription= getInput('Product Description')
    productPrice= getQuantity(float,'Product Price')
    productQuantity= getQuantity(int,'Product Quantity')

    with open('products.txt','a') as f:
        #check if the file is empty, if empty return an empty list
        try:
            content=f.readlines()
        except:
            content=[]
        #appending the new contents into products.txt
        content.append(f'{productId},#{productName},#{productDescription},#{productPrice},#{productQuantity}\n')
        f.writelines(content)

    print('')
    print('Product Added Successfully!')

def updateProduct():
    print('Update Product Details\n')

    if showProducts():
        return

    updateProductId=getInput('Product ID to update')

    with open('products.txt','r') as f:
        lines=f.readlines()
        linesIndex=0
        for i in lines:
            iIndex=i.split(',#')
            if updateProductId==iIndex[0]:
                name=getInput('new Product Name')
                description=getInput('new Product Description')
                price=getQuantity(float,'new Product Price')
                quantity=getQuantity(int,'new Product Quantity')
                confirmation=input('Is all of the details correct? if yes enter 1 or any other value to restart: ')
                if confirmation=='1':
                    updateText= f'{updateProductId},#{name},#{description},#{price},#{quantity}\n'
                    replaceLine('products.txt',linesIndex,updateText)
                    print('\nProduct Updated Successfully!')
                else:
                    updateProduct()
                break
            linesIndex+=1
        else:
            print('Product ID not found.\n')

def addSupplier():
    print('Add a New Supplier')
    supplierId= getInput('Supplier ID')
    supplierName= getInput('Supplier Name')
    supplierContacts= getInput('Contact Details')

    with open('suppliers.txt','a') as f:
        try:
            content=f.readlines()
        except:
            content=[]
        content.append(f'{supplierId},#{supplierName},#{supplierContacts}\n')
        f.writelines(content)

    print('Supplier Added Successfully!\n')

def addProductOrder():
    if showProducts():
        return

    print('Place an order')
    orderId= getInput('Order ID')
    productId= getInput('Product ID')
    quantity = getQuantity(int,'Order Quantity')
    orderDateTime= datetime.now().strftime('%Y-%m-%d') #print out the date(year/month/date)

    with open('products.txt','r+') as f:
        lineCount=0
        for line in f:
            product=line.strip().split(',#')
            if product[0]==f'{productId}':
                if int(product[4])<quantity:
                    print('Sorry, we do not have enough stock to fulfil this order.')
                    break
                else:
                    newQuantity=int(product[4])-quantity
                    newData=f'{product[0]},#{product[1]},#{product[2]},#{product[3]},#{newQuantity}\n'
                    replaceLine('products.txt',lineCount,newData)
                    print('Order Placed Successfully!\n')
                    orderInput=f'{orderId},#{productId},#{quantity},#{orderDateTime}\n'

                    with open('productOrders.txt','a') as f:
                        try:
                            content=f.readlines()
                        except:
                            content=[]
                        content.append(orderInput)
                        f.writelines(content)
                    break
            lineCount+=1
        else:
            print('Sorry, the Product ID entered does not match any products.')
            return
    return

def addSupplierOrder():
    if showSuppliers():
        return

    print('Place an order')
    supplierId= getInput('Supplier ID')
    productId= getInput('Product ID')
    quantity=getQuantity(int,'Order Quantity')
    orderDateTime= datetime.now().strftime('%Y-%m-%d') #print out the date(year/month/date)

    with open('suppliers.txt','r+') as f:
        lineCount=0
        for line in f:
            supplier=line.strip().split(',#')
            if supplier[0]==f'{supplierId}':
                    print('Order Placed Successfully!\n')
                    orderInput=f'{supplierId},#{productId},#{quantity},#{orderDateTime}\n'
                    with open('supplierOrders.txt','a') as f:
                        try:
                            content=f.readlines()
                        except:
                            content=[]
                        content.append(orderInput)
                        f.writelines(content)
                    break
        else:
            print('Sorry, the Supplier ID entered does not match any suppliers in our database.')

def addOrder():
    status=True
    while status:
        status=False
        print('Ordering System\n')
        print('Mode of Order:\n[1] Product Order\n[2] Supplier Order')
        mode=getInput('the number for your desired mode')

        if mode=='1':
            addProductOrder()
        elif mode=='2':
            addSupplierOrder()
        else:
            print('Enter a valid number please. \n')
            reRun= input('if you wish to run the program again, Enter 1 or any input to exit the program.')
            if reRun=='1':
                status=True
            else:
                return

def viewInventory():
    if checkFile('products.txt'):
        printHeader('CURRENT INVENTORY')
        print(f'{"  Product ID":<12} {"Name":<13} {"Description":<22} {"Quantity":<10}')
        print('-'*60)
        with open('products.txt','r') as f:
            count=1
            for line in f:
                productInfo = line.strip().split(',#')
                print(f'{count}.{productInfo[0]:<10} {productInfo[1]:<13} {productInfo[2]:<22} {productInfo[4]:<10}\n')
                count+=1
        print('*'*60)
    else:
        showProducts()

def lowStock():
    if checkFile('products.txt'):
        printHeader('LOW STOCK ITEMS (STOCK < 5 )')
        print(f'{"Product ID":<15}{"Product Name":<25}{"Quantity Remaining":<20}')
        print('-'*60)
        with open('products.txt', 'r') as f:
            for line in f:
                productInfo = line.strip().split(',#')
                if int(productInfo[4]) < 5:
                    print(f'{productInfo[0]:<15}{productInfo[1]:<25}{productInfo[4]:<30}')
        print('*'*60)
    else:
        showProducts()

def productSales():
    if checkFile('productOrders.txt'):
        print('Product Sales Report\n')
        printHeader('ORDER HISTORY')
        print(f'  {"Order ID":<9} {"Product ID":<18} {"Order Quantity":<16} {"Order Date":<12}')
        print('-'*60)
        with open('productOrders.txt','r') as of:
            count=1
            for line in of:
                history=line.strip().split(',#')
                print(f'{count:<2}.{history[0]:<7} {history[1]:<18} {history[2]:<16} {history[3]:<12}')
                count+=1
        print('*'*60)

        sales={} #using a dictionary to store the total sales of each product id
        # Process orders and update sales
        with open('productOrders.txt','r')as of:
            for orders in of:
                if orders.strip(): #skip empty lines, if any
                    order=orders.strip().split(',#')
                    productId = order[1]
                    orderQuantity = int(order[2])
                    if productId in sales:
                        sales[productId] += orderQuantity
                    else:
                        sales[productId] = orderQuantity

        #retriving the unit price of each product from products.txt
        with open('products.txt','r') as pf:
            for details in pf:
                if details.strip():
                    detail=details.strip().split(',#')
                    productId=detail[0]
                    priceDetail= float(detail[3])
                    if productId in sales:
                        sales[productId]=(sales[productId],priceDetail)

        # Write updated sales back to totalSales.txt
        with open('totalSales.txt', 'w+') as sf:
            for productId, detail in sales.items():
                sf.write(f'{productId},{detail[0]},{detail[1]}\n')

        # Display the final contents of totalSales.txt
        printHeader('PRODUCT SALES REPORT')
        print(f'  {"Product ID":<12}{"Quantity Sold":<15} {"Unit Price":<15} {"Total Amount":<15}')
        print('-'*60)

        with open('totalSales.txt', 'r') as sf:
            count=1
            for line in sf:
                data=line.split(',')
                quantitySold= float(data[1])
                unitPrice= float(data[2])
                saleAmount= round(quantitySold*unitPrice,2)
                print(f'{count}.{data[0]:<12}{quantitySold:<15.2f} {unitPrice:<15.2f} RM {saleAmount:<15.2f}')
                count+=1
        print('*'*60)
    else:
        print('There is orders made yet')
        return

def supplierOrder():
    if checkFile('supplierOrders.txt'):
        print('Supplier Order Report\n')
        printHeader('SUPPLIER ORDER HISTORY')
        print(f'  {"Supplier ID":<12} {"Product ID":<15} {"Order Quantity":<16} {"Order Time":<13}')
        print('-'*60)
        with open('supplierOrders.txt', 'r') as of:
            count = 1
            for line in of:
                history = line.strip().split(',#')
                print(f'{count}.{history[0]:<12} {history[1]:<15} {history[2]:<16} {history[3]:13}')
                count += 1
        print('*' * 60)

        orders = {}  # using a dictionary to store the total orders of each supplier
        # Process supplier orders and update orders
        with open('supplierOrders.txt', 'r') as of:
            for order in of:
                if order.strip():  # skip empty lines, if any
                    orderLine = order.strip().split(',#')
                    supplierId = orderLine[0]
                    orderQuantity = int(orderLine[2])
                    if supplierId in orders:
                        orders[supplierId] += orderQuantity
                    else:
                        orders[supplierId] = orderQuantity

        # Write updated orders back to totalOrders.txt
        with open('totalOrders.txt', 'w+') as sf:
            for supplierId, totalQuantity in orders.items():
                sf.write(f'{supplierId},{totalQuantity}\n')

        # Display the final contents of totalOrders.txt
        printHeader('SUPPLIER ORDERS')
        print(f'  {"Supplier ID":<42}{"Total Orders":<12}')
        print('-' * 60)
        with open('totalOrders.txt', 'r') as sf:
            count = 1
            for line in sf:
                data = line.strip().split(',')  # Correct split based on ',' delimiter
                print(f'{count}.{data[0]:<42} {data[1]:<12}')
                count += 1
        print('*' * 60)
    else:
        print('There are no orders made to suppliers yet.')
        return

def report():
    status=True
    while status:
        status=False
        print('Report Generation\n')
        print('[1] Low Stock Items Report\n[2] Product Sales Report\n[3] Supplier Orders Report\n')
        mode=input('Enter the number for your desired report: ')

        if mode=='1':
            lowStock()
        elif mode=='2':
            productSales()
        elif mode=='3':
            supplierOrder()
        else:
            print('Enter a valid number please. \n')
            reRun= input('if you wish to run the program again, Enter 1 or any input to exit the program.')
            if reRun=='1':
                status=True
            else:
                print('Thanks for using our system!')

def menu():
    status=True
    while status:
        status=False

        print('Inventory Management System Function Menu\n[1] Add a new product\n[2] Update product details\n[3] Add a new supplier\n[4] Place an order\n[5] View Inventory\n[6] Generate reports\n[7] Exit')
        mode=input('Enter the number for your mode of choice: ')
        print('')

        match mode:
            case '1':
                loopFunc(addProduct)
            case '2':
                loopFunc(updateProduct)
            case '3':
                loopFunc(addSupplier)
            case '4':
                loopFunc(addOrder)
            case '5':
                loopFunc(viewInventory)
            case '6':
                loopFunc(report)
            case '7':
                pass
            case _:
                print('Enter a valid number please. \n')
                reRun= input('if you wish to run the program again, Enter 1 or any input to exit the program.')
                if reRun=='1':
                    status=True
                else:
                    pass

def main():
    menu()
    print('Thanks for using our system!')
    return

main()

