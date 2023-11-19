# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Curator(models.Model):
    curator_id = models.AutoField(primary_key=True, db_comment='╩юф ъєЁрЄюЁр')
    curator_second_name = models.CharField(max_length=45, db_comment='╘рьшыш  ъєЁрЄюЁр')
    curator_first_name = models.CharField(max_length=45, db_comment='╚ь  ъєЁрЄюЁр')
    curator_middle_name = models.CharField(max_length=45, blank=True, null=True, db_comment='╬ЄўхёЄтю ъєЁрЄюЁр')
    curator_contact_number = models.PositiveBigIntegerField(unique=True, db_comment='╩юэЄръЄэ√щ эюьхЁ ъєЁрЄюЁр')

    class Meta:
        app_label = 'faculty'
        db_table = 'curator'
        db_table_comment = '╩єЁрЄюЁ'


class Department(models.Model):
    department_id = models.AutoField(primary_key=True, db_comment='╩юф ърЇхфЁ√')
    department_name = models.CharField(unique=True, max_length=100, db_comment='═рчтрэшх ърЇхфЁ√')
    department_name_short = models.CharField(unique=True, max_length=8, db_comment='╤юъЁр∙╕ээюх эрчтрэшх ърЇхфЁ√')

    class Meta:
        app_label = 'faculty'
        db_table = 'department'
        db_table_comment = '╩рЇхфЁр'


class Direction(models.Model):
    direction_id = models.AutoField(primary_key=True, db_comment='╩юф эряЁртыхэш ')
    direction_name = models.CharField(max_length=100, db_comment='═рчтрэшх эряЁртыхэш ')
    specialization = models.CharField(max_length=100, blank=True, null=True, db_comment='╤юъЁр∙╕ээюх эрчтрэшх эряЁртыхэш ')
    department = models.ForeignKey(Department, models.DO_NOTHING, db_comment='╩юф ърЇхфЁ√')

    class Meta:
        app_label = 'faculty'
        db_table = 'direction'
        db_table_comment = '═ряЁртыхэшх'


class Group(models.Model):
    group_id = models.AutoField(primary_key=True, db_comment='╩юф уЁєяя√')
    group_number = models.IntegerField(db_comment='═юьхЁ уЁєяя√')
    group_course_number = models.IntegerField(db_comment='═юьхЁ ъєЁёр уЁєяя√')
    direction = models.ForeignKey(Direction, models.DO_NOTHING, db_comment='╩юф эряЁртыхэш ')
    curator = models.ForeignKey(Curator, models.DO_NOTHING, blank=True, null=True, db_comment='╩юф ъєЁрЄюЁр уЁєяя√')
    group_leader = models.OneToOneField('Student', models.DO_NOTHING, blank=True, null=True, db_comment='╩юф ёЄрЁюёЄ√ уЁєяя√',related_name='group_leader',)

    class Meta:
        app_label = 'faculty'
        db_table = 'group'
        db_table_comment = '├Ёєяяр'


class Student(models.Model):
    student_id = models.AutoField(primary_key=True, db_comment='╩юф ёЄєфхэЄр')
    student_second_name = models.CharField(max_length=45, db_comment='╘рьшыш  ёЄєфхэЄр')
    student_first_name = models.CharField(max_length=45, db_comment='╚ь  ёЄєфхэЄр')
    student_middle_name = models.CharField(max_length=45, blank=True, null=True, db_comment='╬ЄўхёЄтю ёЄєфхэЄр')
    group = models.ForeignKey(Group, models.DO_NOTHING, blank=True, null=True, db_comment='╩юф уЁєяя√ ёЄєфхэЄр')
    student_status = models.CharField(max_length=8)

    class Meta:
        app_label = 'faculty'
        db_table = 'student'
        db_table_comment = '╤ЄєфхэЄ'
