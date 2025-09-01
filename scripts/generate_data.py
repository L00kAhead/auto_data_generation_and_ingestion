import csv
import random
import uuid
from datetime import datetime, timedelta

def generate_fake_data():
    """Generate fake data without external dependencies"""
    
    products = [
        ("P101", "Laptop", "Electronics", "Computers", "Dell", 1200.50),
        ("P102", "Mouse", "Electronics", "Accessories", "Logitech", 25.00),
        ("P103", "Keyboard", "Electronics", "Accessories", "HP", 45.75),
        ("P104", "Headphones", "Electronics", "Audio", "Sony", 89.99),
        ("P105", "Monitor", "Electronics", "Displays", "Samsung", 300.00),
        ("P106", "Tablet", "Electronics", "Computers", "Apple", 799.99),
        ("P107", "Smartphone", "Electronics", "Mobiles", "Samsung", 999.00),
        ("P108", "Smartwatch", "Electronics", "Wearables", "Garmin", 199.50),
        ("P109", "Camera", "Electronics", "Photography", "Canon", 450.00),
        ("P110", "Printer", "Electronics", "Office", "HP", 150.00)
    ]
    
    payment_methods = ["Credit Card", "Debit Card", "PayPal", "Cash on Delivery"]
    statuses = ["Shipped", "Pending", "Delivered", "Returned", "Cancelled"]
    genders = ["Male", "Female", "Other"]
    suppliers = ["TechWorld", "GadgetHub", "ElectroMart", "SmartShop", "DeviceZone"]
    
    currencies = {
        "USA": "USD", "Spain": "EUR", "Ireland": "EUR", "China": "CNY", "Italy": "EUR",
        "UAE": "AED", "Germany": "EUR", "Japan": "JPY", "Egypt": "EGP", "UK": "GBP"
    }
    
    countries = list(currencies.keys())
    cities = ["New York", "Madrid", "Dublin", "Beijing", "Rome", "Dubai", "Berlin", "Tokyo", "Cairo", "London"]
    first_names = ["John", "Jane", "Mike", "Sarah", "David", "Emma", "Chris", "Lisa", "Mark", "Anna"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
    email_domains = ["gmail.com", "yahoo.com", "outlook.com", "protonmail.com"]
    
    return {
        'products': products,
        'payment_methods': payment_methods,
        'statuses': statuses,
        'genders': genders,
        'suppliers': suppliers,
        'currencies': currencies,
        'countries': countries,
        'cities': cities,
        'first_names': first_names,
        'last_names': last_names,
        'email_domains': email_domains
    }

def generate_phone_number():
    """Generate a fake phone number"""
    return f"+{random.randint(1, 999)}{random.randint(1000000000, 9999999999)}"

def generate_address():
    """Generate a fake address"""
    street_numbers = range(1, 9999)
    street_names = ["Main St", "Oak Ave", "Park Rd", "First St", "Second Ave", "Elm St", "Maple Ave"]
    return f"{random.choice(street_numbers)} {random.choice(street_names)}"

def generate_data_rows(num_rows, order_date, fake_data):
    """Generate data rows without pandas"""
    rows = []
    customer_map = {}
    
    for _ in range(num_rows):
        customer_id = f"C{uuid.uuid4().hex[:8]}"
        order_id = f"O{uuid.uuid4().hex[:8]}"
        
        first_name = random.choice(fake_data['first_names'])
        last_name = random.choice(fake_data['last_names'])
        gender = random.choice(fake_data['genders'])
        phone_number = generate_phone_number()
        country = random.choice(fake_data['countries'])
        city = random.choice(fake_data['cities'])
        shipping_address = generate_address()
        
        if customer_id not in customer_map:
            domain = random.choice(fake_data['email_domains'])
            email = f"{first_name.lower()}.{last_name.lower()}.{customer_id}@{domain}"
            customer_map[customer_id] = email
        else:
            email = customer_map[customer_id]
        
        product_id, product_name, category, sub_category, brand, unit_price = random.choice(fake_data['products'])
        quantity = random.randint(1, 5)
        discount = round(random.uniform(0, unit_price * 0.2), 2)
        total_amount = round((unit_price * quantity) - discount, 2)
        currency = fake_data['currencies'][country]
        status = random.choice(fake_data['statuses'])
        supplier = random.choice(fake_data['suppliers'])
        payment_method = random.choice(fake_data['payment_methods'])
        
        # Generate order time
        order_time = (datetime.strptime(order_date, "%Y-%m-%d") + 
                     timedelta(minutes=random.randint(0, 720))).strftime("%H:%M:%S")
        
        # Generate delivery date
        delivery_date = (datetime.strptime(order_date, "%Y-%m-%d") + 
                        timedelta(days=random.randint(2, 7))).strftime("%Y-%m-%d")
        
        return_flag = "Y" if status == "Returned" else "N"
        
        rows.append([
            order_id, order_date, order_time, customer_id, first_name, last_name, email,
            phone_number, country, city, gender, payment_method, shipping_address,
            product_id, product_name, category, sub_category, brand,
            quantity, unit_price, discount, total_amount, currency,
            status, delivery_date, return_flag, supplier
        ])
    
    return rows

def write_csv(rows, file_path):
    """Write rows to CSV file"""
    headers = [
        "order_id", "order_date", "order_time", "customer_id", "first_name", "last_name", "email",
        "phone_number", "country", "city", "gender", "payment_method", "shipping_address", "product_id",
        "product_name", "category", "sub_category", "brand", "quantity", "unit_price", "discount",
        "total_amount", "currency", "status", "delivery_date", "return_flag", "supplier"
    ]
    
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)  # Write headers
        writer.writerows(rows)    # Write data rows