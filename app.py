from knowledge_base import VectorDatabase

# Sample enterprise knowledge
documents = [
    "Diligent helps organizations manage governance, risk, and compliance.",
    "Board members need quick insights instead of long reports.",
    "AI summaries reduce time spent reading compliance documents.",
    "Anomaly detection helps identify unusual risk patterns."
]

db = VectorDatabase(documents)

def local_llm_response(query, context):
    return f"Based on what I know: {context}"

def chatbot():
    print("🤖 Jarvis AI Assistant (type 'exit' to quit)")
    while True:
        query = input("You: ")
        if query.lower() == "exit":
            break

        context = db.search(query)[0]
        response = local_llm_response(query, context)
        print("Jarvis:", response)

if __name__ == "__main__":
    chatbot()
