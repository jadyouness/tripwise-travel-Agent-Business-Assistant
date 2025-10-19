
📁 Project: TripWise Travel Agent – Business Domain Chatbot

This project implements a travel planning chatbot that collects user travel preferences, checks the weather for the selected destination, saves customer data, and stores unanswered questions for future improvements. It only answers questions related to the business domain (travel planning) and ignores unrelated ones.

📂 Folder Structure:

younes-travel_agent/
├─ about business/
│   ├─ about_business.pdf – Full business overview
│   └─ business_summary.txt – Short summary of the business idea
├─ .env – Environment variables (API keys)
├─ customer_leads.json – Stores user travel preferences
├─ unanswered_questions.json – Stores user questions the agent couldn’t answer
├─ tools.py – Contains all tool functions (weather API, saving leads, saving unanswered questions)
├─ younes travel_agent.ipynb – Main Jupyter notebook implementing the chatbot
└─ demo_video.mp4 – Demo video showing the app usage (optional)

🔑 .env Setup:

Create a `.env` file in the root folder with the following content, replacing with your actual API keys:

OPENWEATHER_API_KEY=your_openweather_api_key
GEMINI_API_KEY=your_gemini_api_key

- OPENWEATHER_API_KEY – Used to fetch weather forecasts.
- GEMINI_API_KEY – Required if using Gemini LLM for question answering or tool calling.

🛠️ Tools (tools.py):

- Weather API: Fetches a 5-day weather forecast for the travel destination.
- Save Customer Leads: Stores user travel preferences (name, age, destination, budget, etc.) in `customer_leads.json`.
- Save Unanswered Questions: Stores non-business or unanswerable questions in `unanswered_questions.json` for later review.

📂 PDF to Text Feature:

The project includes functionality to read and convert PDF files (e.g., `about_business.pdf`) into text using PyPDF2. This is useful for extracting business information to show or process within the chatbot.

📚 Libraries Used:

- requests – For making API calls
- python-dotenv – For loading environment variables
- gradio – For building the web app interface
- json – For storing leads and unanswered questions
- os – For file and environment handling
- datetime – For date operations
- PyPDF2 – For reading and converting PDF files to text

Install them with:
pip install requests python-dotenv gradio PyPDF2

▶️ How to Run:

1. Place your `.env` file in the root directory and use all the folder that i have iploaded to git hub.
2. Open `younes travel_agent.ipynb` in Jupyter or Google Colab.
3. Run all cells.
4. Enter user info (name, destination, budget, etc.) when prompted.
5. The chatbot will call the weather API to provide destination forecasts.
6. Customer information will be saved to `customer_leads.json`.
7. Any unrelated or unanswered questions will be saved to `unanswered_questions.json`.
8. You can also use the built-in PDF-to-text functionality to read `about_business.pdf`.

🌐 Web App:

A Gradio interface is included. After running the notebook, you’ll get a local or public URL to interact with the chatbot.

Example:
http://127.0.0.1:7860
or
https://<ngrok-id>.gradio.live

📹 Demo Video:

A demo video (`demo_video.mp4`) is included showing how the chatbot works from start to finish.

✅ Features:

- Collects and stores user travel info
- Fetches real-time weather data
- Restricts responses to travel business domain
- Saves unanswered questions for later analysis
- Converts PDFs to text for internal use
- Provides a Gradio web interface
- Demo video provided
