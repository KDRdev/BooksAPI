# BooksAPI
A simple books API created using Django Python framework.

************************************************

After cloning the repository, configure your DB connection parameters: DB_HOST, DB_USER, DB_PASS, DB_NAME in books_api/settings.py file. 

**books_api/settings.py**
```C

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'DB_NAME',
        'HOST': 'DB_HOST',
        'USER': 'DB_USER',
        'PASSWORD': 'DB_PASSWORD',
    }
}

```

************************************************

Create a secret_settings.py file inside books_api directory and paste the secret key there.

**books_api/secret_settings.py**
``` C
    SECRET_KEY = 'MY_SECRET_KEY'
```

************************************************

Run the following command to create DB tables for your app.

```C
    python3 manage.py migrate
```

************************************************

Load the books or reviews file using one of the appropriate commands below.

``` C
    python3 manage.py load-books --path PATH_TO_BOOKS_FILE
    python3 manage.py load-reviews --path PATH_TO_REVIEWS_FILE
```

************************************************

Start the app server using the following command

``` C
    python3 manage.py runserver
```

************************************************

Go to http://localhost:8000 (or different address/port as per your configuration) and review the list of books added in the database and their reviews. Use "Filters" button to search for books (enter book title to find a book).
