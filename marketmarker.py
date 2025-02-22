from kivy_garden.mapview.view import MapMarkerPopup
from locationpopupmenu import LocationPopupMenu

class MarketMarker(MapMarkerPopup):
    market_data = []
    def on_release(self):
        #Open up the locationpopupmenu
        menu = LocationPopupMenu(self.market_data)
        menu.size_hint = [.8, .9]
        menu.open()
