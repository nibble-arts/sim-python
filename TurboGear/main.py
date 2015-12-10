from tg import expose, TGController, AppConfig

class RootController(TGController):
    @expose()
    def index(self):
        return 'Hello World'