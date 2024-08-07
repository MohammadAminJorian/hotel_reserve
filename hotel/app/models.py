from django.db import models
from django.utils import timezone


class Option(models.Model):
    STATUS_CHOICE = (
        ('1', 'منتشر شده'),
        ('0', 'پیش نویس')
    )

    name = models.CharField(max_length=50, verbose_name='عنوان')
    discription = models.TextField(verbose_name='توضیحات', default=None)
    status = models.CharField(max_length=7, choices=STATUS_CHOICE, verbose_name='وضعیت')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "امکانات"

class Room(models.Model):

    price = models.IntegerField(default=0, verbose_name='قیمت هر روز')
    name = models.CharField(max_length=50, verbose_name='نام اتاق')
    number =  models.IntegerField(default=0, verbose_name='شماره اتاق')
    floor =  models.IntegerField(default=0, verbose_name='طبقه اتاق')
    suggested = models.BooleanField(default=False, verbose_name="این اتاق پیشنهاد شده است")
    capacity = models.IntegerField(verbose_name='ظرفیت', default=0)
    option = models.ManyToManyField(Option, verbose_name='امکانات')
    image = models.ImageField(upload_to='room_image', verbose_name='عکس')
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "اتاق ها"


class Food(models.Model):
    STATUS_CHOICE = (
        ('1', 'منتشر شده'),
        ('0', 'پیش نویس')
    )
    TYPE_CHOICE = (
        ('2', 'شام'),
        ('1', 'ناهار'),
        ('0', 'صبحانه')
    )

    name = models.CharField(max_length=50, verbose_name='عنوان')
    status = models.CharField(max_length=7, choices=STATUS_CHOICE, verbose_name='وضعیت')
    foodType = models.CharField(max_length=10, choices=TYPE_CHOICE, verbose_name='تایپ')
    price = models.IntegerField(default=0, verbose_name='قیمت')
    description = models.TextField()
    image = models.ImageField(upload_to='food_image', verbose_name='عکس')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "غذاها"

class Reserve(models.Model):
    COUNTRY_CHOISE = (
        ("0", "المان"),
        ("1", "چین"),
        ("2", "انگلیس"),
        ("3", "فرانسه"),
        ("4", "ژاپن"),
        ("5", "سایر"),
        ("6", "ایران"),
        ("7", "عراق"),
    )

    start_date = models.CharField(max_length=10, verbose_name='از تاریخ')
    finish_date = models.CharField(max_length=10, verbose_name='تا تاریخ')
    name = models.CharField(max_length=20, default='', verbose_name='نام')
    family = models.CharField(max_length=20, default='', verbose_name='نام خانوادگی')
    phone = models.IntegerField(blank=True, null=True, verbose_name='شماره تلفن')
    verify_code = models.CharField(max_length=5 , blank=True, null=True)
    city = models.CharField(max_length=10, blank=True, null=True, verbose_name='شهر')
    address = models.CharField(max_length=10, blank=True, null=True, verbose_name='ادرس')
    state = models.CharField(max_length=10, blank=True, null=True, verbose_name='استان')
    email = models.CharField(max_length=10, blank=True, null=True, verbose_name='ایمیل')
    room = models.ForeignKey(Room, verbose_name='اتاق', on_delete=models.CASCADE)
    total_price = models.IntegerField(blank=False, default=0, verbose_name='مبلغ کل')

    class Meta:
        verbose_name_plural = "رزرو ها"

    def __str__(self):
        return f'{self.family} - {self.room}'
class Contact(models.Model):
    name = models.CharField(max_length=40, verbose_name="نام ارسال کننده پیام/نطر")
    email = models.CharField(max_length=40, verbose_name='ایمیل')
    phone = models.CharField(max_length=40, verbose_name='شماره تماس')
    subject = models.CharField(max_length=40, verbose_name="موضوع")
    message = models.TextField(verbose_name='پیغام')
    show_in_comments = models.BooleanField(default=False, verbose_name="این پیام توسط مدیریت تایید شده و در بخش نمایش نطرات ویژه قابل نمایش است ")
    show_in_comments_two = models.BooleanField(default=False, verbose_name="این پیام توسط مدیریت تایید شده و در بخش نمایش نطرات عادی قابل نمایش است ")
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')

    class Meta:
        verbose_name_plural = "پیام ها"

    def __str__(self):
        return self.subject


class FoodReserve(models.Model):
    food = models.ForeignKey(Food, blank=False, null=False, on_delete=models.CASCADE, verbose_name='غذا سفارش داده شده')
    reserve = models.ForeignKey(Reserve, blank=False, null=False, on_delete=models.CASCADE, verbose_name='سفارش دهنده')
    num_food = models.CharField(max_length=10, verbose_name='تعداد غذا' , blank=True, null=True)

    class Meta:
        verbose_name_plural = "غذا های سفارش داده شده"


