from google import genai

# Your API key
client = genai.Client(api_key="AIzaSyCkV7h5kpmogV_tTCe7D-a6L3uwwEXffI4")

# Make it a Chess Coach
system_prompt = "You are an expert chess coach with 30 years of experience. Answer all questions related to chess in a simple, encouraging and clear way."

# Start chatting
print("♟️ Welcome to Chess Coach AI!")
print("Ask me anything about chess. Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "quit":
        print("Good luck with your chess! Keep learning! ♟️")
        break
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=system_prompt + "\n\nUser question: " + user_input
    )
    print(f"\nChess Coach: {response.text}\n")