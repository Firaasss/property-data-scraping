# Property Data Scraping
--------
To test and use various Python libraries

HTTP request made over realtor website containing list of properties. Python used to get this HTML content, which is parsed into a tree of objects using BeautifulSoup (method of Bs4 library). Each property's attributes are stored in a list of dictionaries, which is exported using Pandas and stored in a CSV file.
--------
 - Bs4 imports BeautifulSoup - Creates a parse tree for HTML/XML documents; used in conjunction with https get request over web page 
 - Pandas - data processing library to create table out of list of dictionaries containing property information, which is then used to export to CSV
 - Requests - Make HTTP requests over websites returning a response object with all response data (encoding, content, etc)
--------
MORE INFO

- outputted CSV file is attached
- http request is made over https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS (cached pages from Century 21 website)


