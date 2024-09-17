# DiscordSelfTools
Custom SelfBot-like tools for discord, includes a troller and an advanced universal message logger

## Setup
Make sure you have python and pip installed, open your terminal/powershell and type
```
pip uninstall discord
```
then
```
pip install discord.py-self
```
## How to use (troller)
in order to use the troller you need to create a config.json file that looks like this (make sure to replace the place holders)
```json
{
    "config": {
        "userIds": [
            123456,
            1234567
        ]
    }
}
```
and to enter your token(s) in the variable inside main.py, then simply run
```
python main.py
```
to execute the troller, after this you can also use .add <user id> and .remove <user id>
to control the config

## How to use (message logger)
To use the message logger simply put in your token inside the MessageLogger.py file and execute it, it will generate an output.txt file **Do not rename it**, after this you can use Leaderboarder.py to generate a leaderboard and UserSearch.py to search for messages by a single user.
