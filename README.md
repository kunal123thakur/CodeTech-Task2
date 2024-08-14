Here’s a README file template for your movie sentiment analysis project, similar to the one you provided:

---

# Movie Sentiment Analysis

## Internship Details

- **Name**: Kunal Thakur
- **Company**: CODETECH IT SOLUTIONS
- **ID**: CT4ML5498
- **Domain**: Machine Learning
- **Duration**: July 20, 2024 - August 20, 2024
- **Mentor**: Muzammil Ahmed
![Screenshot 2024-08-15 032343](https://github.com/user-attachments/assets/1de0ce72-6065-4e9d-817b-fbe159ad5950)

## Overview

This project involves analyzing movie reviews to predict their sentiment (positive or negative). The analysis uses the IMDb dataset to train a Naive Bayes model that can classify the sentiment of a given movie review.

## Dataset

The dataset consists of a single CSV file:

1. **IMDb Dataset**: `IMDB Dataset.csv`

### IMDb Dataset

- **review**: The text of the movie review.
- **sentiment**: The sentiment of the review (`positive` or `negative`).

## Requirements

- Python 3.x
- pandas
- numpy
- scikit-learn
- nltk
- Flask

You can install the required packages using pip:

```bash
pip install pandas numpy scikit-learn nltk Flask
```

## Project Structure

- **app.py**: The main Flask application file that handles the web interface and model prediction.
- **templates/**
  - **index.html**: The HTML template for the web interface.
- **count-vectoriser.pkl**: The saved CountVectorizer model used for text vectorization.
- **movie_review_classification.pkl**: The saved Naive Bayes model used for sentiment classification.
- **IMDB Dataset.csv**: The dataset used for training and testing the model.

## How to Run the Project

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate   # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application**:
   ```bash
   python app.py
   ```

5. **Open the web interface**:
   Navigate to `http://127.0.0.1:5000/` in your web browser.

## Usage

- Enter a movie review in the provided text box on the web page.
- Click the "Review" button to predict whether the review is positive or negative.

## Model Training

The model is trained using the following steps:

1. **Data Preprocessing**:
   - Removal of non-alphabetical characters.
   - Conversion to lowercase.
   - Stemming of words.

2. **Feature Extraction**:
   - Use of `CountVectorizer` to convert text data into numerical features.

3. **Model Training**:
   - Training a Naive Bayes classifier using the preprocessed data.

4. **Model Evaluation**:
   - The model's accuracy is evaluated on a test dataset.

## Results

The trained Naive Bayes model achieved an accuracy of 82.45% on the test set, demonstrating its ability to effectively classify the sentiment of movie reviews.

---

This README provides a comprehensive overview of your movie sentiment analysis project, including how to set it up and use it.
