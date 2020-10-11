import httpx
from lxml.html import fromstring
from lxml.html.clean import clean_html

# Astronomy Picture of the day website
URL = "https://apod.nasa.gov/apod/"

README_FILE=""
# Do file reading here.

def fetch_pictures():
    print('[*] Step 1')
    content = httpx.get(URL).content
    # print(content)
    html = fromstring(clean_html(content))
    img_src_parm = html.xpath("//a")[1].get("href")
    print(f"{URL}{img_src_parm}")
    img_credit_text = html.xpath("//b")[1]
    img_credit_name = html.xpath("//a")[2]
    credit_str = str(img_credit_text.text + img_credit_name.text).strip()
    print(credit_str)


fetch_pictures()


# Do file output here.
