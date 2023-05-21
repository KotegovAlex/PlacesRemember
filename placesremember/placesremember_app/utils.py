menu = [
    {'title': 'Places', 'url_name': 'places'},
    {'title': 'About', 'url_name': 'about'},
    {'title': 'Add Place', 'url_name': 'add_place'},
]


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(0)
        context['menu'] = user_menu
        return context
