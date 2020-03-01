# Using just Twitter Data to track the spread of the Coronavirus (COVID-19)
This application uses Twitter Data (i.e. specifically tweets and user profile or tweet location) to track the spread of the Coronavirus (Covid-19). Exactly 5000 tweets were analysed starting from December 2019 until the end of February 2020. There are a couple of limitations of this application, however, it is a good starting point for further, more detailed development. 

![image](https://user-images.githubusercontent.com/17982289/75628863-d0a6ad00-5bd4-11ea-9ec1-57cac899852f.png)

The number and location of confirmed cases are shown in this map produced by The Center for Systems Science and Engineering at Johns Hopkins University. For the latest results see https://www.nytimes.com/interactive/2020/world/coronavirus-maps.html. 
![image](https://user-images.githubusercontent.com/17982289/75635617-6fe89600-5c0f-11ea-9859-1e2120c04cbf.png)


## Steps to Replicate
* Apply for a Twitter Developer account to gain access to their API (this takes minutes to obtain). Do the same with [Google Maps](https://console.cloud.google.com/apis/credentials?project=mimetic-math-236517&folder=&organizationId=). You only need the **Maps JavaScript API** for this project the others are unnecessary. The Quota for this API is reletively high and you will unlikely overshoot it for this application specifically. 
* Install the latest version of Python onto your machine or alternatively install Anaconda and Jupyter Notebooks (easier/faster approach).
* Place the API credentials you have received into the application.
* Install packages using the pip command, one such package is geopy which helps you integrate Google Maps into your application. You will only come to know of the packages to install when you encounter errors when running the code that prevent you from proceeding.


## Limitations
* Number of tweets collected. Anything > 5000 takes a significant time to process. 
* Only tweets in English were analysed this is because only one language at a time can be processed. There might be a tweepy functionality that supports multiple languages in a query but I could not find it. 
* Still a lot of cleaning of the data needs to be done like removing Retweets and multiple occurrances of the same tweet (maybe a bot produced these).
* The word "coronavirus" is actually a generic term and that is why you will still see tweets from people even before December 2019. So it is **not** conclusive to say that tweets after December 1st 2019 are all related to the COVID-19 outbreak and not any of the other coronaviruses such as [SARS-CoV (2003)](https://www.who.int/ith/diseases/sars/en/) and [MERS-CoV (2012)](https://www.who.int/news-room/fact-sheets/detail/middle-east-respiratory-syndrome-coronavirus-(mers-cov) ).

## Conclusion 
There is a correlation with some descrepancy in the number and location fo people talking about the coronavirus and the actually cases/occurances of it. Now, it is important to note that we see this correlation predominately in the countries that have English as one of their main languages. If more languages such as Chinese, Portuguese, French, Russian, Arabic and so on where integrated into the application then places like China, Brazil, France, Russia and Iran will "light up"  respectively. 

## Resources
For Mapping - [Python Geopy Library Documentation](https://readthedocs.org/projects/geopy/downloads/pdf/latest/)
Getting started with Twitter Data Analysis - [Tweepy Basics Example](https://www.earthdatascience.org/courses/earth-analytics-python/using-apis-natural-language-processing-twitter/get-and-use-twitter-data-in-python/)
An incredibly good, detailed and advanced example of a similar project [here](https://github.com/globalcitizen/2019-wuhan-coronavirus-data)
Twitter query parameters [here](https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets)
Streaming Twitter Data for more recent results [here](https://www.dataquest.io/blog/streaming-data-python/) and [more](https://books.google.co.uk/books?id=YBKSDwAAQBAJ&pg=PA121&lpg=PA121&dq=python+mystreamer+class&source=bl&ots=bJcGzNzquN&sig=ACfU3U2WGfXAIvJmXXm4GvAIcsqCwas8Qw&hl=en&sa=X&ved=2ahUKEwiY1v69uPbnAhUBonEKHexABu0Q6AEwA3oECAkQAQ#v=onepage&q=python%20mystreamer%20class&f=false)
[More examples](https://www.promptcloud.com/blog/scrape-twitter-data-using-python-r/) relating to scraping 


