from constants import *
def start(update,context):
    user_id = update.message.chat_id
    context.bot.send_message(text = 'Привет' , chat_id = user_id)

def answ(update , context) :
    user_id = update.message.chat_id
    ans = update.message.text
    ans1 = A_DCT.get(1)
    ans2 = A_DCT.get(2)
    quest1 = B_DCT.get(1)
    quest2 = B_DCT.get(2)
    if ans in ans1 :
        index = ans1.index(ans)
        context.bot.send_message(text=ans2[index], chat_id=user_id)
    elif ans in quest1  :
        index = quest1.index(ans)
        context.bot.send_message(text=quest2[index], chat_id=user_id)