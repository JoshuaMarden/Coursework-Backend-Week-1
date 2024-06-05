import psycopg2
from flask import Flask, current_app, jsonify, request
from storage import save_to_file, load_from_file
from datetime import datetime, timezone

stories = [
    {
        "created_at": "Sun, 20 Mar 2022 08:43:21 GMT",
        "id": 1,
        "score": 42,
        "title": "Voters Overwhelmingly Back Community Broadband in Chicago and Denver",
        "updated_at": "Tue, 22 Mar 2022 14:58:45 GMT",
        "url": "https://www.vice.com/en/article/xgzxvz/voters-overwhelmingly-back-community-broadband-in-chicago-and-denver",
        "website": "vice.com"
    },
    {
        "created_at": "Wed, 16 Mar 2022 11:05:33 GMT",
        "id": 2,
        "score": 23,
        "title": "eBird: A crowdsourced bird sighting database",
        "updated_at": "Fri, 18 Mar 2022 13:20:47 GMT",
        "url": "https://ebird.org/home",
        "website": "ebird.org"
    },
    {
        "created_at": "Sat, 09 Apr 2022 09:11:52 GMT",
        "id": 3,
        "score": 471,
        "title": "Karen Gillan teams up with Lena Headey and Michelle Yeoh in assassin thriller Gunpowder Milkshake",
        "updated_at": "Mon, 11 Apr 2022 17:13:29 GMT",
        "url": "https://www.empireonline.com/movies/news/gunpowder-milk-shake-lena-headey-karen-gillan-exclusive/",
        "website": "empireonline.com"
    },
    {
        "created_at": "Mon, 07 Feb 2022 06:21:19 GMT",
        "id": 4,
        "score": 101,
        "title": "Pfizers coronavirus vaccine is more than 90 percent effective in first analysis, company reports",
        "updated_at": "Wed, 09 Feb 2022 08:44:22 GMT",
        "url": "https://www.cnbc.com/2020/11/09/covid-vaccine-pfizer-drug-is-more-than-90percent-effective-in-preventing-infection.html",
        "website": "cnbc.com"
    },
    {
        "created_at": "Tue, 01 Mar 2022 12:31:45 GMT",
        "id": 5,
        "score": 87,
        "title": "Budget: Pensions to get boost as tax-free limit to rise",
        "updated_at": "Thu, 03 Mar 2022 15:29:58 GMT",
        "url": "https://www.bbc.co.uk/news/business-64949083",
        "website": "bbc.co.uk"
    },
    {
        "created_at": "Fri, 25 Mar 2022 10:22:36 GMT",
        "id": 6,
        "score": 22,
        "title": "Ukraine war: Zelensky honours unarmed soldier filmed being shot",
        "updated_at": "Sun, 27 Mar 2022 12:55:19 GMT",
        "url": "https://www.bbc.co.uk/news/world-europe-64938934",
        "website": "bbc.co.uk"
    },
    {
        "created_at": "Thu, 17 Mar 2022 09:28:42 GMT",
        "id": 7,
        "score": 313,
        "title": "Willow Project: US government approves Alaska oil and gas development",
        "updated_at": "Sat, 19 Mar 2022 11:34:53 GMT",
        "url": "https://www.bbc.co.uk/news/world-us-canada-64943603",
        "website": "bbc.co.uk"
    },
    {
        "created_at": "Wed, 23 Feb 2022 07:15:59 GMT",
        "id": 8,
        "score": 2,
        "title": "SVB and Signature Bank: How bad is US banking crisis and what does it mean?",
        "updated_at": "Fri, 25 Feb 2022 09:41:22 GMT",
        "url": "https://www.bbc.co.uk/news/business-64951630",
        "website": "bbc.co.uk"
    },
    {
        "created_at": "Sat, 26 Feb 2022 14:38:11 GMT",
        "id": 9,
        "score": 131,
        "title": "Aukus deal: Summit was projection of power and collaborative intent",
        "updated_at": "Mon, 28 Feb 2022 16:02:45 GMT",
        "url": "https://www.bbc.co.uk/news/uk-politics-64948535",
        "website": "bbc.co.uk"
    },
    {
        "created_at": "Thu, 24 Mar 2022 13:49:27 GMT",
        "id": 10,
        "score": 41,
        "title": "Dancer whose barefoot video went viral meets Camilla",
        "updated_at": "Sat, 26 Mar 2022 15:51:34 GMT",
        "url": "https://www.bbc.co.uk/news/uk-england-birmingham-64953863",
        "website": "bbc.co.uk"
    }
]

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


@app.route('/stories', methods=["GET", "POST", "DELETE"])
def manage_stories():
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

        # Get the current date and time
        current_time = datetime.now(timezone.utc)
        formatted_time = current_time.strftime('%a, %d %b %Y %H:%M:%S GMT')

        new_story = {"created_at": formatted_time,
                     "id": new_id, "score": 0,
                     "title": data["title"], "url": data["url"],
                     "website": data["url"][:data["url"].find("/", 10)]}

        stories.append(new_story)
        return jsonify(new_story), 200


@ app.route('/stories/<int:id>/', methods=['PATCH', "DELETE"])
def modify_story(id):

    if request.method == "PATCH":

        for story in stories:
            data = request.json

            if story["id"] == id:
                story["url"] = data["url"]
                story["title"] = data["title"]
                return jsonify(story), 200

    if request.method == "DELETE":
        for index, story in enumerate(stories):
            if story["id"] == id:
                deleted_story = stories.pop(index)
                return jsonify(deleted_story), 200

    return jsonify("Article not found"), 404


@ app.route('/stories/<int:id>/votes', methods=['POST'])
def change_votes(id):
    if request.method == "POST":
        data = request.json

        # Check if the data contains the direction key
        if "direction" not in data:
            return jsonify({"error": True,
                            "message": "Missing 'direction' key"}), 400

        # Find the story with the given id
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
                return jsonify(story), 200

        # If the story is not found
        return jsonify({"error": True,
                        "message": "Story not found"}), 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
