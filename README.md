<div style="text-align: center; margin-bottom: 20px;">
  <h1>Sarcasm Detection (Deep Learning)</h1>
</div>

- Built a deep learning model to classify text as sarcastic or non-sarcastic using TensorFlow and Keras with embedding and dense layers.
- Prepared the dataset by:
  - Importing a real-world sarcasm dataset (news headlines and social media posts, with sarcasm labels).
  - Cleaning and normalizing text: lowercasing, stripping punctuation, removing extra whitespace.
  - Tokenizing and padding sequences for uniform model input.
- Split the data:
  - Used a standard train-test split to evaluate prediction performance on unseen data.
- Built and trained the model:
  - Used Keras Sequential API with Embedding, GlobalAveragePooling, and Dense layers.
  - Tuned hyperparameters to improve learning and avoid overfitting.
- Evaluated model performance with key metrics:
  - Accuracy: Monitored train and validation accuracy during epochs.
  - Visualized learning curves (accuracy and loss) to diagnose overfitting/underfitting.
- Enabled sarcasm prediction:
  - Developed inference function to predict sarcasm probability of new sentences.
- Example results:
  - Model correctly classified both obvious and subtle sarcastic statements.
  - Demonstrated strong practical use for content moderation and automated sentiment tasks.
