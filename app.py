"""
Art Gallery - A simple and elegant Flask web application.
This is a beginner-friendly single-page website for an Art Gallery.
"""

from flask import Flask, render_template

# Create the Flask application instance
app = Flask(__name__)


# Define the single route for the home page
@app.route("/")
def home():
    """Render the main landing page."""
    return render_template("index.html")


# Run the application in debug mode on localhost:5000
if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)