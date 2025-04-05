# Project Title: PDF Book Processing Telegram Bot

## Overview
This project is a Telegram bot designed to process PDF books, extract text and images from them, and provide users with the ability to query the content through a chat interface. The bot utilizes Optical Character Recognition (OCR) to extract text from images when necessary.

## Project Structure
- **data/**: Contains directories and files for storing books, pages, and the database.
  - **books/**: Directory for storing PDF books to be processed.
  - **pages/**: Directory for storing images of the pages extracted from the PDF books.
  - **database.db**: SQLite database file where the extracted content from the books is stored.

- **utils/**: Contains utility functions.
  - **text_to_image.py**: Utility functions for extracting text from images using OCR techniques.

- **bot.py**: Main logic for the Telegram bot. Handles user interactions, processes text and images, and retrieves answers from the database based on user queries.

- **config.py**: Configuration settings for the project, including the Telegram bot token, database path, and folder paths for books and pages.

- **keep_alive.py**: Sets up a simple Flask web server to keep the bot running continuously. It defines a route that responds with a message indicating that the bot is alive.

- **pdf_parser.py**: Functions to initialize the database and process PDF books. Extracts text and images from the PDF files and stores them in the database.

- **requirements.txt**: Lists the dependencies required for the project, specifying the versions of each package needed.

## Setup Instructions
1. **Clone the Repository**: 
   ```
   git clone <repository-url>
   cd comncush
   ```

2. **Install Dependencies**: 
   Ensure you have Python installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Add PDF Books**: 
   Place your PDF books in the `data/books/` directory.

4. **Run the PDF Parser**: 
   Execute the `pdf_parser.py` script to extract content from the PDF books and store it in the database:
   ```
   python pdf_parser.py
   ```

5. **Start the Bot**: 
   Run the `bot.py` script to start the Telegram bot:
   ```
   python bot.py
   ```

6. **Keep the Bot Alive**: 
   The `keep_alive.py` script is included to ensure the bot runs continuously. Make sure to run this script if deploying on platforms like Replit.

## Usage
- Start a chat with the bot on Telegram.
- Send text queries or images to receive answers based on the content of the processed PDF books.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.