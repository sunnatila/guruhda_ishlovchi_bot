import io

from aiogram import types

from aiogram.dispatcher.filters import Command

from filters import GroupFilter, AdminFilter

from loader import dp, bot


@dp.message_handler(GroupFilter(), Command("set_photo", prefixes='!/@'), AdminFilter())
async def set_new_photo(msg: types.Message):
    source_message = msg.reply_to_message
    try:
        print(source_message.photo)
        photo = source_message.photo[-1]
        photo = await photo.download(destination=io.BytesIO())
        input_file = types.InputFile(photo)
        await msg.chat.set_photo(photo=input_file)
    except AttributeError:
        await msg.reply("Rasm ozgartirilmadi")


@dp.message_handler(GroupFilter(), Command("set_title", prefixes='!/@'), AdminFilter())
async def set_new_title(msg: types.Message):
    source_message = msg.reply_to_message
    title = source_message.text
    await bot.set_chat_title(msg.chat.id, title=title)


@dp.message_handler(GroupFilter(), Command("set_description", prefixes='!/@'), AdminFilter())
async def set_new_description(msg: types.Message):
    source_message = msg.reply_to_message
    description = source_message.text
    await msg.chat.set_description(description=description)




