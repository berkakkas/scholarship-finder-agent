from dotenv import load_dotenv
from graph import app_graph

load_dotenv()

query = input("Ask your scholarship question: ")

result = app_graph.invoke({
    "query": query
})

print("\n")
print(result["answer"])