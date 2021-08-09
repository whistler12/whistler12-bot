import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord import DMChannel
import random

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

prefix = ["w12!"]
default_prefix = "w12!"

bot = commands.Bot(command_prefix=prefix, help_command=None)

bot_version = "0.1.0"
bot_stage = "Alpha"
bot_invite = "https://discord.com/api/oauth2/authorize?client_id=874394926413144126&permissions=8&scope=bot"
bot_repo = "https://github.com/whistler12/whistler12-bot"

commands_list = f"``about``, ``avatar``"

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await bot.change_presence(activity=discord.Game(name=f"{default_prefix}help"))

@bot.command(name="about")
async def about(ctx):
    about_embed = discord.Embed(
        title="About this bot"
        ).add_field(
        name="Creator",
        value="whistler_12#0835"
        ).add_field(
        name="Creation date",
        value="August 9th, 2021"
        ).add_field(
        name="Version",
        value=f"{bot_version} ({bot_stage})"
        ).add_field(
        name="Library",
        value="discord.py",
        inline=False
        ).add_field(
        name="Links",
        value=f"**Invite link**: {bot_invite}\n**GitHub repository**: {bot_repo}\n**Changelog**: {bot_repo}/blob/master/CHANGELOG.md",
        inline=False
        )
    await ctx.send(embed=about_embed)
    
@bot.command(name="avatar")
async def avatar(ctx, *, avatar_member: discord.Member=None):
    if not avatar_member:
        avatar_member = ctx.message.author
    avatar_embed = discord.Embed(
        title="Avatar"
        ).set_author(
        name=avatar_member,
        icon_url=avatar_member.avatar_url
        ).set_image(url=avatar_member.avatar_url)
    await ctx.send(embed=avatar_embed)
    
bot.run(TOKEN)
