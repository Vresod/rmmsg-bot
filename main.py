#!/usr/bin/env python3

import discord
from discord.ext import commands

with open("tokenfile","r") as tokenfile:
	token = tokenfile.read()

client = commands.Bot(command_prefix="di!")
client.remove_command("help")

@client.event
async def on_ready():
	print(f"logged in as {client.user}")
	print(f"https://discord.com/oauth2/authorize?client_id={client.user.id}&permissions=8192&scope=bot")
	for guild in client.guilds:
		print(f"In guild: {guild.name}") 

@client.event
async def on_guild_join(guild):
	print(f"Joined guild: {guild.name}")

@client.event
async def on_reaction_add(reaction,user): # the meat
	if type(reaction.emoji) is str:
		return
	if reaction.emoji.name == "delete_this_message" and user.permissions_in(reaction.message.channel).manage_messages:
		await reaction.message.delete()

@client.command()
async def help(ctx):
	await ctx.send("react with :delete_this_message: to delete a message if you have the permission to do that; otherwise i do nothing")

client.run(token)
