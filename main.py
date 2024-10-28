import os
import json

def read_quotes(file_path):
  with open(file_path, 'r') as file:
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
    index = quote_dict['index']
    quote = quote_dict['quote']
    movie = quote_dict['movie']
    year  = quote_dict['year']

    print(f'{index}\t{quote}\t{movie}\t{year}')