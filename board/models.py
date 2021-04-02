from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Material(models.Model):
    main_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    contents = models.TextField()
    image = models.FileField(null=True)

    def __str__(self):
        return '(' + str(self.main_category_id) + ')' + self.pk


class Team(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Report(models.Model):
    title = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    report = models.FileField(upload_to="report")
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title+'(' + self.team.name + ')'