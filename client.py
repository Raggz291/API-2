import requests

BASE_URL = 'http://127.0.0.1:5000/products'

def add_product(name, description, price):
    product_data = {
        'name': name,
        'description': description,
        'price': price
    }
    response = requests.post(BASE_URL, json=product_data)
    if response.status_code == 201:
        print('Product added:', response.json())
    else:
        print('Failed to add product:', response.json())

def get_products():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        print('Products:', response.json())
    else:
        print('Failed to retrieve products:', response.json())

if __name__ == '__main__':
    # Example usage
    add_product('Laptop', 'A powerful laptop', 999.99)
    add_product('Smartphone', 'A latest model smartphone', 699.99)
    get_products()
# The client script sends HTTP requests to the server to add products and retrieve the list of products.