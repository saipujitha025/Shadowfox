
#creating MobilePhone baseclass
class MobilePhone:
    def __init__(self, ScreenType ,NetworkType,DualSim,FrontCamera,
                 rearCamera,RAM,Storage):
        self.ScreenType="Touch Screen"
        self.NetworkType="5G"
        self.DualSim="True"
        self.FrontCamera="12MP"
        self.rearCamera="16MP"
        self.RAM="4GB"
        self.Storage="64GB"
    def make_call(self, number):
        print("Calling",number)
    def recieve_call(self, caller):
        print("Incoming call from",caller)
    def take_a_picture(self,camera_type):
        if camera_type=="rear":
            print("Taking picture with",self.rearCamera,"rearCamera")
        else:
            print("Taking picture with",self.FrontCamera,"FrontCamera")
#creating Apple child class
class Apple(MobilePhone):
    def __init__(self, model, ScreenType,NetworkType,DualSim, FrontCamera, rearCamera, RAM, Storage):
        #Using super() constructor for calling parents class constructor
        super().__init__(ScreenType,DualSim,NetworkType,FrontCamera, rearCamera, RAM, Storage)
        self.brand="Apple"
        self.model="model"
#creating samsung child class
class Samsung(MobilePhone):
    def __init__(self, model, DualSim,ScreenType,NetworkType, FrontCamera, rearCamera, RAM, Storage):
        #Using super() constructor for calling parents class constructor
        super().__init__(ScreenType, NetworkType, DualSim, FrontCamera, rearCamera, RAM, Storage)
        self.brand="Samsung"
        self.model="model"
#creating apple objects
iphone_12=Apple(model="iphone_15", FrontCamera="16MP",DualSim="True",ScreenType="TouchScreen",NetworkType="5G",
                rearCamera="32MP",RAM="4GB",Storage="32GB")
iphone_13=Apple(model="iphone_16", FrontCamera="16MP",DualSim="False",ScreenType="TouchScreen",NetworkType="5G",
                rearCamera="48MP",RAM="4GB",Storage="64GB")
#creating samsung objects
galaxy_s19=Samsung(model="galaxy_s19",DualSim="True",FrontCamera="16MP",ScreenType="TouchScreen",
                   NetworkType="5G",rearCamera="12MP",RAM="4GB",Storage="64GB")
galaxy_s20=Samsung(model="galaxy_s20",DualSim="False",FrontCamera="16MP",ScreenType="TouchScreen",
                   NetworkType="5G",rearCamera="48MP",RAM="4GB",Storage="64GB")
