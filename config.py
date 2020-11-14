from aiogram import types

TOKEN = '1461857485:AAHl4bmhq3f3rjdewQZoKWD5RVtdd3EZ-PI'
API_URL = 'localhost:8000/'
PLACE_ID_URL = 'https://www.google.com/maps/search/?api=1&query=Eiffel%20Tower&query_place_id='
messages = {
    'hello': """Привет это бот HolidayApp. Здесь вы можете найти места поблизости,
     где можно отдохнуть на свежем воздухе. Бот показывает только места схорошей погодой.""",
    'location': 'Выберите скрепку -> Геопозиция -> Выберите на карте место вокруг которого искать.',
    'none_location': 'Неверная локация, попробуйте еще раз.',
    'distance': 'Отправьте радиус поиска в метрах.',
    'error': 'Что-то пошло не так, попробуйте еще раз.',
    'places': 'Это места в радиусе, который вы указали, с хорошей погодой, где можно отдохнуть на свежем воздухе.',
    'what': 'Я вас не понял.'
}
start = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
find = types.KeyboardButton(text='Найти место')
start.add(find)
keyboards = {
    'start': start,
}
