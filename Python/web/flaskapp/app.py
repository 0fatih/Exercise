from flask import Flask, request, render_template
import os


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/',methods=['POST'])
def ip_yazdir():
    try:
        ip = request.form['ip']
        os.system("nmap {} | grep '^[0-9]' > ip.txt".format(ip))
        portlar = ""
        f = open("ip.txt",'r')
        for line in f:
            portlar += '<p>'+line+"</p>"
        f.close()
        os.remove("ip.txt")
        return portlar
    except FileNotFoundError:
        return "Bir sorun olustu!"

if(__name__=="__main__"):
    app.run(debug=True)
    

