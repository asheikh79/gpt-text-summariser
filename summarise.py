from openai import OpenAI

# Replace with your real API key
client = OpenAI(api_key="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")

# One-line input, no multi-line or Ctrl+Z needed
user_input = input("Paste your text and press Enter:\n")

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that summarises text."},
        {"role": "user", "content": user_input}
    ]
)

print("\n💡 Summary:\n")
print(response.choices[0].message.content)
