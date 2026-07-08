from typing import TypedDict, Annotated, Optional, Literal
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()


class Review(TypedDict):
    key_theme: Annotated[list[str], "The main theme of the review"]
    sentiment: Annotated[Literal["positive", "negative"], "The sentiment of the review"]
    summary: Annotated[str, "A brief summary of the review"]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
    reviewer_name: Annotated[
        Optional[str],
        "The human reviewer's name only. Never return a product, brand, company, or model name. Return None if no reviewer name is present.",
    ]


model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    thinking_level="minimal",
    temperature=0,
    max_output_tokens=300,
)

structured_response = model.with_structured_output(Review)

review_text = """I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by AtaurRehman
"""

response = structured_response.invoke(review_text)

result = """ Name : {} \n Key Feature : {} \n Summary : {} \n Pros : {} \n Cons : {} \n Sentiment : {} \n """
result = result.format(response['reviewer_name'], response['key_theme'], response['summary'], response['pros'], response['cons'], response['sentiment'])

print(result)

