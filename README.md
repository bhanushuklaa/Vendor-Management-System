<h1>Project: Vendor Management System</h1>
<h3>
  1. To make a project Django Rest API we need to install some module......<br>
  2. pip install django
</h3>

<h3>
  1- Then we create our project using a django command: 
  <i>django-admin startproject projectName</i> <br>

  2- create a django app using command:
  <i>python manage.py startapp appName</i>
</h3>

<h2>
  Install the module of Django rest framework to create a different APIs
</h2>
<b>
  --> pip install djangorestframework
</b>
<h3>
  According to requirements: I had created a 3 models in models.py --> <br> <i>
    1. Vendor Model <br>
    2. Purchase Order (PO) Model <br>
    3. Historical Performance Model <br>
  </i>
</h3>

<p>
  Other requirements: <br>
  INSTALLED_APPS = [
    ...
    'rest_framework',
] <br>
  --> I had provided read only access to 3rd party user and CURD operation ca only perform by Admin <br>
  REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users. <br>
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
</p>

<h3>
  --> To access admin panel use the url : localhost:8000/admin/
  --> before running server i had to create first models in database using some commands: <br>
      1. python manage.py makemigrations <br>
      2. python manage.py migrate <br>
  then create admin id and password : <br>
  --> python manage.py createsuperuser <br> then run the server --> python manage.py runserver
</h3>

<h3>
  I have perfrom all the operations which are given in the assignment by #Fatmug Company <br><br>
      On-Time Delivery Rate: <br>
    ● Calculated each time a PO status changes to 'completed'. <br>
    ● Logic: Count the number of completed POs delivered on or before <br>
    delivery_date and divide by the total number of completed POs for that vendor. <br><br>
    Quality Rating Average: <br>
    ● Updated upon the completion of each PO where a quality_rating is provided. <br>
    ● Logic: Calculate the average of all quality_rating values for completed POs of 
    the vendor. <br><br>
    Average Response Time: <br>
    ● Calculated each time a PO is acknowledged by the vendor. <br>
    ● Logic: Compute the time difference between issue_date and
    acknowledgment_date for each PO, and then find the average of these times
    for all POs of the vendor. <br><br>
    Fulfilment Rate: <br>
    ● Calculated upon any change in PO status. <br>
    ● Logic: Divide the number of successfully fulfilled POs (status 'completed'
    without issues) by the total number of POs issued to the vendor. <br>
</h3>











