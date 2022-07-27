# Ajax_PostService
1.Project's Title

Web application which contains input window and button submit where you can post any name to database. 

2.Project Description

Trying something different as second mind practice with my new skills in JS and Ajax and Django together.As ussual I send request by html input/submit or Django forms. At that time I combinate Ajax + Form Django for send post request to database. 

3.How to Install and Run the Project

To start our project in local server:

need make clone repo from git https://github.com/MoriartyJam/Ajax_PostService

pip install virtualenv

virtualenv venv -p python3.8

source venv/bin/activate

pip install -U -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver


4.How to Use the Project

On the start page, enter your name in the form and click the Submit button. After that we can see answer as JsonResponse with information message and your name if had success process or error massage if  something was wrong. 

