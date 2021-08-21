from python_graphql_client import GraphqlClient
import feedparser
import httpx
import json
import pathlib
import re
import os
import datetime

root = pathlib.Path(__file__).parent.resolve()
client = GraphqlClient(endpoint="https://api.github.com/graphql")

TOKEN = os.environ.get("PERSONAL_TOKEN", "")

def replace_chunk(content, marker, chunk, inline=False):
    r = re.compile(
        r"<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->".format(marker, marker),
        re.DOTALL,
    )
    if not inline:
        chunk = "\n{}\n".format(chunk)
    chunk = "<!-- {} starts -->{}<!-- {} ends -->".format(marker, chunk, marker)
    return r.sub(chunk, content)

def formatGMTime(timestamp):
    GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
    dateStr = datetime.datetime.strptime(timestamp, GMT_FORMAT) + datetime.timedelta(hours=8)
    return dateStr.date()

def fetch_code_time():
    return httpx.get(
        "https://gist.githubusercontent.com/pseudoyu/48675a7b5e3cca534e7817595d566003/raw/"
    )

def fetch_douban():
    entries = feedparser.parse("https://www.douban.com/feed/people/pseudo-yu/interests")["entries"]
    return [
        {
            "title": item["title"],
            "url": item["link"].split("#")[0],
            "published": formatGMTime(item["published"])
        }
        for item in entries
    ]

if __name__ == "__main__":
    about = root / "content/zh/about.md"
    about_contents = about.open().read()

    code_time_text = "\n```text\n"+fetch_code_time().text+"\n```\n"
    rewritten = replace_chunk(about_contents, "code_time", code_time_text)

    doubans = fetch_douban()[:5]
    doubans_md = "\n".join(
        ["* <a href='{url}' target='_blank'>{title}</a> - {published}".format(**item) for item in doubans]
    )
    rewritten = replace_chunk(rewritten, "douban", doubans_md)
    about.open("w").write(rewritten)