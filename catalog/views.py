from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.list import ListView
from catalog.models import good, category, company, subcategory1, subcategory2, subcategory3
from catalog.forms import GoodForm
from django.urls import path
#Контроллер-класс по выводу страницы с номенклатурой
class good_detail(UpdateView, ListView):
    model = good
    form_class = GoodForm
    template_name = "catalog_home.html"
    pk_url_kwarg = "no"
    success_url = './'
    paginate_by = 10
    cat_no = None
    scat1_no = None
    scat2_no = None
    scat3_no = None
    notexists = None
    no = None
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)  
        context['cats'] = category.objects.all().order_by("name")
        context['companies'] =  company.objects.all().order_by("name")
       # Переменная - нет данных
        context['notexists'] = self.notexists
        return context

    def get(self, *args, **kwargs):

        #Запись в переменную выбранной категории/подкатегории
        try:
            self.scat3_no = subcategory3.objects.get(pk = self.kwargs["scat3"])  
        except:
            try:
                self.scat2_no = subcategory2.objects.get(pk = self.kwargs["scat2"])         
            except:
                try:
                    self.scat1_no = subcategory1.objects.get(pk = self.kwargs["scat1"])      
                except:
                    try:
                        self.cat_no = category.objects.get(pk = self.kwargs["cat"])   
                    except:
                        self.cat_no = None
           
          #Проверка есть ли в контексте номер товара, если нет добавляет первый из сета
        try:
            g_n=self.kwargs["no"]
        except:
            #Если ошибка в первом элементе сета, значит набор пустой, вывести модальное окно
            try:
                if self.scat3_no != None:
                    g_n=good.objects.filter(subcategory3 = self.scat3_no).first().no
                elif self.scat2_no != None:
                    g_n=good.objects.filter(subcategory2 = self.scat2_no).first().no
                elif self.scat1_no != None:
                    g_n=good.objects.filter(subcategory1 = self.scat1_no).first().no
                elif self.cat_no != None:
                    g_n=good.objects.filter(good_category = self.cat_no).first().no
                else:
                    g_n=good.objects.first().no
            except:
                self.notexists = True 
                g_n=good.objects.first().no    
        self.kwargs["no"]=g_n
        self.no=g_n
        return super(good_detail, self).get(self, *args, **kwargs)

        

    def get_queryset(self):
        #Проверяет записана ли какая то категория/подкатегория и если да, то создает сет с выбранной категорией
        if self.scat3_no != None:
            qs = good.objects.filter(subcategory3 = self.scat3_no)
        elif self.scat2_no != None:
            qs = good.objects.filter(subcategory2 = self.scat2_no)
        elif self.scat1_no != None:
            qs = good.objects.filter(subcategory1 = self.scat1_no)
        else:
            qs = good.objects.filter(good_category = self.cat_no)      
        if qs.exists():
            return qs
        else:
            return good.objects.all()
            self.notexists = True

        
#Класс для удаления записи
class good_delete(DeleteView):
    model = good
    form_class = GoodForm
    template_name = "catalog_home.html"
    pk_url_kwarg = "no"
   # success_url = '/catalog/{no}'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['category'] =category.objects.all().order_by("name")
        context['cats'] = category.objects.all().order_by("name")
        context['goods'] =  good.objects.all().order_by("name")
        context['companies'] =  company.objects.all().order_by("name")
        return context
    def get_success_url(self):
        return reverse('catalog:catalog')
    #Переопределәет метод GET в POST чтобы не появлялось дополнительной формы при удалении
    def get(self, *args, **kwargs):
         return self.post(*args, **kwargs)
#def catalog (request): 
    #контроллер для домашней страницы товаров
    # считываем все обьекты
 #   cats = category.objects.all().order_by("name")
 #   cat = category.objects.get(no=1)
 #   goodis = good.objects.all().order_by("name")
 #   return render(request, "catalog_home.html", {"category":cat, "cats": cats, "goods":goodis})

#def id (request, good_id):
    #контроллер вывода товара
 #   cats = category.objects.all().order_by("name")
 #   cat = category.objects.get(no=1)
  #  goodis = good.objects.get(no = good_id)
  #  return render(request, "catalog.html", {"category":cat, "cats": cats, "goods":goodis})

def cat (request, cat_id):
    cats = category.objects.all().order_by("name")
    cat = category.objects.get(no=cat_id)
    goodis = good.objects.filter(good_category = cat).order_by("name")
    return render(request, "catalog.html", {"cat":cat, "cats": cats, "goods":goodis})

def cat_home (request):
    cats = category.objects.all().order_by("name")
    cat = category.objects.get(no=1)
    goodis = good.objects.filter(good_category = cat).order_by("name")
    return render(request, "catalog.html", {"cat":cat, "cats": cats, "goods":goodis})