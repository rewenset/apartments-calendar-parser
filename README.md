## Apartment booking site parser  
**Parsing calendars from appartment booking sites and saving data in JSON file format.**  

This project uses **Selenium WebDriver** and **PhantomJS**   
to get page content and **lxml** library for parsing pages.   

### Installation  
required: Python 3.5  

1. Install requirements from *requirements.txt*:  
  `pip install -r requirements.txt`  
2. Get **PhantomJS**.  
  For Windows users:  
  + [download package](http://phantomjs.org/download.html)  
  + in *settings.py* specify path to phantomjs.exe file  
  
  For users with Linux or MacOS welcome to [google](http://google.com/) :)  

### Usage  
Example of usage shown in *main.py*  

### Currently supporting:  
* [oktv.ua](http://oktv.ua/)  
* [dobovo.com](http://dobovo.com/)  

But you can expand capabilities by adding another site settings in *settings.py*.  
