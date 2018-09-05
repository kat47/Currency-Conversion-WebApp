from flask import Flask, render_template, request
import requests,json
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form["USD"]
      result = float(result)
      val = convert(result)
      return render_template("result.html",res1 = val,res2=result)


def convert(conv):
    data = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=INR&apikey=OCR3ZZ8N6Y54V2ZY')
    #print(type(data.content))
    val = json.loads(data.content)
    #print(type(val))
    from_cur = val['Realtime Currency Exchange Rate']['1. From_Currency Code']
    to_cur = val['Realtime Currency Exchange Rate']['3. To_Currency Code']
    rate = float(val['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    final = conv*rate
    conv = format(conv,'.2f')
    final = format(final,'.2f')
    #res = {conv,final}
    return final
    #print(f"{conv} {from_cur} = {final} {to_cur}")

if __name__ == '__main__':
   app.run(host='127.0.0.1',port=8080, debug=True)
