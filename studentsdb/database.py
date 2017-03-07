# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, '..', 'db.sqlite3'),
    # }
   # 'default': {
    #    'ENGINE': 'django.db.backends.postgresql_psycopg2',
     #   'NAME': 'mydb1',
      #  'USER': 'oleh1',
       # 'PASSWORD': '0000',
       # 'HOST': 'localhost',
       # 'PORT': '',
    #}
    'default': {
      'ENGINE': 'django.db.backends.mysql',
      'HOST': 'localhost',
      'USER': 'students_db_user',
      'PASSWORD': '0000',
      'NAME': 'students_db',
    }
}

