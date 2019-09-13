*******************************************************
prerequisite:
1) install python3.6
2) install django (pip install Django==2.2)
3) install requests (pip install requests==2.22.0)

unzip the "exercise.zip".
for showing the implementation run the below command from the command line.
>>python manage.py makemigrations
>>python manage.py migrate
>>python manage.py runserver


Short description of implementation:

Here I have tried to impement as provided practice document.
- Consume the existing API
- create a simple view and landing page in django
- trnaslate/interlization the view content.
- here is two language supported one is bangal and another is english.
- you can select the language for translate the view.

********************************************************


########################################
optional It may need
Interlization procedure:
have to install gettext tool for development or local environment.

In OS X (assuming you have homebrew installed:
$ brew install gettext
$ brew link gettext --force

In Ubuntu:
sudo get-apt gettext

windows:
https://docs.djangoproject.com/en/2.2/topics/i18n/translation/#gettext-on-windows
https://mlocati.github.io/articles/gettext-iconv-windows.html
#######################################