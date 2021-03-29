# AO3 Fandom Scraper


## Description
A small desktop GUI app built with Python for scraping the fandoms pages on [Archive of Our Own](https://archiveofourown.org/).

Within a genre (ex. [Anime & Manga](https://archiveofourown.org/media/Anime%20*a*%20Manga/fandoms)) and given a lower bound, it collates a list of the fandoms for which the number of works within the fandom exceeds the lower bound.

This app was created for personal use, to help discover new fandoms based on popularity (as prescribed by the number of works written for them).
<br /><strong>It is not associated with the Archive of Our Own project itself.</strong>
<br />The results themselves are updated as the site is updated.

<br /><br />

Built as an alternative to the [AO3 Chrome extension](https://github.com/tiangela1027/AO3-Chrome-Extension), which provides the same functionality but within the Chrome browser. This app serves a nicer-looking GUI ran with Python, with smoother usage and the ability to print the scraped results for viewing.

## Installation

Download the repo and extract the folder from the zip. (Tested for Windows, but it should work on Mac.)

Run the following commands on the command line:
<br />
```
pip install selenium
pip install bs4
```

Run the following within the root folder:
<br />
```
python ao3-scraper.py
```

## Usage

Upon running the Python script, a GUI should pop up.

Within the GUI, select a genre (default 'Anime & Manga') and input a lower bound (default 1000).
<br />Click the 'Submit' button and wait for the results to print (there may be some delay for at most ten seconds, in which the application does not respond - please be patient.)

The scraped results are editable - feel free to make notes in the text window, or save the text to a separate file.
<br /><strong>Warning</strong>: the results will not be saved by the application, and will be overwritten if you execute another query.

## Additional Notes

The currently supported genres are 
- Anime & Manga
- Movies
- TV Shows
- Video Games

Contributions are welcome.

## License

This project is licensed under the terms of the MIT license.
