from django.db import models
from django.utils import timezone

class Department(models.Model):
  name = models.CharField('部署名', max_length=20)
  created_at = models.DateTimeField('日付', default=timezone.now)
  
  def __str__(self):
    return self.name
  
class Club(models.Model):
  name = models.CharField('部活名', max_length=20)
  created_at = models.DateTimeField('日付', default=timezone.now)
  
  def __str__(self):
    return self.name
  
class Employee(models.Model):
  first_name = models.CharField('名', max_length=20)
  last_name = models.CharField('姓', max_length=20)
  email = models.EmailField('メールアドレス', blank=True) # blank必須でなくなる
  department = models.ForeignKey(
    Department, verbose_name='部署', on_delete=models.PROTECT, # PROTECT:社員がいたら削除できない CASCADE:道連れ削除
  )
  club = models.ManyToManyField(
    Club, verbose_name='部活'
  )
  created_at = models.DateTimeField('日付', default=timezone.now)
  address = models.CharField('住所', max_length=20, blank=True)
  
  def __str__(self):
    return '{0} {1} {2}'.format(self.last_name, self.first_name, self.department)

