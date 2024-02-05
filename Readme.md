***Сервис почтовых рассылок сообщений ***

1) Установить зависимости pip install -r requirements.txt
2) Создать базу данных postgres
3) Создать файл .env в корневой папке проекта
4) После настройки применить миграции python manage.py migrate
5) Создание суперпользователя python manage.py csu (в файле csu.py прописать данные для суперпользователя)
6) Для запуска apscheduler  python manage.py runapscheduler (автоматическая рассылка сообщений)

Для подключения к базе данных PostgreSQL, необходимо создать переменную среды пользователя "USER_POSTGRES" - имя
пользователя и "DB_PASS" - пароль для
пользователя "USER_POSTGRES" от БД PostgresSQL.

Для настройки отправки сообщений на почту необходимо создать переменные среды пользователя:

* EMAIL_HOST_USER = os.getenv('YANDEX_MAIL') (YANDEX_MAIL - адрес почты с которой ведется рассылка)
* EMAIL_HOST_PASSWORD = os.getenv('MAIL_PASSWORD') (MAIL_PASSWORD - пароль от почты)

Так же 'SECRET_KEY' для Django. 

Все это нужно записать в созданный в корневой папке файл .env

Для запуска apscheduler  python manage.py runapscheduler (автоматическая рассылка сообщений)

