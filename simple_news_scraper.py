import requests
from bs4 import BeautifulSoup

# Simple web scraper: gets latest headlines from a public news site
# Example site: BBC News (change URL if you want something else)

url = "https://www.bbc.com/news"  # Safe, public site - no login needed

print(f"Scraping headlines from: {url}")
print("-" * 50)

try:
    # Send request to the website
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # Check if request was successful

    # Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find headlines (BBC uses h2 or specific classes - this is a simple selector)
    headlines = soup.find_all(['h2', 'h3'], class_=['sc-2b5e3b35-0', 'sc-2b5e3b35-1'])  # BBC headline classes (may change)

    if not headlines:
        # Fallback: find any h2/h3 tags
        headlines = soup.find_all(['h2', 'h3'])

    # Print first 10 headlines
    count = 0
    for headline in headlines:
        text = headline.get_text().strip()
        if text and len(text) > 10:  # Skip empty or short ones
            print(f"{count+1}. {text}")
            count += 1
            if count >= 10:
                break

    if count == 0:
        print("No headlines found. The site structure may have changed.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching the page: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")

print("\nDone! This is a basic example - web scraping should respect robots.txt and site terms.")
