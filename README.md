## API - сервис Yatube

### О проекте:

Полноценный Api для блогерской платформы, включает в себя следующий функционал:
*регистрация пользователя
*создание, редактирование, удаление, постов
*создание, удаление, редактирование комментариев
*подписка, отписка на других пользователей

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/AlexBatanov/api_final_yatube
```

```
cd yatube_api
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
