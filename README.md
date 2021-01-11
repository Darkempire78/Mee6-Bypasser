![](https://img.shields.io/codefactor/grade/github/Darkempire78/Mee6-Bypasser?style=for-the-badge) 
![](https://img.shields.io/github/repo-size/Darkempire78/Mee6-Bypasser?style=for-the-badge)
![](https://img.shields.io/badge/SOURCERY-ENABLED-green?style=for-the-badge)

# Mee6 Bypasser Discord Bot (free premium level-role)

Mee6 Bypasser is a Discord Bot that allows you to use premium mee6 level role rewards. This bot use the Mee6's level system.

Add new roles            |  Display all roles / Help command
:-------------------------:|:-------------------------:
![](https://github.com/Darkempire78/mee6-bypasser/blob/master/Capture1.PNG)  |  ![](https://github.com/Darkempire78/mee6-bypasser/blob/master/Capture2.PNG)


## Installation

Install all dependencies:

```bash
pip install -r requirements.txt
```
Then put your Discord token that can be found in the Discord's developers portal inside `configuration.json`.

Finally, host the bot and invite it to your own server.

## Features

This Discord Bot bypasses a premium feature of the Bot Mee6. You can use it for free.
You can select roles, that are given to users that reach a certain Mee6-Level.

* Give and remove roles to users that reach a certain Mee6-Level.
* Display the list of role rewards
* Remove previous role rewards. 

## Commands

```
?add <Level number> <Role ID> : Add a role reward.
?remove <Level number> : Remove a role reward.
?rolerewards : Display the list of role rewards.
?removepreviousrewards <true/false> : Change remove-previous-rewards setting.

?help : display help.
```
## Note 

The bot does only work if the Mee6's leaderboard is public.

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
