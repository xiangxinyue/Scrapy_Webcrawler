# Project Name: scrapy_webspider by Xinyue Xiang 
It is a simple sample of the webspider using scrapy frame.
# Requirement
python&scrapy frame 
# Prepare the Environment
Download the scrapy frame. 
I use the Mac OS and I found it hard to use "$ pip install Scrapy" command in my Macbook terminal. So I use the virtualenv to install Scrapy. I posted the install terminal lines in the "install the Scrapy".
# Create and Start Project
Create my new Scrapy project in the Scrapy. We need to find the location of our Scrapy installed and create our project in that folder. $ source bin/activate $ scrapy startproject mySpider (I used the mySpider in this README and we generally named with the website domain name)
# Instruction of Documents
1. mySpider/ (Python module for a project that references code from here)
2. mySpider/items.py (sets the data module for structured data)
3. mySpider/pipelines.py (data processing)
4. mySpider/spiders (directions of spiders code)
5. scrapy.cfg & mySpider/settings.py (project configuration information and files)
# Define the scraped data : items.py
1. define the fields for your item like name = scrapy.Field
2. we can create a scrapy.item class and use scrapy.Field to define a item
# Create the webspider
1. create a webspider in the mySpider/spiders and set the domain of website: $ scrapy genspider movie "meijutt.com"
2. open the douban.py and we need to set the "name", "allow_domains", "start_urls"
3. revise the parse() and use $scrapy crawl mySpider then we got the source code information from this website
