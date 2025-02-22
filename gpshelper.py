from kivy.app import App
from kivy.utils import platform
from kivymd.uix.dialog.dialog import MDDialog
import geopy.distance
from kivy.core.audio import SoundLoader
from kivy.clock import Clock

class GpsHelper():
    has_center_map = False
    sound100 = SoundLoader.load('radar100.wav')
    sound500 = SoundLoader.load('radar300.wav')
    found500 = False
    found100 = False
    lat = None
    lon = None

    def run(self):
        gps_blinker = App.get_running_app().root.ids.mapview.ids.blinker
        gps_blinker.blink()
        if platform == 'android':
            from android.permissions import Permission, request_permissions
            def callback(permission, results):
                if all([res for res in results]):
                    print("Got all permissions")
                else:
                    print("Did not get all permissions")
            request_permissions([Permission.ACCESS_COARSE_LOCATION,
                                 Permission.ACCESS_FINE_LOCATION], callback)
        if platform == "android":
            from plyer import gps
            gps.configure(on_location=self.update_blinker_position,
                          on_status=self.on_auth_status)
            gps.start(minTime=100, minDistance=0)

    def update_blinker_position(self, *args, **kwargs):
        my_lat = kwargs['lat']
        my_lon = kwargs['lon']
        self.lat = my_lat
        self.lon = my_lon
        print("Gps Position", my_lat, my_lon)
        gps_blinker = App.get_running_app().root.ids.mapview.ids.blinker
        gps_blinker.lat = my_lat
        gps_blinker.lon = my_lon
        app = App.get_running_app()
        if not self.has_center_map:
            map = app.root.ids.mapview
            map.center_on(my_lat, my_lon)
            self.has_center_map = True

    def check_for_radar(self, dt):
        lat, lon = self.lat, self.lon
        def reset_100(dt):
            self.found100 = False
        def reset_500(dt):
            self.found500 = False
        mapview = App.get_running_app().root.ids.mapview
        mapview.center_on(lat, lon)
        coords_1 = (lat, lon)
        for radar in mapview.radar_names:
            coords_2 = (radar[0], radar[1])
            distance = geopy.distance.geodesic(coords_1, coords_2).km
            if distance < .3 and distance > .1 and not self.found500:
                if self.sound500:
                    self.sound500.play()
                    self.found500 = True
                    Clock.schedule_once(reset_500, 40)
            elif distance < .1 and not self.found100:
                if self.sound100:
                    self.sound100.play()
                    self.found100 = True
                    Clock.schedule_once(reset_100, 15)

    def on_auth_status(self, general_status, status_message):
        if general_status == "provider-enabled":
            pass
        else:
            self.open_gps_access_popup()

    def open_gps_access_popup(self):
        dialog = MDDialog(title="GPS Error", text="You need to enable GPS access for the app to function properly")
        dialog.size_hint = [.8, .8]
        dialog.pos_hint = {'center_x': .5, 'center_y': .5}
        dialog.open()