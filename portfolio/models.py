from django.db import models


class FirstDisplay(models.Model):
    logo_top = models.ImageField(upload_to='logo_top')

    title = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    image = models.ImageField(upload_to='header_bg/')


class SecondDisplay(models.Model):
    top_left_title = models.CharField(max_length=100)
    top_left_text = models.CharField(max_length=100)

    top_right_title = models.CharField(max_length=100)
    top_right_text = models.CharField(max_length=100)

    bottom_left_title = models.CharField(max_length=100)
    bottom_left_text = models.CharField(max_length=100)

    bottom_right_title = models.CharField(max_length=100)
    bottom_right_text = models.CharField(max_length=100)


class ThirdDisplay(models.Model):
    bg_image = models.ImageField(upload_to='third_bg/')
    text_image_1 = models.ImageField(upload_to='text_image1')
    text_image_2 = models.ImageField(upload_to='text_image2')
    text_image_3 = models.ImageField(upload_to='text_image3')
    text_image_4 = models.ImageField(upload_to='text_image4')


class FourthDisplay(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    image = models.ImageField(upload_to='fourth_bg/')


class Contact(models.Model):
    link1 = models.URLField()
    link2 = models.URLField()
    link3 = models.URLField()
    link4 = models.URLField()

    title = models.CharField(max_length=100)
    text1 = models.CharField(max_length=100)
    text2 = models.CharField(max_length=100)

    mail = models.EmailField()