from django.db import models

class Vote(models.Model):
    title = models.CharField(max_length=50)
    issue1 = models.CharField(max_length=100)
    issue2 = models.CharField(max_length=100)

class Comment(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    choices = models.CharField(
        max_length=3,
        choices= [
            ('1', 'first'),
            ('2', 'second'),
        ]
    )

    