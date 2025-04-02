from crewai import Crew
from .agents import NewsletterCrew
from .tasks import create_tasks

def generate_newsletter(topic):
    newsletter_crew = NewsletterCrew()
    researcher, writer, editor = newsletter_crew.create_agents()
    
    tasks = create_tasks(topic, researcher, writer, editor)
    
    crew = Crew(
        agents=[researcher, writer, editor],
        tasks=tasks,
        verbose=True
    )
    
    result = crew.kickoff()
    
    return result

if __name__ == "__main__":
    topic = "Artificial Intelligence"
    newsletter = generate_newsletter(topic)
    print(newsletter)