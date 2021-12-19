import datetime
import os
import time

import requests
from dotenv import load_dotenv
from requests import Response

load_dotenv()

TOKEN = os.environ.get('TOKEN')
HEADERS = {'Authorization': f'Bearer {TOKEN}'}

URL = os.environ.get('URL')

VALUE_DICT = {}

ID_TO_GET = set()
ID_REMOVE_FROM_GET = set()


def get(report_id: int) -> None:
    """
    GET запрос к серверу.
    Если ответ 'Отчет готов'(200) вызывает функцию сохранения отчета.

    :param report_id: id отчета.
    :return: None
    """
    url = f'{URL}/reports/{report_id}'
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        value = response.json().get('value')
        VALUE_DICT[report_id]['value'] = value

        save_to_file(report_id)
        # для исключения из множества ID_TO_GET
        ID_REMOVE_FROM_GET.add(report_id)


def post(report_id: int) -> Response:
    """
    POST запрос к серверу.

    :param report_id: id отчета.
    :return: Объект ответа Response
    """
    url = f'{URL}/reports'
    report_id = str(report_id)
    response = requests.post(url, headers=HEADERS, json={'id': report_id})
    return response


def save_to_file(report_id: int) -> None:
    """
    Сохраняет готовый отчет в файл 'results.csv'
    и выводит сообщение об успешном сохранении записи.

    :param report_id: id отчета.
    :return: None
    """
    report_data = VALUE_DICT.pop(report_id)

    date_time = report_data.get('date_time')
    value = report_data.get('value')

    with open('results.csv', 'a+') as f:
        row = f'{date_time},{report_id},{value}\n'
        f.write(row)
        print('Добавлена запись:', row[:-1])


def main():
    global ID_TO_GET
    global ID_REMOVE_FROM_GET

    input('Нажмите "ENTER" для старта')

    print('Старт')
    report_id = 1

    try:
        while True:
            ID_TO_GET = ID_TO_GET - ID_REMOVE_FROM_GET

            response = post(report_id)

            if response.status_code == 401:
                print('Авторизация не пройдена.')
                break

            if response.status_code in {201, 409}:

                if response.status_code == 201:
                    date_time = datetime.datetime.now().timestamp()
                    VALUE_DICT[report_id] = {'date_time': date_time, 'value': 0}
                    ID_TO_GET.add(report_id)

                report_id += 1

            for id in ID_TO_GET:
                get(id)

            time.sleep(1)
    except KeyboardInterrupt:
        print('Остановлен с клавиатуры')
    finally:
        print('Конец')


if __name__ == '__main__':
    main()
