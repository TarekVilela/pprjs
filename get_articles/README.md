What it does: download and save the article ou articles in a txt file named with the article's name. 
Requirements:
  - requests
  - bs4
 
 Usage: get_article(x), where x can be a link ou a txt file with one article per line. 
 
 Examples: 
  - get_article('https://www.theatlantic.com/business/archive/2017/10/midwestern-public-research-universities-funding/542889/')
  - get_article('list.txt')
  
Sites supported so far:
  - The Atlantic
  - Yahoo
  - G1
