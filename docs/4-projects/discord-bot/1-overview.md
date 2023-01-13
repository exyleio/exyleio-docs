# Overview

## Introduction

This is the documentation for the
[exyleio-discord-bot](https://github.com/exyleio/exyleio-discord-bot)
repository.

## Getting started

1. [Setup Exyle.io workspace](/docs/contribution-guides/developers/setting-up)

2. [Create a discord bot](https://discordjs.guide/preparations/setting-up-a-bot-application.html)
   if you haven't already. You must also enable all Privileged Gateway Intents.

   ![](/img/privileged-gateway-intents.png)

3. Create `.env` file inside the `exyleio-discord-bot` directory.

   ```dosini
   DISCORD_BOT_TOKEN=<DISCORD_BOT_TOKEN>
   DISCORD_BOT_ID=<DISCORD_BOT_ID>
   ```

4. Start the bot

   ```
   ./tool.sh run discord-bot
   ```

## Learning

Minimum required skills to contribute to this project:

- NodeJS
- npm CLI
- JavaScript
- Typescript
- discord.js

### Learning material

- [Discord developers documentation](https://discord.com/developers/docs)
- [Discord.js Guide](https://discordjs.guide)
- [Sapphire framework Documentation](https://sapphirejs.dev/docs/General/Welcome)
- [TypeScript Tutorial](https://www.typescripttutorial.net)
