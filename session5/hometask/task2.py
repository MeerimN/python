product_data = {
    "store": "TechNova",
    "location": {
        "city": "San Francisco",
        "country": "USA"
    },
    "products": [
        {
            "id": "P1001",
            "name": "Wireless Mouse",
            "brand": "LogiTech",
            "price": 29.99,
            "currency": "USD",
            "stock": 134,
            "specs": {
                "color": "Black",
                "connectivity": "Bluetooth",
                "battery_life": "12 months"
            },
            "ratings": {
                "average": 4.5,
                "count": 240
            }
        },
        {
            "id": "P1002",
            "name": "Mechanical Keyboard",
            "brand": "KeyChron",
            "price": 79.99,
            "currency": "USD",
            "stock": 57,
            "specs": {
                "color": "White",
                "switch_type": "Gateron Brown",
                "backlight": "RGB"
            },
            "ratings": {
                "average": 4.7,
                "count": 145
            }
        },
        {
            "id": "P1003",
            "name": "Sony Wireless Noise-Canceling Headphones",
            "brand": "Sony",
            "price": 199.99,
            "currency": "USD",
            "stock": 23,
            "specs": {
                "color": "Black",
                "connectivity": "Bluetooth",
                "noise_cancellation": "Active",
                "battery_life": "30 hours"
            },
            "ratings": {
                "average": 4.8,
                "count": 529
            }
        }
    ]
}

# Task 2: List Products Over $50 with High Rating
# Print the name, price, and average rating of products where the price is greater than $50 and the average rating is above 4.5.


for product in product_data["products"]:
    if product["price"] > 50 and product["ratings"]["average"] > 4.5:
        print(product["name"], "-", str(product["price"]), "-", "Rating:", product["ratings"]["average"])