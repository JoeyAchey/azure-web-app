from flask import Flask, abort,  render_template
from datetime import datetime


FAVORITES = [
    {"id": 1, "title": "Pizza", "why": "I like choosing different toppings."},
    {"id": 2, "title": "Tacos", "why": "I like the variety of flavors."},
    {"id": 3, "title": "Ice cream", "why": "It is a great dessert."},
]

def create_app():
    app = Flask(__name__)
    setup_routes(app)
    return app


def index():
    return render_template(
        "index.html",
        name="Joey",
        hobby="coding",
        hours_per_week=5,
        fun_fact="I study computer science and marketing.",
        hour=datetime.now().hour,
        show_counter=True,
        favorites=FAVORITES,
    )
    
def favorite_detail(favorite_id: int):
    for favorite in FAVORITES:
        if favorite["id"] == favorite_id:
            return render_template(
                "favorite.html",
                favorite=favorite,
            )
    abort(404)

def setup_routes(app):
    app.route("/")(index)
    app.route("/favorites/<int:favorite_id>")(favorite_detail)


def run_app(debug: bool = True) -> None:
    app = create_app()
    app.run(debug=debug)


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)