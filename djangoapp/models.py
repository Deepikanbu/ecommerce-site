from django.db import models

# Create your models here.
class register(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.IntegerField()
    gender=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    dob=models.DateField()
    password=models.CharField(max_length=20)


class file_upload(models.Model):
    filename=models.CharField(max_length=50)
    fileimage=models.FileField(upload_to='djangoapp/static')
    des=models.CharField(max_length=200)


class file_upload2(models.Model):
    filename = models.CharField(max_length=50)
    fileimage =models.FileField(upload_to='djangoapp/static')
    des = models.CharField(max_length=200)

class empreg(models.Model):
    emp_name=models.CharField(max_length=30)
    mail=models.EmailField()
    cmpnm=models.CharField(max_length=30)
    des=models.CharField(max_length=10)
    phone=models.IntegerField()

class product(models.Model):
    pro_name=models.CharField(max_length=30)
    price=models.IntegerField()
    pro_cmpny=models.CharField(max_length=30)
    quan=models.IntegerField()
    expdt=models.DateField()
    descrp=models.CharField(max_length=50)

class file_upload3(models.Model):
    audioname=models.CharField(max_length=50)
    audio=models.FileField(upload_to='djangoapp/static')
    vedioname=models.CharField(max_length=50)
    vedio=models.FileField(upload_to='djangoapp/static')
    pdfname=models.CharField(max_length=40)
    pdf=models.FileField(upload_to='djangoapp/static')

class check_box(models.Model):
    choice=[
        ('TamilNadu','Tamil Nadu'),
        ('Kerala','Kerala'),
        ('Karnataka','Karnataka')
    ]

    fullname=models.CharField(max_length=30)
    state=models.CharField(max_length=30, choices=choice)
    tamil=models.BooleanField(default=False)
    malayalam=models.BooleanField(default=False)
    english=models.BooleanField(default=False)




