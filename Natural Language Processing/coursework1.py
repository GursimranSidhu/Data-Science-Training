import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Base URLs
BASE_URL = "https://indianexpress.com/"
SECTION_URLS = [
    "https://indianexpress.com/latest-news/",
    "https://indianexpress.com/section/india/",
]

# Headers (avoid blocking)
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

# Get links from homepage
def get_homepage_links():
    articles = set()

    try:
        response = requests.get(BASE_URL, headers=HEADERS, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error fetching homepage:", e)
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup.find_all(["h2", "h3"]):
        a_tag = tag.find("a")

        if a_tag and a_tag.get("href"):
            title = a_tag.text.strip()
            link = a_tag["href"]

            # Fix relative URLs
            if link.startswith("/"):
                link = BASE_URL + link.lstrip("/")

            # Filter valid articles
            if "indianexpress.com/article" in link:
                articles.add((title, link))

    return list(articles)

# Get links from other sections
def get_section_links(url):
    articles = []

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching section {url}:", e)
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup.find_all("h2"):
        a_tag = tag.find("a")

        if a_tag and a_tag.get("href"):
            title = a_tag.text.strip()
            link = a_tag["href"]

            # Fix relative URLs
            if link.startswith("/"):
                link = BASE_URL + link.lstrip("/")

            if "indianexpress.com/article" in link:
                articles.append((title, link))

    return articles


# Get full article content
def get_article_text(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching article {url}:", e)
        return ""

    soup = BeautifulSoup(response.text, "html.parser")

    content = ""

    # Extract all paragraph text
    for p in soup.find_all("p"):
        text = p.get_text(strip=True)
        if text:
            content += text + " "

    return content.strip()


# Main function
def main():
    print("Fetching articles...")

    articles = get_homepage_links()

    # Add articles from sections
    for url in SECTION_URLS:
        articles.extend(get_section_links(url))

    # Remove duplicates
    articles = list(set(articles))

    print(f"Total articles found: {len(articles)}")

    # Limit to 25 articles
    articles = articles[:25]

    data = []

    for idx, (title, link) in enumerate(articles):
        print(f"Scraping article {idx+1}: {title}")

        article_text = get_article_text(link)

        combined_text = f"{title} | {link} | {article_text}"

        data.append({
            "NEWS_TITLE_Gursimran_NEWS_LINK_FULL_SCRAPED_TEXT": combined_text
        })

        # Polite delay
        time.sleep(2)

    # Create DataFrame
    df = pd.DataFrame(data)

    # Save CSV
    df.to_csv("indian_express_news.csv", index=False)

    print("Scraping completed. CSV saved!")


# -------------------------------
if __name__ == "__main__":
    main()