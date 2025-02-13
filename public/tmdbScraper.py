import requests
import csv
import os
from bs4 import BeautifulSoup

# Base URL (TMDb paginated search results)
BASE_URL = "https://www.themoviedb.org/tv?page="
HEADERS = {"User-Agent": "Mozilla/5.0"}

# Directory for saving HTML pages
HTML_DIR = "tmdb_html_data"
os.makedirs(HTML_DIR, exist_ok=True)

movies = []
MAX_PAGES = 100  # Adjust this to scrape more pages

for page in range(1, MAX_PAGES + 1):  # Loop for multiple pages
    url = f"{BASE_URL}{page}"
    print(f"Scraping page: {url}")  # Debugging output
    
    response = requests.get(url, headers=HEADERS)
    html_content = response.text

    # Save HTML to file
    html_filename = os.path.join(HTML_DIR, f"tmdb_page_{page}.html")
    with open(html_filename, "w", encoding="utf-8") as f:
        f.write(html_content)

    # Parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    movie_blocks = soup.find_all("div", class_="card style_1")
    
    for index, movie in enumerate(movie_blocks, start=len(movies) + 1):
        try:
            # Extract movie details
            title_tag = movie.find("h2").find("a")
            title = title_tag.text.strip() if title_tag else "N/A"

            year_tag = movie.find("p")  # The date is inside a <p> tag
            year = year_tag.text.strip() if year_tag else "N/A"

            rating_tag = movie.find("div", class_="user_score_chart")
            rating = rating_tag["data-percent"] if rating_tag else "N/A"

            image_tag = movie.find("img", class_="poster")
            image_url = image_tag["src"] if image_tag else "N/A"

            movie_url_tag = movie.find("a")
            tmdb_url = "https://www.themoviedb.org" + movie_url_tag["href"] if movie_url_tag else "N/A"

            movie_id = f"a{index}"

            movies.append([movie_id, title, year, rating, tmdb_url, image_url])

        except Exception as e:
            print(f"Skipping a movie due to an error: {e}")

# Save Data to CSV
def save_to_csv(filename, data):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Title", "Year", "Rating", "TMDb URL", "Image URL"])
        writer.writerows(data)

save_to_csv("tableA.csv", movies)
print(f"Scraped {len(movies)} movies and saved to tableA.csv")
print(f"HTML pages saved in '{HTML_DIR}' directory")
