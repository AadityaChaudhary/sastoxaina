from django.db import models

# Create your models here.
class Product(models.Model):
    category = models.CharField(max_length=255, default=True)
    title = models.CharField(max_length=255,default=True)
    image = models.URLField(default=True)
    link = models.URLField(default=True)
    price = models.CharField(max_length=50, default=True)
    description = models.TextField(default="-")
    model = models.CharField(max_length=255,default=True)
    ram = models.CharField(max_length=50,default=True)
    generation = models.CharField(max_length=200,default="-")
    display = models.CharField(max_length=200,default="-")
    storage = models.CharField(max_length=200,default="-")
    processor = models.CharField(max_length=250,default="-", blank=True)
    touchscreen = models.CharField(max_length=100,default="-", blank=True)
    graphics = models.CharField(max_length=250,default="-", blank=True)
    maximum_display_resulation = models.CharField(max_length=200,default="-", blank=True)
    color = models.CharField(max_length=100,default="-", blank=True)
    warrenty = models.CharField(max_length=100,default="-", blank=True)
    insurance = models.CharField(max_length=100,default="-", blank=True)
    battery = models.CharField(max_length=100,default="-", blank=True)
    operating_system = models.CharField(max_length=200,default="-", blank=True)
    ports_and_connectivity = models.CharField(max_length=400,default="-", blank=True)
    brand = models.CharField(max_length=100, default="-", blank=True)
    p_speed = models.CharField(max_length=200, default="-", blank=True)
    img1 = models.URLField(default=True, blank=True)
    img2 = models.URLField(default=True, blank=True)
    img3 = models.URLField(default=True, blank=True)
    logo_url = models.URLField(default=True, blank=True)


    def __str__(self):
        return self.title
    
class ProductNeo(models.Model):
    category = models.CharField(max_length=255, default=True)
    title = models.CharField(max_length=255,default=True)
    image = models.URLField(default=True)
    link = models.URLField(default=True)
    price = models.CharField(max_length=50, default=True)
    description = models.TextField(default="-")
    model = models.CharField(max_length=255,default=True)
    ram = models.CharField(max_length=50,default=True)
    generation = models.CharField(max_length=200,default="-")
    display = models.CharField(max_length=200,default="-")
    storage = models.CharField(max_length=200,default="-")
    processor = models.CharField(max_length=250,default="-", blank=True)
    touchscreen = models.CharField(max_length=100,default="-", blank=True)
    graphics = models.CharField(max_length=250,default="-", blank=True)
    maximum_display_resulation = models.CharField(max_length=100,default="-", blank=True)
    color = models.CharField(max_length=100,default="-", blank=True)
    warrenty = models.CharField(max_length=100,default="-", blank=True)
    insurance = models.CharField(max_length=100,default="-", blank=True)
    battery = models.CharField(max_length=100,default="-", blank=True)
    operating_system = models.CharField(max_length=200,default="-", blank=True)
    ports_and_connectivity = models.CharField(max_length=400,default="-", blank=True)
    brand = models.CharField(max_length=100, default="-", blank=True)
    p_speed = models.CharField(max_length=200, default="-", blank=True)
    img1 = models.URLField(default=True, blank=True)
    img2 = models.URLField(default=True, blank=True)
    img3 = models.URLField(default=True, blank=True)
    logo_url = models.URLField(default=True, blank=True)


    def __str__(self):
        return self.title
    

class ProductItti(models.Model):
    category = models.CharField(max_length=255, default=True)
    title = models.CharField(max_length=255,default=True)
    image = models.URLField(default=True)
    link = models.URLField(default=True)
    price = models.CharField(max_length=50, default=True)
    description = models.TextField(default="-")
    model = models.CharField(max_length=255,default=True)
    ram = models.CharField(max_length=50,default=True)
    generation = models.CharField(max_length=200,default="-")
    display = models.CharField(max_length=200,default="-")
    storage = models.CharField(max_length=200,default="-")
    processor = models.CharField(max_length=250,default="-", blank=True)
    touchscreen = models.CharField(max_length=100,default="-", blank=True)
    graphics = models.CharField(max_length=250,default="-", blank=True)
    maximum_display_resulation = models.CharField(max_length=100,default="-", blank=True)
    color = models.CharField(max_length=100,default="-", blank=True)
    warrenty = models.CharField(max_length=100,default="-", blank=True)
    insurance = models.CharField(max_length=100,default="-", blank=True)
    battery = models.CharField(max_length=100,default="-", blank=True)
    operating_system = models.CharField(max_length=200,default="-", blank=True)
    ports_and_connectivity = models.CharField(max_length=400,default="-", blank=True)
    brand = models.CharField(max_length=100, default="-", blank=True)
    p_speed = models.CharField(max_length=200, default="-", blank=True)
    img1 = models.URLField(default=True, blank=True)
    img2 = models.URLField(default=True, blank=True)
    img3 = models.URLField(default=True, blank=True)
    logo_url = models.URLField(default=True, blank=True)


    def __str__(self):
        return self.title
    

class Filtered(models.Model):
    title = models.CharField(max_length=255,default=True)
    brand = models.CharField(max_length=100, default="-", blank=True)
    model = models.CharField(max_length=255,default=True)
    image = models.URLField(default=True)
    link = models.URLField(default=True)
    logo = models.URLField(default="https://www.infotechsnepal.com/wp-content/uploads/2023/02/InfoTechs-Logo.png")
    price = models.CharField(max_length=50, default=True)
    pprice = models.CharField(max_length=100, blank=True)
    processor = models.CharField(max_length=250, blank=True)
    processor_info = models.CharField(max_length=100, blank=True)
    processor_type = models.CharField(max_length=100, blank=True)
    generation = models.CharField(max_length=200,default="-")
    ramm = models.CharField(max_length=100, blank= True)
    ram = models.CharField(max_length=200,default=True)
    ram_type = models.CharField(max_length=100, blank=True)
    ram_speed = models.CharField(max_length=100, blank = True)
    graphics = models.CharField(max_length=250, blank=True)
    graphics_info = models.CharField(max_length=100, blank=True)
    graphics_type = models.CharField(max_length=100, blank=True)
    sstorage = models.CharField(max_length=100, blank=True)
    storage = models.CharField(max_length=200,default="-")
    storage_type = models.CharField(max_length=100, blank=True)
    display = models.CharField(max_length=100, blank=True)
    display_size = models.CharField(max_length=200, blank=True)
    touchscreen = models.CharField(max_length=100,default="-", blank=True)
    maximum_display_resulation = models.CharField(max_length=100,default="-", blank=True)
    battery = models.CharField(max_length=100,default="-", blank=True)
    operating_system = models.CharField(max_length=200,default="-", blank=True)
    description = models.TextField(default="-")
    color = models.CharField(max_length=100,default="-", blank=True)
    warrenty = models.CharField(max_length=100,default="-", blank=True)
    insurance = models.CharField(max_length=100,default="-", blank=True)
    ports_and_connectivity = models.CharField(max_length=400,blank=True)

    def __str__(self):
        return self.title
    
class FilteredItti(models.Model):
    title = models.CharField(max_length=255,default=True)
    brand = models.CharField(max_length=100, default="-", blank=True)
    model = models.CharField(max_length=255,default=True)
    image = models.URLField(default=True)
    link = models.URLField(default=True)
    logo = models.URLField(default="https://itti.com.np/pub/media/logo/stores/1/itti-logo.png")
    price = models.CharField(max_length=50, default=True)
    pprice = models.CharField(max_length=100, blank=True)
    processor = models.CharField(max_length=250, blank=True)
    processor_info = models.CharField(max_length=100, blank=True)
    processor_type = models.CharField(max_length=100, blank=True)
    generation = models.CharField(max_length=200,default="-")
    ramm = models.CharField(max_length=100, blank= True)
    ram = models.CharField(max_length=200,default=True)
    ram_type = models.CharField(max_length=100, blank=True)
    ram_speed = models.CharField(max_length=100, blank = True)
    graphics = models.CharField(max_length=250, blank=True)
    graphics_info = models.CharField(max_length=100, blank=True)
    graphics_type = models.CharField(max_length=100, blank=True)
    sstorage = models.CharField(max_length=100, blank=True)
    storage = models.CharField(max_length=200,default="-")
    storage_type = models.CharField(max_length=100, blank=True)
    display = models.CharField(max_length=100, blank=True)
    display_size = models.CharField(max_length=150, blank=True)
    touchscreen = models.CharField(max_length=100,default="-", blank=True)
    maximum_display_resulation = models.CharField(max_length=100,default="-", blank=True)
    battery = models.CharField(max_length=100,default="-", blank=True)
    operating_system = models.CharField(max_length=200,default="-", blank=True)
    description = models.TextField(default="-")
    color = models.CharField(max_length=100,default="-", blank=True)
    warrenty = models.CharField(max_length=100,default="-", blank=True)
    insurance = models.CharField(max_length=100,default="-", blank=True)
    ports_and_connectivity = models.CharField(max_length=400,blank=True)

    def __str__(self):
        return self.title
    

class FilteredNeo(models.Model):
    title = models.CharField(max_length=255,default=True)
    brand = models.CharField(max_length=100, default="-", blank=True)
    model = models.CharField(max_length=255,default=True)
    image = models.URLField(default=True)
    link = models.URLField(default=True)
    logo = models.URLField(default="https://neostore.com.np/assets/images/neologohigh.png")
    price = models.CharField(max_length=50, default=True)
    pprice = models.CharField(max_length=100, blank=True)
    processor = models.CharField(max_length=250, blank=True)
    processor_info = models.CharField(max_length=100, blank=True)
    processor_type = models.CharField(max_length=100, blank=True)
    generation = models.CharField(max_length=50,default="-")
    ramm = models.CharField(max_length=100, blank= True)
    ram = models.CharField(max_length=200,default=True)
    ram_type = models.CharField(max_length=100, blank=True)
    ram_speed = models.CharField(max_length=100, blank = True)
    graphics = models.CharField(max_length=250, blank=True)
    graphics_info = models.CharField(max_length=200, blank=True)
    graphics_type = models.CharField(max_length=200, blank=True)
    sstorage = models.CharField(max_length=200, blank=True)
    storage = models.CharField(max_length=200,default="-")
    storage_type = models.CharField(max_length=200, blank=True)
    display = models.CharField(max_length=200, blank=True)
    display_size = models.CharField(max_length=250, blank=True)
    touchscreen = models.CharField(max_length=100,default="-", blank=True)
    maximum_display_resulation = models.CharField(max_length=100,default="-", blank=True)
    battery = models.CharField(max_length=100,default="-", blank=True)
    operating_system = models.CharField(max_length=200,default="-", blank=True)
    description = models.TextField(default="-")
    color = models.CharField(max_length=100,default="-", blank=True)
    warrenty = models.CharField(max_length=100,default="-", blank=True)
    insurance = models.CharField(max_length=100,default="-", blank=True)
    ports_and_connectivity = models.CharField(max_length=400,blank=True)

    def __str__(self):
        return self.title
    

class ProductPhoneNeo(models.Model):
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    images = models.URLField(default=True)
    link = models.URLField(default=True)
    price_range = models.CharField(max_length=100)
    pprice = models.CharField(max_length=20,default=True)
    description = models.CharField(max_length=400, default=True)
    logo = models.URLField(default="https://neostore.com.np/assets/images/neologohigh.png")
    model = models.CharField(max_length=50,default=True)
    ram = models.CharField(max_length=200)
    display_size = models.CharField(max_length=200)
    storage = models.CharField(max_length=100,default=True)
    warranty = models.CharField(max_length=200)
    insurance = models.CharField(max_length=200, default=True)
    chipset = models.CharField(max_length=200)
    battery_power = models.CharField(max_length=200) 
    operating_system = models.CharField(max_length=200)
    brand = models.CharField(max_length=250)
    primary_camera = models.CharField(max_length=250)
    secondary_camera = models.CharField(max_length=250)
    sim_type = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    

class ProductPhoneDeal(models.Model):
    link = models.URLField()
    title = models.CharField(max_length=100,default=True, null=True)
    image_url = models.URLField(default=True)
    price_range = models.CharField(max_length=100, default=100, null=True)
    price = models.CharField(max_length=100, default=True, null=True)
    brand = models.CharField(max_length=100,default=True, null=True)
    model = models.CharField(max_length=200,default=True, null=True)
    color = models.CharField(max_length=200,default=True, null=True)
    sim_type = models.CharField(max_length=200, default=True, null=True)
    sound = models.CharField(max_length=200, default=True, null=True)
    date = models.CharField(max_length=200, default=True, null=True)
    dimensions = models.CharField(max_length=200, default=True, null=True)
    weight = models.CharField(max_length=200, default=True, null=True)
    display = models.CharField(max_length=200, default=True, null=True)
    type = models.CharField(max_length=200, default=True, null=True)
    touchscreen = models.CharField(max_length=200, default=True, null=True)
    resolution = models.CharField(max_length=200, default=True, null=True)
    density = models.CharField(max_length=200, default=True, null=True)
    protection = models.CharField(max_length=200, default=True, null=True)
    rear_camera = models.CharField(max_length=200, default=True, null=True)
    rear_camera_extra = models.CharField(max_length=250, default=True, null=True)
    camera_features = models.CharField(max_length=200, default=True, null=True)
    front_camera = models.CharField(max_length=200, default=True, null=True)
    front_camera_extra = models.CharField(max_length=200, default=True, null=True)
    video = models.CharField(max_length=200, default=True, null=True)
    processor = models.CharField(max_length=200, default=True, null=True)
    cpu = models.CharField(max_length=200, default=True, null=True)
    gpu = models.CharField(max_length=200, default=True, null=True)
    ram = models.CharField(max_length=200, default=True, null=True)
    storage = models.CharField(max_length=200, default=True, null=True)
    expandablememory = models.CharField(max_length=200, default=True, null=True)
    memorycardslot = models.CharField(max_length=200, default=True, null=True)
    operatingsystem = models.CharField(max_length=200, default=True, null=True)
    technology = models.CharField(max_length=200, default=True, null=True)
    wlan = models.CharField(max_length=200, default=True, null=True)
    nfc = models.CharField(max_length=200, default=True, null=True)
    usb = models.CharField(max_length=200, default=True, null=True)
    battery = models.CharField(max_length=200, default=True, null=True)
    charger = models.CharField(max_length=200, default=True, null=True)
    sensors = models.CharField(max_length=200, default=True, null=True)
    extra_sensor = models.CharField(max_length=200, default=True)
    warranty = models.CharField(max_length=200, default=True, null=True)

    def __str__(self):
        return self.title


