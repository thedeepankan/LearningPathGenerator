# 📘 Personalized Learning Plan Generator

This application leverages [CrewAI](https://github.com/joaomdmoura/crewAI) and OpenAI’s GPT-4o-mini model to generate a **customized learning plan** based on your goals, time, and preferences. The plan is created collaboratively by AI agents acting as a curriculum designer, a motivator, and a goal assessor. The front end is powered by **Streamlit**, providing an intuitive interface for users to interact with the app.

---

## 🚀 Features

✅ User-friendly Streamlit interface  
✅ Multiple AI agents with distinct roles:  
- 🎯 **Goal Assessor** – Understands your objective and learning context  
- 📚 **Curriculum Designer** – Crafts a structured, day-by-day learning plan  
- 💬 **Motivator** – Adds tips, encouragement, and daily motivation  

✅ Personalized inputs:
- Topic
- Skill level (Beginner, Intermediate, Advanced)
- Time available
- Hours per day
- Learning style (e.g., hands-on, reading, project-based)

✅ Daily breakdown of learning with resources  
✅ Motivational support and productivity tips

---

## 🧠 Tech Stack

- Python
- Streamlit
- [CrewAI](https://github.com/joaomdmoura/crewAI)
- [OpenAI GPT-4o-mini](https://platform.openai.com/docs/models/gpt-4o-mini)

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/thedeepankan/LearningPathGenerator.git
cd LearningPathGenerator
```
### 2. Set Up a Virtual Environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate      # On Linux/Mac
venv\Scripts\activate         # On Windows
```

### 3. Set Up a Virtual Environment (optional but recommended)
```bash
pip install -r requirements.txt
```
### 4. Create a .env File
```ini
OPEN_AI_KEY=your_openai_api_key_here
```
### 5. Run the Streamlit App
```bash
streamlit run streamlit_app.py
```



