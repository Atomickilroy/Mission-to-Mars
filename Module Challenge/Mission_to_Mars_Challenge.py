#!/usr/bin/env python
# coding: utf-8

# In[1]:


# step 1

# Import Splinter and BeautifulSoup

from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[2]:


# step 2 

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# step 3 

# Visit the mars nasa news site

url = 'https://redplanetscience.com'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


# step 4

html = browser.html

news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')

#This means that this element holds all of the other elements
#within it, and we'll reference it when we want to filter search
#results even further. 


# In[5]:


# step 5

slide_elem.find('div', class_='content_title')

#The output should be the HTML containing the content title
#and anything else nested inside of that <div />


# In[6]:


#Step 6

# Use the parent element to find the first `a` tag and save it as `news_title`

news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

#The code above, for example, would return only the title of
#the news article and not any of the HTML tags or elements.


# In[7]:


## look above by chaining the .get_text() to our find
# only the text of the element is returned


# In[8]:


# Step 8

# Grab only the article for this title
# Use the parent elemeent to find the para txt

new_s = slide_elem.find('div' , class_ = 'article_teaser_body').get_text()
new_s


# # **10.3.4 Scrape Mars Data: Featured Image**
# 
# ### Featured Images

# In[9]:


# Visit URL

url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[10]:


# Find and click the full image button

full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[11]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[12]:


# Find the relative image url

img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel 


# In[13]:


# add the partial link to the rest of the url

img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ## *10.3.5 Scrape Mars Data:Mars Facts*

# In[14]:


#Scrape Mars table with pandas read html

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[15]:


df.to_html()


# In[62]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[82]:


# 2. Create a list to hold the images and titles.

hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

html = browser.html
links_soup = soup(html, 'html.parser')

#Identify Common Tag

img_links = links_soup.find_all('img', class_= "thumb")


for i in range(4):
    
    #Find/ click each image
    thumb_img = browser.find_by_tag('h3')[i].click()    
    html = browser.html    
    img_soup = soup(html, 'html.parser')  
    
    #Grab the Url
    #img_url_rel = img_soup.find('img', class_='wide-image').get('src')
    
    img_url = 'https://marshemispheres.com/' + (img_soup.find('img', class_='wide-image').get('src'))  
                                                                
    title = img_soup.find('h2', class_='title').text   
                                                                
    #Create Dictionary/append hemisphere_image_urls      
                                                              
    link_dict = {'img_url' : img_url, 'title' :title}
    hemisphere_image_urls.append(link_dict)
    
    #Direct Back 
                                                              
    browser.back()
  


# In[83]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[ ]:





# In[84]:


browser.quit()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




