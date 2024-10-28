import os
import json

def read_quotes(file_path):
  with open(file_path, 'rb') as file:
    return json.load(file)

def get_intents():
  with open('intents.json', 'r') as file:
    return json.load(file)

# main function
if __name__ == '__main__':
  file_path = os.path.join('data', 'quotes.json')
  quotes = read_quotes(file_path)

  intents = get_intents()
  
  for quote_dict in quotes:
    quote = quote_dict['quote']
    movie = quote_dict['movie']
    
    print(quote, '\t', movie)