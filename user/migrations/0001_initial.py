# Generated by Django 3.1.7 on 2021-03-05 13:51

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=20)),
                ('student_id', models.CharField(max_length=20)),
                ('major', models.IntegerField(choices=[(0, '국어국문학'), (1, '사학'), (2, '철학'), (3, '종교학'), (4, '영미어문'), (5, '미국문화'), (6, '유럽문화'), (7, '중국문화'), (8, '사회학'), (9, '정치외교학'), (10, '심리학'), (11, '국제한국학'), (12, '아트&테크놀로지'), (13, '신문방송학'), (14, '미디어&엔터테인먼트'), (15, '글로벌 한국학'), (16, '수학'), (17, '물리학'), (18, '화학'), (19, '생명과학'), (20, '전자공학'), (21, '화공생명공학'), (22, '컴퓨터공학'), (23, '기계공학'), (24, '경제학'), (25, '경영학'), (26, '커뮤니케이션학')])),
                ('phone', models.CharField(max_length=20)),
                ('state', models.IntegerField(choices=[(0, '재학'), (1, '군휴학'), (2, '일반 휴학'), (3, '졸업'), (4, '교환')])),
                ('grade', models.IntegerField(choices=[(0, '신입'), (1, '일반'), (2, '운영진'), (3, '비활'), (4, '탈퇴')], default=0)),
                ('dues_payment', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
