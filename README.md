# AI Assist - Code Generation & PR Automation

## 📌 Project Description

AI Assist is a tool that automates the development workflow.

It takes a task (like a Jira ticket), generates code using AI, applies changes to a repository, and automatically creates a Pull Request.


## 🚀 Features

- Generate code using Groq AI
- Automatically clone GitHub repository
- Create new branch
- Apply code changes
- Commit and push changes
- Automatically create Pull Request

## 🛠 Tech Stack

- Python
- Groq API (AI)
- Git & GitHub
- Requests library
- vscode

## 📂 Project Structure

ai_automation/
│
├── main.py
├── config.py
├── code_generator.py
├── file_handler.py
├── git_handler.py
├── pr_creator.py
├── utils.py
├── .env

## ⚙️ Setup Instructions

1. Clone the repository
2. Create virtual environment
   python -m venv venv

3. Activate environment
   venv\Scripts\activate

4. Install dependencies
   pip install groq requests python-dotenv

## 🔐 Environment Variables

Create a `.env` file and add:

GROQ_API_KEY=your_groq_api_key
GITHUB_TOKEN=your_github_token
REPO_OWNER=your_username
REPO_NAME=genai-se-2026

## ▶️ How to Run

Run the project:

python main.py

Enter task example:
Add validation to ensure input is not null or empty


## 🔄 Workflow

1. User enters task
2. Groq AI generates code
3. Repository is cloned
4. New branch is created
5. Code is added to file
6. Changes are committed and pushed
7. Pull Request is created automatically


## 📌 Example

Input:
Add validation logic

Output:
- Code added to sample.txt
- Branch created
- Pull Request created in GitHub


## ✅ Conclusion

This project demonstrates how AI can automate development tasks like code generation and PR creation, reducing manual effort.


