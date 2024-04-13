#!/usr/bin/env python3
# pip install requests beautifulsoup4

import argparse
import requests
from bs4 import BeautifulSoup


def fetch_kanji_info(kanji):
    url = f"https://jisho.org/search/{kanji}%20%23kanji"
    r = requests.get(url)
    if r.status_code != 200:
        return None

    soup = BeautifulSoup(r.text, "html.parser")
    bushu = (
        soup.find("div", class_="radicals").find("span").text.split("\n")[-2].strip()
    )
    try:
        onyomi = [
            res.text.strip()
            for res in soup.find("div", class_="row kanji-details--section")
            .find("div", class_="kanji-details__main-readings")
            .find("dl", class_="dictionary_entry on_yomi")
            .find_all("a")
        ]
    except AttributeError:
        onyomi = []
    try:
        kunyomi = [
            res.text.strip().split(".")[0]  # remove okurigana
            for res in soup.find("div", class_="row kanji-details--section")
            .find("div", class_="kanji-details__main-readings")
            .find("dl", class_="dictionary_entry kun_yomi")
            .find_all("a")
        ]
    except AttributeError:  # given character has no kunyomi
        kunyomi = []
    imi = soup.find("div", class_="kanji-details__main-meanings").text.strip()

    return {
        "bushu": bushu,
        "onyomi": onyomi,
        "kunyomi": kunyomi,
        "imi": imi,
    }


def main(args):
    if not (res := fetch_kanji_info(args.kanji)):
        return
    print(res["bushu"])
    print("、".join(res["onyomi"]))
    print("、".join(res["kunyomi"]))
    print(res["imi"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("kanji", type=str, help="Kanji character")
    args = parser.parse_args()
    main(args)
