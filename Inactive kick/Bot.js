const Discord = require('discord.js');
const fs = require('fs');
const { Client, GatewayIntentBits } = require('discord.js');
const client = new Discord.Client({
	intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMembers,
	],
});

client.on('ready', async () => {
    console.log(`Logged in as ${client.user.tag}!`);
    const guild = client.guilds.cache.get('SERVER_ID');
    if (!guild) {
      console.log(`Could not find guild with ID ${guildId}.`);
      return;
    }
    await guild.members.fetch(); // получаем список участников сервера
    const members = guild.members.cache.map(member => member.user.username);
    fs.writeFileSync('nicknames.txt', members.join('\n'));
    console.log(`Nicknames saved to file.`);
    client.destroy();
  });

client.login('DISCORD_BOT_TOKEN');