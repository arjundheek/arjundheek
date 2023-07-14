from django.db import models

from Accounts.models import Profile


class Brand(models.Model):
    image = models.ImageField(upload_to="static/uploads/brands")
    logo = models.ImageField(
        default="", blank=True, upload_to="static/uploads/brands/logos"
    )
    name = models.CharField(max_length=255)
    slogan = models.CharField(max_length=255, default="", blank=True)
    url = models.CharField(max_length=255, default="", blank=True)

    def __str__(self):
        return str(self.name)


class Category(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="static/uploads/categories")
    title = models.CharField(max_length=255, default="", blank=True)
    description = models.CharField(max_length=255, default="", blank=True)

    def __str__(self):
        return str(f"{self.brand.name} - {self.title}")


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    main_image = models.ImageField(upload_to="static/uploads/products")
    image_1 = models.ImageField(
        default="", blank=True, upload_to="static/uploads/products"
    )
    image_2 = models.ImageField(
        default="", blank=True, upload_to="static/uploads/products"
    )
    # image_3 = models.ImageField(default='', blank=True, upload_to='static/uploads/products')
    # image_4 = models.ImageField(default='', blank=True, upload_to='static/uploads/products')
    # image_5 = models.ImageField(default='', blank=True, upload_to='static/uploads/products')
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, default="", blank=True)
    color = models.CharField(max_length=50, default="", blank=True)
    type = models.CharField(max_length=50, default="", blank=True)
    gender = models.CharField(
        max_length=15,
        default="",
        blank=True,
        choices=[
            ("man", "Man"),
            ("woman", "Woman"),
            ("boy", "Boy"),
            ("girl", "Girl"),
            ("babyboy", "Baby Boy"),
            ("babygirl", "Baby Girl"),
        ],
    )
    url = models.CharField(max_length=255, default="", blank=True)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    try_on_main_image = models.ImageField(
        default="", blank=True, upload_to="static/uploads/products"
    )
    try_on_image1 = models.ImageField(
        default="", blank=True, upload_to="static/uploads/products"
    )
    try_on_image2 = models.ImageField(
        default="", blank=True, upload_to="static/uploads/products"
    )
    is_try_on_main_image_enabled = models.BooleanField(default=False)
    is_try_on_image1_enabled = models.BooleanField(default=False)
    is_try_on_image2_enabled = models.BooleanField(default=False)
    # try_on_image3 = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)


class ProductDuplicate(models.Model):
    main_image = models.ImageField(
        upload_to="static/uploads/products", name="Main image"
    )
    image_1 = models.ImageField(
        default="", blank=True, upload_to="static/uploads/products", name="Image 1"
    )
    image_2 = models.ImageField(
        default="", blank=True, upload_to="static/uploads/products", name="Image 2"
    )


class Tryon(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="static/uploads/products")
    url = models.CharField(max_length=255, default="", blank=True)

    def __str__(self):
        return str(f"{self.product.name} - {self.profile.name}")


class Banner(models.Model):
    img = models.ImageField(upload_to="static/uploads/banners")
    page = models.CharField(
        max_length=50,
        default="",
        blank=True,
        choices=[
            ("brand", "Brand"),
            ("categories", "Categories"),
            ("products", "Products"),
            ("tryons", "Tryons"),
        ],
    )
    href = models.CharField(max_length=255, default="", blank=True)


class Document(models.Model):
    file = models.FileField(upload_to="static/uploads/docs")
