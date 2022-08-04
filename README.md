# us_visa_appointment_scrapper

For scheduling and Rescheduling US Visa Appointment


## Prerequisite

* ubuntu arm instance (should be working in non-arm device too !)
* python3
* pip
* Telegram group chat with bot
  * create a new bot [docs](https://sendpulse.com/knowledge-base/chatbot/create-telegram-chatbot)
  * send a test message to the bot
  * Add the Telegram BOT to the group.
    * Get the list of updates for your BOT:
    
    ```
    https://api.telegram.org/bot<YourBOTToken>/getUpdates
    ```

    Ex:
    
    ```
    https://api.telegram.org/bot123456789:jbd78sadvbdy63d37gda37bd8/getUpdates
    ```

    * Look for the "chat" object and get the group_id:

    ```
    {"update_id":8393,"message":{"message_id":3,"from":{"id":7474,"first_name":"AAA"},"chat":{"id":<group_ID>,"title":""},"date":25497,"new_chat_participant":{"id":71,"first_name":"NAME","username":"YOUR_BOT_NAME"}}}
    ```
* pagem api_key and app_id - [docs](https://www.pagem.com/api)

### Additional Info

This script is tested working on follwoing versions on arm device

```
$ date
Thu Aug  4 11:35:25 UTC 2022

$ uname -a
Linux hms-684508 5.13.0-1030-oracle #35~20.04.1-Ubuntu SMP Wed May 25 23:19:48 UTC 2022 aarch64 aarch64 aarch64 GNU/Linux

$ python3 --version
Python 3.8.10

$ pip --version
pip 22.2.1 from /home/ubuntu/.local/lib/python3.8/site-packages/pip (python 3.8)
```

## Setup

1. run `./setup.sh` script
2. replace the values in `creds.py`
3. create a `crontab` entry for your use case, replace `SCRIPT_DIRECTORY` with the location where you cloned the repo
    ```
    # for scheduling
    */15 * * * * ! test -f SCRIPT_DIRECTORY/cron_test.txt && cd SCRIPT_DIRECTORY && python3 check_new_appointment.py > /dev/null 2>&1

    # for re-scheduling
    */15 * * * * ! test -f SCRIPT_DIRECTORY/cron_test.txt && cd SCRIPT_DIRECTORY && python3 reschedule_appointment.py > /dev/null 2>&1
    ```
4. [OPTIONAL] Send a test message to telegram
```
python3 ./telegram.py 
```

## Huge Shout Out (Thanks ! ✨)

Thanks to the following repository and the author for their wonderfull work, I copied most of the code from them and modified for my purpose and use case to support [pagem](https://www.pagem.com/) for paging me.

* https://github.com/Ed1123/visa_web_scraper
* https://github.com/uxDaniel/visa_rescheduler
