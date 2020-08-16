![](https://img.shields.io/github/repo-size/Darkempire78/mee6-bypasser)

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

* Download MP3 and album from Deezer
* Select the best quality (320kbps) if the file doesn't reach Discord's file size limit (8mb).
* Download lyrics if available.
* Get infos about artists, albums...

## Commands

```
?add <Level number> <Role ID> : Add a role reward.
?remove <Level number> : Remove a role reward.
?rolerewards : Display the list of role rewards.
?removepreviousrewards <true/false> : Change remove-previous-rewards setting.

?help : display help.
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


## License

This project is under [GPLv3](https://github.com/Darkempire78/mee6-bypasser/blob/master/LICENSE).
