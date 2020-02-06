from django import forms
from .models import good, interface, kit_interface, cables, company, category, subcategory1, subcategory2, subcategory3, family, subfamily

class GoodForm(forms.ModelForm):
    class Meta:
         model = good
         fields = 'name', 'part_no', 'description', 'producer', 'rrp_price_w_vat', 'good_category', 'subcategory1', 'subcategory2', 'subcategory3', 'good_family', 'subfamily', 'suplayer', 'delivery_time', 'installation_time', 'programming_time', 'comission_time', 'in_stock'
    name = forms.CharField(label = 'Наименование',  widget=forms.TextInput(attrs = {"class":"form-control"}))
    part_no = forms.CharField(label = 'Заводской номер', required = False, widget=forms.TextInput(attrs = {"class":"mb-2 form-control"}))
    description = forms.CharField(label = 'Описание', required = False, widget=forms.Textarea(attrs = {"class":"form-control"}))
    producer = forms.ModelChoiceField(queryset = company.objects.all(), required = False, label = 'Производитель', widget=forms.Select(attrs = {"class":"form-control"}))
    rrp_price_w_vat = forms.FloatField(label = 'Цена', required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    good_category = forms.ModelChoiceField(queryset = category.objects.all(), required = False, label = 'Категория', widget=forms.Select(attrs = {"class":"form-control"}))
    subcategory1 = forms.ModelChoiceField(queryset = subcategory1.objects.all(), required = False, label = 'Подкатегория 1', widget=forms.Select(attrs = {"class":"form-control"}))
    subcategory2 = forms.ModelChoiceField(queryset = subcategory2.objects.all(), required = False, label = 'Подкатегория 2', widget=forms.Select(attrs = {"class":"form-control"}))
    subcategory3 = forms.ModelChoiceField(queryset = subcategory3.objects.all(), required = False, label = 'Подкатегория 3', widget=forms.Select(attrs = {"class":"form-control"}))
    good_family = forms.ModelChoiceField(queryset = family.objects.all(), required = False, label = 'Семейство', widget=forms.Select(attrs = {"class":"form-control"}))
    subfamily = forms.ModelChoiceField(queryset = subfamily.objects.all(), required = False, label = 'Подсемейство', widget=forms.Select(attrs = {"class":"form-control"}))
    suplayer = forms.ModelChoiceField(queryset = company.objects.all(), required = False, label = 'Поставщик', widget=forms.Select(attrs = {"class":"form-control"}))
    delivery_time = forms.IntegerField(label = 'Срок поставки', required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    installation_time = forms.FloatField(label = 'Время на монтаж', required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    programming_time = forms.FloatField(label = 'Время на программирование', required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    comission_time = forms.FloatField(label = 'Время на пусконаладку', required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))
    in_stock = forms.IntegerField(label = 'Наличие на складе', required = False, widget=forms.NumberInput(attrs = {"class":"form-control"}))

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)