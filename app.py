from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the pre-trained model and CountVectorizer
clf = pickle.load(open("movie_review_classification.pkl", "rb"))
cv = pickle.load(open("count-vectoriser.pkl", "rb"))

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the review from the form
        review = request.form['review']
        # Transform the review using the CountVectorizer
        data = cv.transform([review]).toarray()
        # Predict the sentiment
        prediction = clf.predict(data)
        # Convert prediction to readable form
        result = "Positive" if prediction == 1 else "Negative"
        return render_template('index.html', prediction_text=f'The review is {result}')
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
