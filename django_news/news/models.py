from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Tag(models.Model):

    text = models.TextField(max_length=500, verbose_name="Название тега")

    def __str__(self):
        return "{}".format(self.text)

    def get_update_url(self):
        return reverse("tag_update_url", kwargs={"tag_id": self.pk})

    def get_delete_url(self):
        return reverse("tag_delete_url", kwargs={"tag_id": self.pk})

    def get_tagfilter_url(self):
        return reverse("index_filter_url", kwargs={"tag_id": self.pk})

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэг"
        permissions = (
            ("can_see_guest", "Можно видеть гость"),)

    def __str__(self) -> str:
        return self.text


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название статьи')
    text = models.TextField(verbose_name='Текст', max_length=500)
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации', auto_now=True)
    author = models.ForeignKey(
        to=User, on_delete=models.SET_NULL, blank=True, null=True)
    tag_state = models.ManyToManyField(
        to=Tag, blank=True, verbose_name='Тег', related_name="posts")

    def __str__(self):
        return "{}".format(self.text)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статья"

    def get_absolute_url(self):
        return reverse("post_detail_url", kwargs={"id_post": self.pk})

    def get_update_url(self):
        return reverse("post_update_url", kwargs={"id_post": self.pk})

    def get_delete_url(self):
        return reverse("post_delete_url", kwargs={"id_post": self.pk})


class Comment(models.Model):
    text = models.TextField(verbose_name='Текст', max_length=500)
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации', auto_now=True)
    author = models.ForeignKey(
        to=User, on_delete=models.SET_NULL, blank=True, null=True)
    fk_post = models.ForeignKey(
        to=Post, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return "{},{},{}".format(self.fk_post, self.author, self.pub_date)

    class Meta:
        db_table = "comment"
        verbose_name = "Комментариии"
        verbose_name_plural = "Комментариии"
        permissions = (
            ("can_see_author", "Можно видеть автора коментария"),)
