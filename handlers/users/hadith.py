from aiogram.types import Message
from loader import dp
from random import choice
import requests

@dp.message_handler(text='Sahih al Bukhari')
async def send_random_hadith(message: Message):
    api_url = 'https://cdn.jsdelivr.net/gh/fawazahmed0/hadith-api@1/editions/eng-bukhari.json'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        hadiths = data.get('hadiths', [])

        if hadiths:
            random_hadith = choice(hadiths)
            hadith_number = random_hadith.get('hadithnumber')
            hadith_text = random_hadith.get('text')

            await message.reply(f'<b>Total hadiths:</b> {len(hadiths)}\n<b>Random Hadith Number:</b> {hadith_number}')
            await message.reply(f"<b>{hadith_text}</b>")
        else:
            await message.reply('No hadiths found in the response.')
    else:
        await message.reply('Error fetching data from the API.')


@dp.message_handler(text='Sunan Abu Dawud')
async def send_random_hadith(message: Message):
    api_url = 'https://cdn.jsdelivr.net/gh/fawazahmed0/hadith-api@1/editions/eng-abudawud.json'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        hadiths = data.get('hadiths', [])

        if hadiths:
            random_hadith = choice(hadiths)
            hadith_number = random_hadith.get('hadithnumber')
            hadith_text = random_hadith.get('text')

            await message.reply(f'<b>Total hadiths:</b> {len(hadiths)}\n<b>Random Hadith Number:</b> {hadith_number}')
            await message.reply(f"<b>{hadith_text}</b>")
        else:
            await message.reply('No hadiths found in the response.')
    else:
        await message.reply('Error fetching data from the API.')


@dp.message_handler(text='Sunan ibn Majah')
async def send_random_hadith(message: Message):
    api_url = 'https://cdn.jsdelivr.net/gh/fawazahmed0/hadith-api@1/editions/eng-ibnmajah.json'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        hadiths = data.get('hadiths', [])

        if hadiths:
            random_hadith = choice(hadiths)
            hadith_number = random_hadith.get('hadithnumber')
            hadith_text = random_hadith.get('text')

            await message.reply(f'<b>Total hadiths:</b> {len(hadiths)}\n<b>Random Hadith Number:</b> {hadith_number}')
            await message.reply(f"<b>{hadith_text}</b>")
        else:
            await message.reply('No hadiths found in the response.')
    else:
        await message.reply('Error fetching data from the API.')


@dp.message_handler(text='Muwatta Malik')
async def send_random_hadith(message: Message):
    api_url = 'https://cdn.jsdelivr.net/gh/fawazahmed0/hadith-api@1/editions/eng-malik.json'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        hadiths = data.get('hadiths', [])

        if hadiths:
            random_hadith = choice(hadiths)
            hadith_number = random_hadith.get('hadithnumber')
            hadith_text = random_hadith.get('text')

            await message.reply(f'<b>Total hadiths:</b> {len(hadiths)}\n<b>Random Hadith Number:</b> {hadith_number}')
            await message.reply(f"<b>{hadith_text}</b>")
        else:
            await message.reply('No hadiths found in the response.')
    else:
        await message.reply('Error fetching data from the API.')


@dp.message_handler(text='Sahih Muslim')
async def send_random_hadith(message: Message):
    api_url = 'https://cdn.jsdelivr.net/gh/fawazahmed0/hadith-api@1/editions/eng-muslim.json'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        hadiths = data.get('hadiths', [])

        if hadiths:
            random_hadith = choice(hadiths)
            hadith_number = random_hadith.get('hadithnumber')
            hadith_text = random_hadith.get('text')

            await message.reply(f'<b>Total hadiths:</b> {len(hadiths)}\n<b>Random Hadith Number:</b> {hadith_number}')
            await message.reply(f"<b>{hadith_text}</b>")
        else:
            await message.reply('No hadiths found in the response.')
    else:
        await message.reply('Error fetching data from the API.')


@dp.message_handler(text='Sunan an Nasai')
async def send_random_hadith(message: Message):
    api_url = 'https://cdn.jsdelivr.net/gh/fawazahmed0/hadith-api@1/editions/eng-nasai.json'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        hadiths = data.get('hadiths', [])

        if hadiths:
            random_hadith = choice(hadiths)
            hadith_number = random_hadith.get('hadithnumber')
            hadith_text = random_hadith.get('text')

            await message.reply(f'<b>Total hadiths:</b> {len(hadiths)}\n<b>Random Hadith Number:</b> {hadith_number}')
            await message.reply(f"<b>{hadith_text}</b>")
        else:
            await message.reply('No hadiths found in the response.')
    else:
        await message.reply('Error fetching data from the API.')


@dp.message_handler(text='Jami At Tirmidhi')
async def send_random_hadith(message: Message):
    api_url = 'https://cdn.jsdelivr.net/gh/fawazahmed0/hadith-api@1/editions/eng-tirmidhi.json'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        hadiths = data.get('hadiths', [])

        if hadiths:
            random_hadith = choice(hadiths)
            hadith_number = random_hadith.get('hadithnumber')
            hadith_text = random_hadith.get('text')

            await message.reply(f'<b>Total hadiths:</b> {len(hadiths)}\n<b>Random Hadith Number:</b> {hadith_number}')
            await message.reply(f"<b>{hadith_text}</b>")
        else:
            await message.reply('No hadiths found in the response.')
    else:
        await message.reply('Error fetching data from the API.')

