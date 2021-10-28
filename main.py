import requests
from bs4 import BeautifulSoup
import pandas

base_url = ("https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s=")
listProperty = []  #empty list for end data
#looping through pages
for page in range(0,30,10):
    #getting each page
    newurl = base_url+str(page)+".html"

    #header over https to pull page html content
    r = requests.get(newurl, headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    page = r.content
    soup = BeautifulSoup(page, "html.parser")

    #getting all properties
    propertyRows = soup.find_all("div", {"class": "propertyRow"})

    for property in propertyRows:
        d = {} #empty dictionary
        d["Address"] = property.find_all("span", {"class": "propAddressCollapse"})[0].text
        d["Locality"] = property.find_all("span", {"class": "propAddressCollapse"})[1].text
        d["Price"] = property.find("h4", {"class": "propPrice"}).text.replace("\n", "").replace(" ","")
        try:
            d["Beds"] = (property.find("span", {"class": "infoBed"}).find("b", recursive=False).text)
        except (AttributeError):
            d["Beds"] = None
        try:
            d["Full Baths"] = (property.find("span", {"class": "infoValueFullBath"}).find("b", recursive=False).text)
        except (AttributeError):
            d["Full Baths"] = None
        try:
            d["Half Baths"] = int(property.find("span", {"class": "infoValueHalfBath"}).find("b", recursive=False).text)
        except (AttributeError):
            d["Half Baths"] = None
        try:
            d["Square Foot"] = int((property.find("span", {"class": "infoSqFt"}).find("b", recursive=False).text).replace(',', ''))
        except (AttributeError):
            d["Square Foot"] = None


        for columns in property.find_all("div", {"class": "columnGroup"}):
            for feature_group, feature_name in zip(columns.find_all("span", {"class": "featureGroup"}), columns.find_all("span", {"class": "featureName"})):
                # print(feature_group.text)
                try:
                    if "Age" in feature_group.text:
                        d["Age"] = feature_name.text
                except ValueError:
                        d["Age"] = None

        #adding values from dictionary for each property loop into main list
        listProperty.append(d)

    df = pandas.DataFrame(listProperty)
    print(df)
    df.to_csv("output.csv")
