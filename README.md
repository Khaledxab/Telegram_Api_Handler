# Telegram Bot

This is a simple Python script that acts as a Telegram bot and saves received messages in a text file. The bot can be run with a graphical interface, a terminal interface, or both, depending on the user's preference.

## Features

- Receive messages from Telegram users.
- Display received messages in a graphical interface (optional).
- Print received messages in the terminal (optional).
- Save received messages in a text file ("messages.txt").

## Requirements

- Python 3
- `python-telegram-bot` library (install with `pip install python-telegram-bot`)
- `tkinter` library (required for the graphical interface)

## Usage

1. Clone the repository or download the script file.

2. Install the required libraries if not already installed:

   ```bash
   pip install python-telegram-bot
   ```

3. Replace `'token'` with your actual bot token in the script.

4. Run the script:

   ```bash
   python3 app.py
   ```

5. Choose the desired interface option when prompted:
   - Enter `1` for the graphical interface.
   - Enter `2` for the terminal interface.
   - Enter `3` for both graphical and terminal interfaces.

6. Interact with the Telegram bot by sending messages.

7. Received messages will be displayed in the chosen interface(s) and saved in the "messages.txt" file.

8. To stop the bot, press Ctrl+C in the terminal or close the graphical interface window.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to modify and adapt the code according to your needs.
