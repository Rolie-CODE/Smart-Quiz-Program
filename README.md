# Smart Quiz Program

## Project Overview

The Smart Quiz Program is a Python-based command-line application that leverages OpenAI’s language models to generate and evaluate multiple-choice quiz questions. The application is designed to support interactive learning, self-assessment, and revision of computer science concepts through dynamically generated questions and instant feedback.

This project demonstrates practical skills in Python programming, API integration, user input handling, and the application of artificial intelligence in educational software.

---

## Key Features

* Command-line interface for ease of use
* Quiz mode with selectable difficulty levels (easy, medium, hard)
* Slide-to-Quiz mode that generates questions from pasted lecture notes or slides
* Automatic answer evaluation with brief explanations
* Continuous quiz loop until the user chooses to exit

---

## Technologies Used

* Python 3
* OpenAI Python SDK (version 1 or later)
* OpenAI model: gpt-4o-mini

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/smart-quiz-program.git
cd smart-quiz-program
```

### 2. (Optional) Create and Activate a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```bash
pip install openai
```

### 4. Configure API Key

For security reasons, the OpenAI API key should not be hard-coded. Set it as an environment variable instead.

**Windows (PowerShell):**

```powershell
setx OPENAI_API_KEY "your_api_key_here"
```

**macOS/Linux:**

```bash
export OPENAI_API_KEY="your_api_key_here"
```

---

## How to Run the Program

```bash
python quiz.py
```

Follow the on-screen instructions to select a mode and begin answering questions.

---

## Usage Modes

### Quiz Mode

Users can select a difficulty level and answer AI-generated multiple-choice computer science questions. The program provides immediate feedback indicating whether the answer is correct or incorrect, along with a brief explanation.

### Set Questions From Slides

Users can paste lecture slides or study notes into the program. The application analyzes the content and generates relevant multiple-choice questions, making it useful for exam preparation and revision.

---

## Project Structure

```
smart-quiz-program/
│── quiz.py
│── README.md
│── .gitignore
```

---

## Learning Objectives

* Understanding API integration in Python applications
* Applying artificial intelligence to educational use cases
* Designing user-friendly command-line programs
* Managing project structure and documentation for version control

---

## Future Enhancements

* Score tracking and performance analytics
* Support for loading slide content from text files
* Question history management
* Web-based interface using a Python web framework

---

## Disclaimer

This project is intended for educational purposes. Users are responsible for securing their API keys and complying with OpenAI’s usage policies.

---

## Author

Rolie_Code
