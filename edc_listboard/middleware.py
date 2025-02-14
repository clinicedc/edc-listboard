from django.conf import settings

from .dashboard_templates import dashboard_templates


class DashboardMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, *args) -> None:
        template_data = dashboard_templates
        try:
            template_data.update(settings.LISTBOARD_BASE_TEMPLATES)
        except AttributeError:
            pass
        request.template_data.update(**template_data)

    def process_template_response(self, request, response):
        if response.context_data:
            response.context_data.update(**request.template_data)
        return response
