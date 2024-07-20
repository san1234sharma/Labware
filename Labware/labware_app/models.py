from django.db import models

# Create your models here.
class Contact(models.Model):
    # contact_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    ph_num=models.IntegerField()
    query=models.TextField(max_length=500)

    def __str__(self):
        return self.name
    
class   Product(models.Model):
    product_id = models.AutoField(primary_key=id)
    product_name=models.CharField(max_length=100,)
    category=models.CharField(max_length=100,default="")
    subcategory=models.CharField(max_length=50,default='')
    desc=models.CharField(max_length=300)
    image=models.ImageField(upload_to='images/images')
    
    def __str__(self):
        return self.product_name