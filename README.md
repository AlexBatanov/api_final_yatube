![Изображение](https://yastatic.net/q/logoaas/v2/Практикум.svg?color=fff)

## API - сервис Yatube

### О проекте:

Полноценный Api для блогерской платформы, включает в себя следующий функционал:
* регистрация пользователя
* создание, редактирование, удаление, постов
* создание, удаление, редактирование комментариев
* подписка, отписка на других пользователей
* просмотр комментариев, постов, постов выбранных груп или авторов

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
Открыть документацию:

```
http://127.0.0.1:8000/redoc/
```

### Примеры запросов:


все посты:

```
GET http://127.0.0.1:8000/api/v1/posts/
```
вернет ответ в формате JSON:
```
[
    {
        "id": 1,
        "text": "string",
        "pub_date": "2023-03-05T13:48:46.937935Z",
        "author": "author",
        "group": 1
    },
    {
        "id": 2,
        "text": "string",
        "pub_date": "2023-03-05T17:07:04.786442Z",
        "author": "author",
        "group": 0
    },
]
```

создание поста:

```
POST http://127.0.0.1:8000/api/v1/posts/
```
тело запроса:
```
{
    "text": "string",
    "image": "string",
    "group": 0
}
```

создание комментария:

```
POST http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```
тело запроса:
```
{
    "text": "string"
}
```

изменение комментария:

```
PUTCH http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
```
тело запроса:
```
{
    "text": "string"
}
```

