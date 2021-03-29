# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 13:21:03 2021

@author: ahao
"""

# bot.py
import os
import random
from discord.ext import commands
import discord
from dotenv import load_dotenv
import datetime

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

bot = commands.Bot(command_prefix='!')


import sqlite3
dbfile = "pcrd.db"
conn = sqlite3.connect(dbfile)
rows = conn.execute("select * from score;")
for row in rows:
    for field in row:
        print("{}\t".format(field), end="")
    print()
conn.close()

        
@bot.command(name='boss', help='報名指令_周目_幾王_傷害')
async def signup (ctx, weeek: int, boss_number: int, boss_damge: int):
    dbfile = "pcrd.db"
    conn = sqlite3.connect(dbfile)
    sql_str = "insert into score(member, aid, week, boss, damge) values('{}',{},{},{},{});".format(str(ctx.author), ctx.author.id,weeek, boss_number, boss_damge)
    conn.execute(sql_str)
    conn.commit()
    response = str(ctx.author)+' sign up Boss'+ str(boss_number) +' for '+ str(boss_damge)
    await ctx.send(response)

@bot.command(name='showmy', help='秀出自己的刀')
async def showmy (ctx):
    response2='```'
    dbfile = "pcrd.db"
    conn = sqlite3.connect(dbfile)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from score WHERE aid == "+str(ctx.author.id)+" ORDER BY ID DESC;")
    rows = cur.fetchall()
    for row in rows:
            print("{}\t".format(field), end="")
            response2="|{}".format(row['damge'])+" "*(16-len(str(row['damge'])))+"|" +response2
            response2="|{}".format(row['boss'])+" "*(6-len(str(row['boss'])))+response2
            response2="|{}".format(row['week'])+" "*(6-len(str(row['week'])))+response2
            response2="|{}".format(row['member'])+" "*(16-len(str(row['member'])))+response2
            response2="|{}".format(row['id'])+" "*(5-len(str(row['id'])))+response2
            response2="\n+-----+----------------+------+------+----------------+\n"+response2

    conn.close()
    await ctx.send('```| PID |     Member     | Week | Boss |     Damgee     |\n+-----+----------------+------+------+----------------+```')
    response2='```'+response2
    await ctx.send(response3) 
    
@bot.command(name='showall', help='秀出全部周目的報名表')
async def showall(ctx):
    
    response2='```'
    dbfile = "pcrd.db"
    conn = sqlite3.connect(dbfile)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from score ORDER BY week DESC;")
    rows = cur.fetchall()
    for row in rows:
            print("{}\t".format(field), end="")
            response2="|{}".format(row['damge'])+" "*(16-len(str(row['damge'])))+"|" +response2
            response2="|{}".format(row['boss'])+" "*(6-len(str(row['boss'])))+response2
            response2="|{}".format(row['week'])+" "*(6-len(str(row['week'])))+response2
            response2="|{}".format(row['member'])+" "*(16-len(str(row['member'])))+response2
            response2="|{}".format(row['id'])+" "*(5-len(str(row['id'])))+response2
            response2="\n+-----+----------------+------+------+----------------+\n"+response2
    conn.close()
    await ctx.send('```| PID |     Member     | Week | Boss |     Damge      |\n+-----+----------------+------+------+----------------+```')
    response2='```'+response2
    await ctx.send(response2)
    
@bot.command(name='show', help='秀出指定周目的報名表')
async def show(ctx, weeek: int):
    
    response2='```'
    dbfile = "pcrd.db"
    conn = sqlite3.connect(dbfile)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from score WHERE week == "+str(weeek)+" ORDER BY ID DESC;")
    rows = cur.fetchall()
    for row in rows:
            print("{}\t".format(field), end="")
            response2="|{}".format(row['damge'])+" "*(16-len(str(row['damge'])))+"|" +response2
            response2="|{}".format(row['boss'])+" "*(6-len(str(row['boss'])))+response2
            response2="|{}".format(row['week'])+" "*(6-len(str(row['week'])))+response2
            response2="|{}".format(row['member'])+" "*(16-len(str(row['member'])))+response2
            response2="|{}".format(row['id'])+" "*(5-len(str(row['id'])))+response2
            response2="\n+-----+----------------+------+------+----------------+\n"+response2
    conn.close()
    await ctx.send('```| PID |     Member     | Week | Boss |     Damge      |\n+-----+----------------+------+------+----------------+```')
    response2='```'+response2
    await ctx.send(response2)

@bot.command(name='showsp', help='秀出指定周目區間的報名表')
async def showsp(ctx, weeek1: int, weeek2: int):
    
    response2='```'
    dbfile = "pcrd.db"
    conn = sqlite3.connect(dbfile)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from score WHERE week >= "+str(weeek1)+" and week <= "+str(weeek2)+" ORDER BY week DESC;")
    rows = cur.fetchall()
    for row in rows:
            print("{}\t".format(field), end="")
            response2="|{}".format(row['damge'])+" "*(16-len(str(row['damge'])))+"|" +response2
            response2="|{}".format(row['boss'])+" "*(6-len(str(row['boss'])))+response2
            response2="|{}".format(row['week'])+" "*(6-len(str(row['week'])))+response2
            response2="|{}".format(row['member'])+" "*(16-len(str(row['member'])))+response2
            response2="|{}".format(row['id'])+" "*(5-len(str(row['id'])))+response2
            response2="\n+-----+----------------+------+------+----------------+\n"+response2
    conn.close()
    await ctx.send('```| PID |     Member     | Week | Boss |     Damgee     |\n+-----+----------------+------+------+----------------+```')
    response2='```'+response2
    await ctx.send(response2)
    
@bot.command(name='delb', help='刪除指定的報名表')
async def delb (ctx, pid: int):
    dbfile = "pcrd.db"
    conn = sqlite3.connect(dbfile)
    sql_str = "DELETE FROM score WHERE ID = "+str(pid)
    conn.execute(sql_str)
    conn.commit()
    response = ' delete ID '+str(pid)+'succed'
    await ctx.send(response)

bot.run(TOKEN)        



