# Web Scraping and EPUB Generator

This is a Flask web application that allows you to scrape content from web pages and generate EPUB e-books from the scraped content. It provides a user-friendly interface for specifying URLs to scrape and CSS selectors to identify the elements to include in the EPUB book.

## Features

- Scrape content from multiple web pages.
- Include images from the scraped web pages in the EPUB book.
- User-friendly web interface with clear examples and instructions.

## Prerequisites

- Python 3.x
- Flask
- Requests
- Beautiful Soup (bs4)
- ebooklib
- Pillow (PIL)

You can install the required Python libraries using `pip`:
pip install flask requests beautifulsoup4 ebooklib Pillow

## Usage
Clone the repository or download the project files to your local machine.

Run the Flask application:
python your_app_name.py

Access the web application in your web browser by navigating to http://localhost:5000.

Fill out the form with the following details:

Book Title: Enter the title for your EPUB book.
URLs to Scrape (one per line): Provide the URLs of the web pages you want to scrape. Each URL should be on a separate line.
CSS Selectors for Elements to Scrape (one per line): Specify the CSS selectors for the elements you want to include in the EPUB book. Each selector should be on a separate line.
Click the "Generate EPUB" button to initiate the web scraping and EPUB generation process.

Once the process is complete, the EPUB file will be generated and automatically opened in your system's default EPUB reader.

Example
Here's how you can use the form:

Book Title: "My Web Scraping EPUB"
URLs to Scrape (one per line):
Here's how you can use the form:

Book Title: "My Web Scraping EPUB"
URLs to Scrape (one per line):
https://example.com/page1
https://example.com/page2
CSS Selectors for Elements to Scrape (one per line):
.title
.paragraph
.image
The example above will generate an EPUB titled "My Web Scraping EPUB" containing content scraped from the provided URLs, including elements with the specified CSS selectors.
