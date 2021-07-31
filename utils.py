import requests
import json

def remove_tag(username):
    chars = []
    for char in username:
        if char == '#':
            break
        chars.append(char)
    return "".join(chars)

def get_quote():
    response = requests.get("http://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -James Charles"
    return(quote)

def get_chisme():
    chisme = requests.get('https://jasonpersonaldomain.com/chismosabot/random')
    json_data = json.loads(chisme.text)
    quote = json_data['quote']['quote']
    return quote