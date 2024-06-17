import os
import discord
from discord.ext import commands
from discord import app_commands

from myserver import server_on

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

  # แทนที่ด้วย TOKEN ของคุณ
TARGET_CHANNEL_ID = 1245671140135796817  # เปลี่ยนเป็น ID ของช่องที่ต้องการ

@bot.event
async def on_ready():
    print("Bot online now!")
    synced = await bot.tree.sync()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # ตรวจสอบว่าข้อความมาจาก channel ที่ระบุหรือไม่
    if message.channel.id == TARGET_CHANNEL_ID:
        mes = message.content  # แปลงข้อความเป็นตัวพิมพ์เล็กและลบช่องว่าง
        if mes == "Peroxide":
            await message.channel.send("A game inspired by the anime Bleach.")
        elif mes == "Clan":
            await message.channel.send("Soul Reaper Clans , Hollow Clans , Quincy Clans , Fullbringer Clans")
        elif mes == "Soul Reaper Clans":
            await message.channel.send("""
                                       
                                       Common (89%)
Inoue - 5 Spirit
Hayanami – 5 Reiatsu
Mikazuki – 5 Agility
Rengoku – 5 Vitality
Kurosami – 5 Spirit
Uzumaki – 5 Strength
Akashi – 5 Reiatsu
Ken – 5 Spirit
Shen – 5 Agility
Saru – 10% better than Heath Regen (1.1x)
Kuroku – 10% better Reiatsu Regen (1.1x)
Lee – 10% Agility multiplier (1.1x)
Kaneki – 10% EXP Multiplier (1.1x)
Rare (9%)
Chad
20 Strength
20% better Health Regen (1.2x)
Kuchiki
15% Agility multiplier (1.15x)
20% Spirit multiplier (1.2x)
Abarai
15% Strength multiplier (1.15x)
20% Vitality multiplier (1.20x)
Shihouin
20% Agility multiplier (1.2x)
20% Strength multiplier (1.2x)
Legendary (2%)
Kurosaki
12% Vitality multiplier (1.12x)
13% Spirit multiplier (1.13x)
15% Reiatsu multiplier (1.15x)
12% better Reiatsu Regen (1.12x)
Getsuga Tenshou
Aizen
15% Spirit multiplier (1.15x)
13% Vitality multiplier (1.13x)
15% Reiatsu multiplier (1.15x)
10% better Health Regen (1.1x)
Hado 90
Zaraki
15% Strength multiplier (1.15x)
15% Vitality multiplier (1.15x)
10% better Reiatsu Regen (1.1x)
12% better Health Regen (1.12x)
Joy of Battle
Yamamoto
40% EXP multiplier (1.4x)
15% Strength multiplier (1.15x)
10% Agility multiplier (1.1x)
13% Vitality multiplier (1.13x)
15% Spirit multiplier (1.15x)
10% Reiatsu multiplier (1.1x)
10% better Reiatsu Regen (1.1x)
(This clan will not get an ability)   """)
        elif mes == "soul reaper clans":
            await message.channel.send("""
Common (89%)
Inoue - 5 Spirit
Hayanami – 5 Reiatsu
Mikazuki – 5 Agility
Rengoku – 5 Vitality
Kurosami – 5 Spirit
Uzumaki – 5 Strength
Akashi – 5 Reiatsu
Ken – 5 Spirit
Shen – 5 Agility
Saru – 10% better than Heath Regen (1.1x)
Kuroku – 10% better Reiatsu Regen (1.1x)
Lee – 10% Agility multiplier (1.1x)
Kaneki – 10% EXP Multiplier (1.1x)
Rare (9%)
Chad
20 Strength
20% better Health Regen (1.2x)
Kuchiki
15% Agility multiplier (1.15x)
20% Spirit multiplier (1.2x)
Abarai
15% Strength multiplier (1.15x)
20% Vitality multiplier (1.20x)
Shihouin
20% Agility multiplier (1.2x)
20% Strength multiplier (1.2x)
Legendary (2%)
Kurosaki
12% Vitality multiplier (1.12x)
13% Spirit multiplier (1.13x)
15% Reiatsu multiplier (1.15x)
12% better Reiatsu Regen (1.12x)
Getsuga Tenshou
Aizen
15% Spirit multiplier (1.15x)
13% Vitality multiplier (1.13x)
15% Reiatsu multiplier (1.15x)
10% better Health Regen (1.1x)
Hado 90
Zaraki
15% Strength multiplier (1.15x)
15% Vitality multiplier (1.15x)
10% better Reiatsu Regen (1.1x)
12% better Health Regen (1.12x)
Joy of Battle
Yamamoto
40% EXP multiplier (1.4x)
15% Strength multiplier (1.15x)
10% Agility multiplier (1.1x)
13% Vitality multiplier (1.13x)
15% Spirit multiplier (1.15x)
10% Reiatsu multiplier (1.1x)
10% better Reiatsu Regen (1.1x)
(This clan will not get an ability)   """)
        elif mes == "Soul Reaper Clan":
            await message.channel.send("""
                                       Common (89%)
Inoue - 5 Spirit
Hayanami – 5 Reiatsu
Mikazuki – 5 Agility
Rengoku – 5 Vitality
Kurosami – 5 Spirit
Uzumaki – 5 Strength
Akashi – 5 Reiatsu
Ken – 5 Spirit
Shen – 5 Agility
Saru – 10% better than Heath Regen (1.1x)
Kuroku – 10% better Reiatsu Regen (1.1x)
Lee – 10% Agility multiplier (1.1x)
Kaneki – 10% EXP Multiplier (1.1x)
Rare (9%)
Chad
20 Strength
20% better Health Regen (1.2x)
Kuchiki
15% Agility multiplier (1.15x)
20% Spirit multiplier (1.2x)
Abarai
15% Strength multiplier (1.15x)
20% Vitality multiplier (1.20x)
Shihouin
20% Agility multiplier (1.2x)
20% Strength multiplier (1.2x)
Legendary (2%)
Kurosaki
12% Vitality multiplier (1.12x)
13% Spirit multiplier (1.13x)
15% Reiatsu multiplier (1.15x)
12% better Reiatsu Regen (1.12x)
Getsuga Tenshou
Aizen
15% Spirit multiplier (1.15x)
13% Vitality multiplier (1.13x)
15% Reiatsu multiplier (1.15x)
10% better Health Regen (1.1x)
Hado 90
Zaraki
15% Strength multiplier (1.15x)
15% Vitality multiplier (1.15x)
10% better Reiatsu Regen (1.1x)
12% better Health Regen (1.12x)
Joy of Battle
Yamamoto
40% EXP multiplier (1.4x)
15% Strength multiplier (1.15x)
10% Agility multiplier (1.1x)
13% Vitality multiplier (1.13x)
15% Spirit multiplier (1.15x)
10% Reiatsu multiplier (1.1x)
10% better Reiatsu Regen (1.1x)
(This clan will not get an ability)   """)
        elif mes == "Hollow Clans":
            await message.channel.send("""
Common(89%)                                       
Pyximes Clan – 5 Spirit
Reddark Clan – 5 Reiatsu
Hollargo Clan – 5 Agility
Vriess Clan – 5 Vitality
Terges Clan – 5 Spirit
Grindella Clan – 5 Strength
Llargaller Clan – 5 Reiatsu
Roldullen Clan – 5 Spirit
Harrett Clan – 5 Agility
Gillilga Clan – 5% Agility multiplier (1.05x)
Tergeaux Clan – 5% better Health Regen (1.05x)
Weskullen Clan – 5% better Reiatsu Regen (1.05x)
Rare(9%)
Gilga
15% Strength multiplier (1.15x)
20% Vitality multiplier (1.2x)
Rureux
20% Agility multiplier (1.2x)
Arruruerie
15% Spirit multiplier (1.15x)
Harribel
15% Spirit multiplier (1.15x)
20% Vitality multiplier (1.2x)
Llargo
15% Strength multiplier (1.15x)
15% Reiatsu multiplier (1.15x)
15% Vitality multiplier (1.15x)
Legendary(2%)
Jaegerjaquez
15% Strength multiplier (1.15x)Desgarron
10% Agility multiplier (1.1x)
13% Vitality multiplier (1.13x)
Desgarron
Cifer
12% Agility multiplier (1.12x)LanzaDelRelampago
15% Spirit multiplier (1.15x)
15% Reiatsu multiplier (1.15x)
15% better Health Regen (1.15x)
Lanza del Relámpago
StarrkCeroMetralleta
15% Spirit multiplier (1.15x)
12% Reiatsu multiplier (1.12x)
13% better Reiatsu Regen (1.13x)
Cero Metralleta
Louisenbairn
40% EXP multiplier (1.4x)
15% Strength multiplier (1.15x)
10% Agility multiplier (1.1x)
13% Vitality multiplier (1.13x)
15% Spirit multiplier (1.15x)
10% Reiatsu multiplier (1.1x)
10% better Reiatsu Regen (1.1x)
(This clan will not get an ability)                                      
""")
        elif mes == "Hollow Clan":
            await message.channel.send("""Common(89%)                                       
Pyximes Clan – 5 Spirit
Reddark Clan – 5 Reiatsu
Hollargo Clan – 5 Agility
Vriess Clan – 5 Vitality
Terges Clan – 5 Spirit
Grindella Clan – 5 Strength
Llargaller Clan – 5 Reiatsu
Roldullen Clan – 5 Spirit
Harrett Clan – 5 Agility
Gillilga Clan – 5% Agility multiplier (1.05x)
Tergeaux Clan – 5% better Health Regen (1.05x)
Weskullen Clan – 5% better Reiatsu Regen (1.05x)
Rare(9%)
Gilga
15% Strength multiplier (1.15x)
20% Vitality multiplier (1.2x)
Rureux
20% Agility multiplier (1.2x)
Arruruerie
15% Spirit multiplier (1.15x)
Harribel
15% Spirit multiplier (1.15x)
20% Vitality multiplier (1.2x)
Llargo
15% Strength multiplier (1.15x)
15% Reiatsu multiplier (1.15x)
15% Vitality multiplier (1.15x)
Legendary(2%)
Jaegerjaquez
15% Strength multiplier (1.15x)Desgarron
10% Agility multiplier (1.1x)
13% Vitality multiplier (1.13x)
Desgarron
Cifer
12% Agility multiplier (1.12x)LanzaDelRelampago
15% Spirit multiplier (1.15x)
15% Reiatsu multiplier (1.15x)
15% better Health Regen (1.15x)
Lanza del Relámpago
StarrkCeroMetralleta
15% Spirit multiplier (1.15x)
12% Reiatsu multiplier (1.12x)
13% better Reiatsu Regen (1.13x)
Cero Metralleta
Louisenbairn
40% EXP multiplier (1.4x)
15% Strength multiplier (1.15x)
10% Agility multiplier (1.1x)
13% Vitality multiplier (1.13x)
15% Spirit multiplier (1.15x)
10% Reiatsu multiplier (1.1x)
10% better Reiatsu Regen (1.1x)
(This clan will not get an ability""")
        else:
            await message.channel.send("แนะนำให้ถามเป้นภาษาอังกฤษและก็เขียนตัวใหญ่นำหน้าเสมอทุกคำ")

    # เพื่อให้คำสั่งอื่นๆ ของ bot ทำงานด้วย
    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1252199106814808074)  # เปลี่ยนเป็น ID ของช่องที่ต้องการ
    if channel:
        text = f"ยินดีต้อนรับครับสุดหล่อ, {member.mention}"
        await channel.send(text)

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1252200094531326012)  # เปลี่ยนเป็น ID ของช่องที่ต้องการ
    if channel:
        text = f"ไว้เจอกันครับสุดหล่อ, {member.mention}"
        await channel.send(text)

server_on()

bot.run(os.getenv('TOKEN'))
