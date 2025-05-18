import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from crewai import LLM

# Load environment variables
load_dotenv(override=True)

OPEN_AI_KEY = os.getenv("OPEN_AI_KEY") 

#Initialize LLM
llm = LLM(
    model="openai/gpt-4o-mini", # call model by provider/model_name
    temperature=0.8,
    api_key=OPEN_AI_KEY,
 
    top_p=0.9,
    frequency_penalty=0.1,
    presence_penalty=0.1,
  
)


#Sample Input
user_input = {
    "topic": "Python programming",
    "skill_level": "beginner",
    "time_available": "2 weeks",
    "hours_per_day": 2,
    "learning_style": "hands-on with examples"
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
    Ensure the tone is positive and engaging.
    """,
    agent=motivator,
    expected_output="An enhanced learning plan with motivational messages and practical tips."
)

# Create and Run the Crew
crew = Crew(
    agents=[goal_assessor, curriculum_designer, motivator],
    tasks=[assess_task, design_task, motivate_task],
    verbose=True
)

# Run the Crew
result = crew.kickoff()

# Print the final output
print("\n=== Personalized Learning Plan ===")
print(result)