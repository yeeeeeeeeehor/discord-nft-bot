# Discord Wallet Verification Bot

This bot is designed to help verify user wallet addresses on a Discord server. It will assign a specific role to users who successfully provide a valid wallet address. 

## Installation

1. Clone the repository to your local machine.
2. Install the required packages: `pip install -r requirements.txt`
3. Create a Discord bot and obtain its token. Add the bot to your server and give it appropriate permissions.
4. Run the bot using `python bot.py`

## Usage

- The bot will only respond to commands in the designated channel specified in the `config.json` file.
- Users can verify their wallet address by using the command: `!verify <wallet address>`.
- If the wallet address is valid and has not been used before, the bot will assign the designated role to the user.
- If the wallet address is invalid, the bot will not assign any roles and log the attempt in a `log.txt` file.
- If the wallet address has already been used by another user, the bot will not assign any roles and inform the user.

## Configuration


- `channel_id`: The ID of the channel where the bot will react to commands.
- `role_id`: The ID of the role to be assigned to users who successfully provide a valid wallet address.
- `wallet_list_file`: The name of the file containing the list of valid wallet addresses for verification.
- `used_wallets_file`: The name of the file containing the list of wallet addresses that have already been used by other users.
- `!verify`: The prefix to be used before bot commands.

## Credits

This bot was created by [yeeeeeeeeehor]. 