from aiogram.dispatcher.filters.state import StatesGroup, State

class Adder(StatesGroup):
    step1 = State()
    step2 = State()


class Deletr(StatesGroup):
    step1 = State()
    step2 = State()

