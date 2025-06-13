import copy
import discord
import random
import re

class Player:
    def __init__(self, name: str = "p1"):
        self.classes = ["Wylder", "Guardian", "Ironeye", "Duchess",
                        "Raider", "Revenant", "Recluse", "Executor"]
        self.all_classes = ["Wylder", "Guardian", "Ironeye", "Duchess",
                            "Raider", "Revenant", "Recluse", "Executor"]
        self.name = name
    
    def remove_class(self, c):
        c = c.strip().capitalize()
        if c in self.classes:
            self.classes.remove(c)
            response = (f"{self.name}: Removed {c}\n"
                        f"Remaining classes:\n"
                        f"{self.classes}")
            return response
        response = (f"{self.name}: {c} not found.\n"
                    f"Remaining classes:\n"
                    f"{self.classes}")
        return response
    
    def get_random_class(self, not_allowed: tuple[str, ...] = ()):
        cl = copy.deepcopy(self.classes)
        cl = list(set(cl) - set(not_allowed))
        if len(cl) == 0:
            return random.choice(self.all_classes)
        elif len(cl) == 1:
            return cl[0]
        return random.choice(cl)
    
    def change_name(self, name):
        if name.startswith("§"):
            return "Name cannot start with §."
        if "@everyone" in name or "@here" in name:
            return "Name cannot contain @everyone or @here."
        if not re.match(r'^[\w]{1,20}$', name):
            return "Invalid name. Use only letters, numbers, underscores, max 20 chars."
        response = f"{self.name} changed to {name}"
        self.name = name
        return response


TOKEN = "DISCORD TOKEN"  # TODO Set your discord token here
CHANNEL_ID = 1234567890  # TODO Set your discord channel ID here

# TODO change default values for player names here
p1 = Player(name="p1")
p2 = Player(name="p2")
p3 = Player(name="p3")

ALLOW_SAME_CLASS = False  # Players can get duplicate classes if set to True

BOSSES = ["Tricephalos", "Gaping Jaw", "Sentient Pest", "Augur",
          "Equilibrious Beast", "Darkdrift Knight", "Fissure in the Fog", "Heolstor, the Nightlord"]

# bot deletes message after {DELETE_AFTER} seconds
DELETE_AFTER = 120
DELETE_AFTER_REMOVE = 20
DELETE_AFTER_RENAME = 20


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
                response = p1.change_name(msg[4:])
                await message.channel.send(response, delete_after=DELETE_AFTER_RENAME)
            elif msg.startswith("§p2 "):
                response = p2.change_name(msg[4:])
                await message.channel.send(response, delete_after=DELETE_AFTER_RENAME)
            elif msg.startswith("§p3 "):
                response = p3.change_name(msg[4:])
                await message.channel.send(response, delete_after=DELETE_AFTER_RENAME)
            elif msg.startswith("§p1r "):
                response = p1.remove_class(msg[5:])
                await message.channel.send(response, delete_after=DELETE_AFTER_REMOVE)
            elif msg.startswith("§p2r "):
                response = p2.remove_class(msg[5:])
                await message.channel.send(response, delete_after=DELETE_AFTER_REMOVE)
            elif msg.startswith("§p3r "):
                response = p3.remove_class(msg[5:])
                await message.channel.send(response, delete_after=DELETE_AFTER_REMOVE)
            else:
                # Collect players in a list
                players = [p1, p2, p3]
                # Sort players by the number of available classes (ascending)
                players_sorted = sorted(players, key=lambda p: len(p.classes))
                chosen_classes = []

                # Assign classes in sorted order, avoiding duplicates if needed
                for player in players_sorted:
                    not_allowed = tuple(chosen_classes) if not ALLOW_SAME_CLASS else ()
                    chosen = player.get_random_class(not_allowed=not_allowed)
                    chosen_classes.append(chosen)

                # Map chosen classes back to the original player order
                player_to_class = dict(zip(players_sorted, chosen_classes))
                chosen = [player_to_class[p] for p in players]

                chosen_boss = random.choice(BOSSES)

                VS_TEXT = f"VS."
                max_width = len(chosen_boss)

                centered_vs = VS_TEXT.center(max_width)

                response = (
                    f" -------------\n"
                    f"{chosen_boss}\n"
                    f"{centered_vs}\n"
                    f"{p1.name}: {chosen[0]}\n"
                    f"{p2.name}: {chosen[1]}\n"
                    f"{p3.name}: {chosen[2]}"
                )
                print(response)
                await message.channel.send(response, delete_after=DELETE_AFTER)


bot.run(TOKEN)
