# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

1. Скачайте код

2. Установите зависимости с помощью pip:
    ```bash
    pip install -r requirements.txt
    ```
   
4. Переменные окружения:
 - Создайте файл .env в корне проекта.
 - Добавьте переменную EXCEL_WITH_WINES для указания пути к файлу Excel 
```bash 
EXCEL_WITH_WINES=your_file.lsx
```
   
5. Запустите скрипт:
 - Откройте терминал и выполните:
```bash
python3 main.py
```
6. Просмотр веб-страницы:
Откройте браузер и перейдите по адресу http://localhost:8000, чтобы увидеть сгенерированную страницу с коллекцией вин. Если все пункты выполнены вы увидите:
<img src="https://picloud.cc/i/e91b3d22c36747b853e5b99665204af6.png" alt="drawing" width="700"/>

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
