from django.db import models
from datetime import datetime

current_date = datetime.now().strftime('%d%m%Y')


# Create your models here.
class HomeHeading(models.Model):
    Heading = models.TextField()
    def __str__(self):
        return self.Heading
    



socialmedias= (
    ("Facebook", "Facebook"),
    ("Youtube", "Youtube"),
    ("X", "X"),
    ("Instagram","Instagram"),
     ("Linkedin","Linkedin"),
)


class SocialMedias(models.Model):
    name = models.CharField(max_length=30,
                  choices=socialmedias,
                  )
    # Icon_image = models.ImageField(upload_to='socialmedias')
    Link = models.CharField(max_length=150)


    def __str__(self):
        return self.name
    


class Testimonial(models.Model):
    name = models.CharField(max_length=30,)
    Post = models.CharField(max_length=30,)
    description = models.TextField()
    ProfilePic = models.ImageField(upload_to="Testimonial")
    def __str__(self):
        return self.name



class Strategie(models.Model):
    Strategy_name = models.CharField(max_length=30,)
    description = models.TextField()
    IconsImage = models.ImageField(upload_to="Strategy_Icon")
    visual1 = models.CharField(max_length=100,default='1')
    visual2 = models.CharField(max_length=100,default='2')
    visual3 = models.CharField(max_length=100,default='3')
    visual4 = models.CharField(max_length=100,default='4')
    def __str__(self):
        return self.Strategy_name




 



class WebinarRegisteration(models.Model):
    Webinar_name = models.CharField(max_length= 500)
    Webinar_time = models.CharField(max_length=20, default =current_date)
    Webinar_author = models.CharField(max_length=20, default ='not able to get')
    full_name = models.CharField(max_length = 100)
    email_address = models.CharField(max_length=150)
    phone_number  = models.CharField(max_length = 15)
    country = models.CharField(max_length = 100)
    years_of_trading_experience = models.CharField(max_length=3)
    date_of_registeration = models.CharField(max_length=20, default =current_date)
    parmas = models.CharField(max_length=300, default = '')
    
    def __str__(self):
        return self.parmas
    

class Communitie(models.Model):
    full_name = models.CharField(max_length = 100)
    email_address = models.CharField(max_length=150)
    phone_number  = models.CharField(max_length = 15)
    country = models.CharField(max_length = 100)
    years_of_trading_experience = models.CharField(max_length=3)
    date_of_joined  = models.CharField(max_length=20, default =current_date)
    def __str__(self):
        return f'{self.full_name}_{current_date}'
    


class Blog(models.Model):
    posted_on = models.CharField(max_length = 100)
    author_name = models.CharField(max_length = 200)
    Blog_image = models.ImageField(upload_to='Blogs/' )
    Title = models.CharField(max_length = 800)
    short_note = models.CharField(max_length = 2000)
    Description = models.TextField()
    Tages = models.CharField(max_length = 1000)

    def __str__(self):
        return self.Title



class whatweoffer(models.Model):
    Image = models.ImageField(upload_to='what_we_offer/')
    Title = models.CharField(max_length = 200)
    description =  models.TextField()
    long_description = models.TextField()

    def __str__(self):
        return self.Title
    

class Contact(models.Model):
    name = models.CharField(max_length = 200)
    country = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    message = models.TextField()
    phone_number = models.CharField(max_length = 15)
    years_of_trading_experience = models.CharField(max_length=3)
    parmas = models.CharField(max_length=300, null=True)
    def __str__(self):
        return f'{self.name}_{self.country}'


class Lead(models.Model):
    # this is for ekta ma'am 
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    outside_india =models.CharField(max_length = 200)
    whatsapp_number =models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    years_of_trading_experience = models.CharField(max_length=3)
    date_of_joined  = models.CharField(max_length=20, default =current_date)
    parmas = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.date_of_joined}'








class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_author = models.CharField(max_length=100)
    course_price = models.DecimalField(max_digits=10, decimal_places=2)
    course_poster = models.ImageField(upload_to='course_posters/')
    about_company =  models.TextField()
    about_instructor = models.TextField()
    whatsapp_number = models.CharField(max_length=20, blank=True, null=True)
    whatsapp_link = models.URLField(blank=True, null=True)
    paytment_link = models.URLField(blank=True, null=True)
    def __str__(self) :
        return self.course_name


class ProgramDetail(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='program_details')
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField( blank=True, null=True)
    def __str__(self) :
        return self.title



class FAQ(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='faqs')
    title = models.CharField(max_length=100)
    description = models.TextField( blank=True, null=True)
    def __str__(self) :
        return self.title

class List(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lists')
    title = models.CharField(max_length=1000)
    def __str__(self) :
        return self.title











class Webinar(models.Model):
    webinar_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='webinar')
    category = models.CharField(max_length=50)
    description = models.TextField()
    time = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    price = models.CharField(max_length=5)
    Author_name = models.CharField(max_length= 30)
    
    about_instructor = models.TextField()

    def __str__(self):
        return self.webinar_name


class What_you_learn(models.Model):
    content = models.TextField()
    webinar = models.ForeignKey(Webinar, related_name='What_you_learn', on_delete=models.CASCADE)
    def __str__(self):
        return self.content


class ThisClassFor(models.Model):
    content = models.TextField()
    webinar = models.ForeignKey(Webinar, related_name='this_class_for', on_delete=models.CASCADE)
    def __str__(self):
        return self.content







class courseRegisteration(models.Model):
    course_name = models.CharField(max_length= 500)
    course_time = models.CharField(max_length=20, default =current_date)
    course_author = models.CharField(max_length=20, default ='not able to get')
    full_name = models.CharField(max_length = 100)
    email_address = models.CharField(max_length=150)
    phone_number  = models.CharField(max_length = 15)
    city = models.CharField(max_length = 100)
    years_of_trading_experience = models.CharField(max_length=3)
    date_of_registeration = models.CharField(max_length=20, default =current_date)
    parmas = models.CharField(max_length=300, default = '')
    
    def __str__(self):
        return self.parmas