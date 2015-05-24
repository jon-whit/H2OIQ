# H2OIQ

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
    $ cd H2OIQ
    $ H2OIQ> pip install django 
    $ H2OIQ> python manage.py migrate
    $ H2OIQ> python manage.py createsuperuser
    ```
* Follow the prompts


