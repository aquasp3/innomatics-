from flask import Flask, request

app = Flask(__name__)

@app.route("/display")
def display_name():
    name = request.args.get("name", "Guest")
    return name.upper()

if __name__ == "__main__":
    app.run(debug=True)
