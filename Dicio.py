
import requests
import json

app_id = 'seu id aqui'
app_key = 'Sua chave aqui'
language = 'es'
word_id = 'rojo'
url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()
# url Normalized frequency
urlFR = 'https://od-api.oxforddictionaries.com:443/api/v1/stats/frequency/word/' + language + '/?corpus=nmc&lemma=' + word_id.lower()
r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
print("code {}\n".format(r.status_code))
print("text \n" + r.text)
print("json \n" + json.dumps(r.json()))
