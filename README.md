# Four APIs of Django project and MySQL

This project is implemented based on Django basic project.

## Version Information
* python 3.7
* Django 3.2
* MySQL 8.0.34

## MySQL Structure
|column_name | type| key|
| ------------- |:-------------:|:-------------:|
|date        | date| primary|
|title       | varchar(45)|  |
|content     | longtest|  |
|tags        | json|  |

## Steps to Use APIs
1. Install MySQL 8.0.34 [download from MySQL website](https://cdn.mysql.com//Downloads/MySQLInstaller/mysql-installer-community-8.0.34.0.msi)
2. Use commend to create user, in this project I set the ```username="root", password="1234567"```. If want to use other username or password, please remember to modify the seting in `DATABASES` variable.
3. Clone the respository and navigate to the respository directory.
4. Navigate to `db_dump` folder to import database with commend ```musql -u [username] -p articles < *.sql```, then go back.
5. Use commend ```pip install -r requirements.txt```
6. Use commend 
	```
	python manage.py migrate
	python manage.py runserver
	``` 
7. Get the JWT token first. I have set the superuser, `username="user1"`, `password="a135791a"`
```POST http://localhost:8000/api/token/```

![Token.](/img/token.png "Token.")

use "access" token

8. API usage
* In the following, put the token get in step 6 in Header tab. 
```
KEY="Authorization"
VALUE="Bearer [token]"
```
![Auth.](/img/auth.png "Auth.")

* API- add an article

```POST http://localhost:8000/api/articles/create/```

put the columns `date`, `title`, `content`, `tags` in form-data 
![Create.](/img/create.png "Create.")
* API - delete and article
delete the article by date
```DELETE http://localhost:8000/api/articles/delete/```

put the `date` in Params

![Delete.](/img/delete.png "Delete.")
* API - modify the article
search the update article by `date`, and modify the row by `update_date`. 
```PUT http://localhost:8000/api/articles/update/```

![Modify.](/img/modify.png "Modify.")

* API - retrieve the content of article
get the article by `date`.
```GET http://localhost:8000/api/articles/retrieve/```

![Retrieve.](/img/retrieve.png "Retrieve.")

## Docker test
I tried two methods to build docker, each method both build through docker in Win10 and docker in Ubuntu 22.04.3 but both failed. The two methods are both failed in MySQL connection.
1. (In `./docker1/`) In this case, I tried to create two containers, one is python container to run the Django project, the other one is MySQL container to have MySQL database. When start the container using docker compose, it will also start the MySQL service through the entrypoint.sh script defined in the web service.  
* docker build 
```
cp ./docker1/* .
docker compose build 
```
* docker usage
```
docker compose up
```

2. (In `./docker2`) In this case, I built an ubuntu docker image with python 3.7 and MySQL in it.
* docker build 
```
cp ./docker2/* .
docker build -t my-django-app . 
```
* docker usage
```
docker run -t --name django-app-container -p 8000:8000 my-django-app
```