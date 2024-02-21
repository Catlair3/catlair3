import asyncio
import logging


from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command, CommandObject
from aiogram.types import FSInputFile
from aiogram.utils.media_group import MediaGroupBuilder

logging.basicConfig(level=logging.INFO)

bot = Bot(token="7007429239:AAG-XUkGy2uDIEP7RFdHDg9vrEq5DE5eam0")

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message, command: CommandObject):
    if command.args is None:
        await message.answer('Привет')
        return
    else:
        await message.answer(f"Привет, {command.args}")
        return
@dp.message(Command('help'))
async def cmd_start(message: types.Message, command: CommandObject):
     await message.answer('start-Начало работы,\n help-команды,\n shd1- бойцы для столкновения на открытых картах,\nshd2-бойцы для столкновения на закрытых картах,\n brb-бойцы доя броубола,\n gem-бойцы доя захвата кристаллов,\n knk-бойцы для нокаута,\n grab-бойцы для ограбления,\n zah- бойцы для зачистки')
@dp.message(Command('shd1'))
async def cmd_start(message: types.Message):
    albom = MediaGroupBuilder(caption= 'Для таких карт, как: Озеро метвецовб штольня, Двойная проблема, Ветренная долина, затерянный источник. Подходят бойцы:')

    imagebot = FSInputFile('edgar.jpg.jpg')
    imagebot2 = FSInputFile('fang.jpg')
    imagebot3 = FSInputFile('мико.webp')
    albom.add_photo(media=imagebot)
    albom.add_photo(media=imagebot2)
    albom.add_photo(media=imagebot3)
    await message.answer_media_group(media=albom.build())


@dp.message(Command('shd2'))
async def cmd_start(message: types.Message):
    albom2 = MediaGroupBuilder(caption='Для карт: Галактика, Дрифт в дюнах,Убежище. Подходит боец:')

    imagebot4 = FSInputFile('шелли.jpg')

    albom2.add_photo(media=imagebot4)
    await message.answer_media_group(media=albom2.build())

@dp.message(Command('brb'))
async def cmd_start(message: types.Message):
    albom3 = MediaGroupBuilder(caption='Для броубола подходят бойцы:')
    image = FSInputFile('перл.webp')
    image2 = FSInputFile('вольт2.jpg')
    image3 = FSInputFile('мортис.jpg')
    albom3.add_photo(media=image)
    albom3.add_photo(media=image2)
    albom3.add_photo(media=image3)
    await message.answer_media_group(media= albom3.build())

@dp.message(Command('gem'))
async def cmd_start(message: types.Message):
    albom4 = MediaGroupBuilder(caption='Для захвата кристаллов подходят бойцы:')
    imagey = FSInputFile('l;tccb.jpg')
    imagey2 = FSInputFile('мортис.jpg')
    imagey3 = FSInputFile('тара.jpg')
    albom4.add_photo(media=imagey)
    albom4.add_photo(media=imagey2)
    albom4.add_photo(media=imagey3)
    await message.answer_media_group(media= albom4.build())

@dp.message(Command('grab'))
async def cmd_start(message: types.Message):
    albom6 = MediaGroupBuilder(caption='Для ограбления подходят бойцы:')
    imagey12 = FSInputFile('l;tccb.jpg')
    imagey212 = FSInputFile('барли.png')
    imagey312 = FSInputFile('пенни.jpg')
    albom6.add_photo(media=imagey12)
    albom6.add_photo(media=imagey212)
    albom6.add_photo(media=imagey312)
    await message.answer_media_group(media= albom6.build())

@dp.message(Command('grab'))
async def cmd_start(message: types.Message):
    albom6 = MediaGroupBuilder(caption='Для ограбления подходят бойцы:')
    imagey12 = FSInputFile('l;tccb.jpg')
    imagey212 = FSInputFile('барли.png')
    imagey312 = FSInputFile('пенни.jpg')
    albom6.add_photo(media=imagey12)
    albom6.add_photo(media=imagey212)
    albom6.add_photo(media=imagey312)
    await message.answer_media_group(media= albom6.build())
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())