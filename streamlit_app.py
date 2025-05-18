import os
import streamlit as st
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM

# Load environment variables
load_dotenv(override=True)
OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")

# Initialize the LLM
llm = LLM(
    model="openai/gpt-4o-mini",
    temperature=0.8,
    api_key=OPEN_AI_KEY,
    top_p=0.9,
    frequency_penalty=0.1,
    presence_penalty=0.1,
)

# Streamlit UI
st.title("📘 Personalized Learning Plan Generator")

with st.form("learning_plan_form"):
    topic = st.text_input("Learning Topic", value="Python programming")
    skill_level = st.selectbox("Skill Level", ["Beginner", "Intermediate", "Advanced"])
    time_available = st.text_input("Total Time Available (e.g., 2 weeks)", value="2 weeks")
    hours_per_day = st.slider("Hours Per Day", 1, 8, 2)
    learning_style = st.selectbox("Preferred Learning Style", [
        "hands-on with examples", "reading-focused", "project-based"
    ])
    
    submitted = st.form_submit_button("Generate Learning Plan")

if submitted:
    user_input = {
        "topic": topic,
        "skill_level": skill_level,
        "time_available": time_available,
        "hours_per_day": hours_per_day,
        "learning_style": learning_style
    }

    # Define Agents
    goal_assessor = Agent(
        role="Goal Assessor",
        goal="Interpret user input to extract learning objectives, skill level, and constraints.",
        backstory="A skilled analyst who understands user needs and translates them into clear objectives for learning.",
        llm=llm,
        verbose=True
    )

    curriculum_designer = Agent(
        role="Curriculum Designer",
        goal="Create a structured, day-by-day learning plan based on the user's goals and constraints.",
        backstory="An expert educator who designs engaging and effective learning paths tailored to individual needs.",
        llm=llm,
        verbose=True
    )

    motivator = Agent(
        role="Motivator",
        goal="Add encouraging messages and practical tips to enhance the learning experience.",
        backstory="A supportive coach who inspires learners to stay motivated and overcome challenges.",
        llm=llm,
        verbose=True
    )

    # Define Tasks
    assess_task = Task(
        description=f"""
        Analyze the following user input and extract key details:
        - Topic: {user_input['topic']}
        - Skill Level: {user_input['skill_level']}
        - Time Available: {user_input['time_available']}
        - Hours per Day: {user_input['hours_per_day']}
        - Learning Style: {user_input['learning_style']}
        Provide a clear summary of the user's learning objectives and constraints.
        """,
        agent=goal_assessor,
        expected_output="A concise summary of the user's learning goals, skill level, time constraints, and preferences."
    )

    design_task = Task(
        description="""
        Based on the Goal Assessor's summary, create a detailed, day-by-day learning plan for the user.
        Include:
        - Specific topics to cover each day.
        - Recommended resources (e.g., free online tutorials, videos, or exercises).
        - Time allocation for each activity.
        Ensure the plan aligns with the user's skill level, time constraints, and learning style.
        """,
        agent=curriculum_designer,
        expected_output="A structured day-by-day learning plan with topics, resources, and time allocations."
    )

    motivate_task = Task(
        description="""
        Review the Curriculum Designer's learning plan and add:
        - A motivational message to inspire the learner.
        - Practical tips for staying on track (e.g., study habits, time management).
        - Encouraging notes for each day of the plan.
        Ensure the tone is positive and engaging. Add Emojis for positivity
        """,
        agent=motivator,
        expected_output="An enhanced learning plan with motivational messages and practical tips."
    )

    # Run the Crew
    with st.spinner("Generating your personalized learning plan..."):
        crew = Crew(
            agents=[goal_assessor, curriculum_designer, motivator],
            tasks=[assess_task, design_task, motivate_task],
            verbose=True
        )
        result = crew.kickoff()

    # Display result
    st.subheader("📋 Your Personalized Learning Plan:")
    st.markdown(result)
