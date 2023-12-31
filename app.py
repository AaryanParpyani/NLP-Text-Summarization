from flask import Flask, render_template,url_for
from flask import request as req
import requests


app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def Index():
    return render_template("index.html")

@app.route("/Summarize",methods=["GET","POST"])
def Summarize():
    if req.method=="POST":
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": "Bearer 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"}

        data=req.form["data"]

        
        maxL=int(req.form["maxL"])
        minL=maxL//4
        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
            
        output = query({
            "inputs": data,
            "parameters":{"min_length":minL,"max_length":maxL}, 
        })[0]
    
        return render_template("index.html",result=output["summary_text"])
    else:
        return render_template("index.html")
        
    
if __name__ == '__main__':
    app.debug=True
    app.run()
    
    
    
# API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
#     headers = {"Authorization": "Bearer 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"}

#     data='''The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.'''

#     minL=50
#     maxL=70
#     def query(payload):
#         response = requests.post(API_URL, headers=headers, json=payload)
#         return response.json()
        
#     output = query({
#         "inputs": data,
#         "parameters":{"min_length":minL,"max_length":maxL}, 
#     })
    
#     return render_template("index.html",result=output)