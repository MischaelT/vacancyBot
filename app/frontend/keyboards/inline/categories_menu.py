

# menu_cd = CallbackData('show_menu','level', 'category')

async def make_callback_data(level, category = '0'):
    return menu_cd.new(level = level, category = category)



async def settings_keyboard():
    pass