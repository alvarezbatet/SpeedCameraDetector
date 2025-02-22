from kivy_garden.mapview.view import MapView
from kivy.clock import Clock
from kivy.app import App
from marketmarker import MarketMarker

class RadarsMapView(MapView):
    getting_markets_timer = None
    radar_names = []

    def start_getting_markets_in_fov(self):
        # After one second, get the markets in field of view
        try:
            self.getting_markets_timer.cancel()
        except:
            pass
        self.getting_markets_timer = Clock.schedule_once(self.get_radars_in_fov, 1)

    def get_radars_in_fov(self, *args):
        app = App.get_running_app()
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        with open("radars.txt", "r") as myfile:
            radars = myfile.readlines()[0]
            for radar in radars.split(','):
                radar = radar.split(' ')
                if radar in self.radar_names:
                    continue
                else:
                    self.add_radar(radar)

    def add_radar(self, radar):
        # Create the MarketMarket
        lat, lon = radar[0], radar[1]
        marker = MarketMarker(lat=lat, lon=lon, source="marker2.png")
        marker.market_data = radar
        # ADD the MarketMarker to the map
        self.add_widget(marker)
        # Keep track of the marker's name
        name = None
        self.radar_names.append(radar)