from django.db import models
from django.utils import timezone
# Create your models here.
class farmer(models.Model):
    """
    this is the famer table with attributes name,email,password,dob,address
    """
    name=models.CharField(max_length=50,default='')
    email=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=200)
    street=models.CharField(max_length=30,default='')
    city=models.CharField(max_length=30,default='')
    district=models.CharField(max_length=30,default='')
    phone=models.CharField(default=0,max_length=12)
    
class sell(models.Model):
    """
    this is sell table with attributes productname,quantity,price,discription,famer_id,p_id
    """
    p_id=models.AutoField(primary_key=True)
    p_name=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    f_id=models.ForeignKey(farmer,on_delete=models.CASCADE,related_name='famer')
    quantity=models.CharField(max_length=20)
    p_type=models.CharField(max_length=20,default='')
    price=models.IntegerField()

class buy(models.Model):
    """
    this is the buy table with attributes p_id ,farmer_id,date
    """
    p_id=models.ForeignKey(sell,on_delete=models.CASCADE,related_name='sell')
    f_id=models.ForeignKey(farmer,on_delete=models.CASCADE,related_name='farmer')
    date=models.DateField()