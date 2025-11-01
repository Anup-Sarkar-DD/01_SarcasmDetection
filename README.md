<h1>Sarcasm Detection Using Deep Learning</h1>

<h2>Overview</h2>
<p>This project builds a deep learning model to detect sarcasm in news headlines using a Bidirectional LSTM architecture. The goal is to classify headlines as sarcastic or not, providing valuable insight for sentiment analysis and content monitoring.</p>

<h2>Features</h2>
<ul>
  <li>Preprocessing pipeline including data cleaning, lemmatization, and tokenization.</li>
  <li>Training on a large, validated sarcasm dataset with stratified train/validation/test splits.</li>
  <li>Bidirectional LSTM model architecture for capturing contextual relationships.</li>
  <li>Interactive Gradio-based web app for live sarcasm prediction.</li>
  <li>Model evaluation with precision, recall, F1-score on test set.</li>
</ul>

<h2>The Challenge</h2>
<p>Sarcasm is inherently subtle and context-dependent, making it difficult for traditional sentiment analysis models to detect. Headlines are short and often use wordplay or cultural references that require nuanced understanding.</p>

<h2>The Solution</h2>
<p>We addressed this by:</p>
<ul>
  <li>Using a high-quality sarcasm-labeled news headlines dataset.</li>
  <li>Implementing careful preprocessing including lemmatization and tokenization.</li>
  <li>Building a deep learning model with Bidirectional LSTM layers to capture context from both ends of the text.</li>
  <li>Deploying the model in a user-friendly Gradio app hosted on Hugging Face Spaces for easy interactive testing.</li>
</ul>

<h2>Tech Stack Used</h2>
<ul>
  <li>Python 3</li>
  <li>TensorFlow 2 (Keras)</li>
  <li>NLTK for text preprocessing</li>
  <li>Scikit-learn for train/test split and evaluation metrics</li>
  <li>Gradio for app deployment</li>
  <li>Hugging Face Spaces for hosting the live demo</li>
</ul>
