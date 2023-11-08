from flask import Flask, request, jsonify
import os
import requests
from bs4 import BeautifulSoup
from ebooklib import epub
from cssselect import Selector
from PIL import Image
from io import BytesIO
import webbrowser

app = Flask(__name__)

def scrape_website(url, css_selectors):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            content_list = []

            book = epub.EpubBook()
            book.set_language('en')

            for selector in css_selectors:
                elements = soup.select(selector)

                # Process images in each element individually
                for element in elements:
                    for img_tag in element.select('img'):
                        if 'src' in img_tag.attrs:
                            img_url = img_tag['src']
                            if img_url.startswith('http') or img_url.startswith('https'):
                                img_response = requests.get(img_url)
                                if img_response.status_code == 200:
                                    img_data = BytesIO(img_response.content)
                                    img = Image.open(img_data)
                                    img_format = img.format.lower()
                                    img_file = f"image_{len(content_list)}.{img_format}"

                                    # Create EpubImage and add to the EPUB book
                                    epub_img = epub.EpubImage()
                                    epub_img.file_name = img_file
                                    epub_img.media_type = f"image/{img_format}"
                                    epub_img.content = img_response.content
                                    book.add_item(epub_img)

                                    # Set the img_tag['src'] to the image file
                                    img_tag['src'] = img_file

                content_list.append("\n".join(str(element) for element in elements))

            return content_list
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def generate_epub(title, content_list):
    book = epub.EpubBook()

    book.set_title(title)
    book.set_language('en')

    for index, content in enumerate(content_list, 1):
        chapter = epub.EpubHtml(title=f"Chapter {index}", file_name=f'chapter{index}.xhtml', lang='en')
        chapter.content = content
        book.add_item(chapter)
        book.toc.append(chapter)
        book.spine.append(chapter)

    epub.write_epub(f"{title}.epub", book, {})

@app.route('/')
def index():
    with open('index.html') as f:
        return f.read()

@app.route('/generate_epub', methods=['POST'])
def generate_epub_from_form():
    data = request.form
    book_title = data.get('book_title')
    urls = data.get('urls', '').splitlines()
    css_selectors = data.getlist('css_selectors')

    scraped_content = []

    for url in urls:
        content = scrape_website(url, css_selectors)
        if content:
            scraped_content.extend(content)

    if scraped_content:
        generate_epub(book_title, scraped_content)

        # Open the generated EPUB book in the default system application
        webbrowser.open(f"{book_title}.epub")

        return jsonify(success=True)
    else:
        return jsonify(success=False)

if __name__ == '__main__':
    app.run(debug=True)