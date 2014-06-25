# Google Search Trends of Indian Politics

## Check the [demo](http://avinassh.github.io/polistats)

## Instructions:

- Install required libraries from `requirement.txt`:

		pip -r install requirements.txt

- Run `bot.py` to start collecting data. If you want run the bot multiple times a day, use `crontab`:

		$crontab -e
		00 10,14,18,22 * * * /home/johnappleseed/polistats/bot.py

- Run `server.py` to provide API end point