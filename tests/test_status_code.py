"""
Тестуемо усі сторінки сайту:https://www.symphony-solutions.com/ на статус код 200
We test all pages of the site: https://www.symphony-solutions.com/ for status code 200
"""
import pytest
import requests
from configuration import SERVICE_URL, ALL_URL_LIST, WRONG_URL_HTTPS, WRONG_URL_AFTER_SLASH, XML_URL
from src.enums.global_enums import GlobalErrorMassages


@pytest.mark.parametrize('url', ALL_URL_LIST)
def test_get_status_code_all_pages(url):
    response = requests.get(url=SERVICE_URL+url)
    assert response.status_code == 200, GlobalErrorMassages.WRONG_STATUS_CODE.value


@pytest.mark.parametrize('url', WRONG_URL_HTTPS)
def test_url_redirect_to_https(url):
    """
    Переірка роботи редіректі з http, www на сторінку з  hhtps
    Checking the operation of redirects from http, www to a page with https
    """
    response = requests.get(url=url)
    assert response.url == SERVICE_URL, GlobalErrorMassages.WRONG_URL_HTTPS.value


@pytest.mark.parametrize('url', WRONG_URL_AFTER_SLASH)
def test_entering_incorrect_data_in_the_url_after_the_slash(url):
    """
    При введені некоректних данних піля слешу в полі url повинно перенаправити на сторінку 404
    When entering incorrect data after a slash in the url field, it should redirect to a 404 page
    """
    response = requests.get(SERVICE_URL+url)
    assert response.status_code == 404, GlobalErrorMassages.WRONG_STATUS_CODE.value





'''
1. Как с xml вытянуть url и записать их в лист, (может import json, но не вышло)
2. Ввод данных через post, как отправить данные в форму через post без селениума
'''

