import urllib.request as url 
import json
#calea catre fisierul text: 
#cale = "https://example-files.online-convert.com/document/txt/example.txt" 

postObject = {"questionText": "In Python, which of the following is used to declare a variable?",
    "answers": [
      {
        "answerText": "let",
        "correct": False
      },
      {
        "answerText": "var",
        "correct": False
      },
      {
        "answerText": "def",
        "correct": False
      },
      {
        "answerText": "No keyword is needed",
        "correct": True
      }
    ]}

with url.urlopen(url.Request(url="http://localhost:5020/api/Questions",method="POST", data= json.dumps(postObject).encode('utf-8'), headers={"Content-Type": "application/json"})) as f:
    #citim ce exista in fisierul text 
    text = f.read() 

print(text) 