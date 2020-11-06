#import bs4 as bs

import bs4 as bs
import urllib.request

emailSet = set()
urlSet = set()

mailto = "mailto:"
outsideDomain = "http"
tel = "tel:"
javascript = "javascript:"
emptySlash = "/"
hastag = "#"
at = "@"

domain = '' #TYPE IN DOMAIN HERE

source = urllib.request.urlopen(domain).read()

soup = bs.BeautifulSoup(source,'html.parser')



for url in soup.find_all('a'):

    path = url.get('href')

    


    try :
        if mailto in path:
            
            if at in path:
                emailSet.add(path[7:])

        else:

            if tel not in path:
                if javascript not in path:

                    if outsideDomain in path:
                        continue

                    elif domain in path:
                        urlSet.add(path)
                        

                    else:
                        if path != emptySlash:
                            urlSet.add(domain + path)
                                

    except:
        continue

for url in urlSet:

    try:

        print(url)
        source = urllib.request.urlopen(url).read()
        soup = bs.BeautifulSoup(source,'html.parser')

        for url in soup.find_all('a'):
            path = url.get('href')

            if mailto in path:
                if at in path:
                    emailSet.add(path[7:])

            

    except:
        continue
        

for email in emailSet:
    print("email = ",email)


