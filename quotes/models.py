import random

from django.db import models


class Author(models.Model):

    class Meta:
        ordering = ['name', 'surname']

    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=230)
    url = models.URLField(blank=True)
    photo = models.ImageField(upload_to='quotes/author/%Y/', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.surname)


class Quote(models.Model):
    text = models.CharField(max_length=580)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}\n--\n{}'.format(self.text, self.author)

    @classmethod
    def get_random_quote(cls):
        """Get a random quote, or an empty dict in none available.
        """
        quotes = cls.objects.all()
        return random.choice(quotes) if quotes else {}
