import psycopg2
from flask import Flask, current_app, jsonify, request
from storage import load_saved_stories, save_stories
from datetime import datetime, timezone
import json

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return current_app.send_static_file("index.html")


@app.route("/add", methods=["GET"])
def addstory():
    return current_app.send_static_file("./addstory/index.html")


@app.route("/scrape", methods=["GET"])
def scrape():
    return current_app.send_static_file("./scrape/index.html")


def sort_stories(sort_category: str, order: str, stories: list) -> list:
    """Sorts a list of dict-stories depending on key (method) given"""
    if sort_category is None:
        return stories

    if order == "ascending":
        order_bool = False
    else:
        order_bool = True

    return sorted(stories, key=lambda x: x[sort_category], reverse=order_bool)


@app.route('/stories', methods=["GET", "POST"])
def manage_stories():

    stories = load_saved_stories()

    if request.method == "GET":
        args = request.args.to_dict()
        search = args.get("search")
        sort = args.get("sort")
        order = args.get("order")

        if not search:
            sorted_stories = sort_stories(sort, order, stories)
            return jsonify(sorted_stories), 200
        else:
            matching_stories = [
                story for story in stories if search.lower() in story["title"].lower()
            ]

            if matching_stories:
                sorted_matching_stories = sort_stories(
                    sort, order, matching_stories)
                return jsonify(sorted_matching_stories), 200
            else:
                return jsonify([]), 404

    if request.method == "POST":

        data = request.json
        used_ids = [story["id"] for story in stories]

        for id in used_ids:
            new_id = id + 1
            if new_id not in used_ids:
                break

        current_time = datetime.now(timezone.utc)
        formatted_time = current_time.strftime('%a, %d %b %Y %H:%M:%S GMT')

        new_story = {"created_at": formatted_time,
                     "id": new_id, "score": 0,
                     "title": data["title"], "url": data["url"],
                     "website": data["url"][:data["url"].find("/", 10)]}

        stories.append(new_story)
        save_stories(stories)
        return jsonify(new_story), 200


@ app.route('/stories/<int:id>/', methods=['PATCH', "DELETE"])
def modify_story(id):

    stories = load_saved_stories()

    if request.method == "PATCH":

        for story in stories:
            data = request.json

            if story["id"] == id:
                story["url"] = data["url"]
                story["title"] = data["title"]
                if story["url"] == "" or story["title"] == "":
                    return "Null not allowed in story details", 418

                save_stories(stories)
                return jsonify(story), 200

    if request.method == "DELETE":
        for index, story in enumerate(stories):
            if story["id"] == id:
                deleted_story = stories.pop(index)
                save_stories(stories)
                return jsonify(deleted_story), 200

    return jsonify("Article not found"), 404


@ app.route('/stories/<int:id>/votes', methods=['POST'])
def change_votes(id):

    stories = load_saved_stories()

    if request.method == "POST":
        data = request.json

        if "direction" not in data:
            return jsonify({"error": True,
                            "message": "Missing 'direction' key"}), 400

        for story in stories:
            if story["id"] == id:
                current_score = story["score"]
                if data["direction"] == "up":
                    story["score"] += 1
                elif data["direction"] == "down" and current_score > 0:
                    story["score"] -= 1
                elif data["direction"] == "down":
                    return jsonify({"error": True,
                                    "message": "Can't downvote for a "
                                    "story with a score of 0"}), 400
                else:
                    return jsonify({"error": "Invalid direction value"}), 400

                # Return the updated story
                save_stories(stories)
                return jsonify(story), 200

        # If the story is not found
        return jsonify({"error": True,
                        "message": "Story not found"}), 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
