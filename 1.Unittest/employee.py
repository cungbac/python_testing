import requests
import unittest
from unittest.mock import patch, MagicMock

class Employee:
    """A sample Employee class"""
    raise_amt = 10.5

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'
        

def len_joke():
    joke = get_joke()
    print(joke)
    return len(joke)

def get_joke():
    url = 'http://api.icndb.com/jokes/random'
    response = requests.get(url)
    if response.status_code == 200:
        joke = response.json()['value']['joke']
    else:
        joke = 'No jokes'
    
    return joke

if __name__ == '__main__':
    len_joke()
    print(get_joke())