# pushover-cli
A single-file Python script to send Pushover notifications via the command line.

## Dependencies
A standard installation of python3 should be all that is needed.

## Usage and Examples

The `--help` option gives a basic overview:

    usage: pushover.py [-h] [--priority PRIORITY] [--title TITLE] [--sound SOUND]
                    [--quiet]
                    message

    Pushover notification gateway

    positional arguments:
      message              Pushover message

    optional arguments:
      -h, --help           show this help message and exit
      --priority PRIORITY  Message Priority. -1 quiet; 0 default, 1 high; 2
                           emergency
      --title TITLE        Message title. Defaults to system hostname (glados)
      --sound SOUND        Message Sound. See https://pushover.net/api#sounds
      --quiet              Use return codes instead of text

Send the notification "Hello world" (uses system hostname as notification title):  
`./pushover.py "Hello world"`

Send the notification "Hello world" with title "Pushover test":  
`./pushover.py --title "Pushover Test" "Hello world"`

Send the notification "Emergency message" with emergency (level 2) priority (uses system hostname as notification title):  
`./pushover.py --priority 2 "Emergency message"`


## Practical Examples

Cron syntax to send a notification on reboot:  
`@reboot /usr/local/bin/pushover.py --priority 1 "$HOSTNAME has been rebooted: $(/usr/bin/uptime)"`
