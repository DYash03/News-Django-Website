from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

CATEGORY_CHOICES = (
    ('India', 'INDIA'),
    ('World', 'WORLD'),
    ('Election', 'ELECTION'),
    ('Business', 'BUSINESS'),
    ('Tech', 'TECH'),
    ('Science', 'SCIENCE'),
    ('Health', 'HEALTH'),
    ('Entertainment & Arts', 'ENTERTAINMENT & ARTS'),
)

TYPE_CHOICES = (
    ('Breaking', 'BREAKING'),
    ('Latest', 'LATEST'),
    ('Top', 'TOP'),
)

SCATEGORY_CHOICES = (
    ('Cricket', 'CRICKET'),
    ('Football', 'FOOTBALL'),
    ('Hockey', 'HOCKEY'),
    ('Kabaddi', 'KABADDI'),
    ('Basketball', 'BASKETBALL'),
    ('Others', 'OTHERS'),
)


class New(models.Model):
    news_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    title_desc = models.CharField(max_length=400)
    Type = models.CharField(choices=TYPE_CHOICES, max_length=30)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=30)
    image = models.ImageField(upload_to="news_app/images")
    description = RichTextUploadingField(config_name='special', extra_plugins=['embed'], external_plugin_resources=[(
        'embed',
        '/static/ckeditor/ckeditor/plugins/embed/',
        'plugin.js',
    )],)
    datetime = models.DateTimeField()
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(New, self).save(*args, **kwargs)


class Sport(models.Model):
    sports_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    title_desc = models.CharField(max_length=300)
    Type = models.CharField(choices=TYPE_CHOICES, max_length=30)
    category = models.CharField(choices=SCATEGORY_CHOICES, max_length=30)
    image = models.ImageField(upload_to="news_app/images")
    description = RichTextUploadingField(config_name='special', extra_plugins=['embed'], external_plugin_resources=[(
        'embed',
        '/static/ckeditor/ckeditor/plugins/embed/',
        'plugin.js',
    )],)
    PointsTable1_embed = models.CharField(
        max_length=5000, blank=True, null=True)
    PointsTable2_embed = models.CharField(
        max_length=5000, blank=True, null=True)
    datetime = models.DateTimeField()
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name = 'Sport'
        verbose_name_plural = 'Sports'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Sport, self).save(*args, **kwargs)


class Video(models.Model):
    video_id = models.AutoField(primary_key=True)
    video_name = models.CharField(max_length=300)
    video = models.FileField(upload_to="news_app/videos")
    datetime = models.DateTimeField()

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        return self.video_name


class Tv(models.Model):
    Tv_id = models.AutoField(primary_key=True)
    channel_name = models.CharField(max_length=200)
    channel_embed = models.CharField(max_length=5000)

    class Meta:
        verbose_name = 'TV'
        verbose_name_plural = 'TV'

    def __str__(self):
        return self.channel_name


class Weather(models.Model):
    weather_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    title_desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to="news_app/images")
    description = RichTextUploadingField(config_name='special', extra_plugins=['embed'], external_plugin_resources=[(
        'embed',
        '/static/ckeditor/ckeditor/plugins/embed/',
        'plugin.js',
    )],)
    datetime = models.DateTimeField()
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name = 'Weather'
        verbose_name_plural = 'Weather'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Weather, self).save(*args, **kwargs)


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    mob = models.CharField(max_length=50)
    textarea = models.TextField(max_length=10000, default="")

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'

    def __str__(self):
        return self.name+str(self.msg_id)
