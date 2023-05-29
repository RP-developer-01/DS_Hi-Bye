# Discord Bot

This is a simple Discord bot that sends welcome and goodbye messages to new members joining or leaving a server. The bot uses the Discord.py library and requires a bot token to function properly.

## Functionality

- Sends a random welcome message from a predefined list to new members when they join a server.
- Sends a random goodbye message from a predefined list when members leave a server.
- The bot logs in as a user and requires the necessary permissions to access member and message data.

## Installation

To use this bot, you need to follow these steps:

1. Clone or download the repository to your local machine.
2. Install the required dependencies by running the following command in your terminal:

   ```
   pip install -r requirements.txt
   ```

3. Obtain a bot token from the Discord Developer Portal by creating a new bot application.
4. Replace `'YOUR_BOT_TOKEN'` in the code with the bot token you obtained.
5. Customize the `welcome_messages` and `goodbye_messages` lists with your own messages or translations.
6. Set the `CHANNEL_NAME_MESSAGE` to the name of the channel where you want the welcome and goodbye messages to be sent.
7. Run the bot by executing the following command:

   ```
   python bot.py
   ```

8. The bot should now be online and ready to respond to events in your Discord server.

Make sure to invite the bot to your server using the OAuth2 URL generated in the Discord Developer Portal.

## Contributions

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please create a new issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code as per the terms of the license.
