import google.generativeai as genai

genai.configure(api_key="AIzaSyBsiTD_8tqIeGIXUE8G4BVIvjoJxenzG38")

model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content("Explain how AI works in a few words")

print(response.text)
