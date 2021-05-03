from bs4 import BeautifulSoup
import requests
import sys

sys.stdout = open('weather_data_urls1.txt', 'w')


# urls = []


def scrape(site):
    r = requests.get(site)
    s = BeautifulSoup(r.text, "html.parser")

    hrefs = []
    for i in s.find_all("a"):
        href = i.attrs['href']

        if href.startswith("."):
            continue

        if href.endswith("/"):
            hrefs.append(href)

        if href.endswith(".csv"):
            if "2005" in href or "2006" in href or "2007" in href or "2009" in href or "2010" in href or "2011" in href or "2012" in href or "2013" in href or "2014" in href:
                    hrefs.append(href)

    if "qc-version-1/" in hrefs and "qc-version-0/" in hrefs:
        hrefs.remove("qc-version-0/")

    for href in hrefs:
        # print(href)
        if href.endswith(".csv"):
            url = site + href
            print(url)
            # if url not in urls:
            #     urls.append(site)

        elif href.endswith("/"):
            new_site = site + href
            scrape(new_site)



if __name__ == "__main__":


    site = "https://dap.ceda.ac.uk/badc/ukmo-midas-open/data/uk-hourly-weather-obs/dataset-version-201908/"
    scrape(site)

    sys.stdout.close()
