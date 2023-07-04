from string import ascii_lowercase
from random import shuffle

from django.http import JsonResponse
from django.template.loader import render_to_string


def form_new_page_service(template_path: str, form_context: dict) -> [bool, JsonResponse]:
    new_form_html = render_to_string(template_path, form_context)
    return JsonResponse({"new_form_html": new_form_html})


generated_name = {}


def get_file_random_name(file_number: int):
    if file_number not in generated_name:
        possible_choice = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] + list(ascii_lowercase)
        shuffle(possible_choice)
        random_name = ''.join(possible_choice[:9])
        generated_name[file_number] = random_name
    return generated_name[file_number]
