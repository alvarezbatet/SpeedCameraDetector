from kivymd.uix.dialog.dialog import MDInputDialog
from urllib import parse
from geopy.geocoders import Nominatim
from kivy.app import App

class SearchPopupMenu(MDInputDialog):
    title = 'Search by Address'
    text_button_ok = 'Search'
    def __init__(self):
        super().__init__()
        self.size_hint = [.9, .3]
        self.events_callback = self.callback

    def callback(self, *args):
        address = self.text_field.text
        self.geocode_get_lat_lon(address)

    def geocode_get_lat_lon(self, address):
        address = parse.quote(address)
        geolocator = Nominatim(user_agent="alvarezbatet@gmail.com")
        location = geolocator.geocode(address)
        if location:
            latitude = location.latitude
            longitude = location.longitude
            app = App.get_running_app()
            mapview = app.root.ids.mapview
            mapview.center_on(latitude, longitude)
        else:
            print("Address not found")