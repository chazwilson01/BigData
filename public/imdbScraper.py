import requests
import csv
import os
from bs4 import BeautifulSoup

# Base URL (IMDb paginated search results)
BASE_URL = "https://www.imdb.com/search/title/?title_type=feature,tv_movie,tv_special,video,tv_series,tv_miniseries&interests=in0000001&start="
HEADERS = {"User-Agent": "Mozilla/5.0"}

# Directory for saving HTML pages
HTML_DIR = "html_data"
os.makedirs(HTML_DIR, exist_ok=True)

movies = []
MAX_PAGES = 80  # Adjust this to scrape more pages (each page has ~50 movies)

for page in range(1, MAX_PAGES * 50, 50):  # Loop for multiple pages
    url = f"{BASE_URL}{page}"
    print(f"Scraping page: {url}")  # Debugging output
    
    response = requests.get(url, headers=HEADERS)
    html_content = response.text
    
    # Save HTML to file
    html_filename = os.path.join(HTML_DIR, f"imdb_page_{page}.html")
    with open(html_filename, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    # Parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    movie_blocks = soup.find_all("div", class_="ipc-metadata-list-summary-item__c")

    for index, movie in enumerate(movie_blocks, start=len(movies) + 1):
        try:
            # Extract movie details
            title_tag = movie.find("h3", class_="ipc-title__text")
            title = title_tag.text.strip() if title_tag else "N/A"

            year_tag = movie.find("span", class_="sc-d5ea4b9d-7")
            year = year_tag.text.strip() if year_tag else "N/A"

            rating_tag = movie.find("span", class_="ipc-rating-star--rating")
            rating = rating_tag.text.strip() if rating_tag else "N/A"

            genre_tag = movie.find("span", class_="sc-d5ea4b9d-4")
            genre = genre_tag.text.strip() if genre_tag else "N/A"

            desc_tag = movie.find("div", class_="ipc-html-content-inner-div")
            description = desc_tag.text.strip() if desc_tag else "N/A"

            movie_url_tag = movie.find("a", class_="ipc-title-link-wrapper")
            imdb_url = "https://www.imdb.com" + movie_url_tag["href"] if movie_url_tag else "N/A"

            image_tag = movie.find("img", class_="ipc-image")
            image_url = image_tag["src"] if image_tag else "N/A"

            movie_id = f"b{index}"

            movies.append([movie_id, title, year, rating, genre, description, imdb_url, image_url])

        except Exception as e:
            print(f"Skipping a movie due to an error: {e}")

# Save Data to CSV
def save_to_csv(filename, data):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Title", "Year", "Rating", "Genre", "Description", "IMDb URL", "Image URL"])
        writer.writerows(data)

save_to_csv("tableB.csv", movies)
print(f"Scraped {len(movies)} movies and saved to tableB.csv")
print(f"HTML pages saved in '{HTML_DIR}' directory")
