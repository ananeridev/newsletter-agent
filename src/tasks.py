from crewai import Task

def create_tasks(topic, researcher, writer, editor):
    research_task = Task(
        description=f"Research the latest news and trends about {topic}. "
                   "Identify 3-5 main stories.",
        agent=researcher
    )
    
    writing_task = Task(
        description="Create the newsletter content using the researched stories. "
                   "Include engaging headlines and concise descriptions.",
        agent=writer
    )
    
    editing_task = Task(
        description="Review the content, fix errors and improve formatting. "
                   "Ensure consistent and professional tone.",
        agent=editor
    )
    
    return [research_task, writing_task, editing_task]