import random
class LLM:
     def __init__(self):
        print("Created LLM")
     def invoke(self , prompt):
          response_list =[
            'Islamabad is the capital of India',
            'PSL is a cricket league',
            'AI stands for Artificial Intelligence'
               ]
          return {"response" : random.choice(response_list) }

model = LLM()
respones = model.invoke("how are you ? ")
print(respones['response'])

class NakliPromptTemplate:

  def __init__(self, template, input_variables):
    self.template = template
    self.input_variables = input_variables

  def format(self, input_dict):
    return self.template.format(**input_dict)

template = NakliPromptTemplate(
    template='Write a {length} poem about {topic}',
    input_variables=['length', 'topic']
)
prompt = template.format({'length':'short','topic':'india'})


class NakliLLMChain:
  def __init__(self, llm, prompt):
    self.llm = llm
    self.prompt = prompt

  def run(self, input_dict):
    final_prompt = self.prompt.format(input_dict)
    result = self.llm.invoke(final_prompt)
    return result['response']

template = NakliPromptTemplate(
    template='Write a {length} poem about {topic}',
    input_variables=['length', 'topic']
)

llm = LLM()
chain = NakliLLMChain(llm, template)

chain.run({'length':'short', 'topic': 'pakistan'})


