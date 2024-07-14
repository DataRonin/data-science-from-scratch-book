import re

def tokenize(text: str) -> set:

    text = text.lower()
    all_words = re.findall('[a-z0-9]+',text) # extract words
    return set(all_words)

assert tokenize('Data science is science') == set(['data','science','is'])

from typing import NamedTuple

class Message(NamedTuple):
    text: str
    is_spam: bool

from typing import List, Tuple, Dict, Iterable, Set
from collections import defaultdict
import math

class NaiveBayesClassifier:

    def __init__(self, k: float = 0.5) -> None:
        self.k = k
        self.tokens: Set[str] = set()
        self.token_spam_counts: Dict[str,int] = defaultdict(int)
        self.token_ham_counts: Dict[str,int] = defaultdict(int)
        self.spam_messages = self.ham_messages = 0
    
    def train(self, messages: Iterable[Message]) -> None:

        for message in messages:

            if message.is_spam:
                self.spam_messages += 1
            
            else:
                self.ham_messages += 1
            
            for token in tokenize(message.text):

                self.tokens.add(token)

                if message.is_spam:
                    self.token_spam_counts[token] += 1
                
                else:
                    self.token_ham_counts[token] += 1

    def _probalities(self, token: str) -> Tuple[float, float]:
        spam = self.token_spam_counts[token]
        ham = self.token_ham_counts[token]
        
        p_token_spam = (spam + self.k) / (self.spam_messages + 2 * self.k)
        p_token_ham = (ham + self.k) / (self.ham_messages + 2 * self.k)

        return p_token_spam, p_token_ham
    
    def predict(self, text: str) -> float:
        text_tokens = tokenize(text)
        log_prob_is_spam = log_prob_is_ham = 0.0
        for token in self.tokens:
            prob_if_spam, prob_if_ham = self._probalities(token)
            if token in text_tokens:
                log_prob_is_spam += math.log(prob_if_spam)
                log_prob_is_ham += math.log(prob_if_ham)
            else:
                log_prob_is_spam += math.log(1.0 - prob_if_spam)
                log_prob_is_ham += math.log(1.0 - prob_if_ham)
        prob_if_spam = math.exp(log_prob_is_spam)
        prob_if_ham = math.exp(log_prob_is_ham)
        return prob_if_spam / (prob_if_spam + prob_if_ham)
# testing model

messages = [
            Message('spam rules', is_spam = True), 
            Message('ham rules', is_spam = False), 
            Message('hello ham', is_spam = False)
            ]
model = NaiveBayesClassifier(k = 0.5)
model.train(messages)

assert model.tokens == {'spam','ham','rules','hello'}
assert model.spam_messages == 1
assert model.ham_messages == 2
assert model.token_spam_counts == {'spam':1,'rules':1}
assert model.token_ham_counts == {'ham':2,'rules':1,'hello':1}

text = 'hello spam'

probs_if_spam = [ 
                (1 + 0.5) / (1 + 2 * 0.5), # spam 
                 1 - (0 + 0.5)/(1 + 2 * 0.5), # ham
                 1 - (1 + 0.5) / (1 + 2 * 0.5), # rules
                 (0 + 0.5) / (1 + 2 * 0.5) # hello
]

probs_if_ham = [
    (0 + 0.5) / (2 + 2 * 0.5), # spam
    1 - (2 + 0.5) / (2 + 2 * 0.5), # ham
    1 - (1 + 0.5) / (2 + 2 * 0.5), # rules
    (1 + 0.5) / (2 + 2 * 0.5) # hello
]

p_if_spam = math.exp(sum(math.log(p) for p in probs_if_spam))
p_if_ham = math.exp(sum(math.log(p) for p in probs_if_ham))

assert model.predict(text) == p_if_spam / (p_if_spam + p_if_ham)

# using model

from io import BytesIO
import requests
import tarfile

# dataset - https://spamassassin.apache.org/old/publiccorpus/ | prefix - 20021010

BASE_URL = 'https://spamassassin.apache.org/old/publiccorpus/'
FILES = ['20021010_easy_ham.tar.bz2',
         '20021010_hard_ham.tar.bz2',
         '20021010_spam.tar.bz2'
         ] 

OUTPUT_DIR = 'spam_data'

for filename in FILES:
    
    content = requests.get(f'{BASE_URL}/{filename}').content
    fin = BytesIO(content)

    with tarfile.open(fileobj=fin,mode='r:bz2') as tf:
        tf.extractall(OUTPUT_DIR)

import glob, re

path = 'spam_data/*/*'
data: List[Message] = []

for filename in glob.glob(path):
    is_spam = 'ham' not in filename
    with open(filename,errors='ignore') as email_file:
        for line in email_file:
            if line.startswith('Subject:'):
                subject = line.strip('Subject: ')
                data.append(Message(subject, is_spam))
                break

import random
import ml

random.seed(0)
train_messages, test_messages = ml.split_data(data, 0.75)
model = NaiveBayesClassifier()
model.train(train_messages)

from collections import Counter

predictions = [(message, model.predict(message.text)) for message in test_messages]

confusion_matrix = Counter((message.is_spam, spam_probability > 0.5) for message, spam_probability in predictions)

print(confusion_matrix)

def p_spam_given_token(token: str, model: NaiveBayesClassifier) -> float:
    prob_if_spam, prob_if_ham = model._probalities(token)
    return prob_if_spam / (prob_if_spam + prob_if_ham)

words = sorted(model.tokens, key = lambda t: p_spam_given_token(t, model))

print(f'most_spam_words: {words[-10:]}')
print(f'not_most_spam_words: {words[:10]}')
