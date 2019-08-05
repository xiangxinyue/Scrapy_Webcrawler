# Project Name: 
It is a simple sample of the webspider using scrapy frame. I use it to practice my skill of Python and self learn the Scrapy frame.
This README showing the process of my self study and I got some ideas from this project so that I can use this frame well in my future to do some Data Collect. I also read some paper about collect data through API after reading the document and want to do it later. Though this project is really simple at pratice level, it still can have a strong power after adding more elements so it is revised flexiable. I also want to do some Data Visualization and combine it with webspider in the future.

# Requirement
Python&Scrapy frame

# Understand what is webspider(webcrawler)
A webcrawler is an automated program that can do requests websites and collect data. In my words, Request, Collect and Automation is the corn or key term of the webspider
The whole process may have this 4 steps: First, send requests to the website. Second, get the response. Third, parse the response. Finally, save the data

# Prepare the Environment
Download the scrapy frame. 
I used the Mac OS and I found it hard to use "$ pip install Scrapy" command in my Macbook terminal. So I use the virtualenv to install Scrapy. I posted the install terminal lines in the "install the Scrapy"

# Create and Start Project
Create my new Scrapy project in the Scrapy. We need to find the location of our Scrapy installed and create our project in that folder. $ source bin/activate $ scrapy startproject mySpider (I used the mySpider in this README and it generally named with the website domain name)

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
4. we can use Chrome to get the XPATH address ( just copy the XPATH)
5. revise the parse
6. import the mySpiderItem 

# Deal with the pipelines.py and set settings.py
Set the Class and execution priority for processing the returned data

# How to save our data?
I only use the csv and it can open with Excel.
$ scrapy crawl xxx -o xxxx.csv

# Some problems may meet
1. You may need to buy a ip basement because while you are running your webspider, a error may come out. You may forbidden by the anti-robot
2. Website may always change their format and the architecture maybe really flexibility

# Conclusion 
It is easy to learn webcrawler at the entry level. However, the efficiency of webcrawler is really important. The Time and the quality of Data collected are two challenge. I still need to learn more and become stronger because Computer Science need the long time study and we will getting better and better


