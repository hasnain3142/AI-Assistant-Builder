from fastapi import APIRouter
from utils.Database import DatabaseConnector
from utils.StreamingResponseByOpenAI import ask_question
from utils.DataModels import QueryRequestModel
import GlobalConstants
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_openai import OpenAIEmbeddings
from fastapi.responses import StreamingResponse

    
router = APIRouter()

@router.post("/")
async def query(request_body: QueryRequestModel):
    post_request_JSON_body = request_body.model_dump()
    chatbot_name = post_request_JSON_body['chatbot_name']
    pre_filter = post_request_JSON_body['pre_filter']
    query = post_request_JSON_body['query']

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
    print(search_results)
    content_fetched_list = [item.page_content for item in search_results]
    content_fetched = ''.join(content_fetched_list)
    references = list({doc.metadata['url'] for doc in search_results if 'url' in doc.metadata})
    if chatbot_name == "lawyer" and references:
        system_message = GlobalConstants.AI_LAWYER_ASSISTANT_SYSTEM_MESSAGE + f'\n These are the references from where content is fetched. {''.join(references)}. Make sure to add refereneces at the end of the response.'
    return StreamingResponse(ask_question(query, system_message, content_fetched), media_type="plain/text")

