import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Downloading NLTK resources
nltk.download('punkt')

# --- Knowledge Base (FAQs) ---
faq = {
    "Hello": "Hello! 👋 How can I help you today?",
    "What are your working hours?": "We’re open Monday to Friday, 9 AM to 6 PM.",
    "How can I get a refund?": "Our refund policy allows returns within 30 days of purchase.",
    "How do I track my order?": "You can track your order at: www.SD_logistics.com/track",
    "Do you offer international shipping?": "Yes, we ship worldwide with additional charges.",
    "Can I change my delivery address?": "Yes, you can update your delivery address before your order is dispatched.",
    "What payment methods do you accept?": "We accept credit/debit cards, UPI, PayPal, and net banking.",
    "Do you have Cash on Delivery (COD)?": "Yes, COD is available in selected regions.",
    "How long does delivery take?": "Standard delivery takes 3–5 business days. International shipping may take 7–14 days.",
    "Can I cancel my order?": "Yes, you can cancel your order within 24 hours of placing it.",
    "Do you provide customer support on weekends?": "Our support team is available Monday to Saturday. For urgent queries, email us at support@sd_logistics.com.",
    "How do I contact customer support?": "You can call us at +91-9876543210 or email support@sd_logistics.com.",
    "Do you offer discounts or promotions?": "Yes, we frequently run special offers. Subscribe to our newsletter to stay updated.",
    "Is my personal information secure?": "Absolutely! We use end-to-end encryption and do not share your information with third parties.",
    "Do you offer gift wrapping?": "Yes, we offer gift wrapping for an additional charge.",
    "Where are you located?": "Our headquarters are in Bangalore, India, and we have warehouses across major cities."
}

# --- Preprocess ---
questions = list(faq.keys())
answers = list(faq.values())

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

def chatbot_response(user_input):
    # Clean input
    user_input = user_input.lower().translate(str.maketrans('', '', string.punctuation))
    
    # Vectorize user query
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X)
    idx = similarity.argmax()
    
    # Threshold check
    if similarity.max() > 0.3:
        return answers[idx]
    else:
        return "🤔 I’m not sure about that. Let me connect you to a support agent."

# --- Chat Loop ---
print("🤖 Customer Service Bot: Hello! Type 'bye' to exit.")
while True:
    user = input("You: ")
    if user.lower() == "bye":
        print("Bot: Goodbye! 👋 Have a great day!")
        break
    print("Bot:", chatbot_response(user))