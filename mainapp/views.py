from django.views.generic import TemplateView


# Create your views here.

# def hello_world(request):
#     return HttpResponse("Hellow wolrd!")
#
# def check_kwargs(request, **kwargs):
#     return HttpResponse(f'kwargs:<br>{kwargs}')


class MainPageView(TemplateView):
    template_name = 'mainapp/index.html'


class MainPageView(TemplateView):
    template_name = 'mainapp/index.html'


class NewsPageView(TemplateView):
    template_name = 'mainapp/news.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_title'] = 'Новость №'
        context[
            'news_preview'
        ] = 'Новости новости новости'
        context['range'] = range(5)
        return context

class NewsWithPaginatorView(NewsPageView):
    def get_context_data(self,page, **kwargs):
        context = super().get_context_data(page=page,**kwargs)
        return context

class CoursesPageView(TemplateView):
    template_name = 'mainapp/courses_list.html'


class DocSitePageView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class LoginPageView(TemplateView):
    template_name = 'mainapp/login.html'


class ContactsPageView(TemplateView):
    template_name = 'mainapp/contacts.html'
