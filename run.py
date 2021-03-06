from app.models.ext import db
from app import create_app
from app.api_1_0 import bp
from app.api_1_0 import user, index, bg_index, task, note, notebook

app = create_app("DevelopConfig")
db.init_app(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
