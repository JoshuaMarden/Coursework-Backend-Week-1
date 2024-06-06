import pytest
from flask.testing import FlaskClient
from api import app


@pytest.fixture
def test_client() -> FlaskClient:
    return app.test_client()


@pytest.fixture
def sample_news_stories():
    return [
        {
            "created_at": "Sat, 26 Feb 2022 14:38:11 GMT",
            "id": 1,
            "score": 131,
            "title": "Biden Signs Executive Order To Deport All 340 Million Americans And Start From Scratch",
            "updated_at": "Mon, 28 Feb 2022 16:02:45 GMT",
            "url": "https://www.theonion.com/biden-signs-executive-order-to-deport-all-340-million-a-1851516638",
            "website": "http://www.theonion.com"
        },
        {
            "created_at": "Wed, 13 May 2022 11:20:22 GMT",
            "id": 2,
            "score": 189,
            "title": "Alec Baldwin To Host Exciting New Game Show 'Is It Loaded?'",
            "updated_at": "Mon, 28 Feb 2022 16:02:45 GMT",
            "url": "https://babylonbee.com/news/alec-baldwin-to-host-exciting-new-game-show-is-it-loaded",
            "website": "https://babylonbee.com"
        },
        {
            "created_at": "Thur, 23 Aug 2022 13:03:18 GMT",
            "id": 3,
            "score": 245,
            "title": "Gorilla Mother Constantly Reminding Children To Slouch",
            "updated_at": "Mon, 28 Feb 2022 16:02:45 GMT",
            "url": "https://www.theonion.com/gorilla-mother-constantly-reminding-children-to-slouch-1851515892",
            "website": "https://www.theonion.com"
        },
    ]


@pytest.fixture
def sample_new_story():
    return {
        "title": "Last five years don't count because I had my fingers crossed, says Sunak",
        "url": "https://www.thedailymash.co.uk/politics/last-five-years-dont-count-because-i-had-my-fingers-crossed-says-sunak-20240604248378"
    }
