from flask import Flask, render_template, request

    app = Flask(__name__)

    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "POST":
            name = request.form.get("name")
            adjective1 = request.form.get("adjective1")
            noun = request.form.get("noun")
            verb = request.form.get("verb")
            number = request.form.get("number")
            adjective2 = request.form.get("adjective2")

            story = f"""Once upon a time, {name} decided to learn cloud deployment on Microsoft Azure.

It was a {adjective1} day, and while working on a Flask project,
{name} built a Mad Libs game using a {noun} as the main character.

Every day, the app would {verb} exactly {number} times,
making users laugh at how {adjective2} their stories became.

Thanks to Azure App Service, the Flask Mad Libs app is now live on the internet
and anyone can play it from anywhere in the world!"""

            return render_template("story.html", story=story)

        return render_template("index.html")

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000, debug=True)
