
import numpy as np
import joblib
import json
import random
from tensorflow.keras.models import load_model

# Load trained files
model = load_model("chat_model.keras")
vector = joblib.load("vector.pkl")
classes = joblib.load("classes.pkl")

# Load responses
with open("data.json", "r") as file:
    data = json.load(file)

def chatbot_response(user_input):

    user_vector = vector.transform([user_input.lower()]).toarray()

    prediction = model.predict(user_vector, verbose=0)

    index = np.argmax(prediction)
    confidence = prediction[0][index]

    if confidence < 0.50:
        return "Sorry, mujhe samajh nahi aaya."

    tag = classes[index]

    for intent in data["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])

# Chat loop
if __name__ == "__main__":

    print("Chatbot Started!")
    print("Type exit to stop chatbot.")

    while True:
        message = input("You: ")

        if message.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        reply = chatbot_response(message)
        print("Chatbot:", reply)
