# text2sheet
Simple tool which allows you to send a text message to a number and have it appear in a Google Spreadsheet.

## Setup
* Deploy an AWS Lambda using the [python-lambda](https://github.com/nficano/python-lambda) library with the code in the [text2sheet](text2sheet/) directory. 
* Hook up the Lambda with API Gateway and a Twilio account using [these](https://www.twilio.com/docs/sms/tutorials/how-to-receive-and-reply-python-amazon-lambda) instructions
* Create a Google Spreadsheets Service Account using the instructions from [here](https://gspread.readthedocs.io/en/latest/oauth2.html)
* Add the Google authentication credentials into a file called `gauth.json` which is packaged along with the lambda
* Add a list of verified numbers you wish to be receiving messages from and responding to in a file called `phone_numbers.json`. This is also packaged with the lambda.
* Text your Twilio number and enjoy great success!

![](https://www.myinstants.com/media/instants_images/boratgs.jpg)
