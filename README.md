# H20IQ

### Version
1.0.0

### Installation and Setup

NOTE

We use virtualenv along with virtualenvwrapper in order to keep our python development environment clean and neat. 

See http://docs.python-guide.org/en/latest/dev/virtualenvs/ for a brief introduction to virtual environments.

END NOTE

Actual Installation:

* Install Python 3.x.x
* Install virtualenv and virtualenvwrapper
* In a terminal window:
    ```sh
    $ cd root/for/H2OIQ
    $ git clone (repo address)
    $ mkvirtualenv H2OIQ
    $ workon H2OIQ
    $ cd H20IQ
    $ pip install -r Environment_Requirements.txt
    $ H20IQ> python manage.py migrate
    $ H20IQ> python manage.py createsuperuser
    ```
* Follow the prompts
