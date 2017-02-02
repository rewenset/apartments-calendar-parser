from lxml import html
from datetime import datetime
import json

from . import settings
from .browser import Browser


class Parser:
    def __init__(self, browser=None):
        if browser:
            self.browser = browser
        else:
            self.browser = Browser(settings.PHANTOM_JS_PATH)
        self.elements = None

    def load_settings(self, url):
        """
        Loads settings from settings.py for current hostname
        :param url: retrieves hostname from
        :return: True if loaded successfully, False -- otherwise
        """
        hostname = self.browser.get_hostname(url)
        if hostname in settings.SITE_SETTINGS:
            self.hostname = hostname
            self.dateformat = settings.DATE_FORMAT
            self.settings = settings.SITE_SETTINGS[hostname]
            return True

        print("Error. Unable to find settings for given hostname.")
        return False

    def retrieve_elements(self, url):
        """
        Builds elements tree from content given by browser
        and retrieves only desired elements.
        If setting was not loaded than no point of getting
        content because we don't know how to parse it.
        :param url:
        :return: depends on load_settings() method
        """
        if self.load_settings(url):
            content = self.browser.make_request(url)

            tree = html.fromstring(content)

            xpath = self.settings['xpath']
            self.elements = tree.xpath(xpath)

            return True

        return False

    def parse_day(self, element):
        """
        Depending on settings search date and status
        in the element
        :param element:
        :return: dictionary with useful data
        """
        dt = datetime.strptime(
            element.get(self.settings['date-attr']),
            self.settings['date-format']
        ).date()

        status = element.get(self.settings['busy-attr'])

        return {
            'date': dt.strftime(self.dateformat),
            'status': self.settings['is_free'](status)
        }

    def save_data(self, display=True):
        """
        Iterates through all elements and saves all data in JSON file.
        :param display: if where is need to display on console
        :return:
        """
        if not self.elements:
            print('Error. Unable to find elements.')
            return

        data_list = []

        for element in self.elements:
            data_list.append(
                self.parse_day(element)
            )

        output = {
            'url': self.browser.get_url(),
            'data': data_list
        }
        with open('output.json', 'w') as outfile:
            json.dump(output, outfile, indent=4)

        if display:
            print("DATE\t\tIS FREE")
            for d in data_list:
                print(d['date'] + "\t" + str(d['status']))
