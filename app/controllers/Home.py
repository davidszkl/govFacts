from . import application


class Home:
    @application.app.get("/")
    def home():
        return []