from customer import Customer
from coffee import Coffee
from order import Order

# Clears the Order list if re-running
Order.all = []

# Creates customers
paul = Customer("Paul")
james = Customer("James")

# Creates coffees
cortado = Coffee("Cortado")
mocha = Coffee("Mocha")

# Create orders
paul.create_order(cortado, 3.5)
james.create_order(cortado, 4.0)
paul.create_order(mocha, 5.0)
james.create_order(mocha, 6.0)

print("\n--- Testing Properties ---")
print("Paul's name:", paul.name)
print("Cortado's name:", cortado.name)
print("Order count:", len(Order.all))

print("\n--- Testing Relationships ---")
print("Paul's orders:", paul.orders())
print("Paul's coffees:", [c.name for c in paul.coffees()])
print("Cortado's orders:", cortado.orders())
print("Cortado's customers:", [c.name for c in cortado.customers()])

print("\n--- Testing Aggregates ---")
print("Cortado total orders:", cortado.num_orders())
print("Cortado average price:", cortado.average_price())

print("\n--- Testing Bonus ---")
most_spent = Customer.most_aficionado(cortado)
print("Most aficionado (Cortado):", most_spent.name if most_spent else "None")
