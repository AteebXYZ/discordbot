import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import subprocess
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True
mathtests = 'Math: \n \u2022 31-10-23 Tuesday (nodetail) \n \u2022 22-11-23 Wednesday (nodetail). \n'
chemtests = 'Chemistry: \n \u2022 31-10-23 Tuesday Assignment (nodetail) \n \u2022 20-11-23 Monday (nodetail). \n'
phystests = 'Physics: \n \u2022 12-11-23 Sunday Assignment (nodetail). \n'
biotests = 'Biology: \n \u2022 29-10-23 Sunday Assignment (nodetail) \n \u2022 15-11-23 Wednesday (nodetail). \n'
icttests = 'ICT: \n \u2022 22-10-23 Sunday Project (nodetails) \n \u2022 29-10-23 Sunday (nodetails) \n \u2022 13-11-23 Monday Assignment (nodetails). \n'
histtests = 'History: \n \u2022 5-11-23 Sunday (nodetails) \n \u2022 15-11-23 Wednesday Assignment Write an auto biography about Hitler 500-700 words. \n \u2022 19-11-23 Sunday Project (nodetails). \n'
geotests = 'Geography: \n \u2022 2-11-23 Thursday (nodetails) \n \u2022 6-11-23 Monday Assignment Write about your country 500-700 words, use the headings of chapter 6 as guideline \n \u2022 13-11-23 Monday Project (nodetails). \n'
urdutests = 'Urdu: \n \u2022 25-10-23 Wednesday Quiz Memorize the quiz MCQs. \n'
arabictests = 'Arabic: \n \u2022 22-10-23 Sunday Project (nodetails) \n \u2022 29-10-23 Sunday Assignment (nodetails) \n \u2022 1-11-23 Wednesday Reading \n \u2022 25-11-23 Saturday?(incorrect date) (nodetail). \n'
isl1tests = 'Islamic 1: \n \u2022 16-10-23 Monday (nodetail) \n \u2022 2-11-23 Thursday Project (nodetail) \n \u2022 23-11-23 Thursday Reading and Recitation. \n'
isl2tests = 'Islamic 2 : \n \u2022 (date not confirmed) Monday PG 78 - 81 all, 87 all, pg 88 until paragraph line 15, pg 89 Abbas (RA) description, pg 90 all, pg 91 first 2 paragrapghs.\n \u2022 16-10-23 Monday (nodetail) \n \u2022 23-11-23 Thursday Reading and Recitation. \n'
engtests = 'English: \n \u2022 26-10-23 Thursday Comprehension \n \u2022 12-10-23 Thursday Assignment (nodetail) \n \u2022 26-10-23 Thursday Project (nodetail). \n'
weekurd = 'Urdu Weekly Tests: \n \u2022 Urdu Meanings Test 18-10-23 Wednesday \n \u2022 Writing 22-10-23 Sunday'
resources = "Chemistry: \n \u2022 Drive Link: https://drive.google.com/drive/folders/1G_qQfRroP1uikltjMRbpsiyfcblf-GJT?usp=drive_link \n Physics: \n \u2022 Drive Link: https://drive.google.com/drive/folders/1MSIED1KFt4qeUl4jh5cRg_-1bxdgtscF?usp=drive_link \n Biology: \n \u2022 Drive Link: https://drive.google.com/drive/folders/1Yhm9Aie7ALd4V9evJp_LxaEH3wh1hTIf?usp=drive_link \n ICT: \n \u2022 Drive Link: https://drive.google.com/drive/folders/1x-5GmDj7npKZQK64q1X-IGJfnuOztCYA?usp=drive_link \n English: \n \u2022 Drive Link: https://drive.google.com/drive/folders/1lVjA0XPxHT8Fj7-n6JE2LNCHxvadyZ3W?usp=sharing"

client = discord.Client(intents=intents)
items = [
    mathtests, chemtests, phystests, biotests, icttests, histtests, geotests,
    urdutests, arabictests, isl1tests, isl2tests, engtests, weekurd
]
list_message = "\n".join(items)

bot = commands.Bot(command_prefix="/", intents=intents)


@bot.tree.command(
    name="testsall",
    description=
    "Displays all tests for the year note: these are based on the timetable given"
)
async def testsall(interaction: discord.Interaction):
  await interaction.response.send_message(list_message)


@bot.tree.command(name="testsmath",
                  description="Displays all the tests for Math")
async def testsmath(interaction: discord.Interaction):
  await interaction.response.send_message(mathtests)


@bot.tree.command(name="testschem",
                  description="Displays all the tests for Chemistry")
async def testschem(interaction: discord.Interaction):
  await interaction.response.send_message(chemtests)


@bot.tree.command(name="testsphys",
                  description="Displays all the tests for Physics")
async def testsphys(interaction: discord.Interaction):
  await interaction.response.send_message(phystests)


@bot.tree.command(name="testsbio",
                  description="Displays all the tests for Biology")
async def testsbio(interaction: discord.Interaction):
  await interaction.response.send_message(biotests)


@bot.tree.command(name="testsict",
                  description="Displays all the tests for ICT")
async def testsict(interaction: discord.Interaction):
  await interaction.response.send_message(icttests)


@bot.tree.command(name="testshist",
                  description="Displays all the tests for History")
async def testshist(interaction: discord.Interaction):
  await interaction.response.send_message(histtests)


@bot.tree.command(name="testsgeo",
                  description="Displays all the tests for Geography")
async def testsgeo(interaction: discord.Interaction):
  await interaction.response.send_message(geotests)


@bot.tree.command(name="testsurdu",
                  description="Displays all the tests for Urdu")
async def testsurdu(interaction: discord.Interaction):
  await interaction.response.send_message(urdutests)


@bot.tree.command(
    name="testsarabic",
    description=
    "Displays all the tests for Arabic note: These dates may not be accurate.")
async def testsarabic(interaction: discord.Interaction):
  await interaction.response.send_message(arabictests)


@bot.tree.command(
    name="testsisl1",
    description="Displays all the tests for Islamic 1st language students")
async def testsisl1(interaction: discord.Interaction):
  await interaction.response.send_message(isl1tests)


@bot.tree.command(
    name="testsisl2",
    description="Displays all the tests for Islamic 2nd language students")
async def testsisl2(interaction: discord.Interaction):
  await interaction.response.send_message(isl2tests)


@bot.tree.command(name="testseng",
                  description="Displays all the tests for English")
async def testseng(interaction: discord.Interaction):
  await interaction.response.send_message(engtests)


@bot.tree.command(
    name="testsurdweek",
    description="Displays all the tests that happen weekly in Urdu")
async def testsurdweek(interaction: discord.Interaction):
  await interaction.response.send_message(weekurd)


@bot.tree.command(name="timetable", description="Send timetable image")
async def send_timetable(interaction: discord.Interaction):
  await interaction.response.send_message(file=discord.File(r"C:\Users\ateeb\OneDrive\Desktop\test\BOT\timetable.png"))


@bot.tree.command(name="resources",
                  description="List all resources available for all subjects")
async def send_resources(interaction: discord.Interaction):
  await interaction.response.send_message(resources)
  
@bot.tree.command(name="sync", description="Sync Commands With Tree")
async def sync(interaction: discord.Interaction):
    if interaction.user.id == 1116316139224567818:
        await bot.tree.sync()
        print('Commands Synced.')
    else:
        await interaction.response.send_message('You must be the owner to use this command!')
        
@bot.tree.command(name="ping", description="Pong!")
async def send_resources(interaction: discord.Interaction):
  await interaction.response.send_message("PONG!")


@bot.event
async def on_ready():
  print('iwork')


keep_alive()
load_dotenv()
token = os.getenv("TOKEN")
bot.run(token)
