from assets.datathon_api import get_embedding

# Define your API key here 
API_KEY = "U3Zd9yQZZr6IFRy1kodQx6BYCQOHvcXo83nOkPrA"
TEXT = "Hey there, I am batman"

# Call the get_embedding function located in ./assets
embedding = get_embedding(TEXT, API_KEY)

# Print stuff out and be prepared for a ton of numbers
print(embedding)

