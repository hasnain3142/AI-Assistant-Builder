from tenacity import retry
from tenacity import stop_after_delay
from tenacity import RetryError
from tenacity import stop_after_attempt
from tenacity import wait_exponential
from openai import OpenAI
import GlobalConstants

@retry(stop=stop_after_delay(30))
def ask_question(query, system_message, content):
    client = OpenAI(api_key=GlobalConstants.OPENAI_KEY, timeout=GlobalConstants.OPENAI_REQUEST_TIMEOUT)

    messages = [
                {"role": "system", "content": system_message},
                {"role": "system", "content": content},
                {"role": "user", "content":query}
                ]           
    response = client.chat.completions.create(
                                messages=messages,                            
                                temperature=0.5,
                                frequency_penalty=1,
                                max_tokens=GlobalConstants.OPENAI_MAX_TOKENS,
                                timeout=GlobalConstants.OPENAI_REQUEST_TIMEOUT,
                                model=GlobalConstants.OPENAI_MODEL,
                                stream=True
                                )
    for chunk in response:
        if type(chunk.choices[0].delta.content)==str:
            yield chunk.choices[0].delta.content
    return 