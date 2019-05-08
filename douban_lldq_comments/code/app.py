from code.crawl import crawl
from code.save_to_mongo import save_to_mongo


def main():
    for contents in crawl():
        for content in contents:
            save_to_mongo(content)
