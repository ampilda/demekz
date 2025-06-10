from django.db import models

#Описание структуры базы данных для Django ORM

class Product_Name (models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    

    class Meta:
       #db_table необходим, так как Django видит названия классов как Django_ClassName
       db_table = "product_name"

    def __str__(self):
        return self.name

class Product_Type (models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    coef = models.FloatField()
    

    class Meta:
        db_table = "product_type"
        
    def __str__(self):
        return self.name

class Material_Type (models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    loss = models.FloatField(max_length=4)
    

    class Meta:
        db_table = "material_type"

    def __str__(self):
        return self.name

class Product_Workshop (models.Model):
    id = models.IntegerField(primary_key=True)
    #db_column обязателен для внешних клюей, так как Django видит ячейку как id_name
    name = models.ForeignKey(Product_Name, on_delete=models.CASCADE, max_length=100, db_column="name")
    time = models.FloatField(max_length=40)
    

    class Meta:
        db_table = "product_workshop"

    def __str__(self):
        return self.name


class Products (models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.ForeignKey(Product_Type, on_delete=models.CASCADE, max_length=100, db_column="type")
    name = models.ForeignKey(Product_Name, on_delete=models.CASCADE, max_length=100, db_column="name")
    article = models.IntegerField(max_length=10)
    min_cost = models.FloatField(max_length=15)
    material = models.ForeignKey(Material_Type, on_delete=models.CASCADE, max_length=100, db_column="material")
    class Meta:
        db_table = "products"

    def __str__(self):
        return self.name 

    #встроенная модель для расчитывания время изготовления
    @property
    def get_time(self):
        # берём из таблицы product_workshop id продукта
        summary = Product_Workshop.objects.filter(name=self.name.id).first()
        #присваиваем общее значение переменной total
        total = summary.time
        return total

class Workshop_Name (models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    

    class Meta:
        db_table = "workshop_name"

    def __str__(self):
        return self.name

class Workshop_Type (models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    

    class Meta:
        db_table = "worskshop_type"

    def __str__(self):
        return self.name


class Workshops (models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.ForeignKey(Workshop_Name, on_delete=models.CASCADE, max_length=100)
    type = models.ForeignKey(Workshop_Type, on_delete=models.CASCADE, max_length=100)
    counts = models.IntegerField(max_length=50)

    class Meta:
        db_table = "workshops"

    def __str__(self):
        return self.name




# Create your models here.
