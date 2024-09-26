from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'clothing/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        context['content'] = 'Магазин мебели HOME'
        return context


class AboutView(TemplateView):
    template_name = 'clothing/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О сайте'
        context['content'] = 'Это сайт магазин-мебели'
        context['text_on_page'] = 'Смотрите, заказывайте. Поддерживайте экономику.'
        return context

