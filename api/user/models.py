from django.db import models
from django import forms
from django.contrib.auth.models import BaseUserManager, AbstractUser, UserManager as DjangoUserManager
from django.utils.translation import gettext_lazy as _


def student_id_validator(value):
    if len(value) != 8:
        raise forms.ValidationError('학번 8자리를 모두 입력해주세요(예시: 20210001)')


class UserManager(BaseUserManager):
    def _create_user(self, username, name, email, phone, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            name=name,
            email=self.normalize_email(email),
            phone=phone,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, name, email, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(username, name, email, phone, password, **extra_fields)

    def create_superuser(self, username, email, name, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(username, name, email, phone, password, **extra_fields)


# AbstractUser의 username이 학번
class User(AbstractUser):

    objects = UserManager()

    MAJOR_CHOICE = [(0, '국어국문학'), (1, '사학'), (2, '철학'), (3, '종교학'),
                    (4, '영미어문'), (5, '미국문화'), (6, '유럽문화'), (7, '중국문화'),
                    (8, '사회학'), (9, '정치외교학'), (10, '심리학'), (11, '국제한국학'), (12, '아트&테크놀로지'),
                    (13, '신문방송학'), (14, '미디어&엔터테인먼트'), (15, '글로벌 한국학'),
                    (16, '수학'), (17, '물리학'), (18, '화학'), (19, '생명과학'),
                    (20, '전자공학'), (21, '화공생명공학'), (22, '컴퓨터공학'), (23, '기계공학'),
                    (24, '경제학'), (25, '경영학'), (26, '커뮤니케이션학'), (27, '인문계')]
    STATE_CHOICE = [(0, '재학'), (1, '군휴학'), (2, '일반 휴학'), (3, '졸업'), (4, '교환'), (5, '기타')]

    class Grade(models.IntegerChoices):
        NON = 0, _('대기')
        NEW = 1, _('신입')
        GEN = 2, _('일반')
        GRAD = 3, _('졸업')
        MAN = 4, _('운영진')
        LEAVE = 5, _('탈퇴')

    name = models.CharField(verbose_name='이름', max_length=20)
    username = models.CharField(
        verbose_name='학번',
        max_length=8,
        unique=True,
        help_text=_('학번 8자리를 모두 입력해주세요(예시: 20210001)'),
        validators=[student_id_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(
        verbose_name='이메일',
        max_length=255,
        unique=True,
    )
    major = models.IntegerField(verbose_name='본전공', choices=MAJOR_CHOICE, default=0)
    second_major = models.IntegerField(verbose_name='제 2전공', choices=MAJOR_CHOICE, null=True, blank=True)
    third_major = models.IntegerField(verbose_name='제 3전공', choices=MAJOR_CHOICE, null=True, blank=True)
    phone = models.CharField(verbose_name='휴대폰 번호', max_length=20)
    state = models.IntegerField(choices=STATE_CHOICE, default=0)
    grade = models.IntegerField(choices=Grade.choices, default=0)
    dues_payment = models.BooleanField(default=False)

    # USERNAME_FIELD = 'student_id'
    REQUIRED_FIELDS = ['name', 'phone', 'email']

    class Meta:
        verbose_name = '유저'
        verbose_name_plural = verbose_name
        ordering = ['-date_joined']

    def __str__(self):
        return self.name + '('+self.username+')'


class JoinSGCC(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField(verbose_name='가입 사유')
    read_notice = models.BooleanField()
    approval = models.BooleanField(default=False)

    def __str__(self):
        return self.user.name +'(' + self.user.username + ') 입회원서'
