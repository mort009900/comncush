# Project Title: PDF Telegram Bot

## Overview
This project is a Telegram bot that processes PDF books, extracts text and images from them, and allows users to query the content through the bot. The bot utilizes Optical Character Recognition (OCR) to extract text from images when necessary.

## Project Structure
- **data/books**: Directory for storing PDF books to be processed by the application.
- **data/pages**: Directory for storing images of the pages extracted from the PDF books.
- **data/database.db**: SQLite database file that stores the extracted content from the PDF books.
- **utils/text_to_image.py**: Contains utility functions for extracting text from images using OCR techniques.
- **bot.py**: Main logic for the Telegram bot, handling user interactions and retrieving answers from the database.
- **config.py**: Configuration settings for the project, including the Telegram bot token and paths.
- **keep_alive.py**: Sets up a Flask web server to keep the bot running continuously.
- **pdf_parser.py**: Logic for parsing PDF files, extracting text and images, and storing results in the database.
- **requirements.txt**: Lists the Python dependencies required for the project.

## Setup Instructions
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using:
   ```
   pip install -r requirements.txt
   ```
4. Place your PDF books in the `data/books` directory.
5. Update the `config.py` file with your Telegram bot token.
6. Run the bot using:
   ```
   python bot.py
   ```

## Usage
- Start a chat with the bot on Telegram.
- Send a text query or an image to the bot.
- The bot will respond with the relevant content extracted from the PDF books.

## Deployment
To keep the bot running 24/7, consider deploying it on a cloud platform like Replit, Heroku, or any other service that supports Python applications. Use the `keep_alive.py` file to maintain the bot's uptime by running a simple web server.

## License
This project is licensed under the MIT License.