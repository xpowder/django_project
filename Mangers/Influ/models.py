from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static

CITY_CHOICES = [
    ('casablanca', 'Casablanca'),
    ('rabat', 'Rabat'),
    ('marrakech', 'Marrakech'),
    ('fes', 'Fes'),
    ('tangier', 'Tangier'),
    ('agadir', 'Agadir'),
    ('meknes', 'Meknes'),
    ('oujda', 'Oujda'),
    ('kenitra', 'Kenitra'),
    ('tetouan', 'Tetouan'),
    # Add more cities as needed
]

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=65)
    last_name = models.CharField(max_length=65)
    profile_images = models.ImageField(upload_to='image/', null=True, blank=True, default='images/default_avatar.png')
    bio = models.TextField()
    specialization = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=20, choices=CITY_CHOICES, default='casablanca')  # Set default value here
    contact_email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    available_for_consultation = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user)

    @property
    def name(self):
        if self.first_name and self.last_name:
            name = f"{self.first_name} {self.last_name}"
        elif self.last_name:
            name = self.last_name
        else:
            name = self.user.username
        return name

    @property
    def avatar(self):
        try:
            avatar = self.profile_images.url
        except Exception as e:
            print(f"Exception occurred while fetching avatar URL: {str(e)}")
            avatar = static('images/default_avatar.png')  # Default avatar image path from static files
        return avatar
