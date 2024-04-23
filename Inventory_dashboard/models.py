from django.db import models

# Category tuple created for Product to store value in database and display.
CATEGORY = (
    ('Meat' , 'Meat'),
    ('Dessert' , 'Dessert'),
    ('Vegetable' , 'Vegetable'),
    ('Sauces' , 'Sauces'),
    ('Fruit' , 'Fruit'),
    )
# Product model is created with the following fields.
class Product(models.Model):
    name=models.CharField(max_length=100,null=True)
    category=models.CharField(max_length=20,choices=CATEGORY,null=True)
    quantity=models.PositiveIntegerField(null=True)
    expirydate =models.DateField(null=True) 

    objects = models.Manager()

# This displays how instances of the Product model should be represented as strings. 

    def __str__(self):
      return f'{self.name}-{self.quantity}'
      
# Order model is created with the following fields.      
class Order(models.Model):
    name = models.CharField(max_length=100,null=True)
    quantity = models.PositiveIntegerField(null=True)
    category=models.CharField(max_length=20,choices=CATEGORY,null=True)
    
    objects = models.Manager()
    

# This displays how instances of the Order model should be represented as strings. 
    def __str__(self):
        return f'{self.name}-{self.quantity}'