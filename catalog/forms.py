from django import forms
#from .models import power_types, good, interface, kit_interface, cables, company, category, subcategory1, subcategory2, subcategory3, family, subfamily
from .models import *

class NameQTYWidget(forms.MultiWidget):
    def __init__(self, attrs):
        widgets = [
          #forms.SelectMultiple(attrs=attrs),
         forms.SelectMultiple(attrs=attrs),
         forms.NumberInput( attrs=attrs)
          ]
        super().__init__(widgets, attrs)
    def decompress(self, value):
        print(value)
        if value:
            return [value[0].no, value[1]]
        else:
            return [None, None]

class Interface_Field(forms.MultiValueField):
    
    def __init__(self, attrs, *args, **kwargs):
        list_fields = [forms.ModelMultipleChoiceField(queryset = interface.objects.all()),
                       forms.IntegerField()]
        super(Interface_Field, self).__init__(list_fields, widget=NameQTYWidget(attrs,*args, **kwargs))
        self.widget.widgets[0].choices = self.fields[0].widget.choices
    def compress(self, values):
        return values[0]


   # def decompress (self, value):
     #   return ["WiFi", 6]
  #  def value_from_datadict(self, data, files, name):
   #     if value:
   #         return [value.str()]
#ФОрма показа и редактирования параметров
class GoodForm(forms.ModelForm):
    class Meta:
         model = good
         fields = ('name', 'part_no', 'description', 'producer', 'rrp_price_w_vat', 'good_category', 'subcategory1', 'subcategory2', 
         'subcategory3', 'good_family', 'subfamily', 'suplayer', 'delivery_time', 'installation_time', 'programming_time',
         'comission_time', 'in_stock', 'purchase_price_wo_vat', 
         'purchase_price_w_vat', 'rrp_wo_vat', 'rrp_price_w_vat',  'discount_standart',  'discount_max', 'multiplayer_standart',
         'multiplayer_min', 'profit_rrp', 'profit_standart', 'profit_min')
    name = forms.CharField(label = 'Наименование',  widget=forms.TextInput(attrs = {"class":"form-control"}))
    part_no = forms.CharField(label = 'Заводской номер', required = False, widget=forms.TextInput(attrs = {"class":"mb-2 form-control"}))
    description = forms.CharField(label = 'Описание', required = False, widget=forms.Textarea(attrs = {"class":"form-control"}))
    producer = forms.ModelChoiceField(queryset = company.objects.all(), required = False, label = 'Производитель', widget=forms.Select(attrs = {"class":"form-control"}))
    good_category = forms.ModelChoiceField(queryset = category.objects.all(), required = False, label = 'Категория', widget=forms.Select(attrs = {"class":"form-control"}))
    subcategory1 = forms.ModelChoiceField(queryset = subcategory1.objects.all(), required = False, label = 'Подкатегория 1', widget=forms.Select(attrs = {"class":"form-control"}))
    subcategory2 = forms.ModelChoiceField(queryset = subcategory2.objects.all(), required = False, label = 'Подкатегория 2', widget=forms.Select(attrs = {"class":"form-control"}))
    subcategory3 = forms.ModelChoiceField(queryset = subcategory3.objects.all(), required = False, label = 'Подкатегория 3', widget=forms.Select(attrs = {"class":"form-control"}))
    good_family = forms.ModelChoiceField(queryset = family.objects.all(), required = False, label = 'Семейство', widget=forms.Select(attrs = {"class":"form-control"}))
    subfamily = forms.ModelChoiceField(queryset = subfamily.objects.all(), required = False, label = 'Подсемейство', widget=forms.Select(attrs = {"class":"form-control"}))
    suplayer = forms.ModelChoiceField(queryset = company.objects.all(), required = False, label = 'Поставщик', widget=forms.Select(attrs = {"class":"form-control"}))
    delivery_time = forms.IntegerField(label = 'Срок поставки', min_value=0, required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    installation_time = forms.DecimalField(label = 'Время на монтаж', min_value=0, decimal_places = 2, required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    programming_time = forms.DecimalField(label = 'Время на программирование', min_value=0, decimal_places = 2, required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    comission_time = forms.DecimalField(label = 'Время на пусконаладку', min_value=0, decimal_places = 2, required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    in_stock = forms.IntegerField(label = 'Наличие на складе', min_value=0, required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    purchase_price_wo_vat = forms.DecimalField(label = 'Закупочная цена без НДС', min_value=0, max_digits = 50, decimal_places = 2, required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    purchase_price_w_vat = forms.DecimalField(label = 'Закупочная цена включая НДС', min_value=0, max_digits = 50, decimal_places = 2, required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    rrp_wo_vat = forms.DecimalField(label = 'Розничная цена без НДС', min_value=0, decimal_places = 2, required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    rrp_price_w_vat = forms.DecimalField(label = 'Розничная цена включая НДС', min_value=0, decimal_places = 2, required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    discount_standart = forms.DecimalField(label = 'Скидка стандартная', min_value=0, decimal_places = 2, required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    discount_max = forms.DecimalField(label = 'Скидка максимальная', min_value=0, decimal_places = 2, required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    multiplayer_standart = forms.DecimalField(label = 'Наценка стандартная', min_value=0, decimal_places = 2, required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    multiplayer_min = forms.DecimalField(label = 'Наценка минимальная',min_value=0, decimal_places = 2,  required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    profit_rrp = forms.DecimalField(label = 'Прибыль от розницы', min_value=0, decimal_places = 2, required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    profit_standart = forms.DecimalField(label = 'Прибыль стадартная', min_value=0, decimal_places = 2, required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    profit_min = forms.DecimalField(label = 'Прибыль минимальная', min_value=0, decimal_places = 2, required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    plc_DI = forms.IntegerField(label = 'Количество дискрентных входов', min_value=0, required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    plc_DO = forms.IntegerField(label = 'Количество дискрентных выходов', min_value=0, required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    plc_AI = forms.IntegerField(label = 'Количество аналоговых входов', min_value=0, required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    plc_AO = forms.IntegerField(label = 'Количество аналоговых выходов', min_value=0, required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    plc_UI = forms.IntegerField(label = 'Количество универсальных входов', min_value=0, required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    plc_UO = forms.IntegerField(label = 'Количество универсальных выходов', min_value=0, required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    plc_UIO = forms.IntegerField(label = 'Количество универсальных входов/выходов', min_value=0, required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    plc_io_qty = forms.IntegerField(label = 'Общее количество входов/выходов',min_value=0,  required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    power_type = forms.ChoiceField(choices=power_types, required = False, label = 'Тип питающего напряжения', widget=forms.Select(attrs = {"class":"form-control"}))
    voltage = forms.FloatField(label = 'Напряжение', min_value=0,  required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    power = forms.FloatField(label = 'Мощность', min_value=0,  required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    current = forms.FloatField(label = 'Ток', min_value=0,  required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    work_temp_low = forms.FloatField(label = 'Нижний диапазон рабочей температуры', min_value=0,  required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    work_temp_high = forms.FloatField(label = 'Верхний диапазон рабочей температуры', min_value=0,  required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    in_box = forms.BooleanField(label = 'Установка в шкаф', initial=False,  required = False, widget=forms.Select(choices={(True,"Да"), (False,"Нет")}, attrs = {"class":"form-control"}))
    cable_type = forms.ModelChoiceField(queryset = cables.objects.all(), required = False, label = 'тип кабеля', widget=forms.Select(attrs = {"class":"form-control"}))
    accessories = forms.ModelMultipleChoiceField(queryset = good.objects.all(), required = False, label = 'Акссесуары', widget=forms.SelectMultiple(attrs = {"class":"form-control"}))
    
    def __init__(self, *args, **kwargs):
        super(GoodForm, self).__init__(*args, **kwargs)
        for ints in interface.objects.all():
           self.fields[ints.name] = forms.IntegerField(label = 'ints.name', min_value=0, required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
   
    

