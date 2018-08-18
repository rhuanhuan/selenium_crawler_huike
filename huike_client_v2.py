import logging
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
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


def select_newspaper_only():
    try:
        BROWSER.find_element_by_css_selector('.toggle-collapse').click()
        BROWSER.find_element_by_css_selector('#accordion-queryfilter #queryfilter-scope-publisher-region .stop-propagation .wf-check-circle').click()
        BROWSER.find_element_by_css_selector('#accordion-queryfilter #queryfilter-scope-publisher-region .dropdown-queryfilter-check .label-dropdown').click()
    except Exception:
        logging.error("remove_synonymicon error", exc_info=True)


def do_search():
    BROWSER.find_element_by_id('toggle-query-execute').click()
    print("excute search")

###################################################


def wait_search_result_loaded():
    locator = (By.ID, "navbar-nav-opt-article-checkbox-div")
    try:
        print('choose_all_of_current_page')
        WebDriverWait(BROWSER, 90, 0.5).until(expected_conditions.presence_of_element_located(locator))
        time.sleep(10)
        display_summary()
        time.sleep(10)
        display_200_elements_on_one_page()
        time.sleep(10)
        while CONFIG['start_index'] > CONFIG['current_index']:
            go_to_next_page()
            time.sleep(5)
    except Exception:
        logging.error('Exception', exc_info=True)
    WebDriverWait(BROWSER, 90, 0.5).until(expected_conditions.presence_of_element_located(locator))


def display_200_elements_on_one_page():
    try:
        print('display_200_elements_on_one_page')
        BROWSER.find_element_by_css_selector('.navbar-nav-tools-settings .dropdown-toggle').click()
        time.sleep(1)
        BROWSER.find_elements_by_css_selector('.select-page-count .circles li')[4].click()
        ActionChains(BROWSER).move_by_offset(1, 1).click()
    except Exception:
        logging.error('Exception', exc_info=True)


def display_summary():
    print('add summary')
    js = 'document.querySelector("#toggle-button").click();'
    BROWSER.execute_script(js)


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
    locator = (By.CLASS_NAME, 'fa-angle-right')
    WebDriverWait(BROWSER, 90, 0.5).until(expected_conditions.presence_of_element_located(locator))
    time.sleep(1)

    BROWSER.find_element_by_css_selector('.pagination .fa-angle-right').click()

    CONFIG['current_index'] += 1
    print('current page index is ' + str(CONFIG['current_index']))


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


def export_news_info():
    print('export_news_info')
    locator = (By.CLASS_NAME, "list-group")
    WebDriverWait(BROWSER, 90, 0.5).until(expected_conditions.presence_of_element_located(locator))

    news = BROWSER.find_elements_by_css_selector('#article-tab-1-view-1 .list-group .list-group-item')
    print('\n+++++\n')
    print(len(news))
    print('\n+++++\n')
    last_record_time = None
    for new in news:
        title = new.find_element_by_css_selector('.list-group-item-heading span').text.replace("\"", "'")
        news_office = new.find_element_by_css_selector('small a').text
        word_number = str(new.find_element_by_css_selector('small span').text).split()[-1][:-1]
        record_time = new.find_element_by_css_selector('.article-main .pull-right').text
        description = new.find_element_by_css_selector('.media-body .list-group-item-text').text.replace("\n", "").replace("\"", "'")
        news_result = News(title=title, news_office=news_office, words_number=word_number, news_time=record_time, description=description)
        with open("result20030101-20061231.json", "a+", encoding='utf8') as f:
            f.write(news_result.to_str() + ',\n')
        last_record_time = record_time

    print(last_record_time)
    print('all info exported, go to next windows')


open_start_page()
open_huike()
show_current_page_info()
input_search_date('2003-01-01', '2006-12-31')
remove_synonymicon()
select_newspaper_only()
do_search()

wait_search_result_loaded()

print('wait page fully loaded')
time.sleep(5)
export_news_info()

while True:
    go_to_next_page()
    print('wait page fully loaded')
    time.sleep(5)
    export_news_info()
