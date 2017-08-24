from .models import Brand, Aksesoris, Apparel, Sepeda, Sparepart

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
# Create your views here.


# generic view index
def __base(isindex):
	'''
		nilai[0] = isindex	--> bool
		nilai[1] = Brand 	--> obj list
		nilai[2] = navigasi	--> obj dict
	'''
	nilai = [isindex]
	brand = Brand.objects.filter(tgl_input__lte=timezone.now()).order_by('-tgl_input')

	navigasi = {
		'aksesoris': sorted(Aksesoris.tampilkan_kategori()), 
		'apparel': sorted(Apparel.tampilkan_kategori()), 
		'sepeda': sorted(Sepeda.tampilkan_kategori()), 
		'sparepart': sorted(Sparepart.tampilkan_kategori()),
	}

	nilai.extend([brand, navigasi])
	return nilai

def index(request):
	data_awal = __base(True) 
	context = {
		'isindex': data_awal[0],
		'brand': data_awal[1],
		'navigasi': data_awal[2],
	}
	return render(request, 'produk/index.html', context)

def kategori(request, nilai):
	data_awal = __base(False)
	context = {
		'isindex': data_awal[0],
		'navigasi': data_awal[2],
	}
	tampilkan = None
	template = None

	try:
		objek = eval(nilai.capitalize())
		
		if objek == Aksesoris or objek == Apparel or objek == Brand or objek == Sparepart:
			tampilkan = objek.objects.filter(tgl_input__lte=timezone.now()).order_by('-tgl_input')
			template = 'produk/parts.html'
		elif objek == Sepeda:
			tampilkan = Sepeda.objects.filter(tgl_input__lte=timezone.now()).order_by('kategori')
			template = 'produk/bicycles.html'

		context['tampilkan'] = tampilkan
		context['loop'] = range(1, 5)
		
	except NameError as e:
		template = 'produk/404.html'

	return render(request, template, context)

def sub_kategori(request, nilai, sub_nilai):
	pass