import json
import string
import random
from json import JSONDecodeError
from datetime import datetime

def Register(type,gamers_json_file,sellers_json_file,Email_ID,Username,Password,Contact_Number):
    '''Register Function || Already Given'''
    if type.lower()=='seller':
        f=open(sellers_json_file,'r+')
        d={
            "Email":Email_ID,
            "Username":Username,
            "Password":Password,
            "Contact Number":Contact_Number,
        }
        try:
            content=json.load(f)
            if d not in content and d["Username"] not in str(content):
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()
        return True
    elif type.lower()=='gamer':
        f=open(gamers_json_file,'r+')
        d={
            "Email":Email_ID,
            "Username":Username,
            "Password":Password,
            "Contact Number":Contact_Number,
            "Wishlist":[],
            "Cart":[],
        }
        try:
            content=json.load(f)
            if d not in content and d["Username"] not in str(content):
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()

def Login(type,gamers_json_file,sellers_json_file,Username,Password):
    '''Login Functionality || Return True if successfully logged in else False || Already Given'''
    d=0
    if type.lower()=='seller':
        f=open(sellers_json_file,'r+')
    else:
        f=open(gamers_json_file,'r+')
    try:
        content=json.load(f)
    except JSONDecodeError:
        return False
    for i in range(len(content)):
        if content[i]["Username"]==Username and content[i]["Password"]==Password:
            d=1
            break
    f.seek(0)
    f.truncate()
    json.dump(content,f)
    f.close()
    if d==0:
        return False
    return True

def AutoGenerate_ProductID():
    '''Return a autogenerated random product ID || Already Given'''
    product_ID=''.join(random.choices(string.ascii_uppercase+string.digits,k=4))
    return product_ID

def AutoGenerate_OrderID():
    '''Return a autogenerated random product ID || Already Given'''
    Order_ID=''.join(random.choices(string.ascii_uppercase+string.digits,k=3))
    return Order_ID

def days_between(d1, d2):
    '''Calculating the number of days between two dates || Already Given'''
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

def Create_Product(Owner,Product_json_file,Product_ID,Product_Title,Product_Type,Price_per_day,Total_stock_available):
    '''Creating a product || Return True if successfully created else False'''
    '''Write your code below'''
    with open(Product_json_file, 'r') as f:
        Products = json.load(f)
    Product_ID = str(len(Products) + 1)

    # Create a dictionary to store the product details
    Product = {
        'Product_Id': Product_ID,
        'Product_Title': Product_Title,
        'Product_Type': Product_Type,
        'Price_per_day': Price_per_day,
        'Total_stock_available': Total_stock_available,
        'Owner': Owner
    }

    # Add the new product to the products list and save to file
    Products.append(Product)
    with open(Product_json_file, 'w') as f:
        json.dump(Products, f)

    return True
    

def Fetch_all_Products_created_by_seller(Owner, Products_json_file):
    '''Get all products created by seller'''
    with open(Products_json_file) as f:
        Products=json.load(f)
    result = []
    for p in Products:
        if "Owner" in p and p["Owner"] == Owner:
            result.append(p)
    return result


def Fetch_all_products(Products_json_file):
    '''Get all products created till now || Helper Function || Already Given'''
    All_Products_list=[]
    f=open(Products_json_file,'r')
    try:
        content=json.load(f)
        All_Products_list=content
    except JSONDecodeError:
        pass
    return All_Products_list

def Fetch_Product_By_ID(Products_json_file,Product_ID):
    '''Get product deatils by product ID'''
    '''Write your code below'''
    with open(Products_json_file) as f:
        Products=json.load(f)
    for Product in Products:
        if Product["Product_ID"] == Product_ID:
            return Product
    return None



def Update_Product(Username,Products_json_file,Product_ID,detail_to_be_updated,new_value):
    '''Updating Product || Return True if successfully updated else False'''
    '''Write your code below'''
    with open(Products_json_file, 'r') as f:
        Products = json.load(f)

    # Find the product with the given ID and owned by the given seller
    for Product in Products:
        if Product['Product ID'] == Product_ID and Product['owner'] == Username:

            # Update the product detail with the new value
            Product[detail_to_be_updated] = new_value

            # Save the updated products list to the JSON file
            with open(Products_json_file, 'w') as f:
                json.dump(Products, f)

            return True

    # If no matching product is found, return False
    return False

def Add_item_to_wishlist(Username,Product_ID,Gamers_json_file):
    '''Add Items to wishlist || Return True if added successfully else False'''
    '''Write your code below'''
    with open(Gamers_json_file, 'r') as f:
        Gamers = json.load(f)

    # Find the gamer with the given username
    for Gamer in Gamers:
        if Gamer['Username'] == Username:

            # Add the product ID to the gamer's wishlist
            if Product_ID not in Gamer['Wishlist']:
                gamer['Wishlist'].append(product_ID)

                # Save the updated gamers list to the JSON file
                with open(Gamers_json_file, 'w') as f:
                    json.dump(Gamers, f)

                return True

    # If no matching gamer is found, return False
    return False


def Remove_item_from_wishlist(Username,Product_ID,Gamers_json_file):
    '''Remove items from wishlist || Return True if removed successfully else False'''
    '''Write your code below'''
    with open(Gamers_json_file, 'r') as f:
        Gamers = json.load(f)

    # Find the gamer with the given username
    for Gamer in Gamers:
        if Gamer['Username'] == Username:

            # Remove the product ID from the gamer's wishlist
            if Product_ID in Gamer['Wishlist']:
                Gamer['Wishlist'].remove(Product_ID)

                # Save the updated gamers list to the JSON file
                with open(Gamers_json_file, 'w') as f:
                    json.dump(Gamers, f)

                return True

    # If no matching gamer is found, return False
    return False
    

def Add_item_to_cart(Username,Product_ID,Quantity,Gamers_json_file,booking_start_date,booking_end_date,Products_json_file):
    '''Add item to the cart || Check whether the quantity mentioned is available || Return True if added successfully else False'''
    '''Add the Product ID, Quantity, Price, Booking Start Date, Booking End Date in the cart as list of dictionaries'''
    '''Write your code below'''
    with open(Gamers_json_file, 'r') as f:
        Gamers = json.load(f)

    with open(Products_json_file, 'r') as f:
        Products = json.load(f)

    # Find the gamer with the given username
    for Gamer in Gamers:
        if Gamer['Username'] == Username:

            # Find the product with the given product ID
            for Product in Products:
                if Product['ProductID'] == Product_ID:

                    # Check if the requested quantity is available
                    if Quantity > Product['Total Stock Available']:
                        return False

                    # Calculate the total cost based on the price per day and booking period
                    start_date = datetime.strptime(booking_start_date, '%Y-%m-%d').date()
                    end_date = datetime.strptime(booking_end_date, '%Y-%m-%d').date()
                    booking_period = (end_date - start_date).days + 1
                    total_cost = booking_period * product['Price Per Day'] * Quantity

                    # Add the item to the gamer's cart
                    cart_item = {
                        'ProductID': Product_ID,
                        'Quantity': Quantity,
                        'Price': product['Price Per Day'],
                        'Booking Start Date': booking_start_date,
                        'Booking End Date': booking_end_date,
                        'Total Cost': total_cost
                    }
                    Gamer['Cart'].append(cart_item)

                    # Update the product's stock
                    Product['Total Stock Available'] -= Quantity

                    # Save the updated gamers and products lists to the JSON files
                    with open(Gamers_json_file, 'w') as f:
                        json.dump(Gamers, f)

                    with open(Products_json_file, 'w') as f:
                        json.dump(products, f)

                    return True

    # If no matching gamer or product is found, return False
    return False

    

def Remove_item_from_cart(Username,Product_ID,Gamers_json_file):
    '''Remove items from the cart || Return True if removed successfully else False'''
    '''Write your code below'''
    try:
        with open(Gamers_json_file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("File not found.")
        return False
    
    # Check if user exists in the file
    if Username not in data:
        print("User does not exist.")
        return False
    
    cart = data[Username]['Cart']
    
    # Remove the item from the cart if it exists
    for item in cart:
        if item['ProductID'] == Product_ID:
            cart.remove(item)
            print("Item removed from cart.")
            with open(Gamers_json_file, 'w') as f:
                json.dump(data, f, indent=4)
            return True
    
    print("Item not found in cart.")
    return False



    

def View_Cart(Username,Gamers_json_file):
    '''Return the current cart of the user'''
    '''Write your code below'''
    with open(Gamers_json_file, 'r') as f:
        Gamers_data = json.load(f)

    # Find the gamer's data by username
    Gamer_data = next((Gamer for Gamer in Gamers_data if Gamer['Username'] == Username), None)

    # If the gamer is found, return their cart
    if Gamer_data and 'Cart' in Gamer_data:
        return Gamer_data['Cart']
    else:
        return []
    

def Place_order(Username,Gamers_json_file,Order_Id,Orders_json_file,Products_json_file):
    '''Place order || Return True is order placed successfully else False || Decrease the quantity of the product orderd if successfull'''
    '''Write your code below'''
    with open(Gamers_json_file, 'r') as f:
        Gamers_data = json.load(f)
    
    # Check if the user exists
    if Username not in Gamers_data:
        print("User does not exist!")
        return False
    
    # Load products data
    with open(Products_json_file, 'r') as f:
        Products_data = json.load(f)
    
    # Load orders data
    with open(Orders_json_file, 'r') as f:
        orders_data = json.load(f)
    
    # Get the user's cart
    Cart = Gamers_data[Username]['Cart']
    
    # Check if the cart is empty
    if not Cart:
        print("Cart is empty!")
        return False
    
    # Calculate the total price and create the order
    total_price = 0
    Products_ordered = []
    for item in Cart:
        # Get the product details
        Product_id = item['product_Id']
        Quantity = item['Quantity']
        start_date = datetime.strptime(item['booking_start_date'], '%Y-%m-%d')
        end_date = datetime.strptime(item['booking_end_date'], '%Y-%m-%d')
        Product = None
        for p in Products_data:
            if p['Product_ID'] == Product_Id:
                Product = P
                break
        
        # Check if the product exists
        if not Product:
            print("Product does not exist!")
            return False
        
        # Check if the quantity is available
        if Quantity > Product['Total_Stock']:
            print("Quantity not available!")
            return False
        
        # Calculate the price
        price_per_day = Product['Price_Per_Day']
        num_days = (end_date - start_date).days + 1
        price = price_per_day * num_days * quantity
        total_price += Price
        
        # Add the product to the list of ordered products
        Products_ordered.append({
            'Product_Id': Product_Id,
            'Quantity': Quantity,
            'Price': Price,
            'booking_start_date': item['booking_start_date'],
            'booking_end_date': item['booking_end_date']
        })
        
        # Decrease the product's stock
        Product['Total_Stock'] -= Quantity
    
    # Add the order to the orders data
    Orders_data.append({
        'Order_Id': Order_Id,
        'Username': Username,
        'Products_Ordered': Products_ordered,
        'Total_Price': Total_price,
        'Order_Date': str(datetime.now())
    })
    
    # Clear the user's cart
    Gamers_data[Username]['Cart'] = []
    
    # Update the gamers data
    with open(Gamers_json_file, 'w') as f:
        json.dump(Gamers_data, f, indent=4)
    
    # Update the products data
    with open(Products_json_file, 'w') as f:
        json.dump(Products_data, f, indent=4)
    
    # Update the orders data
    with open(Orders_json_file, 'w') as f:
        json.dump(Orders_data, f, indent=4)
    
    print("Order placed successfully!")
    return True
   

def View_User_Details(Gamers_json_file,Username):
    '''Return a list with all gamer details based on the username || return an empty list if username not found'''
    '''Write your code below'''
    with open(Gamers_json_file) as f:
        Gamers = json.load(f)
    for Gamer in Gamers:
        if Gamer['Username'] == Username:
            return Gamer
    return []
    

def Update_User(Gamers_json_file,Username,detail_to_be_updated,updated_detail):
    '''Update the detail_to_be_updated of the user to updated_detail || Return True if successful else False'''
    '''Write your code below'''
    with open(Gamers_json_file) as f:
        Gamers = json.load(f)
    for Gamer in Gamers:
        if Gamer['Username'] == Username:
            Gamer[detail_to_be_updated] = updated_detail
            with open(gamers_json_file, 'w') as f:
                json.dump(gamers, f, indent=4)
            return True
    return False

    

def Fetch_all_orders(Orders_json_file,Username):
    '''Fetch all previous orders for the user and return them as a list'''
    '''Write your code below'''
    with open(Orders_json_file) as f:
        Orders = json.load(f)
    Gamer_orders = []
    for Order in Orders:
        if Order['Username'] == Username:
            Gamer_orders.append(Order)
    return Gamer_orders
    
    

