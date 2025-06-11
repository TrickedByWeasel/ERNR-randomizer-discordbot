import discord
import random

TOKEN = "DISCORD TOKEN"  # TODO Set your discord token here
CHANNEL_ID = 1234567890  # TODO Set your discord channel ID here

CLASSES = ["Wylder", "Guardian", "Ironeye", "Duchess",
           "Raider", "Revenant", "Recluse", "Executor"]
BOSSES = ["Tricephalos", "Gaping Jaw", "Sentient Pest", "Augur",
          "Equilibrious Beast", "Darkdrift Knight", "Fissure in the Fog", "Heolstor, the Nightlord"]

# TODO change default values for player names here
p1 = "p1"
p2 = "p2"
p3 = "p3"

# bot deletes message after {DELETE_AFTER} seconds
DELETE_AFTER = 120

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


@bot.event
async def on_message(message):
    global p1, p2, p3
    if message.author == bot.user:
        return
    if message.channel.id == CHANNEL_ID:
        msg = message.content.strip()
        if msg.lower().startswith('§'):
            if msg == "§help":
                response = (
                    "§ -> Gives random boss and random classes for players\n"
                    "§p1 {name} -> sets name for player1\n"
                    "§p2 {name} -> sets name for player2\n"
                    "§p3 {name} -> sets name for player3\n"
                )
                await message.channel.send(response, delete_after=120)
            elif msg.startswith("§p1 "):
                p1 = msg[4:]
            elif msg.startswith("§p2 "):
                p2 = msg[4:]
            elif msg.startswith("§p3 "):
                p3 = msg[4:]
            else:
                chosen = random.sample(CLASSES, 3)
                chosen_boss = random.choice(BOSSES)
                
                response = (
                    f" -------------\n{chosen_boss}\n"
                    f"       VS.\n"
                    f"{p1}: {chosen[0]}\n"
                    f"{p2}: {chosen[1]}\n"
                    f"{p3}: {chosen[2]}"
                )
                
                print(response)
                await message.channel.send(response, delete_after=DELETE_AFTER)

bot.run(TOKEN)
