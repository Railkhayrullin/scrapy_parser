# scrapy_parser

python 3.8

## Установка

В консоли переходим в папку для проекта и вводим команду клонирования репозитория

    git clone https://github.com/Railkhayrullin/scrapy_parser.git

Устанавливаем виртуальное окружение

    python3 -m venv .env

Активируем виртуальное окружение

    source .env/bin/activate

Устанавливаем зависимости

    pip install -r requirements.txt



## Запуск

Переходим в папку парсера

    cd site_parser

Запускаем парсер

    scrapy crawl news_spider

Команда запуска парсера с сохранением полученных данных в желаемом формате, например json

    scrapy crawl news_spider -o items.json

Полученные данные будут в файле items.json
