#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Anandpskerala


#Secret configs
from config import Config


def start(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hello [{update.message.from_user.first_name}](tg://user?id={update.message.from_user.id}) I am Bot Made By @ImortalKingTG. I can attach medias to your long text.100% Secure. Video Will Encrypted😮‍💨. Support Channel @TheSerialZone .", parse_mode="Markdown")
