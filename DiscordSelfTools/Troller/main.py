import discord
import random
import subprocess
import json
import threading


def loadConfig():
    with open("config.json", "r") as f:
        return json.load(f)

def updateConfig(config):
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)



config = loadConfig()
userIds = config['config']['userIds']

tokens = [
    "token-1",
    "token-2",
    "etc-etc"
]
scripts = []
value = 0

def main():
    global value, scripts
    for token in tokens:
        value = value+1
        content = f"""
from main import SelfBot
import discord
token = "{token}"
client = SelfBot()
client.run(token)
        """
        name = f"Bot{value}.py"
        scripts.append(name)
        with open(name, "w") as f:
            f.writelines(content)
    processes = []
    for script in scripts:
        process = subprocess.Popen(['python', script])
        processes.append(process)
    for process in processes:
        process.wait()


class SelfBot(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def on_message(self, message):
        global allowedUsers
        allowedUsers = [whitelisted-userid, whitelisted-user id] # Add users allowed to run .add and .remove
        user_id = userIds

        reply_messages = ['BOO! Did i scare you? I\'m a bar of soap 🧼 just here to remind you to get ur ah in the 🚿 shower and go outside because the smell through the screen is not very pleasant over and out 👋\n-# (the user I replied to is an harmless skid)', "Remember to drink! :droplet:\n-# (the user I replied to is an harmless skid)", f'\"{message.content}\" :nerd:\n-# (the user I replied to is an harmless skid)']  # Messaggio di risposta
        debugThing = random.choice(reply_messages)
        if message.guild is not None:
            server_name = message.guild.name
            channel_name = message.channel.name
        else:
            server_name = "[dms]"
            channel_name = "[dms]"
        if message.content.startswith(".add") and message.author.id in allowedUsers:
            id = int(message.content[5:])
            print(f"New id!: {id}")
            await message.reply(f"```Adding {self.get_user(id).display_name} to the list```")
            user_id.append(id)
            config['config']['userIds'] = user_id
            updateConfig(config)
        if message.content.startswith(".remove") and message.author.id in allowedUsers:
            id = int(message.content[8:])
            print(id)
            print(f"Removing id!: {id}")
            await message.reply(f"```Removing {self.get_user(id).display_name} from the list```")

            if id in user_id:
                user_id.remove(id)  
                config['config']['userIds'] = user_id
                updateConfig(config)
                print(f"Id {id} removed successfully.")
            else:
                print(f"Id {id} not found in the list.")
        if message.content == "Ping":
            await message.reply("Pongo")
        if message.author.id in user_id:
            await message.reply(debugThing)
            print(f'Answered to {message.author.name}, in {server_name}, channel: {channel_name} with: {debugThing}\n')

if __name__ == "__main__":
    main()
