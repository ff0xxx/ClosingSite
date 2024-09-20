from django.db import models
from django.urls import reverse


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True , verbose_name='Изображение')
    price = models.DecimalField(max_digits=7, default=0.00, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(max_digits=4, default=0.00, decimal_places=2, verbose_name='Скидка')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.PROTECT, verbose_name='Категория')

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('id',)

    def __str__(self):
        return f"{self.name} Количество - {self.quantity}"

    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={'product_slug': self.slug})

    # переопределяет отображение поля user
    def display_id(self):
        return f"{self.id:05}"

    # переопределяет отображение поля product
    def sell_price(self):
        if self.discount:
            return round(self.price*(1-self.discount/100), 2)
        return self.price
