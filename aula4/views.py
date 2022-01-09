
def init_app(app):

    @app.route("/")
    def index():
        return "Hello CodeShow"


    @app.route("/contato")
    def contato():
        return "<form><input type='text'></input></form>"
