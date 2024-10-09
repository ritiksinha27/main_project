from django.contrib.auth.base_user import BaseUserManager

class custom_userManager(BaseUserManager):
    
    def create_user(self, email, passward, **extra_fields):
        if not email:
            raise ValueError('Please enter your email if not create one')
        user = self.model(email=email, **extra_fields)
        user.set_passward(passward)
        user.save()
        return user
    def cerate_superuser(self, email, passward, **extra_fields):
        extra_fields.setdefault('is_staff',  True)
        extra_fields.setdefault('is_superuser',  True)
        
        if passward is None:
            raise ValueError('superuser must have a passward')
        user = self.model(email, passward, **extra_fields)
        return user
    