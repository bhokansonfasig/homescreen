from django.conf.urls import url

import importlib
import pkgutil

from . import views

# Get all tile view modules
viewmodules = {}
for module in pkgutil.iter_modules(["./infotiles"]):
    if module.ispkg and module.name!="migrations":
        viewmodules[module.name] = importlib.import_module("."+module.name+".views",
                                                           "infotiles")


urlpatterns = [
    url(r'^$', views.DesktopView.as_view(), name='desktop'),
]

for name,module in viewmodules.items():
    urlpatterns.append(
        url(r'^'+name+'/', module.TileView.as_view(), name=name)
    )
