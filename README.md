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

1. `./pushover.py "Hello world"` will send a notification with the system hostname as the title and "Hello world" as the message.
2. `./pushover.py --title "Pushover Test" "Hello world"` will send a notification with the title "Pushover Test" and the message "Hello world".
3. `./pushover.py --priority 2 "Emergency message"` will send a notification with emergency priority and the message "Emergency message"


## Practical Examples

Cron syntax to send a notification on reboot:  
`@reboot /usr/local/bin/pushover.py --priority 1 "$HOSTNAME has been rebooted: $(/usr/bin/uptime)"`
