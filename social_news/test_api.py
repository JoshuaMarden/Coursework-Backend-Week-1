from api import app
import json
from unittest.mock import patch
import storage


@patch("api.load_saved_stories")
def test_get_stories(fake_load_saved_stories, test_client):

    fake_load_saved_stories.return_value = [{
        "created_at": "Sat, 26 Feb 2022 14:38:11 GMT",
        "id": 9,
        "score": 131,
        "title": "Biden Signs Executive Order To Deport All 340 Million Americans And Start From Scratch",
        "updated_at": "Mon, 28 Feb 2022 16:02:45 GMT",
        "url": "https://www.theonion.com/biden-signs-executive-order-to-deport-all-340-million-a-1851516638",
        "website": "www.theonion.com"
    }]

    response = test_client.get("/stories")
    body = response.json

    assert response.status_code == 200
    assert type(body) == list
    assert body[0]["title"] == "Biden Signs Executive Order To Deport All 340 Million Americans And Start From Scratch"

    assert fake_load_saved_stories.called
    assert fake_load_saved_stories.call_count == 1


@patch("api.save_stories")
@patch("api.load_saved_stories")
def test_post_new_story(fake_load_saved_stories, fake_save_stories, test_client,
                        sample_news_stories, sample_new_story):

    fake_load_saved_stories.return_value = sample_news_stories

    response = test_client.post("/stories", json=sample_new_story)
    body = response.json

    assert response.status_code == 200
    assert fake_save_stories.call_count == 1
    assert body["title"] == sample_new_story["title"]

    # Extract the new story from the stories passed to save_stories
    newly_saved_stories = fake_save_stories.call_args[0][0]
    newly_added_story = next(story for story in newly_saved_stories
                             if story["url"] == sample_new_story["url"]
                             and story["title"] == sample_new_story["title"])

    # Assertions to ensure the new story was processed correctly
    assert newly_added_story["title"] == sample_new_story["title"]
    assert newly_added_story["url"] == sample_new_story["url"]


@patch("api.save_stories")
@patch("api.load_saved_stories")
def test_patch_story(fake_load_saved_stories, fake_save_stories,
                     sample_news_stories, sample_new_story, test_client):

    id_to_edit = sample_news_stories[0]["id"]
    fake_load_saved_stories.return_value = sample_news_stories
    response = test_client.patch(
        f"stories/{id_to_edit}/", json=sample_new_story)
    body = response.json

    assert response.status_code == 200
    assert fake_save_stories.call_count == 1
    assert body["title"] == sample_new_story["title"]

    # Extract the new story from the stories passed to save_stories
    newly_saved_stories = fake_save_stories.call_args[0][0]
    newly_added_story = next(story for story in newly_saved_stories
                             if story["url"] == sample_new_story["url"]
                             and story["title"] == sample_new_story["title"])

    # Assertions to ensure the new story was processed correctly
    assert newly_added_story["title"] == sample_new_story["title"]
    assert newly_added_story["url"] == sample_new_story["url"]


@patch("api.save_stories")
@patch("api.load_saved_stories")
def test_delete_story(fake_load_saved_stories, fake_save_stories,
                      sample_news_stories, test_client):

    id_to_delete = sample_news_stories[0]["id"]

    fake_load_saved_stories.return_value = sample_news_stories
    response = test_client.delete(f"/stories/{id_to_delete}/")

    assert response.status_code == 200
    assert fake_save_stories.call_count == 1

    newly_saved_stories = fake_save_stories.call_args[0][0]
    assert not any(
        story["id"] == id_to_delete for story in newly_saved_stories)
