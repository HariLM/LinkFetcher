import requests
from bs4 import BeautifulSoup, SoupStrainer
import requests.exceptions as exc

def getAllLinks(url):
    link_urls = set() #to store all link urls seperately
    link_names = set() #to store all link names seperately
    try:
        response = requests.get(url)    #make a http request to get the page we want to find links for
        
        for link in BeautifulSoup(response.content,'html.parser', parse_only=SoupStrainer("a"), ):  # for all links in the page
            if link.has_attr("href"): # if anchor tag has href tag then process
                url = link['href'] #extract the url from the anchor tag     
                name = link.get_text()  #extract the text inside the anchor tag
                link_urls.add(url)  #add link to link_urls
                link_names.add(name)    #add link name to link_names
        
        result = list(zip(link_urls,link_names)) #combine the two separate link_names set and link_urls set into a single list    

        return result,""        #return list along with an empty string, the empty string cause no error occured

    except exc.MissingSchema:       
        return None,"URL_EMPTY"     #if empty url is provided
    except exc.InvalidSchema:
        return None,"URL_INVALID"    #to handle invalid urls
    except exc.ConnectionError:
        return None,"CONNECTION_ERROR" #to handle connection error