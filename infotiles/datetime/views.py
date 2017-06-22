from infotiles.views import BaseTileView

class TileView(BaseTileView):
    template_name = "datetime/tile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = "today"
        return context
