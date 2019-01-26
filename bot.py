import discord
from discord.ext import commands

TOKEN = 'NTMzNjg2MTA0OTE4OTgyNjc2.Dy2zgA.zgovXYWnt5gxT_HhqzrhhNzWL2g'
@client.event
async def on_ready():
    print('Bot pronto')
    await client.change_presence(activity=discord.Game{name="Alacazammm Lounge"})

@client.command()
async def kick(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Perfavore, menziona l'utente da kickare :x:")
        return
    await member.kick()
    await ctx.send(":high_heel: Kickato {member.mention} con successo :white_check_mark:")

@client.command()
async def ban(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Perfavore menziona l'utente da bannare :x:")
        return
    await member.ban()
    await ctx.send(":hammer: Bannato {member.mention} con successo :white_check_mark:")

@client.command()
async def mute(ctx, member: discord.Member=None):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not member:
        await ctx.send("Perfavore menziona l'utente da mutare :x:")
        return
    await member.add_roles(@Muted Voice)
    await ctx.send(":mute: Mutato {member.mention} con successo :white_check_mark:")

@client.command()
async def unmute(ctx, member: discord.Member=None):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not member:
        await ctx.send("Perfavore menziona l'utente da smutare :x:")
        return
    await member.remove_roles(@Muted Voice)
    await ctx.send(":loud_sound: Mutato {member.mention} con successo :white_check_mark:")

@client.command()
async def coinflip(ctx):
    choices = ("È uscito Testa", "È uscito Croce")
    raincoin = random.choice(choices)
    await ctx.send(rancoin)

@client.command()
async def invite():
    await client.say('Invita i tuoi amici (o nemici) al Alacazammm Lounge: https://discord.gg/tz5R4sC')

client.run('NTMzNjg2MTA0OTE4OTgyNjc2.Dy2zgA.zgovXYWnt5gxT_HhqzrhhNzWL2g')
