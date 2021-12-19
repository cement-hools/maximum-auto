# maximum-auto
Скрипт запрашивает отчет на сервере и сохраняет ответ в файле.

## stack
- python 3.8
- requests
- load_dotenv

## Запуск
1. Клонировать репозиторий
    ```
    git clone https://github.com/cement-hools/maximum-auto
    ```
2. Перейдите в директорию maximum-auto
    ```
   cd maximum-auto
    ```
3. Заполните переменные окружения в файле .env
   ```
   TOKEN=""
   URL="https://analytics.maximum-auto.ru/vacancy-test/api/v0.1"
   ```
4. Создать виртуальное окружение, активировать и установить зависимости
    ``` 
   python -m venv venv
    ```
   Варианты активации окружения:
   - windows ```. venv/Scripts/activate ```
   - linux ```source venv/bin/activate ```
     <br><br>
   ```
   python -m pip install -U pip
   ```
   ```
   pip install -r requirements.txt
   ```
5. Запустить скрипт
   ```
   python report.py
   ```
6. Остановить скрипт. Нажать на клавиатуре сочетание клавиш.
   ```
   ctrl + c
   ```