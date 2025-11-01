import gradio as gr
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json
import json

# Constants (must match training)
max_len = 25

# Load saved model and tokenizer
model = tf.keras.models.load_model("sarcasm_model.keras")

with open("tokenizer.json") as f:
    tokenizer_data = f.read()
tokenizer = tokenizer_from_json(tokenizer_data)

def predict_sarcasm(text):
    # Preprocess input text using the saved tokenizer
    sequences = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(sequences, maxlen=max_len, padding='post', truncating='post')
    pred = model.predict(padded)[0][0]
    
    # Interpretation of sarcasm probability
    if pred > 0.8:
        label = "Highly Sarcastic"
    elif pred > 0.6:
        label = "Moderately Sarcastic"
    elif pred > 0.4:
        label = "Neutral"
    elif pred > 0.2:
        label = "Mildly Sarcastic"
    else:
        label = "Not Sarcastic"
    
    return f"Sarcasm Probability: {pred:.2f}", label

iface = gr.Interface(
    fn=predict_sarcasm,
    inputs=gr.Textbox(lines=2, placeholder="Enter headline here..."),
    outputs=[gr.Textbox(label="Probability"), gr.Textbox(label="Interpretation")],
    title="Sarcasm Detection",
    description="Enter a headline to check if it is sarcastic."
)

if __name__ == "__main__":
    iface.launch()
