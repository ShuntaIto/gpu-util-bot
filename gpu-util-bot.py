import discord
import subprocess
from PIL import Image, ImageDraw, ImageFont
import io
import os

TOKEN = "<discord token>"

intents = discord.Intents.all()
client = discord.Client(intents=intents)

def get_nvidia_smi_result_image() -> io.BytesIO:
    # subprocess で nvidia-smi コマンドを実行
    # Execute the nvidia-smi command with subprocess
    result = subprocess.run(["nvidia-smi"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    gpu_info = result.stdout

    # 等幅フォントの読み込み
    # Load a monospaced font
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"  # Linux の場合
    font_size = 14
    # Windows の場合のフォントパス
    # Font path for Windows
    if not os.path.exists(font_path):  
        font_path = "C:/Windows/Fonts/consola.ttf"
    font = ImageFont.truetype(font_path, font_size)

    padding = 10
    # 各行の間隔
    # Line spacing
    line_spacing = 4  

    # テキストの各行の幅と高さを取得し、画像のサイズを計算
    # Get the width and height of each line of text and calculate the size of the image
    max_width = max([font.getbbox(line)[2] for line in gpu_info.splitlines()]) + 2 * padding
    max_height = (font.getbbox("Ay")[3] + line_spacing) * len(gpu_info.splitlines()) + 2 * padding

    # 画像の作成（背景は白）
    # Create an image (white background)
    image = Image.new("RGB", (max_width, max_height), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    # テキストを画像に描画（黒色で描画）
    # Draw text on the image (draw in black)
    y = padding
    for line in gpu_info.splitlines():
        draw.text((padding, y), line, font=font, fill=(0, 0, 0))
        y += font.getbbox(line)[3] + line_spacing

    # 画像をバイトIOオブジェクトに保存
    # Save the image to a byte IO object
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format="PNG")
    img_byte_arr.seek(0)

    return img_byte_arr

# Botの起動時に実行されるイベント
# Event that is executed when the bot is started
@client.event
async def on_ready():
    print('Ready!')

# メッセージを受信したときに実行されるイベント
# Event that is executed when a message is received
@client.event
async def on_message(message):
    # メッセージがBot自身のメッセージの場合は無視
    # Ignore messages from the bot itself
    if message.author.bot:
        return
    
    # メッセージが '/nvidia-smi' の場合、nvidia-smi の結果を画像として送信
    # If the message is '/nvidia-smi', send the result of nvidia-smi as an image
    if message.content == '/nvidia-smi':
        image = get_nvidia_smi_result_image()
        await message.channel.send(file=discord.File(fp=image, filename="nvidia_smi_result.png"))
    
    # Botがメンションされた場合、nvidia-smi の結果を画像として送信
    # If the bot is mentioned, send the result of nvidia-smi as an image
    if client.user in message.mentions:
        image = get_nvidia_smi_result_image()
        await message.channel.send(file=discord.File(fp=image, filename="nvidia_smi_result.png"))


if __name__ == "__main__":
    client.run(TOKEN)
