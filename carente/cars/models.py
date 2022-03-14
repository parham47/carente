from unicodedata import name
from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
gearboxchoice = (('dandei', 'دنده ای'),
              ('automatic', 'اتوماتیک'),
              )
driver_choices = (('with_driver', 'با راننده'),
              ('without_driver', 'بدون راننده'),
              ('both','با راننده و بدون راننده هر دو امکان پذیر است'), 
              )

class sazande(models.Model):
    name = models.CharField(max_length = 20, verbose_name="نام سازنده")
    class Meta:
        verbose_name = "سازنده"
        verbose_name_plural = 'سازنده ها'

    def __str__(self):
        return self.name

nahve_tahvil = (('dayaft', 'دریافت در محل'),
              ('tahvil', 'تحویل ماشین'),
              )
class modelcar(models.Model):
    name = models.CharField(max_length = 20, verbose_name="نام مدل")
    sazande= models.ForeignKey(sazande,on_delete=models.CASCADE,max_length = 20, verbose_name="سازنده")
    saltolid = models.DateField(default = 1 , verbose_name = "سال تولید")
    typebadane = models.CharField(max_length=20, verbose_name = "نوع بدنه")
    gearbox2 = MultiSelectField(choices=gearboxchoice,verbose_name = "جعبه دنده ")
    
    class Meta:
        verbose_name = "مدل ماشین"
        verbose_name_plural = 'مدل های ماشین'

    def __str__(self):
        return self.name

class cars(models.Model):
    sazande =models.ForeignKey(sazande,on_delete=models.CASCADE,related_name='sazande')
    modelcar=models.ForeignKey(modelcar,on_delete=models.CASCADE,related_name='modelcar')
    
    available = models.BooleanField(default = 1 , verbose_name = "آمادگی برای اجاره")
   ## published_at = models.DateTimeField(default = timezone.now , verbose_name = "تاریخ اضافه شدن به سایت")
   ## created_at = models.DateTimeField(auto_now_add = True)
    ##updated_at = models.DateTimeField(auto_now = True)
    color = models.CharField(max_length = 20 , verbose_name = "رنگ")  
    karkard = models.CharField(default = 50 , verbose_name = "کارکرد",max_length =20)
    pelak = models.CharField( primary_key = True , max_length = 20 ,verbose_name = "پلاک")
    city =models.CharField ( max_length = 20 ,verbose_name= "شهر")
    pricecar = models.IntegerField( verbose_name = "قیمت تقریبی ماشین")
    zabt = models.BooleanField(default = 0 , verbose_name = "ضبط صوتی")
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    
    
    class Meta:
        verbose_name = "ماشین"
        verbose_name_plural = 'ماشین ها'

    def __str__(self):
        return self.modelcar


class ghavanin(models.Model):
    tozihat =models.TextField(verbose_name = "توضیحات")
    driver_status = MultiSelectField(choices=driver_choices,verbose_name = "با راننده یا بدون راننده؟")
    mahdoodiatperhour =models.IntegerField(verbose_name = "هزینه اضافه به ازای هر ساعت")
    mahdoodiatperkm= models.IntegerField(verbose_name = "محدودیت کیلومتری")
    priceperkm= models.IntegerField(verbose_name = "هزینه اضافه به ازای هر کیلومتر")
    zemanat=models.TextField(verbose_name = "ضمانت")
    kamtarin_rooz_ejare=models.IntegerField(verbose_name = "حداقل مدت اجاره")
    nahve_tahvil=MultiSelectField(choices=nahve_tahvil)
    priceperday = models.IntegerField( verbose_name = "قیمت اجاره روزانه به تومان")
    cars=models.OneToOneField(cars, verbose_name=("ماشین"), on_delete=models.CASCADE)

class emkanat(models.Model):
    
    zabt = models.BooleanField(default = 0 , verbose_name = "ضبط صوتی")
    