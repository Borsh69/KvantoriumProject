from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import FileExtensionValidator
from PIL import Image as PILImage
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

class Project(models.Model):
    kvantumType = models.TextChoices('kvantumType',
                                     'VR IT MEDIA IND-DESIGN ENERGY BIO NEURO NANO HI-TECH GEO AERO IND-ROBO')
    name = models.CharField(max_length=200, verbose_name="Название")
    kvantum = models.CharField(choices=kvantumType.choices, max_length=10, verbose_name="Квантум")
    face = models.ImageField(upload_to='images/', verbose_name="Лицевое изображение")
    description = models.TextField(verbose_name="Описание проекта")
    image = models.ManyToManyField("Image", null=True, blank=True, verbose_name="Дополнительные изображения")
    creators = models.ManyToManyField("Account", verbose_name="Создатели проектов")
    PDFdescription = models.FileField(upload_to ='pdf/', validators =[FileExtensionValidator(allowed_extensions=['pdf'])], null=True, blank=True) 
    contact = models.CharField(max_length=200, verbose_name="Контакты", null=True)
    def __str__(self) -> str:
        return self.name


class Shop(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=400)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    price = models.IntegerField()
    stock = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.title


class Timetable(models.Model):
    classroom = models.CharField(max_length=50)
    dayWeek = models.CharField(max_length=50)
    time = models.TimeField(auto_now=False, auto_now_add=False,default=None)
    def __str__(self) -> str:
        return self.classroom + ' ' + str(self.time)



class Competitions(models.Model):
    kvantumType = models.TextChoices('kvantumType',
                                     'VR IT MEDIA IND-DESIGN ENERGY BIO NEURO NANO HI-TECH GEO AERO IND-ROBO')
    name = models.CharField(max_length=200, verbose_name="Название")
    kvantum = models.CharField(choices=kvantumType.choices, max_length=10, verbose_name="Квантум")
    face = models.ForeignKey("Image", verbose_name="Обложка на главной странице", on_delete=models.CASCADE,
                             related_name='Image_Face_Comp', null=True, blank=True)
    description = models.TextField(verbose_name="Описание конкурса")
    images = models.ManyToManyField("Image", null=True, blank=True, verbose_name="Дополнительные изображения")
    contacts = models.CharField(max_length=250, verbose_name="Ссылка на конкурс")
    date = models.DateTimeField(auto_now=False, auto_now_add=False, default=None)
    current = models.BooleanField(default=True, verbose_name="Активный")
    def __str__(self) -> str:
        return self.name


class Account(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    age = models.IntegerField()
    email = models.EmailField(max_length=200)
    time_created = models.DateTimeField(auto_now_add=True)
    rank = models.IntegerField(default=0)
    login = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    score = models.IntegerField(default=0)
    contact = models.CharField(max_length=80, null=True)
    size = models.CharField(max_length=10)
    projects = models.ManyToManyField(Project, null=True, blank=True)
    city = models.CharField(max_length=255, default="none")
    favorite = models.ManyToManyField(Competitions, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        unique_together = ('email', 'login', 'password', 'age', 'name')

class Teacher(models.Model):
    name = models.CharField(max_length=80)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    age = models.IntegerField()
    email = models.EmailField(max_length=200)
    time_created = models.DateTimeField(auto_now_add=True)
    login = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    size = models.CharField(max_length=10)
    favorite = models.ManyToManyField(Competitions, null=True, blank=True)
    city = models.CharField(max_length=255, default="none")
    def __str__(self) -> str:
        return self.name

    class Meta:
        unique_together = ('email', 'login', 'password', 'age', 'name')

class Buy(models.Model):
    key = models.CharField(max_length=11)
    name = models.CharField(max_length=80)
    size = models.CharField(max_length=11, default="M")
    type = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} - {str(self.type)} - {str(self.key)}"


class Image(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название изображения")
    image = models.ImageField(upload_to='images/', verbose_name="Изображение")

    def __str__(self):
        return f"{self.name}"



class Group(models.Model):
    name = models.CharField(max_length=60)
    direction = models.TextChoices('kvantumType',
                                     'VR IT MEDIA IND-DESIGN ENERGY BIO NEURO NANO HI-TECH GEO AERO IND-ROBO')
    #Сделать лидера квантума, убрать тичера из аккаунта.!
    timetable = models.ManyToManyField(Timetable, verbose_name="Дни учёбы")
    pupils = models.ManyToManyField(Account, blank=True, null=True)
    teachers = models.ForeignKey(Teacher, blank=True, null=True, on_delete=models.SET_NULL)
    def __str__(self) -> str:
        return self.name




@receiver(pre_save, sender=Project)
def resize(sender,instance, **kwargs):
    if(instance.face):
        face = PILImage.open(instance.face)
        width,height = face.size
        new_width,new_height = 800, 600
        left = (width-new_width)/2
        right = (width+new_width)/2
        top = (height-new_height)/2
        bottom = (height+new_height)/2
        face = face.crop((left,top,right,bottom))
        thumb_io = BytesIO()
        face.save(thumb_io, format='PNG')
        instance.face.save(instance.face.name, InMemoryUploadedFile(thumb_io, None, f'{instance.face.name}', 'face', thumb_io.tell(), None), save=False)



