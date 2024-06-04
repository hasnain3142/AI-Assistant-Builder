from fastapi import APIRouter
from utils.Database import DatabaseConnector
from utils.StreamingResponseByOpenAI import ask_question
from utils.DataModels import QueryRequestModel
import GlobalConstants
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_openai import OpenAIEmbeddings
from fastapi.responses import StreamingResponse
from thefuzz import fuzz

chatGreetings = ["Hi", "Hello", "Hey", "Good morning", "Good afternoon", "What's up?", "Howdy", "Hi there", "Hello there", "Hey there", "Greetings", "Salutations", "Hiya", "How are you?", "Good evening", "Yo", "Heya", "What's happening?", "Hello again", "Hey, what's going on?"]
thanksMessages = ["Thanks", "Thank", "Cheers", "👍", "That helped", "That helped 👍", "Thank you", "Thanks a lot", "Thank you so much", "Thanks!", "Thank you!", "Much appreciated", "I appreciate it", "Thanks a bunch", "Thanks a million", "Many thanks", "Thanks so much", "Thank you very much", "Thank you kindly", "Gracias", "Ty", "Ta", "Thanks a ton", "Thank you, sir", "Thank you for your help", "Appeciate it", "Cheers mate", "Thx", "tyty", "thnx"]

def is_match(query, messages, threshold=75):
    return any(fuzz.ratio(query, message.lower()) >= threshold for message in messages)

router = APIRouter()

@router.post("/")
async def query(request_body: QueryRequestModel):
    post_request_JSON_body = request_body.model_dump()
    chatbot_name = post_request_JSON_body['chatbot_name']
    pre_filter = post_request_JSON_body['pre_filter']
    query = post_request_JSON_body['query']
    print(is_match(query, chatGreetings))
    if is_match(query, chatGreetings):
        return ({"answer": "Hey there, how can I help you today?"}), 200

    if is_match(query, thanksMessages):
        return ({"answer": "You're welcome! I'm here if you need help with anything else."}), 200

    db = DatabaseConnector().getDatabase(GlobalConstants.DATABASE_NAME)
    collection = db[GlobalConstants.COLLECTION_NAME]
    embedding_model  = OpenAIEmbeddings(api_key=GlobalConstants.OPENAI_KEY)
    vector_search = MongoDBAtlasVectorSearch(
        collection,
        embedding_model,
        index_name=GlobalConstants.VECTOR_INDEX_NAME,
        text_key=GlobalConstants.VECTOR_TEXT_EQUIVALENT_ATTR,
        relevance_score_fn="cosine"
    
    )    
    search_results = vector_search.similarity_search(query, k=5, pre_filter=pre_filter, additional={"similarity_score":0.7})
    content_fetched_list = [item.page_content for item in search_results]
    content_fetched = ''.join(content_fetched_list)
    references = list({doc.metadata['url'] for doc in search_results if 'url' in doc.metadata})
    if chatbot_name == "lawyer" and references:
        system_message = GlobalConstants.AI_LAWYER_ASSISTANT_SYSTEM_MESSAGE + f'\n These are the references from where content is fetched. {''.join(references)}. Make sure to add refereneces URL at the end of the response.'
    return StreamingResponse(ask_question(query, system_message, content_fetched), media_type="plain/text")

