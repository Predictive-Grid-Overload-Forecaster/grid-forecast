from langchain_core.output_parsers import PydanticOutputParser , StrOutputParser
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from pydantic import Field , BaseModel
from datetime import datetime
from typing import Optional , Literal , List
from langchain_google_genai import ChatGoogleGenerativeAI
from os import getenv
from langchain.schema.runnable import RunnableSequence

load_dotenv()
class Current(BaseModel):
    Current_Temperature: str = Field(description="The current temperature of the zone input by the user, in degrees.")
    Feels_like: str = Field(description="What the current temperature feels like, in degrees")
    Condition: str = Field(description="What the current weather condition is", examples=["windy","light rain", "heavy rain","sunny","clear","thunderstorm","foggy","hail storm"])
    Wind_Speed: float = Field(description="The current wind speed")

class Forecast(BaseModel):
    Time: datetime = Field(description="The date and time of the forecast")
    Forecast_Temperature: str = Field(description="Forecast temperature at the time of user input")
    Condition: str = Field(description="What the current weather condition is", examples=["windy","light rain", "heavy rain","sunny","clear","thunderstorm","foggy","hail storm"])
    
    
class Work(BaseModel):
    current_details: Current = Field(description="Current weather condition")
    forecast_details: List[Forecast] = Field(description="Forecasted weather conditions")
    
structify = PydanticOutputParser(pydantic_object = Work)

prompt = PromptTemplate(
    template = "From the {user_input}, follow the \n {format_instruction}",
    input_variables = ['user_input'],
    partial_variables={'format_instruction':structify.get_format_instructions()},
    validate_template = True
)


# Model
model = ChatGoogleGenerativeAI(model="gemini-2.5-pro")


chain = prompt | model | structify

result = chain.invoke({"user_input":"Current Temperature and Forecast of West Delhi"})

print(result)
