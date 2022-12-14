import discord


def help():
    help_embed = discord.Embed(title="コマンド一覧", color=0xff0000)
    help_embed.add_field(name="!j host 部屋名 最大人数(20人まで)", value="自分で部屋をホストすることができます。", inline=False)
    help_embed.add_field(name="!j rand", value="今存在する部屋の中からランダムで5個部屋を持ってきます", inline=False)
    help_embed.add_field(name="!j join 部屋名", value="参加したい部屋の名前を入力して参加することができます。部屋はroomlistから探すことができます", inline=False)
    help_embed.add_field(name="!j leave", value="部屋から離脱することができます。", inline=False)
    help_embed.add_field(name="!j chat メッセージ", value="部屋に参加している状態で使用すると、会話することができます。", inline=False)
    return help_embed


def embed(titlems, message, val):
    ms = discord.Embed(title=titlems, color=0xff0000)
    ms.add_field(name=message, value=val, inline=False)
    return ms


def credit():
    credit_embed = discord.Embed(title="CREDIT", color=0xff0000)
    credit_embed.add_field(name="CREATOR", value="AKAZ", inline=False)
    credit_embed.add_field(name="CREATION DATE", value="2022/10/02", inline=False)
    return credit_embed


def word():
    prohibited_word = ["http", "://", "://www", ".com", ".co.jp", ".jp", "@", ":"]
    return prohibited_word
