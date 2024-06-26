from django.urls import path, include
# from myapp.models import New_user
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.core.mail import send_mail
User=get_user_model()
# Serializers define the API representation.
class UserRegister(serializers.ModelSerializer):
    #password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        #fields=["username","password","email","password2","phone","image"]
        fields=["username","email","phone","image"]
    def save(self):
        
        reg=User(email=self.validated_data['email'],
                 username=self.validated_data['username'],
                 phone=self.validated_data['phone'],
                 image=self.validated_data['image']
                 )
        
        # password=self.validated_data['password']
        # password2=self.validated_data['password2']
        # if password!=password2:
        #     raise serializers.ValidationError({'password':'password does not match'})
        password=User.objects.make_random_password()
        reg.set_password(password)
        reg.save()
        from_email = self.validated_data['email']
        email=self.validated_data['email']
        name=self.validated_data['username']
        
        if name and email:
                subject = "New User registration"
                message = f"Name: {name}\nEmail: {email}\n Password:{password}"
                to_email = [email]
                send_mail(subject, message, from_email, to_email,fail_silently=False)
                
        return reg
              
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

