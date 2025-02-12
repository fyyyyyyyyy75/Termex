from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

- مرحبـاً بـك عزيـزي {}
- فـي بـوت كود تيرمكس$بايروجرام التابع لحفرة 🇹🇷

- يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه للحصـول على كـود تيرمكـس والبايروجرام تم انشـاء هـذا البـوت بواسطـة : @D_racon
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("- بدأ استخراج الكود", callback_data="generate")],
        [InlineKeyboardButton(text=" الرجوع للرئيسية ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("- بدأ استخراج الكود", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("- بدأ الاستخراج الكود", callback_data="generate")],
        [InlineKeyboardButton("- قناة السورس", url="https://t.me/D_racon")],
        [
            InlineKeyboardButton("- كيف تستخدمني ?", callback_data="help"),
            InlineKeyboardButton("- حول ", callback_data="about")
        ],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - حول البوت
/help - لتسوي روحك كلشي متعرف
/start - حتى تشغل البوا
/generate - حتى تبدا بأستخراج البوت
/cancel - لألغاء الاستخراج
/restart - اعادة تشغيل البوت
"""

    # About Message
    ABOUT = """
- حـول البـوت . 

- بـوت استخـراج كـود تيرمكـس خـاص بســورس جيبثون
- قنـاة السـورس : @D_racon

- المطور : @a_bd80 .

- لغـة البـوت : بـايثـون .
    """
