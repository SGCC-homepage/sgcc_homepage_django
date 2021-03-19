from django.db import models
from django.contrib.auth.models import AbstractUser

# AbstractUser의 username이 학번
class User(AbstractUser):
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
    major = models.IntegerField(choices=MAJOR_CHOICE, default=0)
    phone = models.CharField(max_length=20)
    state = models.IntegerField(choices=STATE_CHOICE, default=0)
    grade = models.IntegerField(choices=GRADE_CHOICE, default=0)
    dues_payment = models.BooleanField(default=False)

    def __str__(self):
        return self.name + '('+self.username+')'
