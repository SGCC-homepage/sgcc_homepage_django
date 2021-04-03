from django.db import models
from django import forms
from django.contrib.auth.models import BaseUserManager, AbstractUser


def student_id_validator(value):
    if len(value) != 8:
        raise forms.ValidationError('학번 8글자 모두 입력해주세요(예시: 20210001)')


class UserManager(BaseUserManager):
    def create_user(self, student_id, name, email, phone, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            student_id=student_id,
            name=name,
            email=self.normalize_email(email),
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, student_id, name, email, phone, password=None):
        user = self.create_user(
            student_id=student_id,
            name=name,
            email=self.normalize_email(email),
            phone=phone,
            password=password,
        )
        user.is_admin = True,
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


# AbstractUser의 username이 학번
class User(AbstractUser):

    objects = UserManager()

    MAJOR_CHOICE = [(0, '국어국문학'), (1, '사학'), (2, '철학'), (3, '종교학'),
                    (4, '영미어문'), (5, '미국문화'), (6, '유럽문화'), (7, '중국문화'),
                    (8, '사회학'), (9, '정치외교학'), (10, '심리학'), (11, '국제한국학'), (12, '아트&테크놀로지'),
                    (13, '신문방송학'), (14, '미디어&엔터테인먼트'), (15, '글로벌 한국학'),
                    (16, '수학'), (17, '물리학'), (18, '화학'), (19, '생명과학'),
                    (20, '전자공학'), (21, '화공생명공학'), (22, '컴퓨터공학'), (23, '기계공학'),
                    (24, '경제학'), (25, '경영학'), (26, '커뮤니케이션학')]
    STATE_CHOICE = [(0, '재학'), (1, '군휴학'), (2, '일반 휴학'), (3, '졸업'), (4, '교환')]
    GRADE_CHOICE = [(0, '신입'), (1, '일반'), (2, '운영진'), (3, '비활'), (4, '탈퇴')]

    name = models.CharField(max_length=20)
    student_id = models.CharField(max_length=20, unique=True, validators=[student_id_validator])
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    major = models.IntegerField(choices=MAJOR_CHOICE, default=0)
    phone = models.CharField(max_length=20)
    state = models.IntegerField(choices=STATE_CHOICE, default=0)
    grade = models.IntegerField(choices=GRADE_CHOICE, default=0)
    dues_payment = models.BooleanField(default=False)

    USERNAME_FIELD = 'student_id'
    REQUIRED_FIELDS = ['name', 'phone', 'email']

    def __str__(self):
        return self.name + '('+self.student_id+')'

