from langchain_text_splitters import CharacterTextSplitter

raw_text = """
FastAPI is a modern, fast (high-performance) web framework for building APIs with Python.
It is based on standard Python type hints.

System design requires understanding load balancers, database scaling, and caching strategies.
DevSecOps integrates security directly into the continuous integration and delivery pipeline.
"""

text_splitting = CharacterTextSplitter(
      chunk_size=50,
      chunk_overlap=10,
      separator=''
     )

chunks = text_splitting.split_text(raw_text)

for i , chunk in enumerate(chunks):
     print(f"----- Chunk{i+1}------")
     print(chunk)
