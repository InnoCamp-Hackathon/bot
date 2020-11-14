import asyncio
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ContentType
import requests
from config import TOKEN, messages, keyboards, API_URL

loop = asyncio.get_event_loop()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

args = {
    'lon': None,
    'lat': None,
    'dist': None
}


@dp.message_handler(commands=['start'])
async def start_message(message):
    await bot.send_message(message.chat.id, messages['hello'], reply_markup=keyboards['start'])


@dp.message_handler(content_types=ContentType.LOCATION)
async def location(message):
    if message.location is not None:
        await bot.send_message(message.chat.id, messages['distance'])
        print(message.location)
        args['lon'] = message.location.longitude
        args['lat'] = message.location.latitude
    else:
        await bot.send_message(message.chat.id, messages['none_location'], reply_markup=keyboards['start'])


@dp.message_handler(content_types=ContentType.TEXT)
async def text(message):
    if message.text == 'Найти место':
        await bot.send_message(message.chat.id, messages['location'], reply_markup=keyboards['start'])

    elif message.text.isdigit():
        global args
        args['dist'] = message.text

        if all(args):
            locations = await get_locations(args)
            await bot.send_message(message.chat.id, locations)
        else:
            await bot.send_message(message.chat.id, messages['error'], reply_markup=keyboards['start'])

        args = {
            'lon': None,
            'lat': None,
            'dist': None
        }


    else:
        print(message)


async def get_locations(args):
    locs = requests.get(API_URL + f'api/get_location?lat={args["lat"]}&lon={args["lon"]}&r={args["dist"]}')

    return 0


if __name__ == '__main__':
    executor.start_polling(dp)
