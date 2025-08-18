#%%
from pydantic import BaseModel, Field
from langchain_core.messages import SystemMessage
from langchain_core.tools import tool
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from typing import Literal
from langchain_aws import ChatBedrock
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper

#%%
# Define our Pydantic model for the movie review
class MovieReview(BaseModel):
    movie_name: str = Field(description="The name of the movie being reviewed")
    review_sentiment: Literal["positive", "negative"]  = Field(description="The sentiment of the review, either positive or negative")
    lead_actor_name: str = Field(description="The name of the leading actor in the movie")
    director_name: str = Field(description="The name of the director of the movie")
    
#%%
# Create Wikipedia tool
@tool
def wikipedia_tool(query: str) -> str:
    """
    Search Wikipedia for information about movies, actors, and directors.
    Use this when you need to find details not mentioned in the review.
    """
    wikipedia = WikipediaAPIWrapper(top_k_results=2)
    return wikipedia.run(query)
#%%
# Define the system prompt for the agent
prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a movie review analyzer that extracts structured information from reviews.
    Your goal is to create a complete MovieReview object with the following fields:
    - movie_name: Extract this from the review
    - review_sentiment: Determine if the sentiment is "positive" or "negative"
    - lead_actor_name: Find the lead actor using the wikipedia_tool if not mentioned in the review
    - director_name: Find the director using the wikipedia_tool if not mentioned in the review
    
    Always search for the movie first to get accurate information."""),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])

# Define the tools list
tools = [wikipedia_tool]

# Initialize the model and bind tools to it
model_id = "anthropic.claude-3-haiku-20240307-v1:0"
model = ChatBedrock(model_id=model_id).bind_tools(tools)

# Create the tool-calling agent
agent = create_tool_calling_agent(model, tools, prompt)

# Create the agent executor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Function to process a review and return structured data
def parse_movie_review(review_text):
    # Process through the agent to gather all necessary information
    result = agent_executor.invoke({
        "input": f"Extract structured information from this movie review: {review_text}"
    })
    
    # Convert the result to our structured Pydantic model
    structured_model = ChatBedrock(model=model_id).with_structured_output(MovieReview)
    # structured_model = model.with_structured_output(MovieReview)
    
    # Use the model to finalize the structured output
    prompt = f"""Based on the movie review and research, create a MovieReview object with these fields:
    - movie_name: The name of the movie
    - review_sentiment: Either "positive" or "negative"
    - lead_actor_name: The lead actor in the movie
    - director_name: The director of the movie

    Here's what we know so far: {result["output"]}
    """

    final_result = structured_model.invoke(prompt)
    
    return final_result
#%%
if __name__ == "__main__":
    review_text = '"The Mask of Zorro" is a thrilling and charismatic title that instantly evokes a sense of mystery, heroism, and adventure. It perfectly captures the essence of a legendary swashbuckling hero, promising an exciting and unforgettable cinematic experience.'
    
    # Process the review
    parsed_review = parse_movie_review(review_text)
    print(parsed_review)
# %%
