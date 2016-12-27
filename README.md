### bdgabot

This is a script for periodically checks for new arrivals at *Bodega*, Boston's famous [hidden sneaker store](http://vergecampus.com/2016/04/bodega-bostons-best-kept-sneaker-secret/).

![bodega](http://redirect.viglink.com/?format=go&jsonp=vglnk_148280453683015&key=df0db99c24b1b40137920f96d4493326&libId=ix6v1jrr0101hgtq000DLs5re1x1qaufp&loc=http%3A%2F%2Fvergecampus.com%2F2016%2F04%2Fbodega-bostons-best-kept-sneaker-secret%2F&v=1&out=http%3A%2F%2Fd2118lkw40i39g.cloudfront.net%2Fwp-content%2Fuploads%2F2016%2F04%2Fg8kcdcn92fkpqhnm6kzo.jpg&title=Bodega%3A%20Boston%27s%20Best%20Kept%20Sneaker%20Secret%20-%20Verge%20Campus&txt=)

To accomplish this, we periodically make HTTP requests Bodega's `New Arrivals` page and compare the response via `SHA1`. If the current hash does not match the previous one, we know that th page has updated. We then send ourselves and SMS alert via Twilio. 

-

##### Setup

First, you must install Twilio for Python:

```
pip install twilio
```

You must also set up a file named `twilio_credentials.py` in the project directory with the following contents:

```
account_sid = "YOUR_TWILIO_ACCOUNT_SID"
auth_token  = "YOUR_TWILIO_AUTH_TOKEN"
welsny_cell = "YOUR_CELL_NUMBER"
twilio_cell = "YOUR_TWILIO_NUMBER"
```

Finally, run the script in the background with `./main.py &`

-

##### Configuration

You can configure the delay between checks in `main.py`. You can also configure this script to run on different websites. 

-

##### Misc.

For those of you interested in fashion, check out [my page on Grailed](https://www.grailed.com/users/120044-wslyksfbs/wardrobe)! Discount if I know you irl 😂
