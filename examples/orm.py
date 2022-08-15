import sqlite3

conn = sqlite3.connect('./examples/chinook.db')
conn.row_factory = sqlite3.Row
cur = conn.cursor()

sql = '''
SELECT FirstName, LastName FROM customers
'''

cur.execute(sql)
customers = cur.fetchall()

conn.close()

class Customer:
   def __init__(self, customer_id=None, first_name=None, last_name=None):
      self.customer_id = customer_id
      self.first_name = first_name
      self.last_name = last_name

customer_objects = []
for customer in customers:
   customer_objects.append(Customer(customer_id=customer["FirstName"]))

for customer in customers:
   #print(f'Full Name: {customer[1]} {customer[2]}')
   print(f'Full Name: {customer["FirstName"]} {customer["LastName"]}')

