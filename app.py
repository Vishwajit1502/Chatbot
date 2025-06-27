from flask import Flask, render_template, request, jsonify
import cohere
import sys

app = Flask(__name__)

co = cohere.Client("yRjaFtWUyipJPCtlprmK0aSBSzxzwqxabj4eBPXy")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    try:
        response = co.chat(message=user_input)
        return jsonify({'reply': response.text})
    except Exception as e:
        return jsonify({'reply': f"Error: {str(e)}"})

if __name__ == '_main_':
    app.run(debug=True)

# Added for compatibility with the command "C:/Users/LENOVO/AppData/Local/Programs/Python/Python312/python.exe app.py"
if __name__ == "__main__":
    app.run()