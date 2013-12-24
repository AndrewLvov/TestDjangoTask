from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=128)

    # make it displayable in friendly format (e.g. in Admin panel)
    def __unicode__(self):
        return self.name

    class Meta:
        db_table = u'departments'


class Employee(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    # employee can't be outside department
    department = models.ForeignKey(Department, related_name='employees')

    def __unicode__(self):
        return u'{} {}'.format(self.first_name, self.last_name)

    class Meta:
        db_table = u'employees'
