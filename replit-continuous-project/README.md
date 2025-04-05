# Replit Continuous Project

## Overview
This project is designed to create a Telegram bot that processes PDF books, extracts text and images from them, and allows users to interact with the content through a chat interface. The bot utilizes Optical Character Recognition (OCR) to handle images and provides a seamless experience for users seeking information from the books.

## Project Structure
- **data/books**: Directory for storing PDF books that the application will process.
- **data/pages**: Directory for storing images extracted from the PDF pages.
- **utils/text_to_image.py**: Contains utility functions for extracting text from images using OCR techniques.
- **.replit**: Configuration settings specific to the Replit environment.
- **replit.nix**: Defines the environment and dependencies for the Replit project.
- **bot.py**: Main logic for the Telegram bot, handling user interactions and processing requests.
- **config.py**: Holds configuration constants such as the Telegram bot token and paths for books and pages.
- **keep_alive.py**: Sets up a simple Flask web server to keep the project running continuously on Replit.
- **pdf_parser.py**: Functions to initialize the database and process PDF books, extracting text and images.
- **requirements.txt**: Lists the Python dependencies required for the project.

## Setup Instructions
1. Clone the repository or download the project files.
2. Place your PDF books in the `data/books` directory.
3. Install the required dependencies by running:
   ```
   pip install -r requirements.txt
   ```
4. Update the `config.py` file with your Telegram bot token.
5. Run the project using the command specified in the `.replit` file.

## Usage
- Start the bot by running `bot.py`.
- Interact with the bot on Telegram by sending text or images.
- The bot will respond with relevant information extracted from the PDF books.

## License
This project is open-source and available for modification and distribution under the MIT License.