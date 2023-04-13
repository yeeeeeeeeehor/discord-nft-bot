import discord
import datetime
import json
from discord import ui

# The channel where the bot will react to commands
CHANNEL_ID = #CHANNEL ID

# The ID of the role to be assigned
ROLE_ID = #ID ROLE

# Open the file in 'append' mode to preserve previous log entries
with open('log.txt', 'a') as f:
    pass

# Open the wallet.json file with the list of wallets for verification
with open('wallet.json') as f:
    WALLET_LIST = json.load(f)

# Open the true.json file to get the list of used wallets
try:
    with open('true.json') as f:
        USED_LIST = json.load(f)
except FileNotFoundError:
    # If the file doesn't exist yet, create an empty list
    USED_LIST = []

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('Bot is now online and ready to accept commands!')

@client.event
async def on_message(message):
    # Ignore messages from the bot
    if message.author == client.user:
        return

    # Check if message is in the correct channel
    if message.channel.id != CHANNEL_ID:
        return

#############################################################
#                                                           #
#               Кeplace "!verefy" with your command.        #
#                                                           #
#############################################################

    # Delete messages that don't start with !verefy
    if not message.content.startswith('!verefy'): 
        await message.delete()
        await message.channel.send(f'{message.author.mention}, this channel is only for the !verefy command.')
        return

    # Delete messages from users and log the attempt
    wallet_address = message.content[6:].strip()
    now = datetime.datetime.now()
    log_entry = f'{now} - {message.author}: '

    if wallet_address in WALLET_LIST:
        if wallet_address in USED_LIST:
            # Wallet already used by another user
            log_entry += f'tried to get the role for the wallet {wallet_address}, but it has already been used by another user'
            await message.channel.send(f'{message.author.mention}, this wallet has already been used by another user.')
        else:
            # Wallet not yet used by any user
            log_entry += f'got the role for the wallet {wallet_address}'
            role = message.guild.get_role(ROLE_ID)
            await message.author.add_roles(role)
            await message.channel.send(f'{message.author.mention}, role successfully assigned.')
            USED_LIST.append(wallet_address)

            # Записать в файл true.json
            with open('true.json', 'w') as f:
                json.dump(USED_LIST, f)
        await message.delete()
    else:
        # Invalid wallet address
        log_entry += f'tried to get the role for the invalid wallet {wallet_address}'
    
    # Записать в файл log.txt
    with open('log.txt', 'a') as f:
        f.write(log_entry + '\n')


client.run('bot_token_here')