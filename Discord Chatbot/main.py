from typing import Final

import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

#Load token
load_dotenv()
#set the token
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

#debug command
#print(TOKEN)

#---------- Setting up the bot ----------
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents = intents)

#---------- Message functionality ----------
async def send_message(message: Message, user_message: str) -> None:
    #check for user message
    if not user_message:
        print('message null, intents error')
        return
    #check for private message
    if is_private := user_message[0] == '-':
        user_message = user_message[1:]
    try:
        response: str = get_response(user_message)
        #send the message to the author if private, otherwise send it into the channel
        await message.author.send(response) if is_private else await message.channel.send(response)
    #print out any errors
    except Exception as e:
        print(e)

#---------- Handling bot startup ----------
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running . . .')
    
# ---------- Handle incoming messages ----------
@client.event
async def on_message(message: Message) -> None:
    #Make sure the bot doesnt respond to itself causing an infinite loop
    if message.author == client.user:
        return
    #take in message parameters
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    #log the message received
    print(f'[{channel}] {username}: "{user_message}"')
    #respond to the message
    await send_message(message, user_message)

#---------- Main ----------
def main() -> None:
    client.run(token=TOKEN)
#main block
if __name__ == '__main__':
    main()