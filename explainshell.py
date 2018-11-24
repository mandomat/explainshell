#!/usr/bin/env python3
import requests
import re
import sys
from html.parser import HTMLParser


def main():
    args = sys.argv

    page = requests.get("https://explainshell.com/explain?cmd="+' '.join(args[1:]))

    regex = re.compile("<pre class=\"help-box\"[^>]+>(.*?)<\/pre>",re.S)

    boxes = regex.findall(page.text)
    h = HTMLParser()
    for box in boxes:
        box = clean(box)
        print(h.unescape(box))

def clean(html):
  regex = re.compile('<.*?>')
  cleantext = re.sub(regex, '', html)
  return cleantext

if __name__ == "__main__":
    main()
