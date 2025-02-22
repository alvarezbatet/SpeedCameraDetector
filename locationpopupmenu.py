from kivymd.uix.dialog.dialog import ListMDDialog

class LocationPopupMenu(ListMDDialog):
    def __init__(self, market_data):
        super().__init__()
        #headers = "FMID,MarketName,Website,Facebook,Twitter,Youtube,OtherMedia,street,city,County,State,zip,Season1Date,Season1Time,Season2Date,Season2Time,Season3Date,Season3Time,Season4Date,Season4Time,x,y,Location,Credit,WIC,WICcash,SFMNP,SNAP,Organic,Bakedgoods,Cheese,Crafts,Flowers,Eggs,Seafood,Herbs,Vegetables,Honey,Jams,Maple,Meat,Nursery,Nuts,Plants,Poultry,Prepared,Soap,Trees,Wine,Coffee,Beans,Fruits,Grains,Juices,Mushrooms,PetFood,Tofu,WildHarvested,updateTime"
        #headers = headers.split(',')
        attribute_name = "lon"
        attribute_value = market_data[0][0]
        setattr(self, attribute_name, attribute_value)
        attribute_name = "lat"
        attribute_value = market_data[0][1]
        setattr(self, attribute_name, attribute_value)