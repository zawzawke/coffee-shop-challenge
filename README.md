# coffee-shop-challenge
This is a simple Python OOP project to model a coffee shop using classes and object relationships (Customer, Coffee, and Order).

## Concepts Covered:
- Object-Oriented Programming (OOP)
- Class relationships and aggregation
- Property decorators (`@property`, setters)
- Data validation and immutability
- Aggregation methods

##  Models:

### 1.`Customer`
- Has a `name` (1–15 characters, string only)
- Methods:
  - `orders()`: List of their `Order` instances
  - `coffees()`: Unique list of `Coffee` instances they’ve ordered
  - `create_order(coffee, price)`: Creates an order
  - `most_aficionado(coffee)`: *(Bonus)* Returns the customer who spent the most on the coffee

### 2.`Coffee`
- Has a `name` (≥3 characters, string only, immutable)
- Methods:
  - `orders()`: All orders of this coffee
  - `customers()`: Unique customers who ordered it
  - `num_orders()`: Total number of orders
  - `average_price()`: Mean price of its orders

### 3.`Order`
- Has a `customer`, `coffee`, and `price` (float between 1.0–10.0)
- Immutable after initialization

##  How to Test:
1. Clone this repo
2. Run `python debug.py` to see outputs and test relationships

##  File Structure
coffee-shop-challenge/
├── customer.py
├── coffee.py
├── order.py
├── debug.py
└── README.md

Author - Paul Simiyu - Made for educational purposes

