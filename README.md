# Quote-Scraper

## Overview

The Quote Scraper is a Python script that allows users to search for quotes by specific authors from the [Quotes to Scrape](http://quotes.toscrape.com/) website. This repository provides a CLI tool to search for quotes and handles various edge cases to ensure robust functionality.

## Features

- Search for quotes by author name.
- Handles various edge cases, including empty input and partial matches.
- Includes automated tests to verify functionality.

## Installation

To use this tool, you need to install the required Python packages. Ensure you have Python 3.6 or higher installed.

1. Clone the repository:

   ```bash
    git clone https://github.com/yourusername/quote-scraper.git
    cd quote-scraper
    ```
   
2. Create and activate a virtual environment (optional but recommended):
    ```commandline
   python -m venv venv
   source venv/bin/activate  
   
   On Windows use: venv\Scripts\activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
## Usage

You can run the script from the command line to search for quotes 
by a specific author. Here’s how to use it:

   ```bash
    python scrapping.py --author "Author Name"
   ```

Replace "Author Name" with the name of the author you want to search for. For example:

```bash
    python scrapping.py --author "Eleanor"
```
