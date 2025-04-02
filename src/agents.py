from crewai import Agent
from langchain.tools import DuckDuckGoSearchRun
from langchain.llms import OpenAI

class NewsletterCrew:
    def __init__(self):
        self.llm = OpenAI(temperature=0.7)
        self.search_tool = DuckDuckGoSearchRun()
        
    def create_agents(self):
        researcher = Agent(
            role='Content Researcher',
            goal='Find the most relevant news and trends in the industry',
            backstory='Expert in research and content curation',
            tools=[self.search_tool],
            llm=self.llm
        )
        
        writer = Agent(
            role='Writer',
            goal='Create engaging and informative content for the newsletter',
            backstory='Experienced writer specialized in creating compelling content',
            llm=self.llm
        )
        
        editor = Agent(
            role='Editor',
            goal='Review and refine the final newsletter content',
            backstory='Editor with years of experience in digital publications',
            llm=self.llm
        )
        
        return researcher, writer, editor