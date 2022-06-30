from flask import Flask, request
import time
import requests
app = Flask(__name__)
# http://localhost:port/numbers?url=http://something.com/primes&url=http://anything.com/fibo
# http://localhost:port/numbers?url=http://localhost:8090/primes&url=http://localhost:8090/fibo&url=http://localhost:8090/odd


@app.route('/numbers',methods = ['GET','POST'])
def numbers():
    args = request.args
    print(args,type(args))
    urls = args.getlist('url')
    print(urls)
    total_numbers = []
    for url in urls:
        resp = requests.get(url)
        if(resp.status_code==200):
            content = resp.json()
            # print(content,type(content))
            total_numbers.extend(content['numbers'])
        time.sleep(0.005)
    total_numbers = sorted(list(set(total_numbers)))
    return {"numbers:":total_numbers}

if __name__ == '__main__':
   app.run(debug=True)