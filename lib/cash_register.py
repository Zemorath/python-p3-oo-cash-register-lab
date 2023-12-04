#!/usr/bin/env python3

class CashRegister:

  last_transaction = 0

  def __init__(self, discount=0, total=0, items=[]):
    self.discount = discount
    self.total = total
    self.items = []

  def add_item(self, title, price, quantity=1):
    self.price = price
    self.quantity = quantity
    self.title = title
    self.total = (quantity*price) + self.total
    self.last_transaction = price*quantity
    for i in range(quantity):
      self.items.append(title)

  def apply_discount(self):
    if self.discount == 0:
      self.total = self.price
      print("There is no discount to apply.")
    else:
      self.total = self.price - (self.price/float(100/self.discount))
      print(f"After the discount, the total comes to ${int(self.total)}.")
    
  def void_last_transaction(self):
    self.total = self.total - self.last_transaction
