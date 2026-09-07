## Intucate Case Study
A Flask REST API that accepts user questions, gets an AI-generated response, and stores the request and response in MongoDB.

# What this project does
The project has two main APIs:
/ask - Accepts one question and returns an AI response.
/ask-multiple - Accepts multiple questions and processes them asynchronously.

The project also:
- Gets the prompt template from MongoDB.
- Sends the question to the OpenAI API.
- Stores the question and response in MongoDB.
- Validates the API input.
- Handles errors.

# Technologies Used
- Python
- Flask
- MongoDB
- PyMongo
- OpenAI API
- python-dotenv

