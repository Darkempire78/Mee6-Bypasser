![](https://img.shields.io/codefactor/grade/github/Darkempire78/Mee6-Bypasser?style=for-the-badge) 
![](https://img.shields.io/github/repo-size/Darkempire78/Mee6-Bypasser?style=for-the-badge)
![](https://img.shields.io/badge/SOURCERY-ENABLED-green?style=for-the-badge) <a href="https://discord.com/invite/sPvJmY7mcV"><img src="https://img.shields.io/discord/831524351311609907?color=%237289DA&label=DISCORD&style=for-the-badge"></a>

# Mee6 Bypasser Discord Bot (free premium level-role)

Mee6 Bypasser is a Discord Bot that allows you to use premium mee6 level role rewards. This bot use the Mee6's level system.

Add new roles            |  Display all roles / Help command
:-------------------------:|:-------------------------:
![](https://github.com/Darkempire78/mee6-bypasser/blob/master/Capture1.PNG)  |  ![](https://github.com/Darkempire78/mee6-bypasser/blob/master/Capture2.PNG)


## Installation

* Install all dependencies: `pip install -r requirements.txt`

Edit `configuration.json` :
```Javascript
{
    "token": "", // Your token here
    "removePreviousRewards": true, // true / false
    "updateEachMessage": true, // true / false
    "updateEachTime": [] // ⚠️ only for active server : set false updateEachMessage and add your guild id in updateEachTime => update each 5 minutes users from the server
}
```

* This bot have to use the "server members intent", so you have to enable it in the Discord's developers portal.

Finally, host the bot and invite it to your own server.

## Features

This Discord Bot bypasses a premium feature of the Bot Mee6. You can use it for free.
You can select roles, that are given to users that reach a certain Mee6-Level.

* Give and remove roles to users that reach a certain Mee6-Level.
* Display the list of role rewards.
* Remove previous role rewards.
* update the whole server.
* Update each 5 minutes the all users from the server.

## Commands

```
?add <Level number> <Role ID> : Add a role reward.
?remove <Level number> : Remove a role reward.
?rolerewards : Display the list of role rewards.
?removepreviousrewards <true/false> : Change remove-previous-rewards setting.
?leaderboard : updates the roles of the users of the whole server.

?help : display help.
```
## Note 

The bot does only work if the Mee6's leaderboard is public.

## Do not work ?

If you have an error with the mee6 api, your server must be too active for the api. You must use the task system (updateEachTime).

## Discord

Join the Discord server !

[![](https://i.imgur.com/UfyvtOL.png)](https://discord.gg/sPvJmY7mcV)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

This project is under [GPLv3](https://github.com/Darkempire78/mee6-bypasser/blob/master/LICENSE).


# Advice :

You should use [Discord Tools](https://marketplace.visualstudio.com/items?itemName=Darkempire78.discord-tools) to code your Discord bots on Visual Studio Code easier.
Works for Python (Discord.py), Javascript (Discord.js) and Java (JDA). Generate template bot and code (snippets).
- **Download :** https://marketplace.visualstudio.com/items?itemName=Darkempire78.discord-tools
- **Repository :** https://github.com/Darkempire78/Discord-Tools
