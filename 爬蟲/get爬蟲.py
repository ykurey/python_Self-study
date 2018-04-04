
import requests;


res = requests.get("http://www.pu.edu.tw/");

res.encoding= 'big5'

print(res.text);

