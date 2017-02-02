from selenium import webdriver
from urllib.parse import urlparse


class Browser:
    def __init__(self, exec_path=None):
        print("Creating browser...")
        if exec_path:
            self.driver = webdriver.PhantomJS(
                executable_path=exec_path
            )
        else:
            self.driver = webdriver.PhantomJS()

    def make_request(self, url):
        """
        :param url: makes GET request to that url
        :return: source of loaded page
        """
        print("Making request...")
        self.driver.get(url)
        return self.driver.page_source

    def get_hostname(self, url=None):
        """
        Retrieves hostname from given url
        :param url:
        :return: hostname without 'www.'
        """
        if not url:
            url = self.get_url()
        url = urlparse(url)
        hostname = url.netloc
        return hostname.replace('www.', '')

    def get_url(self):
        return self.driver.current_url

    def __del__(self):
        self.driver.quit()
