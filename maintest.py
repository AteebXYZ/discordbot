import interactions
import os
from dotenv import load_dotenv
import json
import re
load_dotenv()
bottoken=os.getenv("TOKEN")

bot = interactions.Client(token=bottoken)

FILE_PATH = r"C:\Users\ateeb\OneDrive\Desktop\test\BOT\test_info.json"

# Check if the file exists, and create it with default values if not
if not os.path.isfile(FILE_PATH):
    default_info = {
        "mathtests": "Math:\n",
        "chemtests": "\nChemistry:\n",
        "phystests": "\nPhysics:\n",
        "biotests":  "\nBiology:\n",
        "icttests":  "\nICT:\n",
        "histtests": "\nHistory:\n",
        "geotests":  "\nGeography:\n",
        "urdutests": "\nUrdu:\n",
        "arabictests": "\nArabic:\n",
        "isl1tests": "\nIslamic 1st Language:\n",
        "isl2tests": "\nIslamic 2nd Language:\n",
        "engtests": "\nEnglish:\n",
        "weekurd":  "\nWeekly Urdu Tests:\n",
        "resources": "\nChemistry: \n \u2022 Drive Link: https://drive.google.com/drive/folders/1G_qQfRroP1uikltjMRbpsiyfcblf-GJT?usp=drive_link \n Physics: \n \u2022 Drive Link: https://drive.google.com/drive/folders/1MSIED1KFt4qeUl4jh5cRg_-1bxdgtscF?usp=drive_link \n Biology: \n \u2022 Drive Link: https://drive.google.com/drive/folders/1Yhm9Aie7ALd4V9evJp_LxaEH3wh1hTIf?usp=drive_link \n ICT: \n \u2022 Drive Link: https://drive.google.com/drive/folders/1x-5GmDj7npKZQK64q1X-IGJfnuOztCYA?usp=drive_link \n English: \n \u2022 Drive Link: https://drive.google.com/drive/folders/1lVjA0XPxHT8Fj7-n6JE2LNCHxvadyZ3W?usp=sharing",
    }
    with open(FILE_PATH, "w") as file:
        json.dump(default_info, file)

# Load test information from the file
try:
    with open(FILE_PATH, "r") as file:
        options_info = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    options_info = {
        "mathtests": "",
        "chemtests": "",
        "phystests": "",
        "biotests":  "",
        "icttests":  "",
        "histtests": "",
        "geotests":  "",
        "urdutests": "",
        "arabictests": "",
        "isl1tests": "",
        "isl2tests": "",
        "engtests": "",
        "weekurd":  "",
        "resources": "Resources:\nChemistry: \n \u2022 Drive Link: https://drive.google.com/drive/folders/1G_qQfRroP1uikltjMRbpsiyfcblf-GJT?usp=drive_link \n Physics: \n \u2022 Drive Link: https://drive.google.com/drive/folders/1MSIED1KFt4qeUl4jh5cRg_-1bxdgtscF?usp=drive_link \n Biology: \n \u2022 Drive Link: https://drive.google.com/drive/folders/1Yhm9Aie7ALd4V9evJp_LxaEH3wh1hTIf?usp=drive_link \n ICT: \n \u2022 Drive Link: https://drive.google.com/drive/folders/1x-5GmDj7npKZQK64q1X-IGJfnuOztCYA?usp=drive_link \n English: \n \u2022 Drive Link: https://drive.google.com/drive/folders/1lVjA0XPxHT8Fj7-n6JE2LNCHxvadyZ3W?usp=sharing",
        # Add more options as needed
    }

def replace_special_characters(text):
    # Replace all occurrences of \\n and other escaped characters
    return re.sub(r'\\[n|r|u][^\\]*', lambda match: bytes(match.group(0), 'utf-8').decode('unicode_escape'), text)

@bot.command(
    name="set_test_info",
    description="Set test information for a specific option",
    options=[
        interactions.Option(
            name="subject",
            description="Choose an option",
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.Choice(name="Math Tests", value="mathtests"),
                interactions.Choice(name="Chemistry Tests", value="chemtests"),
                interactions.Choice(name="Biology Tests", value="biotests"),
                interactions.Choice(name="ICT Tests", value="icttests"),
                interactions.Choice(name="History Tests", value="histtests"),
                interactions.Choice(name="Geography Tests", value="geotests"),
                interactions.Choice(name="Urdu Tests", value="urdutests"),
                interactions.Choice(name="Arabic Tests", value="arabictests"),
                interactions.Choice(name="Islamic 1st Language Tests", value="isl1tests"),
                interactions.Choice(name="Islamic 2nd Language Tests", value="isl2tests"),
                interactions.Choice(name="English Tests", value="engtests"),
                interactions.Choice(name="Weekly Urdu Tests", value="weekurd"),
                interactions.Choice(name="Resources", value="resources"),
                
                # Add more choices as needed
            ]
        ),
        interactions.Option(
            name="test_info",
            description="Enter the test information",
            type=interactions.OptionType.STRING,
            required=True
        )
    ]
)
async def set_test_info(ctx, subject: str, test_info: str):
    # Use the function to replace special characters
    if ctx.author.id == 1116316139224567818:
        test_info = replace_special_characters(test_info)
        options_info[subject] = test_info

        with open(FILE_PATH, "w") as file:
            json.dump(options_info, file, ensure_ascii=False)
            
        await ctx.send(f'Test information for {subject} set to:\n{test_info}')
    else:
        await ctx.send('No.')

@bot.command(
    name="display_tests",
    description="Display the Tests and their Dates",
    scope = 1148659207420268736,
    options=[
        interactions.Option(
            name="subject",
            description="Specify which subject to display tests for.",
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.Choice(name="All", value="all")] + [
                interactions.Choice(name=option, value=option) for option in options_info.keys()
            ]
        )
    ]
)
async def print_options(ctx, subject: str = None):
    
    if subject == "all":
        # Print values of all options
        options_text = "".join([f"{info}" for info in options_info.values()])
        await ctx.send(f'{options_text}')
    elif subject:
        # Print the value of the specified option
        await ctx.send(f'{options_info.get(subject)}')
        
@bot.command(name="timetable", description="Display the timetable.", scope = 1148659207420268736)
async def timetable(ctx):
    # Replace 'path/to/image.png' with the actual path to your image file
    image_path = r"C:\Users\ateeb\OneDrive\Desktop\test\BOT\timetable.png"
    
    # Check if the file exists
    if os.path.isfile(image_path):
        await ctx.send(r"https://cdn.discordapp.com/attachments/1151840425791987782/1193919270581710991/timetable.png?ex=65ae76f8&is=659c01f8&hm=2ae4b2a06ef9079b64d70b23f06e62316e1ea8fa711257d57f8629f9ddc33ff1&")
    else:
        await ctx.send("Image not found.")



bot.start()