from sys import prefix
from flask import Flask, request
import time
import requests
app = Flask(__name__)

# http://localhost:port/prefixes?keywords=bonfire,bool

@app.route('/prefixes',methods = ['GET','POST'])
def numbers():
    hardcode_words = ["bonfire", "cardio", "case", "character", "bonsai"]
    args = request.args
    print(args,type(args))
    keywords = args.getlist('keywords')[0].split(",")
    print(keywords)
    total_keywords = []
    for key_word in keywords:
        if key_word in hardcode_words:
            key_w = key_word
            for i in range(1,len(key_w)+1):
                count = 0
                for hard_word in hardcode_words:
                    if(key_w[:i] in hard_word):
                        prefix = key_w[:i]
                        count+=1
                if(count==1):
                    prefix = key_w[:i]
                    break                
            total_keywords.append({
                "keyword":key_word,
                "status":"found",
                "prefix":prefix
            })
        else:
            total_keywords.append({
                "keyword":key_word,
                "status":"not_found",
                "prefix":"not_applicable"
            })

    return {"keywords:":total_keywords}

if __name__ == '__main__':
   app.run(debug=True)