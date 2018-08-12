import json
import logging
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


from secret import wu_da_library_entrance
from news import News


firefox_driver = '/Users/rhuan/project/graduateTraining/python-example/CrawlerChineseLib/geckodriver'
BROWSER = webdriver.Firefox()
CONFIG = {
    "start_index": 0,
    "current_index": 0
}



def open_start_page():
    print('start to open wu da library entrance page')
    BROWSER.get(wu_da_library_entrance)
    print('page opened')


def open_huike():
    print('start to open hui ke page')
    BROWSER.find_element_by_css_selector('#url a').click()
    print('hui ke opened')


def show_current_page_info():
    BROWSER.switch_to.default_content()
    print('switch to default frame')
    print('page title %s' % BROWSER.title)
    print('page url %s' % BROWSER.current_url)


def switch_to_new_windows():
    handles = BROWSER.window_handles
    BROWSER.switch_to.window(handles[1])


def switch_to_init_windows():
    handles = BROWSER.window_handles
    BROWSER.switch_to.window(handles[0])


def close_training_model():
    print('close training page')
    # webdriver.ActionChains(BROWSER).move_by_offset(1, 1).click()
    BROWSER.find_element_by_css_selector('#app-userstarterguide-0 .close').click()
    time.sleep(3)
    print('close training page')


def input_search_texts(input_text):
    print('input search text')
    js = 'document.querySelectorAll("#app-query-tageditor-instance")[0].style.display="block";'
    BROWSER.execute_script(js)
    try:
        print('change input bar attribute')
        time.sleep(3)
        search_input_bar = BROWSER.find_element_by_id('app-query-tageditor-instance')
        search_input_bar.send_keys(input_text)
        save_sc("search_text")
        print('input search finished')
        time.sleep(3)
    except Exception:
        logging.error('input error', exc_info=True)


def input_search_date(start_date, end_date):
    BROWSER.find_element_by_css_selector('#DatePickerApp .dropdown-toggle').click()
    BROWSER.find_element_by_css_selector('#searchPage .custom').click()
    try:
        start_date_input_bar = BROWSER.find_element_by_css_selector('#searchPage .rs-input-datepicker-from')
        end_date_input_bar = BROWSER.find_element_by_css_selector('#searchPage .rs-input-datepicker-to')
        start_date_input_bar.send_keys(Keys.COMMAND + "a")
        start_date_input_bar.send_keys(start_date)
        end_date_input_bar.send_keys(Keys.COMMAND + "a")
        end_date_input_bar.send_keys(end_date)
        print('input date ended')
    except Exception:
        logging.error('input error', exc_info=True)

    BROWSER.find_element_by_css_selector('#searchPage .datepicker-opt .btn-sm').click()
    print('submit date')


def save_sc(name):
    local_time = time.time()
    file_name = "%s" % str(local_time) + name + ".png"
    BROWSER.get_screenshot_as_file(file_name)


def remove_synonymicon():
    try:
        BROWSER.find_element_by_css_selector('#app-queryfilter .panel-queryfilter-scope-others .fa-angle-right').click()
        BROWSER.find_element_by_css_selector('#queryfilter-scope-others .wf-check-circle').click()
    except Exception:
        logging.error("remove_synonymicon error", exc_info=True)


def do_search():
    BROWSER.find_element_by_id('toggle-query-execute').click()
    print("excute search")

###################################################


def first_choose_all_of_current_page():
    try:
        print('choose_all_of_current_page')
        locator = (By.ID, "navbar-nav-opt-article-checkbox-div")
        WebDriverWait(BROWSER, 90, 0.5).until(expected_conditions.presence_of_element_located(locator))
        time.sleep(10)
        while CONFIG['start_index'] > CONFIG['current_index']:
            go_to_next_page()
            time.sleep(0.5)

        BROWSER.find_element_by_css_selector('#navbar-nav-opt-article-checkbox-div i').click()
        time.sleep(3)

    except Exception:
        logging.error('Exception', exc_info=True)


def choose_all_of_current_page():
    try:
        print('choose_all_of_current_page')
        locator = (By.ID, "navbar-nav-opt-article-checkbox-div")
        WebDriverWait(BROWSER, 90, 0.5).until(expected_conditions.presence_of_element_located(locator))
        time.sleep(1)
        BROWSER.find_element_by_css_selector('#navbar-nav-opt-article-checkbox-div i').click()
        time.sleep(1)

    except Exception:
        logging.error('Exception', exc_info=True)


def remove_all_of_current_page():
    try:
        print('remove_all_of_current_page')
        BROWSER.find_element_by_css_selector('#navbar-nav-opt-article-checkbox-div .fa-check-square').click()
    except Exception:
        logging.error('Exception', exc_info=True)


def go_to_next_page():
    print('go_to_next_page')
    CONFIG['current_index'] += 1

    print('current page index is' + str(CONFIG['current_index']))
    BROWSER.find_element_by_css_selector('.pagination .fa-angle-right').click()


def click_view_with_page():
    try:
        print('click_view_with_page')
        BROWSER.find_element_by_css_selector('#browse').click()
    except Exception:
        logging.error('Exception', exc_info=True)


def go_to_detail_page():
    try:
        print('go_to_detail_page')
        locator = (By.CLASS_NAME, "btn-primary")
        WebDriverWait(BROWSER, 90, 0.5).until(expected_conditions.presence_of_element_located(locator))

        BROWSER.find_element_by_css_selector('.navbar-right .dropdown-eye .btn-primary').click()
    except Exception:
        logging.error('Exception', exc_info=True)


def export_news_info_and_go_back_to_init_page():
    print('export_news_info')
    locator = (By.CLASS_NAME, "app-article")
    WebDriverWait(BROWSER, 90, 0.5).until(expected_conditions.presence_of_element_located(locator))

    news = BROWSER.find_elements_by_class_name('app-article')
    for new in news:
        title = new.find_element_by_css_selector('.col-xs-12 h3').text
        other_information = new.find_elements_by_css_selector('.col-xs-12 .article-subheading span')
        source = other_information[0].text
        word_number = other_information[1].text
        record_time = other_information[2].text
        description = new.find_element_by_css_selector('.col-xs-12 .description').text.replace("\n", "")
        news_result = News(title=title, source=source, words_number=word_number, news_time=record_time, description=description)
        with open("result.json", "a+", encoding='utf8') as f:
            f.write(news_result.to_str() + ',\n')
    print('all info exported, close current windows')
    BROWSER.close()
    switch_to_init_windows()


open_start_page()
open_huike()
# close_training_model()
show_current_page_info()
# switch_to_new_windows()
# input_search_texts(u"“烟草” / “控烟” / “禁烟”+“烟”+“烟”+“烟”-“烟花”-“烟火”")
input_search_date('2003-01-01', '2006-12-31')
remove_synonymicon()
do_search()

first_choose_all_of_current_page()
click_view_with_page()
go_to_detail_page()
switch_to_new_windows()
export_news_info_and_go_back_to_init_page()

while True:
    remove_all_of_current_page()
    go_to_next_page()

    choose_all_of_current_page()
    go_to_detail_page()
    switch_to_new_windows()
    export_news_info_and_go_back_to_init_page()
