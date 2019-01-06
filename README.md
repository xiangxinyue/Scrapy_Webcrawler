# Project Name: scrapy_webspider by Xinyue Xiang 
# Requirement
python&scrapy frame 
# Prepare the Environment
Download the scrapy frame. 
I use the Mac OS and I found it hard to use "$ pip install Scrapy" command in my Macbook terminal. So I use the virtualenv to install Scrapy. I posted the install terminal lines in the "install the Scrapy".
# Create and Start Project
Create my new Scrapy project in the Scrapy. We need to find the location of our Scrapy installed and create our project in that folder.
$ scrapy startproject XXX (I used the mySpider in this README and we generally named with the website domain name)
# Instruction of Documents
1. mySpider/ (Python module for a project that references code from here)
2. mySpider/items.py (sets the data store template for structured data)
3. mySpider/pipelines.py (data processing)
4. mySpider/spiders (directions of spiders code)
5. scrapy.cfg & mySpider/settings.py (project configuration information and files)
# items.py : Define the data we want to scrape


