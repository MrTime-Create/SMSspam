import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.messages = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print(f"🤖 บอทเชื่อมต่อสำเร็จในชื่อ: {client.user}")


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  # แปลงข้อความให้เป็นตัวพิมพ์เล็กและแยกคำด้วยช่องว่าง เพื่อดึงค่าตัวแปร pp และ oo
  parts = message.content.strip().split()

  # ตรวจเช็คว่าพิมพ์ขึ้นต้นด้วย /test ตามด้วยตัวแปร 2 ตัว (เช่น /test ค่า1 ค่า2)
  if len(parts) == 3 and parts[0].lower() == "/test":
    pp = parts[1]  # ตัวแปรที่ 1
    oo = parts[2]  # ตัวแปรที่ 2

    # สร้างข้อความตอบกลับโดยใช้ตัวแปร pp และ oo ตามต้องการ
    reply_text = (
        f"✅ **ตรวจพบคำสั่งเรียบร้อย!**\n"
        f"• ตัวแปร pp คือ: `{pp}`\n"
        f"• ตัวแปร oo คือ: `{oo}`\n"
        f"• ผู้ส่ง: {message.author.mention}"
    )

    # ส่งข้อความกลับไปที่แชทเดิมทันที
    await message.channel.send(reply_text)


client.run(TOKEN)