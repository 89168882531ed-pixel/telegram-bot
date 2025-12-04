import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils import executor

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# ---------- КЛАВИАТУРЫ ----------

main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.add("⭐ Полезные ссылки")
main_kb.add("📄 Чек-листы ДМС")
main_kb.add("📊 Исследование дозвонов")

links_kb = ReplyKeyboardMarkup(resize_keyboard=True)
links_kb.add("🔗 BestDoc")
links_kb.add("💬 Отзывы")
links_kb.add("⬅️ Назад")

checklists_kb = ReplyKeyboardMarkup(resize_keyboard=True)
checklists_kb.add("📘 Раздел 1")
checklists_kb.add("📗 Раздел 2")
checklists_kb.add("📙 Раздел 3")
checklists_kb.add("📕 Раздел 4")
checklists_kb.add("⬅️ Назад")

research_kb = ReplyKeyboardMarkup(resize_keyboard=True)
research_kb.add("📊 Скачать PDF")
research_kb.add("⬅️ Назад")

# ---------- ОБРАБОТЧИКИ ----------

@dp.message_handler(commands=["start", "menu"])
async def send_menu(message: types.Message):
    await message.answer("Выберите раздел:", reply_markup=main_kb)

@dp.message_handler(lambda m: m.text == "⬅️ Назад")
async def back(message: types.Message):
    await message.answer("Главное меню:", reply_markup=main_kb)

# ---- Полезные ссылки ----
@dp.message_handler(lambda m: m.text == "⭐ Полезные ссылки")
async def show_links(message: types.Message):
    await message.answer("Полезные ссылки:", reply_markup=links_kb)

@dp.message_handler(lambda m: m.text == "🔗 BestDoc")
async def send_bestdoc(message: types.Message):
    await message.answer("🔗 BestDoc:\nhttps://dms.iicon.ru/bestdoc")

@dp.message_handler(lambda m: m.text == "💬 Отзывы")
async def send_reviews(message: types.Message):
    await message.answer("💬 Отзывы:\nhttps://dms.iicon.ru/otzyvydms")

# ---- Исследование ----
@dp.message_handler(lambda m: m.text == "📊 Исследование дозвонов")
async def send_research_menu(message: types.Message):
    await message.answer("Исследование:", reply_markup=research_kb)

@dp.message_handler(lambda m: m.text == "📊 Скачать PDF")
async def send_pdf(message: types.Message):
    file_path = "files/research.pdf"
    await message.answer_document(open(file_path, "rb"))

# ---- Чек-листы ----
@dp.message_handler(lambda m: m.text == "📄 Чек-листы ДМС")
async def show_checklists(message: types.Message):
    await message.answer("Выберите раздел:", reply_markup=checklists_kb)

@dp.message_handler(lambda m: m.text == "📘 Раздел 1")
async def send_section1(message: types.Message):
    await message.answer(
        "📘 Раздел 1:\n"
        "1) https://docs.google.com/document/d/14BRik5mPhi4jA8B-24Bji0qcLK22YivCjodC0N4EXIg/edit\n"
        "2) https://docs.google.com/document/d/1IOLmYoBWkQEBrTC25GasGEH87e4zJb8G9BKOn-_fb9o/edit\n"
        "3) https://docs.google.com/document/d/15F11EFKvT4eOHVSiw6j-1H32cp38yxLpUvZFgtktwI0/edit"
    )

@dp.message_handler(lambda m: m.text == "📗 Раздел 2")
async def send_section2(message: types.Message):
    await message.answer(
        "📗 Раздел 2:\n"
        "1) https://docs.google.com/document/d/1agIrGH29kzF6uh-1jvRRNhCCTz2WT6U4bcMdxeWv07w/edit\n"
        "2) https://docs.google.com/document/d/1ZqygIPSaTwiHqNJnBOpp28cYgqZpvwXXMqC2YDDguXE/edit\n"
        "3) https://docs.google.com/document/d/1tApHI1hC-jHo7YX1NhFf-rQBOJKnkporT65573mAk-A/edit"
    )

@dp.message_handler(lambda m: m.text == "📙 Раздел 3")
async def send_section3(message: types.Message):
    await message.answer(
        "📙 Раздел 3:\n"
        "1) https://docs.google.com/document/d/1IV7WiirJz0tPAAHLLt4xjDQMJf6eY-CHA0fdBY6jSgg/edit\n"
        "2) https://docs.google.com/document/d/1DMLV0Cm8oEwdepdG9lIt7i4AE_oandr3gs24_H_OFJ0/edit\n"
        "3) https://docs.google.com/document/d/1S0ZAvFXkDfAzcGYy9iL0-3I4gTbdEww_AozEe37_xy0/edit"
    )

@dp.message_handler(lambda m: m.text == "📕 Раздел 4")
async def send_section4(message: types.Message):
    await message.answer(
        "📕 Раздел 4:\n"
        "1) https://docs.google.com/document/d/1E_JZzmqSg1DnSt961EHDEDtOwQoBYYnKyf79M9OelmQ/edit\n"
        "2) https://docs.google.com/document/d/1EwMiPOsfEhYHtU79JBHKXRBKLQZ38lvWWbkJl2DP0qY/edit\n"
        "3) https://docs.google.com/document/d/1s5dSgA8mf42hIKux1w7B9oo7bBFs9-Tdgg5t4wcRlt8/edit"
    )

# ---------- СТАРТ ----------
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
