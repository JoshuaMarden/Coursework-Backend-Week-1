import json


def load_saved_stories():
    with open("stories.json", 'r') as f:
        stories_data = json.load(f)
    return stories_data


def save_stories(stories):
    with open("stories.json", 'w') as f:
        json.dump(stories, f, indent=4)
