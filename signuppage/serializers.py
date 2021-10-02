from rest_framework import serializers
from . models import signuppage


class signuppageSerializer(serializers.ModelSerializer):

    class Meta:
        model = signuppage
        fields = '__all__'


def create(self, validated_data):
    # return user.objects.create(**validated_data)
    Userobj = signuppage.objects.create(
        email=validated_data['email'],
        password=validated_data['password'],
        last_login=validated_data['last_login'],
        is_superuser=validated_data['is_superuser'],
        first_name=validated_data['first_name'],
        last_name=validated_data['last_name'],
        is_staff=validated_data['is_staff'],
        is_active=validated_data['is_active'],
        date_joined=validated_data['date_joined'],
        Business_type=validated_data['Business_type'],
        Nature_of_Business=validated_data['Nature_of_Business'],
        Country=validated_data['Country'],
        User_Type=validated_data['User_Type'],
        PhoneNumber=validated_data['PhoneNumber'],
        username=validated_data['username']
    )
    # Userobj = CustomUser.objects.create(**validated_data)
    Userobj.set_password(validated_data['password'])
    Userobj.save()
    return Userobj


def update(self, instance, validated_data):
    instance.email = validated_data.get('email', instance.email)
    instance.password = validated_data.get(
        'password', instance.password)
    instance.last_login = validated_data.get(
        'last_login', instance.last_login)
    instance.is_superuser = validated_data.get(
        'is_superuser', instance.is_superuser)
    instance.first_name = validated_data.get(
        'first_name', instance.first_name)
    instance.last_name = validated_data.get(
        'last_name', instance.last_name)
    instance.is_staff = validated_data.get('is_staff', instance.is_staff)
    instance.is_active = validated_data.get(
        'is_active', instance.is_active)
    instance.date_joined = validated_data.get(
        'date_joined', instance.date_joined)
    instance.Business_type = validated_data.get(
        'Business_type', instance.Business_type)
    instance.Nature_of_Business = validated_data.get(
        'Nature_of_Business', instance.Nature_of_Business)
    instance.Country = validated_data.get('Country', instance.Country)
    instance.User_Type = validated_data.get(
        'User_Type', instance.User_Type)
    instance.PhoneNumber = validated_data.get(
        'PhoneNumber', instance.PhoneNumber)
    instance.username = validated_data.get('username', instance.username)
    instance.set_password(validated_data['password'])
    instance.save()
    return instance
