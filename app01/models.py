from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()


from django.db import models


# Create your models here.


# class Book(models.Model):
#     name = models.CharField(max_length=32)
#     publish = models.CharField(max_length=32)
#     price = models.IntegerField()


class Book(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publish_date = models.DateField()

    publish = models.ForeignKey(to='Publish', to_field='nid', on_delete=models.CASCADE)
    authors = models.ManyToManyField(to='Author')

    def __str__(self):
        return self.name

    def publish_name(self):
        return {'name': self.publish.name, 'city': self.publish.city}


    # def publish_name(self):
    #     return self.publish.name

    def publish_name(self):
        return {'name': self.publish.name, 'city': self.publish.city}

    @property
    def author_list(self):
        return [{'name': author.name, 'age': author.age, 'id': author.nid} for author in self.authors.all()]


class Author(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    author_detail = models.OneToOneField(to='AuthorDatail', to_field='nid', unique=True, on_delete=models.CASCADE)


class AuthorDatail(models.Model):
    nid = models.AutoField(primary_key=True)
    telephone = models.BigIntegerField()
    birthday = models.DateField()
    addr = models.CharField(max_length=64)


class Publish(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Email(models.Model):
    send_user = models.CharField(max_length=100)
    recv_user = models.CharField(max_length=100)
    title = models.TextField()
    content = models.TextField()

class User(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)