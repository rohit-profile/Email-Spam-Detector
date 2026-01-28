from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('spam.pkl', 'rb'))
cv = pickle.load(open('vectorizer.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    if request.method == 'POST':
        msg = request.form['message']
        data = [msg]
        vec = cv.transform(data).toarray()
        prediction = model.predict(vec)

        if prediction[0] == 0:
            result = "This is NOT a Spam Email"
        else:
            result = "This is a SPAM Email"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
