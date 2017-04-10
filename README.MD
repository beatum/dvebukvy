# TEST CASE / FOR DVEBUKVY

This project is scaffolded by Ivan Semernyakov <direct@beatum-group.ru>

## Architecture

Tested on:

* Ubuntu 14.04
* PostgreSQL 9.6.1

## Usage

#### Clone project:
```
$ mkdir testproject && cd $_
$ git clone https://github.com/beatum/dvebukvy.git
```

#### Initialize ```virtualenv``` if needed:
```
$ virtualenv {path}
```

#### Activate ```virtualenv```:
```
$ source {virtualenv_path}/bin/activate
```

#### Install ```pip``` dependencies using ```./requirements.txt``` they are not already installed:
```
$ cd project
$ pip install -r requirements.txt
```

#### Verify ```pip``` dependencies installed correctly under ```virtualenv```:
```
$ which django-admin.py
```

#### Configure PostgreSQL if needed:
```
$ sudo su postgres
$ createuser -P username
$ createdb --owner username dbname
$ exit
```

Check up settings.py !

#### Apply initial migration:
```
$ ./manage.py migrate
```

#### Collect Static
```
$ ./manage.py collectstatic
```

#### Create admin user:
```
$ ./manage.py createsuperuser
```

#### Parse data with scrapy!
```
$ scrapy runspider myspider.py -o items.json
```

#### Create new content with command:
```
$ ./manage.py make_content
```

#### Test dev environment.
```
$ ./manage.py runserver
```

Now you can go to the localhost:8000 and you should see "Hello, World!" - page.

### That's all! Good luck!

## License

This software is released under the [MIT License](http://opensource.org/licenses/MIT).

