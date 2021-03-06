# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 18:43:46 2020

@author: PRATMS
"""

import time
import webScrapping
import listToNestedDict
import writeToExcelFromDict
#import googleSearchQuery

bookNestedDict = {}
extractedValueDict = []


def main():
    start = time.time()
    urlIMDb={"https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&ref_=adv_prv",
	"https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=51&ref_=adv_nxt",
	"https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=101&ref_=adv_nxt",
	"https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=151&ref_=adv_nxt",
	"https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=201&ref_=adv_nxt"}
    for url in urlIMDb:
        extractedValueDict.append(webScrapping.scrapingFunction(url,"h3","lister-item-header"))
        print("exctred value dict from main"+str(extractedValueDict))
        time.sleep(2)
        bookNestedDict=(listToNestedDict.listToDictFunction(extractedValueDict))
    # webScrapping.scrapingFunction(url, "strong", "id ke")
    #extractedValueDict = webScrapping.scrapingFunction(url, "strong", "id ke")
    # dictToNestedDict.HtmlToDictFunction(webScrapping.scrapingFunction.extractedValueDict)
    #bookNestedDict = listToNestedDict.listToDictFunction(extractedValueDict)
    #writeToExcelFromDict.writeToExcelFunction(bookNestedDict)
    print(bookNestedDict)
    end = time.time()
    print("time taken by program is:" + str(end - start))


if __name__ == '__main__':
    main()
