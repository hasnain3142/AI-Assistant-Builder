# AI-Assistant-Builder

To run the backend:

- cd backend
- pip install virutalenv
- python -m virutalenv venv
- venv\Scripts\activate
- pip install -r requirements.txt
- uvicorn main:app --reload #You can add more flags by reading the docs of uvicorn

We will be getting data from various sources across the internet and storing them in following dbs:
- MongoDB Atlas
- Elasticsearch
- Qdrant Vector Database

Then we can do the vector search that is we call RAG approach to get the similar chunks out of the db and get the answer for the query.

