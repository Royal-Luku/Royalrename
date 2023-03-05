"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
      **VIP** 
	Daily  Upload  limit unlimited
	Price Rs 100 🇮🇳
	
	Upi id :- ```adityakar052@paytm```
    
        After Payment Done Send Screen shot To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN",url = "https://t.me/OTT_Zone_Admin")], 
        			[InlineKeyboardButton("MOVIES CHANNEL",url = "https://t.me/worldofmovies8"),
        			InlineKeyboardButton("JOIN BACKUP",url = "https://t.me/Wombackup")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP** 
	Daily  Upload  limit unlimited
	Price Rs 100 🇮🇳
	
	Upi id :- ```adityakar052@paytm```
    
        After Payment Done Send Screen shot To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN",url = "https://t.me/OTT_Zone_Admin")], 
        			[InlineKeyboardButton("MOVIES CHANNEL",url = "https://t.me/worldofmovies8"),
        			InlineKeyboardButton("JOIN BACKUP",url = "https://t.me/Wombackup")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	
