menu = [
    {"title": "Main Page", "url_name": "home"},
    {"title": "About", "url_name": "about"},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context["menu"] = menu
        return context
