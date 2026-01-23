from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    # We changed the response to HTML to verify deployment
    return "<h1>Kaniko Build & Deploy Successful!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
