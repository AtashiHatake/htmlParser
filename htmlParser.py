import requests
from bs4 import BeautifulSoup

# article url
articleURL = 'https://indianexpress.com/article/cities/pune/pimpri-chinchwad-sub-inspector-arrested-for-links-to-45kg-mephedrone-seizure-9192223/'

# GET request to URL
getResponse = requests.get(articleURL)

# parsing the html content
soup = BeautifulSoup(getResponse.text, 'html.parser')


# extractong SEO

titleTag = soup.find('title').text if soup.find('title') else None
metaDescription = soup.find('meta', attrs={'name': 'description'})['content'] if soup.find('meta', attrs={'name': 'description'}) else None
metaKeyword = soup.find('meta', attrs={'name': 'keywords'})['content'] if soup.find('meta', attrs={'name': 'keywords'}) else None
metaAuthor = soup.find('meta', attrs={'name': 'author'}) if soup.find('meta', attrs={'name': 'author'}) else None



#printing SEO
print('title', titleTag)
print('description', metaDescription)
print('keywords', metaKeyword)
print('Author', metaAuthor)