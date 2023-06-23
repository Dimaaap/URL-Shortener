from django.http import JsonResponse
from django.template.loader import render_to_string


def form_new_page_service(template_path: str, form_context: dict) -> [bool, JsonResponse]:
    new_form_html = render_to_string(template_path, form_context)
    return JsonResponse({"new_form_html": new_form_html})