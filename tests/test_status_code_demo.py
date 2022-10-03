"""
Тестуемо усі сторінки сайту:https://www.symphony-solutions.com/ на статус код 200
We test all pages of the site: https://www.symphony-solutions.com/ for status code 200
"""
"""
Для запуску усіх тестів в терміналі:pytest -v -s C:\Test_status_code_symphony_com\tests
Для запуску тестів в файл з збереженням файлу Allure: 
pytest -v -s C:\Test_status_code_symphony_com\tests --alluredir=allure_ss_com
pytest -v -s /Users/antongrunt/Desktop/project/Test_status_code_symphony_com/tests --alluredir=allure_ss_com
Збгенерувати посилання на звіт по тестах allure serve allure_ss_com
"""
import pytest
import requests
from configuration import SERVICE_URL, ALL_URL_LIST, WRONG_URL_HTTPS, WRONG_URL_AFTER_SLASH, \
    SERVICE_URL_DEMO, WRONG_URL_HTTPS_DEMO
from src.enums.global_enums import GlobalErrorMassages


@pytest.mark.parametrize('url', ALL_URL_LIST)
def test_get_status_code_all_pages(url):
    response = requests.get(url=SERVICE_URL + url)
    assert response.status_code == 200, GlobalErrorMassages.WRONG_STATUS_CODE.value(print(SERVICE_URL + url))


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
    response = requests.get(SERVICE_URL + url)
    assert response.status_code == 404, GlobalErrorMassages.WRONG_STATUS_CODE.value


@pytest.mark.parametrize('url', ALL_URL_LIST)
def test_get_status_code_all_pages_demo(url):
    response = requests.get(url=SERVICE_URL_DEMO + url)
    assert response.status_code == 200, GlobalErrorMassages.WRONG_STATUS_CODE.value(print(SERVICE_URL_DEMO + url))


@pytest.mark.parametrize('url', WRONG_URL_HTTPS_DEMO)
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
    response = requests.get(SERVICE_URL_DEMO + url)
    assert response.status_code == 404, GlobalErrorMassages.WRONG_STATUS_CODE.value
