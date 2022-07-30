# discord-birthday-bot
Hello world, welcome to my discord birthday bot.
You can easily deploy this super small bot which can help you post the birthdays of your community in your channel of choice. All of this is not really tested and also super quickly written. So use at own risk!

## How to insert birthdays:
Create a file app/birthdays.csv in your folder. Please use the following format:
```
name, dd.mm
name2, dd.mm
```

Save the file it will be in the gitignore.

The file will be copied into the Dockercontainer to have a default value. I highly suggest overmounting that file to make updates way easier for you.

## How to deploy:

Build your container.

```
docker build -t discord-birthday-bot:<your-tag> .
```

Create a Discord token and find the channel ID of the channel you want to push.

You can now run this service. Please add the two environment variables as you prefer:

DISCORD_TOKEN
DISCORD_CHANNEL_ID

Quick example for docker:
```
docker run -e DISCORD_TOKEN=ABCDEFG -e DISCORD_CHANNEL_ID=123456 discord-birthday-bot:latest
```

For overmounting the birthday file:
```
docker run -e DISCORD_TOKEN=ABCDEFG -e DISCORD_CHANNEL_ID=123456 -v ${PWD}/app/birthdays.csv:/app/birthdays.csv discord-birthday-bot:latest
```

For kubernetes I would suggest a configmap.

The Service should now work properly.



## Things I want to improve:
* adding kubernetes deployment example
* customize messages via configfile
* adding gifs/images/quotes
