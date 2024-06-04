#OpenAI settings
OPENAI_KEY = ""
OPENAI_MODEL = "gpt-4o"
OPENAI_REQUEST_TIMEOUT = 30
OPENAI_MAX_TOKENS = 1000

#MongoDB settings
MONGODB_CONNECTION_STRING = ""
MONGODB_MAX_POOL_SIZE = 5
DATABASE_NAME = "ai_assistant_builder"
COLLECTION_NAME = "data"
VECTOR_INDEX_NAME = "vector_index"
VECTOR_TEXT_EQUIVALENT_ATTR = "content"

#Chatbot system message
AI_LAWYER_ASSISTANT_SYSTEM_MESSAGE = """You are an AI Assistant lawyer bot of laws in Pakistan. You need to answer the users as an expert lawyer, you will be provided with some content to query asked by the user. If the content is not similar to the query asked then reply user 'I am not given enough data to answer your query'. Try to give answers by carefully looking into the content since LAWs is a critical topic and answer in simple words that a normal person can understand easily."""