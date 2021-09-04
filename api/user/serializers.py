from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.db import transaction

from api.user.models import User, JoinSGCC


class RegisterSGCCSerializer(serializers.Serializer):
    name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    major = serializers.IntegerField()
    second_major = serializers.IntegerField(required=False)
    third_major = serializers.IntegerField(required=False)
    phone = serializers.CharField()
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    reason = serializers.CharField()
    read_notice = serializers.BooleanField()

    def validate(self, attrs):
        username = attrs.get('username')
        if len(username) != 8:
            raise ValidationError({'username': '학번 8자리를 모두 입력해주세요.(예시: 20210001)'})
        read_notice = attrs.get('read_notice')
        if not read_notice:
            raise ValidationError({'read_notice': '가입 안내사항을 읽고 확인해주세요.'})
        major_len = len(User.MAJOR_CHOICE)
        major = attrs.get('major')
        if major >= major_len:
            raise ValidationError({'major': '유효하지 않은 전공입니다.'})
        password = attrs.get('password1')
        password_confirm = attrs.get('password2')
        if password != password_confirm:
            raise ValidationError({'password': '비밀번호가 일치하지 않습니다.'})

        return attrs

    @transaction.atomic
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data.get('username'),
            name=validated_data.get('name'),
            email=validated_data.get('email'),
            phone=validated_data.get('phone'),
            major=validated_data.get('major'),
            password=validated_data.get('password'),
        )
        join_sgcc = JoinSGCC.objects.create(
            user=user,
            reason=validated_data.get('reason'),
            read_notice=validated_data.get('read_notice')
        )
        join_sgcc.save()
        return validated_data
