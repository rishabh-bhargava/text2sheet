## Testing the lambda locally
Run `lambda invoke -v` in your terminal and the event from `event.json` will be sent to your lambda code. 

## Deploying the lambda to AWS
From within this folder, run `lambda deploy --requirements requirements.txt`. This will deploy the lambda using the configuration from `config.yaml` by zipping the code and dependencies specified in the `requirements.txt` file and pushing to AWS. 