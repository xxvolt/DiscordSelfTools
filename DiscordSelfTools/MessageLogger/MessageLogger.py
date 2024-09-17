import discord

blacklisted = [820745488231301210, 123, 00] # add blacklisted guilds here

class bot(discord.Client):
    async def on_ready(self):
        print(f"{self.user} has connected to discord!")
    async def on_message(self, msg):
        if msg.guild is not None:
            if msg.guild.id in blacklisted:
                print("Skipped a message in a blacklisted guild")
                return
        with open("output.txt", "a") as f:
            if msg.guild is not None:
                content = f"Message by {msg.author} in {msg.channel.name} in {msg.guild.name}: {msg.content}\n"
            else:
                content = f"Message by {msg.author} in dms: {msg.content}\n"
            f.write(content)
        print(f"Message by {msg.author} has been logged!")

client = bot()

client.run("Your token here")
