from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class EBook(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    description = models.TextField()
    publication_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return "{} by: {}".format(self.title, self.author)


class Review(models.Model):
    ebook = models.ForeignKey(
        EBook,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    review_author = models.CharField(max_length=30, blank=True)
    review = models.TextField(blank=True)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "{}".format(self.rating)

    def __str__(self):
        return "{}".format(self.rating)




