import httpx
from lxml.html import fromstring
from lxml.html.clean import clean_html

# Astronomy Picture of the day website
URL = "https://apod.nasa.gov/apod/"

README_FILE=""
# Do file reading here.

def fetch_pictures():
    content = httpx.get(URL).content
    html = fromstring(clean_html(content))
    img_src_parm = html.xpath("//a")[1].get("href")
    url = URL + str(img_src_parm).strip()

    pic_xpath = html.xpath("//center[2]//b")[0]

    # img_credit_text = html.xpath("//b")[1]
    # img_credit_name = html.xpath("//a")[2]
    # credit_str = str(img_credit_text.text).strip() + str(img_credit_name.text).strip()

    pic_name = str(pic_xpath.text).strip()
    return url, pic_name


url, credit = fetch_pictures()
print(url)
print(credit)


# Do file output here.
