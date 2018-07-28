#!/usr/bin/env python

# import your random module here
import random
#import time module

import time

# create a list of mystic responses
mystic_responses = ['Of course',
                    'No way',
                    'I don\'t think so',
                    'Maybe',
                    'Perhaps']

# create a list of wait responses
wait_responses = ['Please, wait',
                  'Thinking',
                  'Asking the universe',
                  'Listening to the universe',
                  'Hmmmm']

# create a list of fortunes
list_of_fortunes = ['Good things come to those who wait',
                  'Patience is a virtue',
                  'The early bird gets the worm',
                  'A wise man once said, everything in its own time and place',
                  'Fortune cookies rarely shares fortunes']

# ask for a yes/no question or a fortune
# do the mystic response if they wanted a question
# do the fortune if they asked for a fortune
question = input ('What is your questions?')
print(random.choice(mystic_responses))
time.sleep(5)
print(random.choice(wait_responses))
print(random.choice(list_of_fortunes))
