# MailingService

This is Project for candidate testing task.
Authentication is applied even if it is not mentioned on task
Authentication is the most important and default feature of any kind of web application.

First of all, create python virtual environment:
python -m venv venv

On linux:
source venv/bin/activate

On windows:
.\venv\Scripts\activate

Install all required packages with following command:
pip install -r requirements.txt

manage operations like migrations:
python manage.py makemigrations
python manage.py migrate


In the directory called Redis there is redis executable installer for windows if 
you are windows user, if you are linux user and love pinguins, just type this command:

sudo apt install redis-server
sudo systemctl start redis
sudo systemctl enable redis

to check redis status:
sudo systemctl status redis

Type "celery" to check if celery is installed

Add Redis environment variable to PATH
On linux:
export PATH=$PATH:/path/to/directory

On windows:
$env:Path += ";C:\Program Files\Redis\" # Where your Redis root directory is located

run these two commands to start project:
python manage.py runserver
celery -A config.celery worker --pool=solo -l info



API Usage:
in the docs/ there is a nice user friendly swagger UI which allows to easily make requests

