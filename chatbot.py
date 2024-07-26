import nltk # type: ignore
nltk.download('punkt')
from nltk.chat.util import Chat, reflections

# Define some reflections (for transforming user input)
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

# Define some pattern-response pairs for the chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"what is your name?",
        ["My name is ChatBot and I'm here to help you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright","No problem",]
    ],
    [
        r"(.*) (good|great|fine)",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon :) ","It was nice talking to you. Goodbye!"]
    ],
]

# Create a Chatbot
def chatbot():
    print("Hi, I'm ChatBot. How can I help you today?")

    chat = Chat(pairs, reflections)
    chat.converse()

if _name_ == "_main_":
    nltk.download('punkt')  # Ensure the NLTK tokenizer is downloaded
    chatbot()