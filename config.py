from aiogram import types

TOKEN = '1461857485:AAHl4bmhq3f3rjdewQZoKWD5RVtdd3EZ-PI'
API_URL = 'localhost:8000/'
messages = {
    'hello': 'Привет это бот шашлыков',
    'location': 'Выберите скрепку -> Геопозиция -> Выберите на карте место вокруг которого искать',
    'none_location': 'Неверная локация, попробуйте еще раз',
    'distance': 'Отправьте радиус поиска в метрах',
    'error': 'Что-то пошло не так, попробуйте еще раз.'
}
start = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
find = types.KeyboardButton(text='Найти место')
start.add(find)
keyboards = {
    'start': start,
}
