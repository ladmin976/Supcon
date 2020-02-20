from django.db import models
from django.contrib import admin
power_types = {
	(1, "AC"),
	(2, "DC"),
	(3, "AC/DC")
}

from django.db import models

class unit (models.Model):	
	no = models.AutoField(verbose_name = "Номер", unique = True, primary_key = True)
	name = models.CharField(verbose_name = "Наименование", db_index = True, max_length = 100, blank = True, null = True)
	level = models.CharField(verbose_name = "Единицы измерения", db_index = True, max_length = 100)
	description = models.TextField(verbose_name = "Описание", blank = True, null = True)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = "Единицы измерения"
		verbose_name = "Единица измерения"
		ordering = ['-name']

class contact (models.Model):	
	no = models.AutoField(verbose_name = "Номер", unique = True, primary_key = True)
	first_name = models.CharField(verbose_name = "Имя", unique = True, max_length = 100)
	family_name = models.CharField(verbose_name = "Фамилия", unique = True, db_index = True, max_length = 100)
	third_name = models.CharField(verbose_name = "Отчество", max_length = 100, blank = True, null = True)
	description = models.TextField(verbose_name = "Описание", blank = True, null = True)
	position = models.CharField(verbose_name = "Должность", max_length = 100, blank = True, null = True)
	email = models.EmailField(verbose_name = "email", db_index = True, blank = True, null = True)
	site = models.URLField(verbose_name = "Сайт", blank = True, null = True)
	phone_mobile = models.CharField(verbose_name = "Телефон мобильный", max_length = 100, blank = True, null = True)
	phone_company = models.CharField(verbose_name = "Телефон рабочий", max_length = 100, blank = True, null = True)
	def __str__(self):
		return self.family_name
	class Meta:
		verbose_name_plural = "Контакты"
		verbose_name = "Контакт"
		ordering = ['-family_name']

class country (models.Model):	
	no = models.AutoField(verbose_name = "Номер", unique = True, primary_key = True)
	name = models.CharField(verbose_name = "Наименование", unique = True, db_index = True, max_length = 100)
	description = models.TextField(verbose_name = "Описание", blank = True, null = True)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = "Страны"
		verbose_name = "Страна"
		ordering = ['-name']

class comp_type (models.Model):	
	no = models.AutoField(verbose_name = "Номер", unique = True, primary_key = True)
	name = models.CharField(verbose_name = "Наименование", unique = True, db_index = True, max_length = 100)
	description = models.TextField(verbose_name = "Описание", blank = True, null = True)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = "Типы компаний"
		verbose_name = "Тип компании"
		ordering = ['-name']

class company (models.Model):	
	no = models.AutoField(verbose_name = "Номер", unique = True, primary_key = True)
	name = models.CharField(verbose_name = "Наименование компании", unique = True, db_index = True, max_length = 100)
	name_eng = models.CharField(verbose_name = "Наименование английское", unique = True, db_index = True, max_length = 100, blank = True, null = True)
	type = models.ForeignKey(comp_type, verbose_name = "Тип компании", on_delete = models.SET_DEFAULT, default = 0)
	description = models.TextField(verbose_name = "Описание", blank = True, null = True)
	local = models.BooleanField(verbose_name = "Локальное или нет", db_index = True, blank = True, null = True, default = False)
	production = models.ForeignKey(country, verbose_name = "Страна производства", db_index = True, blank = True, null = True, on_delete = models.SET_NULL, related_name = '+')
	origin = models.ForeignKey(country, verbose_name = "Страна происхождения", db_index = True, blank = True, null = True, on_delete = models.SET_NULL, related_name = '+')
	rating = models.IntegerField(verbose_name = "Рейтинг", db_index = True, blank = True, null = True)
	contact = models.ForeignKey(contact, verbose_name = "Контакт", db_index = True, blank = True, null = True, on_delete = models.SET_NULL)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = "Компании"
		verbose_name = "Компания"
		ordering = ['-name']
class category (models.Model):	
	no = models.AutoField(verbose_name = "Номер", unique = True, primary_key = True)
	name = models.CharField(verbose_name = "Наименование", unique = False, db_index = True, max_length = 100)
	description = models.TextField(verbose_name = "Описание", blank = True, null = True)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = "Категории"
		verbose_name = "Категория"
		ordering = ['-name']
class subcategory1 (models.Model):	
	no = models.AutoField(verbose_name = "Номер", unique = True, primary_key = True)
	name = models.CharField(verbose_name = "Наименование", unique = False, db_index = True, max_length = 100)
	description = models.TextField(verbose_name = "Описание", blank = True, null = True)
	category = models.ForeignKey(category, verbose_name = "Категория", db_index = True, blank = True, null = True, on_delete = models.SET_NULL, related_name = 'CAT')
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = "Подкатегории 1"
		verbose_name = "Подкатегория 1"
		ordering = ['-name']
class subcategory2 (models.Model):	
	no = models.AutoField(verbose_name = "Номер", unique = True, primary_key = True)
	name = models.CharField(verbose_name = "Наименование", unique = False, db_index = True, max_length = 100)
	description = models.TextField(verbose_name = "Описание", blank = True, null = True)
	subcategory1 = models.ForeignKey(subcategory1, verbose_name = "Подкатегория 1", db_index = True, blank = True, null = True, on_delete = models.SET_NULL, related_name = 'SC1')
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = "Подкатегории 2"
		verbose_name = "Подкатегория 2"
		ordering = ['-name']	
class subcategory3 (models.Model):	
	no = models.AutoField(verbose_name = "Номер", unique = True, primary_key = True)
	name = models.CharField(verbose_name = "Наименование", unique = False, db_index = True, max_length = 100)
	description = models.TextField(verbose_name = "Описание", blank = True, null = True)
	subcategory2 = models.ForeignKey(subcategory2, verbose_name = "Подкатегория 2", db_index = True, blank = True, null = True, on_delete = models.SET_NULL, related_name = 'SC2')
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = "Подкатегории 3"
		verbose_name = "Подкатегория 3"
		ordering = ['-name']

class family (models.Model):	
	no = models.AutoField(verbose_name = "Номер", unique = True, primary_key = True)
	name = models.CharField(verbose_name = "Наименование", unique = True, db_index = True, max_length = 100)
	description = models.TextField(verbose_name = "Описание", blank = True, null = True)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = "Семейства"
		verbose_name = "Семейство"
		ordering = ['-name']

class subfamily (models.Model):	
	no = models.AutoField(verbose_name = "Номер", unique = True, primary_key = True)
	name = models.CharField(verbose_name = "Наименование", unique = True, db_index = True, max_length = 100)
	description = models.TextField(verbose_name = "Описание", blank = True, null = True)
	family = models.ForeignKey(family, verbose_name = "Семейство", db_index = True, blank = True, null = True, on_delete = models.SET_NULL, related_name = '+')
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = "Подсемейства"
		verbose_name = "Подсемейство"
		ordering = ['-name']
class cables (models.Model):	
	no = models.AutoField(verbose_name = "Номер", unique = True, primary_key = True)
	name = models.CharField(verbose_name = "Наименование", unique = True, db_index = True, max_length = 100)
	description = models.TextField(verbose_name = "Описание", blank = True, null = True)
	cable_type = models.CharField(verbose_name = "Тип кабеля", max_length = 100,  blank = True, null = True)
	cable_name = models.CharField(verbose_name = "Имя кабеля", max_length = 100, blank = True, null = True)
	pare_qty = models.IntegerField(verbose_name = "Количество пар", db_index = True, blank = True, null = True)
	wire_qty = models.IntegerField(verbose_name = "Количество жил", db_index = True, blank = True, null = True)
	cable_section = models.FloatField(verbose_name = "Сечение кабеля", db_index = True, blank = True, null = True)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = "Типы кабелей"
		verbose_name = "Тип кабеля"
		ordering = ['-name']
class interface (models.Model):	
	no = models.AutoField(verbose_name = "Номер", unique = True, primary_key = True)
	name = models.CharField(verbose_name = "Наименование", db_index = True, max_length = 100)
	description = models.TextField(verbose_name = "Описание", blank = True, null = True)
	interface_type = models.CharField(verbose_name = "Тип интерфейса", max_length = 100, blank = True, null = True)
	cable_type = models.ForeignKey(cables, verbose_name = "Тип кабеля", db_index = True, blank = True, null = True, on_delete = models.SET_NULL, related_name = '+')
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = "Сетевые интерфейсы"
		verbose_name = "Сетевые интерфейс"
		ordering = ['-name']

class control_interface (models.Model):	
	no = models.AutoField(verbose_name = "Номер", unique = True, primary_key = True)
	name = models.CharField(verbose_name = "Наименование управляющего интерфейса", db_index = True, max_length = 100)
	description = models.TextField(verbose_name = "Описание", blank = True, null = True)
	interface_type = models.CharField(verbose_name = "Тип управляющего интерфейса", max_length = 100, blank = True, null = True)
	physic_range = models.CharField(verbose_name = "Диапазон", max_length = 100, blank = True, null = True)
	cable_type = models.ForeignKey(cables, verbose_name = "Тип кабеля", db_index = True, blank = True, null = True, on_delete = models.SET_NULL, related_name = '+')
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = "Управляющие интерфейсы"
		verbose_name = "Управляющий интерфейс"
		ordering = ['-name']




 
class good (models.Model):	
	no = models.AutoField(verbose_name = "Номер", unique = True, primary_key = True)
	name = models.CharField(verbose_name = "Название", unique = True, db_index = True, max_length = 100)
	part_no = models.CharField(verbose_name = "Заводской номер", unique = True, db_index = True, max_length = 100, blank = True, null = True)
	description = models.TextField(verbose_name = "Описание", blank = True, null = True)
	unit = models.ForeignKey(unit, verbose_name = "Единица измерения", blank = True, null = True, on_delete = models.SET_NULL)
	purchase_price_wo_vat = models.DecimalField(verbose_name = "Закупочная цена, без НДС",  max_digits = 50, decimal_places = 2, db_index = True, blank = True, null = True)
	purchase_price_w_vat = models.DecimalField(verbose_name = "Закупочная цена, с НДС",  max_digits = 50,   decimal_places = 2, db_index = True, blank = True, null = True)
	rrp_wo_vat = models.DecimalField(verbose_name = "Розница, без НДС",  max_digits = 50,  decimal_places = 2, db_index = True, blank = True, null = True)
	rrp_price_w_vat = models.DecimalField(verbose_name = "Розница, с НДС",  max_digits = 50,  decimal_places = 2, db_index = True, blank = True, null = True)
	discount_standart = models.DecimalField(verbose_name = "Скидка стандартная",  max_digits = 50,  decimal_places = 2, blank = True, null = True)
	discount_max = models.DecimalField(verbose_name = "Скидка максимальная",  max_digits = 50,  decimal_places = 2, blank = True, null = True)
	multiplayer_standart = models.DecimalField(verbose_name = "Наценка стандартная",  max_digits = 50,  decimal_places = 2, blank = True, null = True)
	multiplayer_min = models.DecimalField(verbose_name = "Наценка минимальная",  max_digits = 50,  decimal_places = 2, blank = True, null = True)
	profit_rrp = models.DecimalField(verbose_name = "Прибыль от розницы", max_digits = 50,   decimal_places = 2, db_index = True, blank = True, null = True)
	profit_standart = models.DecimalField(verbose_name = "Прибыль при стандартной скидке",  max_digits = 50,  decimal_places = 2, db_index = True, blank = True, null = True)
	profit_min = models.DecimalField(verbose_name = "Прибыль при максимальной скидке", max_digits = 50,   decimal_places = 2, db_index = True, blank = True, null = True)
	producer = models.ForeignKey(company, verbose_name = "Производитель", db_index = True, blank = True, null = True, on_delete = models.SET_NULL, related_name = 'PRODUCER')
	suplayer = models.ForeignKey(company, verbose_name = "Поставщик", db_index = True, blank = True, null = True, on_delete = models.SET_NULL, related_name = '+')
	good_category = models.ForeignKey(category, verbose_name = "Категория", blank = True, null = True, on_delete = models.SET_NULL, related_name = 'CATEGORY')
	subcategory1 = models.ForeignKey(subcategory1, verbose_name = "Подкатегория 1", db_index = True, blank = True, null = True, on_delete = models.SET_NULL, related_name='SUBCATEGORY1')
	subcategory2 = models.ForeignKey(subcategory2, verbose_name = "Подкатегория 2", db_index = True, blank = True, null = True, on_delete = models.SET_NULL, related_name='SUBCATEGORY2')
	subcategory3 = models.ForeignKey(subcategory3, verbose_name = "Подкатегория 3", db_index = True, blank = True, null = True, on_delete = models.SET_NULL, related_name='SUBCATEGORY3')
	good_family = models.ForeignKey(family, verbose_name = "Семейство", db_index = True, blank = True, null = True, on_delete = models.SET_NULL, related_name = '+')
	subfamily = models.ForeignKey(subfamily, verbose_name = "Подсемейство", db_index = True, blank = True, null = True, on_delete = models.SET_NULL, related_name = '+')
	delivery_time = models.IntegerField(verbose_name = "Срок поставки", blank = True, null = True)
	doc_file = models.FileField(verbose_name = "Файл с документацией", blank = True, null = True)
	picture = models.ImageField(verbose_name = "Изображение", blank = True, null = True)
	schematic = models.FileField(verbose_name = "Схема", blank = True, null = True)
	svg = models.FileField(verbose_name = "svg", blank = True, null = True)
	installation_time = models.DecimalField(verbose_name = "Время на монтаж",  max_digits = 50,   decimal_places = 2,blank = True, null = True)
	programming_time = models.DecimalField(verbose_name = "Время на программирование",   max_digits = 50,  decimal_places = 2,blank = True, null = True)
	comission_time = models.DecimalField(verbose_name = "Время на пуско - наладку",  max_digits = 50,  decimal_places = 2, blank = True, null = True)
	plc_DI = models.IntegerField(verbose_name = "Количество цифровых входов", blank = True, null = True)
	plc_DO = models.IntegerField(verbose_name = "Количество цифровых выходов", blank = True, null = True)
	plc_AI = models.IntegerField(verbose_name = "Количество аналоговых входов", blank = True, null = True)
	plc_AO = models.IntegerField(verbose_name = "Количество аналоговых выходов", blank = True, null = True)
	plc_UI = models.IntegerField(verbose_name = "Количество универсальных входов", blank = True, null = True)
	plc_UO = models.IntegerField(verbose_name = "Количество универсальных выходов", blank = True, null = True)
	plc_UIO = models.IntegerField(verbose_name = "Количество универсальных входов/выходов", blank = True, null = True)
	plc_io_qty = models.IntegerField(verbose_name = "Количество входов/выходов", blank = True, null = True)	
	accessory = models.BooleanField(verbose_name = "Акссесуар или нет", blank = True, null = True, default = False)
	power_type = models.IntegerField(choices = power_types, verbose_name = "Тип питающего напряжения", blank = True, null = True)
	voltage = models.FloatField(verbose_name = "Напряжение", blank = True, null = True)
	power = models.FloatField(verbose_name = "Мощность", blank = True, null = True)
	current = models.FloatField(verbose_name = "Ток", blank = True, null = True)
	work_temp_low = models.FloatField(verbose_name = "Рабочая температура нижняя", blank = True, null = True)
	work_temp_high = models.FloatField(verbose_name = "Рабочая температура верхняя", blank = True, null = True)
	port_qty = models.IntegerField(verbose_name = "Количество портов", blank = True, null = True)
	in_stock = models.IntegerField(verbose_name = "Количество на складе", db_index = True, blank = True, null = True)
	in_box = models.BooleanField(verbose_name = "Монтаж в шкаф или нет", blank = True, null = True, default = False)
	cable_type = models.ForeignKey(cables, verbose_name = "Тип кабеля", db_index = True, blank = True, null = True, on_delete = models.SET_NULL, related_name = '+')
	accessories = models.ManyToManyField("self", blank = True, verbose_name = "Аксессуары")
	twin = models.ManyToManyField("self", blank = True, verbose_name = "Обязательный акссесуар")
	network_interfaces = models.ManyToManyField(interface, verbose_name = "Сетевые интерфейсы", through= "kit_interface")
	control_interfaces = models.ManyToManyField(control_interface, verbose_name = "Управляющие интерфейсы", through= "kit_control_interface")

	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = "Номенклатура"
		verbose_name = "Номенклатура"
		ordering = ['-name']

class kit_interface (models.Model):	
	good = models.ForeignKey(good,  verbose_name = "Номенклатура", on_delete = models.CASCADE)
	interface = models.ForeignKey(interface,  verbose_name = "Сетевой интерфейс", on_delete = models.CASCADE)
	count = models.IntegerField (verbose_name = "Количество", blank = True, null = True)
	def __str__(self):
		return ""
	class Meta:
		verbose_name_plural = "Подключения"
		verbose_name = "Подключение"
	

class kit_control_interface (models.Model):	
	good = models.ForeignKey(good,  on_delete = models.CASCADE)
	control_interface = models.ForeignKey(control_interface,  on_delete = models.CASCADE)
	count = models.IntegerField (verbose_name = "Количество", blank = True, null = True)
	def __str__(self):
		return ""
	class Meta:
		verbose_name_plural = "Физический интерфейсы"
		verbose_name = "Физические интерфейсы"

# класс для отображения в админке поля многие ко многим
class kit_interfaceInLine(admin.StackedInline):
	model= kit_interface
	extra = 1
# класс для отображения в админке поля многие ко многим
class kit_control_interfaceInLine(admin.StackedInline):
	model= kit_control_interface 
	extra = 1
