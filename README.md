## Intucate Case Study
A Flask REST API that accepts user questions, gets an AI-generated response, and stores the request and response in MongoDB.

### What this project does
The project has two main APIs:
/ask - Accepts one question and returns an AI response.
/ask-multiple - Accepts multiple questions and processes them asynchronously.

The project also:
- Gets the prompt template from MongoDB.
- Sends the question to the OpenAI API.
- Stores the question and response in MongoDB.
- Validates the API input.
- Handles errors.

### Technologies Used
- Python
- Flask
- MongoDB
- PyMongo
- OpenAI API
- python-dotenv

### Steps to run
1. Clone the project
2. Open the project folder
3. Create a virtual environment:-
   python -m venv venv
4. Activate the virtual environment:-
   For Windows PowerShell:- .\venv\Scripts\Activate.ps1
5. Install required packages
   pip install -r requirements.txt
6. Create the .env file
7. Create a .env file in the project root and add:-
   MONGO_URI=your_mongodb_connection_string
   MONGO_DB_NAME=db name
   OPENAI_API_KEY=your_openai_api_key
   OPENAI_MODEL=gpt-4.1-mini
8. Run the application:-
   python run.py

