# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL сервиса
import configuration

# Импорт библиотеки requests для выполнения HTTP-запросов
import requests

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data


# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

response = post_new_user(data.user_body);
print(response.status_code)
print(response.json())


def get_users_table(body):
    return requests.post(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH,json=body, headers=data.headers)
response = get_users_table(data.user_body);
print(response.status_code)
print(response.json())