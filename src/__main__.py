#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 17:44:12 2020

@author: VictorioMolina
"""

from operator import itemgetter
import numpy as np
import requests as reqs
import csv, json, re

# Get position of an item in a given list
def get_position(l, n=0):
    if l[0]==n and l[-1]==n:
       print("Found at the start and at the end of the list")
    elif n in l:
        print("Found")
    else:
        print("Not found")
        
             
# Check if an specific number is prime
def is_prime(n):
    if n < 1:
        return False
    
    for i in range(2, n):
        if not (n % i):
            return False;
    else:
        return True

    
# Check if a given string is a palyndrome
def is_palyndrome(_str):
    return _str.lower() == _str[::-1].lower()


# Auxiliar function
def get_longest_common_prefix(strs):
    if not strs:
        return ""
    
    min_s = min(strs)
    max_s = max(strs)
    
    if not min_s:
        return ""
    
    for i in range(len(min_s)):
        if max_s[i] != min_s[i]:
            return max_s[:i]        
    else:
        return min_s
    
# Get a set with all common prefix in a list of words
def get_prefix_set(l):
    for subl in l:
        print(get_longest_common_prefix(subl))
        
        
# Functions to remove duplicates in a list      
def remove_duplicates(l):
    return list(np.unique(l))

def remove_duplicates_list_of_lists(l):
    # Flatten the list
    flattened_list = [y for x in l for y in x]
    return remove_duplicates(flattened_list)


# Sort a given list of tasks by priority
def get_sorted_tasks(tasks):
    if(not tasks):
        print('There are no tasks...')
        return []
    
    return sorted(tasks, key=itemgetter('priority'), reverse=True)


# 'Pop' most priority task in a given list
def pop_most_priority_task(tasks):
    most_priority_task = get_sorted_tasks(tasks)[0]
    tasks.remove(most_priority_task)

    return most_priority_task


# .csv to dict
def csv_to_dict(path):
    dict = {}
    
    with open(path) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            # The first word of the row is the key
            # The other words of the row form part of the value
            dict.update({row[0]: [x.strip(' ') for x in row[1:]]})
            
    return dict


# Get percent of vowels and spaces in a string
def get_vowels_spaces_percent(_str):
    tokens = (' ', 'a', 'e', 'i', 'o', 'u')
    return '{:.2f}%'.format(sum(_str.count(_) for _ in tokens) / len(_str) * 100)
    

# Hangman game
def mini_hangman_game():
    # Fetching a random word from Rest API
    url = "http://api.wordnik.com/v4/words.json/randomWords?\
        hasDictionaryDef=true\
        &minCorpusCount=0\
        &minLength=5\
        &maxLength=15\
        &limit=1\
        &api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5"
   
    response = reqs.get(url).text
    
    # Jsonifying the reponse
    response_json = json.loads(response[1:len(response)-1])
    
    # Getting the random word
    random_word = response_json['word']
    secret_word = '_'*len(random_word)
    
    # Game
    for n_attempt in range(int(len(random_word) * 1.5)):
        if secret_word == random_word:
            print("You are a winner!")
            return
        
        print('-> The secret word:', secret_word)
        letter = input('Enter a letter: ')
        if letter in random_word:
            for i in [i.start() for i in re.finditer(letter, random_word)]:
                secret_word = secret_word[:i] + letter + secret_word[i+1:]
    
    print("Haha loser!")
    print('The secret word was: ' + random_word)
            
        
def main():
    mini_hangman_game()
    
    
if __name__ == '__main__':
    main()