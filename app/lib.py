import requests
from bs4 import BeautifulSoup, SoupStrainer
import requests.exceptions as exc
from urllib import parse

def getAllLinks(url):
    link_urls = list() #to store all link urls seperately
    link_names = list() #to store all link names seperately
    try:
        response = requests.get(url)    #make a http request to get the page we want to find links for
        parsed_url = parse.urlsplit(url)

        for link in BeautifulSoup(response.content,'html.parser', parse_only=SoupStrainer("a"), ):  # for all links in the page
            if link.has_attr("href"): # if anchor tag has href tag then process
                
                href = link['href'] #extract the url from the anchor tag    
                if not href.startswith('http'):             # some paths in the anchor tag may be relative paths, we convert it into absolute
                    href = parsed_url.hostname+parsed_url.path+href

                name = link.get_text()  #extract the text inside the anchor tag

                link_urls.append(href)  #add link to link_urls
                link_names.append(name)    #add link name to link_names
        
        result = list(zip(link_urls,link_names)) #combine the two separate link_names set and link_urls set into a single list    

        return result,""        #return list along with an empty string, the empty string cause no error occured

    except exc.MissingSchema:       
        return None,"URL_EMPTY"     #if empty url is provided
    except exc.InvalidSchema:
        return None,"URL_INVALID"    #to handle invalid urls
    except exc.ConnectionError:
        return None,"CONNECTION_ERROR" #to handle connection error