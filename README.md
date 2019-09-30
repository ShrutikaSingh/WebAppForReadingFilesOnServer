1. Select lightweight web server, which is fast, low footprint and simple (should work on ARM based IoT devices). Please provide pros and cons while compairing web server.

The config.txt file contain the python script for displaying the data from api  i.e from https://reqres.in/api/users
when we press the button the config.txt script will run and fetch the data from https://reqres.in/api/users

Requirements: python3, django, requests,

Step1:
        >> sudo apt-get install python3 python3-pip
        >> pip3 install Django
        >> sudo pip3 install requests

Step2:
      go to the scriptingApp Directory
      >> cd scriptingApp
step4:
      make migrations
      >> python3 manage.py migrate

Step3:
       now run the manage.py script
       >> python3 manage.py runserver

Step4:
        go to http://127.0.0.1:8000/

Step5:
        there is a button "press button to execute script"
        when we press the button the script of config.txt will be executed
        and the data from the api https://reqres.in/api/users will be displayed
