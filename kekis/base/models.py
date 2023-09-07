from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Project(models.Model):
    kvantumType = models.TextChoices('kvantumType',
                                     'VR IT MEDIA IND-DESIGN ENERGY BIO NEURO NANO HI-TECH GEO AERO IND-ROBO')
    name = models.CharField(max_length=200, verbose_name="Название")
    kvantum = models.CharField(choices=kvantumType.choices, max_length=10, verbose_name="Квантум")
    face = models.ForeignKey("Image", verbose_name="Обложка на главной странице", on_delete=models.CASCADE,
                             related_name='Image_Face', null=True, blank=True)
    description = models.TextField(verbose_name="Описание проекта")
    image = models.ManyToManyField("Image", null=True, blank=True, verbose_name="Дополнительные изображения")
    contacts = models.ManyToManyField("Contacts", verbose_name="Кониакты учеников")

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

class Group(models.Model):
    name = models.CharField(max_length=60)
    direction = models.TextChoices('kvantumType',
                                     'VR IT MEDIA IND-DESIGN ENERGY BIO NEURO NANO HI-TECH GEO AERO IND-ROBO')
    #Сделать лидера квантума, убрать тичера из аккаунта.!
    timetable = models.ManyToManyField(Timetable, verbose_name="Дни учёбы")
    def __str__(self) -> str:
        return self.name

class Account(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    age = models.IntegerField()
    email = models.EmailField(max_length=200)
    teacher = models.CharField(max_length=40)
    time_created = models.DateTimeField(auto_now_add=True)
    rank = models.IntegerField()
    login = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    request_buy = models.CharField(max_length=999)
    score = models.IntegerField()
    size = models.CharField(max_length=10)
    group = models.ManyToManyField(Group, null=True)
    projects = models.ManyToManyField(Project, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        unique_together = ('email', 'teacher', 'login', 'password', 'age', 'name')


class Buy(models.Model):
    key = models.CharField(max_length=11)
    name = models.CharField(max_length=80)
    size = models.CharField(max_length=11)
    type = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} - {str(self.type)} - {str(self.key)}"


class Image(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название изображения")
    type = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='Project_type',
                             verbose_name="Что за проект")
    image = models.ImageField(upload_to='images/', verbose_name="Изображение")

    def __str__(self):
        return f"{self.name}, {str(self.type)}"


class Contacts(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    phone = PhoneNumberField(null=False, blank=False, verbose_name="Номер телефона")

    class Meta:
        unique_together = ("first_name", "last_name", "phone")

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name}"


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
    def __str__(self) -> str:
        return self.name




