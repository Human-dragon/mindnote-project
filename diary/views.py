from django.shortcuts import render,redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse
from .models import Page
from .forms import PageForm

# Create your views here.
# def page_list(request):
#     object_list = Page.objects.all() # 데이터 조회
#     return render(request, 'diary/page_list.html', {'object_list': object_list})

class PageListView(ListView):
    model = Page
    ordering = ['-dt_created']


# def page_detail(request, page_id):
#     object = Page.objects.get(id=page_id)
#     return render(request, 'diary/page_detail.html', {'object': object})

class PageDetailView(DetailView):
    model = Page

def info(request):
    return render(request, 'diary/info.html')


# def page_create(request):
#     form = PageForm()
#     return render(request, 'diary/page_form.html', {'form': form})

# def page_create(request):
#     if request.method == 'POST':
#         form = PageForm(request.POST)
#         if form.is_valid():
#             new_page = form.save()
#             return redirect('page-detail', page_id=new_page.id)
#     else:
#         form = PageForm()
#     return render(request, 'diary/page_form.html', {'form': form})

class PageCreateView(CreateView):
    model = Page
    form_class = PageForm

    def get_success_url(self):
        return reverse('page-detail', kwargs={'pk': self.object.id})


# def page_update(request, page_id):
#     object = Page.objects.get(id=page_id)
#     if request.method == 'POST': # 요청이 POST 방식이라면
#         form = PageForm(request.POST, instance=object) # 기존의 데이터 모델에 새로운 데이터를 설정하고
#         if form.is_valid(): # 유효성 검사를 통과했다면
#             form.save() # 데이터를 저장한 뒤
#             return redirect('page-detail', page_id=object.id) # 상세 보기 페이지로 안내합니다.
#     else:
#         form = PageForm(instance=object)
#     return render(request, 'diary/page_form.html', {'form': form})

class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm

    def get_success_url(self):
        return reverse('page-detail', kwargs={'pk': self.object.id})


class PageDeleteView(DeleteView):
    model = Page

    def get_success_url(self):
        return reverse('page-list')

def index(request):
    return render(request, 'diary/index.html')




