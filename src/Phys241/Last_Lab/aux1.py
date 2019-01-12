import sys
import time

trek1 = open('contact.txt', 'r')
trek2 = open('frontier.txt', 'r')
contact = trek1.read()
frontier = trek2.read()


def printer(str):
    for letter in str:
        try:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.05)
        except KeyboardInterrupt:
            continue
