import requests


def post_cake(payload):
    url = 'http://127.0.0.1:8000/cake/'
    response = requests.post(url, params=payload)
    response.raise_for_status()

    return response.json()


# в джанго можно сделать их методами класса Order
def create_order(order_info: dict) -> Order:
    '''обработчик для оформления заказа'''
    pass


def update_order(order_id: int, order_info: dict) -> Order:
    pass


def get_orders(user_id: int) -> list[Order]:
    '''обработчик для ветки "повторить заказ"'''
    pass


def get_current_orders(user_id: int) -> list[Order]:
    '''обработчик для ветки "где мой заказ"'''
    pass

# в джанго можно сделать их методами класса Cake
def get_catalog_cakes() -> list[Cake]:
    '''обработчик для ветки "каталог"'''
    pass


def get_random_cake() -> Cake:
    '''обработчик для ветки "Удиви меня"'''
    pass


def create_cake(cake_info: dict) -> Cake:
    '''обработчик для ветки "Создать торт"'''


def create_user(user_info: dict) -> User:
    pass


def update_user(user_info: dict) -> User:
    pass
