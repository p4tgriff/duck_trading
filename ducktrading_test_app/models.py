from django.db import models
import re
import bcrypt


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 3:
            errors['first_name'] = "First name should be at least 3 characters."
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name should be at least 2 characters."
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # if not EMAIL_REGEX.match(postData['email_address']):
        #     errors['email_address'] = ("Invalid email address!")
        if len(postData['email_address']) == 0:
            errors['email_address'] = "You must enter an email"
        elif not EMAIL_REGEX.match(postData['email_address']):
            errors['email_address'] = "Must be a valid email"

        current_users = User.objects.filter(
            email_address=postData['email_address'])
        if len(current_users) > 0:
            errors['duplicate'] = "that email is already in use."

        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters long"
        if postData['password'] != postData['confirm_password']:
            errors['mismatch'] = "Your passwords do not match"

        return errors

    def login_validator(self, postData):
        errors = {}
        existing_user = User.objects.filter(
            email_address=postData['email_address'])
        print(existing_user)
        if len(postData['email_address']) == 0:
            errors['email_address'] = "Email must be entered"
        if len(postData['password']) < 8:
            errors['password'] = "An 8 character password must be entered"
        elif bcrypt.checkpw(postData['password'].encode(), existing_user[0].password.encode()) != True:
            errors['password'] = "email and password do not match"
        return errors


class User(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return '{} {}' .format(self.first_name, self.last_name)

    # def __str__(self):
    #     return self.first_name, self.last_name


class SecurityManager(models.Manager):
    def basic_validator2(self, postData):
        errors = {}
        if len(postData['ticker']) < 3:
            errors['ticker'] = "A tickery symbol must consist of at least 3 characters!"
        # if len(postData['description']) < 3:
        #     errors['description'] = "A description should be at least 3 characters!"
        # if len(postData['location']) < 3:
        #     errors['location'] = "Location should be at least 3 characters."
        return errors


class Security(models.Model):
    CATEGORY = (
        ('Large Cap', 'Large Cap'),
        ('Small Cap', 'Small Cap'),
        ('Growth', 'Growth'),
        ('Income', 'Income'),
    )

    company_name = models.CharField(max_length=255, null=True)
    ticker_symbol = models.CharField(max_length=5, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=255, null=True, choices=CATEGORY)
    # users = models.ManyToManyField(User, related_name="security")
    # user = models.ForeignKey(User, related_name="my_jobs", on_delete = models.CASCADE)
    # location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = SecurityManager()

    def __str__(self):
        return self.company_name


class Order(models.Model):

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    security = models.ForeignKey(
        Security, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(null=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BankAccount(models.Model):

    user = models.ForeignKey(
        User, related_name="accounts", on_delete=models.CASCADE)
    balance = models.DecimalField(
        default=200000.00, max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.user

    # def __init__(self, balance=200000):
    #     self.balance = balance

    # def deposit(self, amount):
    #     self.balance += amount
    #     return self

    # def withdraw(self, amount):
    #     if(amount <= self.balance):
    #         self.balance -= amount
    #     else:
    #         print("Insufficient funds: trade not placed")
    #         redirect('/sell')
    #     return self

    # def displayAccountInfo(self):
    #     print("Balance:", self.balance)
    #     return self
