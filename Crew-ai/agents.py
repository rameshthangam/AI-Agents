from crewai import Agent
from tools import yt_tool
# from embedchain import App


from dotenv import load_dotenv

load_dotenv()
# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# openai.api_key = os.getenv('OPENAI_API_KEY')

# api_key = os.getenv("OPENAI_API_KEY")
# if not api_key:
#     raise EnvironmentError("OPENAI_API_KEY environment variable is not set!")
import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4o-mini"

print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))

# Initialize embedchain App
# app = App()

## Create an agent for a Blog content researcher

blog_researcher=Agent(
    role='Blog Researcher from Youtube Videos',
    goal='get the relevant video transcription for the topic {topic} from the provided Yt channel',
    verbose=True,
    memory=True,
    backstory=(
       "Expert in understanding videos in AI Data Science , MAchine Learning And GEN AI and providing suggestion" 
    ),
    llm='gpt-4o-mini',
    tools=[yt_tool],
    allow_delegation=True
)


## creating an agent for a senior blog writer agent with YT tool

blog_writer=Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT video',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    llm='gpt-4o-mini',
    tools=[yt_tool],
    allow_delegation=False


)