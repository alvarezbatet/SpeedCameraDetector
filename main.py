from kivymd.app import MDApp
from radarsmapview import RadarsMapView
import sqlite3
from searchpopupmenu import SearchPopupMenu
import geocoder
from kivy.app import App
from kivy.uix.button import Button
from gpshelper import GpsHelper
from kivy.clock import Clock

class MainApp(MDApp):
    connection = None
    cursor = None
    search_menu = None
    clock = None
    def on_start(self):
        # Inititalize GPS
        self.gps = GpsHelper()
        self.gps.run()
        #Connect to database
        self.connection = sqlite3.connect("markets.db")
        self.cursor = self.connection.cursor()
        #Instantiate SearchPopupMenu
        self.search_menu = SearchPopupMenu()

    def location_press(self):
        g = geocoder.ip('me')
        [lat, lon] = g.latlng
        app = App.get_running_app()
        mapview = app.root.ids.mapview
        mapview.center_on(lat, lon)

    def start_tracking(self):
        #self.gps.update_blinker_position(lat=42.346428, lon=1.954628)
        self.clock = Clock.schedule_interval(self.gps.check_for_radar, 1)

    def stop_tracking(self):
        self.clock.cancel()

MainApp().run()