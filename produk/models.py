import time
from django.db import models

# Create your models here.

class Brand(models.Model):

	class Meta:
		verbose_name = "Brand"
		verbose_name_plural = "Brands"

	nama = models.CharField(max_length=100)
	deskripsi = models.TextField('Deskripsi Brand')
	logo = models.ImageField()
	tgl_input = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.nama


class Aksesoris(models.Model):

	class Meta:
		verbose_name = "Aksesoris"
		verbose_name_plural = "Aksesoris"

	__KATEGORI_AKSESORIS = ('SAFETY', 'PROTECTION', 'MAINTENANCE', 'HYDRATION', 'TAS & PANNIERS', 
		'CARRIER & RAK', 'TRAINERS', 'SPEEDOMETER', 'OTHER')

	__SUBKATEGORI_AKSESORIS =(
		('hl', 'SAFETY - Helm'),
		('lp', 'SAFETY - Lampu Sepeda'),
		('bl', 'SAFETY - Bell'),
		('mr', 'SAFETY - Mirror'),
		('rf', 'SAFETY - Reflector'),

		('lk', 'PROTECTION - Locks'),
		('fr', 'PROTECTION - Fender'),
		('cv', 'PROTECTION - Bike Cover'),
		('ch', 'PROTECTION - Chain Cover'),
		('pr', 'PROTECTION - Chain Stay Protector'), 

		('pm', 'MAINTENANCE - Pompa'),
		('st', 'MAINTENANCE - Standart'),
		('tl', 'MAINTENANCE - Tools'),
		('pl', 'MAINTENANCE - Pelumas'),

		('bl', 'HYDRATION - Botol Minum'),
		('cg', 'HYDRATION - Cage Botol Minum'),
		('bg', 'HYDRATION - Water Bags'),

		('pn', 'TAS & PANNIERS - Panniers'),
		('ts', 'TAS & PANNIERS - Tas Sadel'),

		('cr', 'CARRIER & RAK - Carrier'),
		('bb', 'CARRIER & RAK - Baby Carrier'),
		('cr', 'CARRIER & RAK - Car Rack'),

		('tr','TRAINERS - Trainers'),

		('cl', 'SPEEDOMETER - Cyclo Computer'),

		('ft', 'OTHER - Footstep'),
		('hd', 'OTHER - Holder'),
		('kr', 'OTHER - Keranjang Sepeda'),
		('kt', 'OTHER - Kits'),
		('kn', 'OTHER - Konektor'),
		('tg', 'OTHER - Peralatan Touring'),
	)
	
	brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
	model = models.CharField(max_length=50)
	kategori = models.CharField('Kategori Aksesoris', max_length=100, choices=[(A[:3], A) for A in __KATEGORI_AKSESORIS])
	subkategori = models.CharField('Subkategori Aksesoris', max_length=100, choices=__SUBKATEGORI_AKSESORIS)
	deskripsi = models.TextField('Deskripsi Produk')
	harga = models.DecimalField(max_digits=5, decimal_places=2)
	kuantitas = models.IntegerField(default=0)
	tgl_input = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '(%s) %s %s' %(self.tahun_buat, self.brand, self.tipe)

	@classmethod
	def tampilkan_kategori(cls):
		return cls.__KATEGORI_AKSESORIS


class Apparel(models.Model):

	class Meta:
		verbose_name = "Apparel"
		verbose_name_plural = "Apparels"

	__KATEGORI_APPAREL = ('ARM WARMER', 'BAJU', 'BODY PROTECTOR', 'CELANA', 'JERSEY', 'KACAMATA', 'GLOVES', 'SEPATU',
		'TOPI', 'CLEAT SEPATU')
	
	brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
	model = models.CharField(max_length=50)
	kategori = models.CharField('Kategori Aksesoris', max_length=100, choices=[(C[:3], C) for C in __KATEGORI_APPAREL])
	deskripsi = models.TextField('Deskripsi Produk')
	harga = models.DecimalField(max_digits=10, decimal_places=2)
	kuantitas = models.IntegerField(default=0)
	gambar = models.ImageField()
	tgl_input = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s %s' %(self.brand, self.kategori)

	@classmethod
	def tampilkan_kategori(cls):
		return cls.__KATEGORI_APPAREL


class Sepeda(models.Model):

	class Meta:
		verbose_name = "Sepeda"
		verbose_name_plural = "Sepeda"

	__KATEGORI_SEPEDA = ('ROAD BIKE', 'MOUNTAIN BIKE', 'TOURING & CITY BIKE', 'BMX & DIRT JUMP BIKE',
		'FOLDING BIKE & OTHER', 'YOUTH & KIDS BIKE', 'FRAME SET')

	__SUBKATEGORI_SEPEDA = (
		('rp', 'ROAD BIKE - Road Performance'),
		('ce', 'ROAD BIKE - Commute or Endurance'),
		('gv', 'ROAD BIKE - Gravel Bike'),
		('fb', 'ROAD BIKE - Flatbar'),
		('wr', 'ROAD BIKE - Women\'s Road Bike'),

		('ht', 'MOUNTAIN BIKE - Hardtail'),
		('fs', 'MOUNTAIN BIKE - Full Suspension'),
		('wm', 'MOUNTAIN BIKE - Women\'s MTB'),

		('tr', 'TOURING & CITY BIKE - Touring'),
		('hb', 'TOURING & CITY BIKE - Hybrid'),
		('cb', 'TOURING & CITY BIKE - City Bike'),
		('us', 'TOURING & CITY BIKE - Urban Sport'),

		('dj', 'BMX & DIRT JUMP BIKE - Dirt Jump'),
		('fs', 'BMX & DIRT JUMP BIKE - BMX Freestyle'),
		('rs', 'BMX & DIRT JUMP BIKE - BMX Race'),

		('fd', 'FOLDING BIKE & OTHER - Folding Bike'),
		('ot', 'FOLDING BIKE & OTHER - Other'),

		('yb', 'YOUTH & KIDS BIKE - Youth Bike'),
		('kb', 'YOUTH & KIDS BIKE - Kids Bike'),

		('fs', 'FRAME SET - Bike Frame'),
	)

	brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
	model = models.CharField('Model', max_length=50)
	tahun = models.CharField('Tahun Rilis', max_length=50, choices=[(str(y), y) for y in range(2009, 2100)])
	kategori = models.CharField('Kategori Sepeda', max_length=100, choices=[(B[:3], B) for B in __KATEGORI_SEPEDA])
	subkategori = models.CharField('Subkategori Sepeda', max_length=100, choices=__SUBKATEGORI_SEPEDA)
	deskripsi = models.TextField('Deskripsi Produk')
	pic = models.ImageField()
	tgl_input = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '(%s) %s %s' %(self.tahun, self.brand, self.model)

	@classmethod
	def tampilkan_kategori(cls):
		return cls.__KATEGORI_SEPEDA


class DetailSepeda(models.Model):

	class Meta:
		verbose_name = "DetailSepeda"
		verbose_name_plural = "Detail Sepeda"

	__MATERIAL = (
		('alu', 'Aluminum/Alloy'),
		('car', 'Carbon Fiber'),
		('stl', 'Steel')
	)

	model = models.ForeignKey(Sepeda, on_delete=models.CASCADE)
	warna = models.CharField(max_length=50)
	ukuran = models.IntegerField('Size')
	kuantitas = models.IntegerField(default=0)
	harga = models.DecimalField(max_digits=10, decimal_places=2)

	#frameset
	frame = models.CharField('Material Frame', max_length=50, choices=__MATERIAL)
	fork = models.CharField('Material Fork', max_length=50, choices=__MATERIAL)

	#komponen
	handlebar = models.CharField(max_length=100)
	stem = models.CharField(max_length=100)
	headset = models.CharField(max_length=100)
	saddle = models.CharField(max_length=100)
	seatpost = models.CharField(max_length=100)
	brake_lever = models.CharField(max_length=100)
	front_brake = models.CharField(max_length=100)
	rear_brake = models.CharField(max_length=100)

	#drivetrain
	shifting_lever = models.CharField(max_length=100)
	front_derailleur = models.CharField(max_length=100)
	rear_derailleur = models.CharField(max_length=100)
	crankset = models.CharField(max_length=100)
	bottom_bracket = models.CharField(max_length=100)
	chain = models.CharField(max_length=100)
	cassette_sprocket = models.CharField(max_length=100)

	#wheelset
	tire = models.CharField('Ban', max_length=100)
	wheels = models.CharField('Velg', max_length=100)

	def __str__(self):
		return self.model


class Sparepart(models.Model):

	class Meta:
		verbose_name = "Sparepart"
		verbose_name_plural = "Spare Part"

	__KATEGORI_SPAREPART = ('BRAKE', 'DRIVE TRAIN', 'OTHER', 'SEATING', 'STEERING', 'WHEELS TIRES')

	__SUBKATEGORI_SPAREPART = (
		('bl', 'BRAKE - Brake Levers'),
		('bp', 'BRAKE - Brake Pads'),
		('br', 'BRAKE - Brake Rotors'),
		('cb', 'BRAKE - Cable Brakes'),
		('db', 'BRAKE - Disc Brakes'),
		('vb', 'BRAKE - V-Brakes'),

		('bb', 'DRIVE TRAIN - Bottom Bracet'),
		('ch', 'DRIVE TRAIN - Chain'),
		('cr', 'DRIVE TRAIN - Chainring'),
		('fc', 'DRIVE TRAIN - Front Chainwheel'),
		('fd', 'DRIVE TRAIN - Front Derailleur'),
		('rd', 'DRIVE TRAIN - Rear Derailleur'),
		('sh', 'DRIVE TRAIN - Shifter'),
		('sc', 'DRIVE TRAIN - Shifter Cable'),
		('sp', 'DRIVE TRAIN - Sprocket'),

		('bl', 'OTHER - Belt'),
		('do', 'OTHER - Drop Out'),
		('la', 'OTHER - Linkage'),
		('op', 'OTHER - Other Part'),
		('qr', 'OTHER - Quick Release SetLock'),
		('sn', 'OTHER - spoke and Nipple'),
		('pd', 'OTHER - Pedal'),

		('sd', 'SEATING - Sadel'),
		('sc', 'SEATING - Seat Clamp'),
		('sp', 'SEATING - Seat Post'),

		('be', 'STEERING - Bar End'),
		('bt', 'STEERING - Bar Tape'),
		('fr', 'STEERING - Fork'),
		('hg', 'STEERING - Handle Grip'),
		('hs', 'STEERING - Handle stem'),
		('hb', 'STEERING - Handle Bar'),
		('hs', 'STEERING - Head Set'),
		('sh', 'STEERING - Shok'),

		('tr', 'WHEELS & TIRES - Tire'),
		('tb', 'WHEELS & TIRES - Tube'), 
		('fh', 'WHEELS & TIRES - Front Hub'),
		('rh', 'WHEELS & TIRES - Rear Hub'),
		('rm', 'WHEELS & TIRES - Rim'),
		('rt', 'WHEELS & TIRES - Rim Tape'),
		('ws', 'WHEELS & TIRES - Wheel Set'),
	)

	brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
	model = models.CharField(max_length=50)
	kategori = models.CharField('Kategori Spare Part', max_length=100, choices=[(P[:3], P) for P in __KATEGORI_SPAREPART])
	subkategori = models.CharField('Subkategori Spare Part', max_length=100, choices=__SUBKATEGORI_SPAREPART)
	deskripsi = models.TextField('Deskripsi Produk')
	harga = models.DecimalField(max_digits=5, decimal_places=2)
	kuantitas = models.IntegerField(default=0)
	tgl_input = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.model

	@classmethod
	def tampilkan_kategori(cls):
		return cls.__KATEGORI_SPAREPART