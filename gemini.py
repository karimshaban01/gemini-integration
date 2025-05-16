import google.generativeai as genai

# Configure the API key
genai.configure(api_key="API_KEY")

# Instantiate the model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")  # Use available model name

# Generate content
response = model.generate_content("Explain how digital signature works.")

# Print the result
print(response.text)
