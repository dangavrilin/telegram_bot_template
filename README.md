# Telegram bot template
## Installing
### Install dependencies
Make sure you installed [pipenv](https://github.com/pypa/pipenv)

clone this project

`cd you_project_folder`

`pipenv install`

### Set Telegram Webhook

Remove previous webhook if needed:
`curl https://api.telegram.org/bot{TOKEN}/deleteWebhook`

Set webhook:
`curl -F "url={HOST}/telegram" https://api.telegram.org/bot{TOKEN}/setWebhook`

Status and errors:
`curl https://api.telegram.org/bot{TOKEN}/getWebhookInfo`


