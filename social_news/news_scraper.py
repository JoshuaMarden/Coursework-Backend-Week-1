from urllib.request import urlopen
from datetime import datetime, timezone
from bs4 import BeautifulSoup
from storage import save_stories, load_saved_stories
import requests


def get_html(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    return response.text


def parse_stories_bs(html: str) -> list:
    titles_and_urls = []
    soup = BeautifulSoup(html, "html.parser")
    div_elements = soup.find_all("div", class_="grid-iTt_Zp4a")

    for div_element in div_elements:
        a_elements = div_element.find_all("a", class_="card-DmjQR0Aa")

        for a_element in a_elements:
            url = a_element.get("href")
            title_div = a_element.find("div", class_="apply-overflow-tooltip")
            title = title_div.get(
                "data-overflow-tooltip-text") if title_div else None

            if url and title:
                titles_and_urls.append((title, url))

    return titles_and_urls


def update_stories(titles_and_urls: list) -> None:

    stories = load_saved_stories()

    for details in titles_and_urls:

        used_ids = [story["id"] for story in stories]
        if not used_ids:
            used_ids = [0]

        for id in used_ids:
            new_id = id + 1
            if new_id not in used_ids:
                break

        current_time = datetime.now(timezone.utc)
        formatted_time = current_time.strftime('%a, %d %b %Y %H:%M:%S GMT')

        new_story = {"created_at": formatted_time,
                     "id": new_id, "score": 0,
                     "title": details[0], "url": details[1],
                     "website": details[1][:details[1].find("/", 10)]}
        stories.append(new_story)

        print(new_story)

    save_stories(stories)


if __name__ == "__main__":
    trading_view_url = "https://www.tradingview.com/news/"
    trading_view_html_doc = get_html(trading_view_url)

    story_details = parse_stories_bs(trading_view_html_doc)
    update_stories(story_details)
