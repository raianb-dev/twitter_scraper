# twtter_minig

## Google Search Engine Robot

User-agent: Googlebot

*Allow: /i/api/* 

check:https://twitter.com/Robots.txt


## Browser local access key

The client will need to collect signature data from your local browser,
visit : _(https://twitter.com/explore)/__
press to ```F2``` navigate to the ```network``` tab and go over a random call and capture ```x-guest-token``` and ```authorization```.

paste in:
```
head = {'x-guest-token':'','authorization':''}
```


