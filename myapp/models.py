from django.db import models


# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=100)


class User(models.Model):
    first_name = models.CharField(max_length=100)


class Currency(models.Model):
    name = models.CharField(max_length=100)

# cmd + K
# ctrl + K nebo alt + k

# continuous integration
# devops
# git actions
# circle CI
