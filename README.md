# twtter_scraper

1nfluencersmarketing.com
@Author : Raian Barbosa


## Google Search Engine Robot

User-agent: Googlebot

*Allow: /i/api/* 

check: https://twitter.com/Robots.txt


## Browser local access key

The client will need to collect signature data from your local browser,
visit : _(https://twitter.com/explore)_
press to ```F2``` navigate to the ```network``` tab and go over a random call 'http' and capture ```x-guest-token``` and ```authorization```.

paste in:
```
head = {'x-guest-token':'','authorization':''}
```
## Install requirements

``` 
pip install pandas
pip install numpy
pip install requests
```
#### run:

``` main.ipynb``` for Jupyter Notebook, Python3

``` main.py``` for Python2

