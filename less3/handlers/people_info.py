from aiogram import types, F, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.male_keyboards import male_keyboards

router = Router()

male = ["мужчина","женщина"]
age = ["больше 50","меньше 50","мне 50"]

class ChoiceMaleNames(StatesGroup):
    choice_male = State()
    choice_age = State()

@router.message(Command('male'))
async def chosen_male(message: types.Message, state: FSMContext):
    name = message.chat.first_name
    await message.answer(
        f'Привет, {name}, '
        f'Какой твой пол?', reply_markup=male_keyboards(male)
    )
    await state.set_state(ChoiceMaleNames.choice_male)


@router.message(ChoiceMaleNames.choice_male, F.text.in_(male ))
async def cmd_chosen_male(message: types.Message, state: FSMContext):
    await state.update_data(chosen_male=message.text.lower())
    await message.answer(
        f'А сколько тебе лет? ',
        reply_markup=male_keyboards(age)
    )
    await state.set_state(ChoiceMaleNames.choice_age)

@router.message(ChoiceMaleNames.choice_male)
async def cmd_chosen_male_incorrectly(message: types.Message):
    await message.answer(
        f'Я не знаю такого пола',
        reply_markup=male_keyboards(male)
    )


@router.message(ChoiceMaleNames.choice_age, F.text.in_(age))
async def age_chosen(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    if message.text.lower() == 'мне 50':
        await message.answer(f'Вы {user_data.get("chosen_male")} и Вам 50 лет',
        reply_markup = types.ReplyKeyboardRemove()
        )

    else:
        await message.answer(
        f'Ваш возраст составляет {message.text.lower()}. Вы {user_data.get("chosen_male")} ',
        reply_markup=types.ReplyKeyboardRemove()
        )
    await state.clear()

@router.message(ChoiceMaleNames.choice_age)
async def age_chosen_incorrectly(message: types.Message):
    await message.answer(
        f'Я не знаю такого возраста',
        reply_markup=male_keyboards(age)
    )