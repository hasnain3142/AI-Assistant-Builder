# AI-Assistant-Builder

AI-Assistant-Builder is a flexible platform that enables users to create their own AI assistants tailored to any profession or field. By customizing some data and values, users can effortlessly build specialized AI assistants such as an AI Doctor or an AI Lawyer.

## Getting Started

### Prerequisites

Ensure you have Python installed on your machine.

### Running the Backend

Follow these steps to set up and run the backend:

1. Navigate to the `backend` directory:
    ```bash
    cd backend
    ```
2. Install `virtualenv`:
    ```bash
    pip install virtualenv
    ```
3. Create a virtual environment:
    ```bash
    python -m virtualenv venv
    ```
4. Activate the virtual environment:
    ```bash
    venv\Scripts\activate
    ```
    For Unix or MacOS, use:
    ```bash
    source venv/bin/activate
    ```
5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
6. Start the backend server using Uvicorn:
    ```bash
    uvicorn main:app --reload
    ```
    You can add more flags by referring to the [Uvicorn documentation](https://www.uvicorn.org/#command-line-options).


### Building the Frontend

Follow these steps to set up and run the frontend:

1. Navigate to the `frontend` directory:
    ```bash
    cd frontend
    ```
2. Create a separate `requirements.txt` for the frontend and list your frontend dependencies there.
3. Create a virtual environment:
    ```bash
    python -m virtualenv .frontend
    ```
4. Activate the virtual environment:
    ```bash
    .frontend\Scripts\activate
    ```
    For Unix or MacOS, use:
    ```bash
    source .frontend/bin/activate
    ```
5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
6. Setting Up Qdrant

    Follow these steps to set up Qdrant:

    1. Pull the Qdrant Docker image:
        ```bash
        docker pull qdrant/qdrant
        ```
    2. Run the Qdrant container:
        ```bash
        docker run -p 6333:6333 -p 6334:6334 -v ${PWD}qdrant_storage:/qdrant/storage:z qdrant/qdrant
        ```

7. Run the frontend application using Streamlit:
    ```bash
    streamlit run streamlit_app.py
    ```

### Data Sources and Databases

We collect data from various sources across the internet and store it in the following databases:
- **MongoDB Atlas**
- **Elasticsearch**
- **Qdrant Vector Database**

### Vector Search and RAG Approach

To provide accurate answers to user queries, we implement a vector search technique known as the Retrieval-Augmented Generation (RAG) approach. This method involves searching for similar chunks of data within our databases to generate precise and relevant responses.

## Customizing Your AI Assistant

Creating your own AI assistant is straightforward. By modifying specific data and values in the provided templates, you can develop an AI assistant tailored to any profession or field of your choice.

1. Open globalconstants and simply change values, like category and assistant.
2. Add the data inside the data folder.

Explore the possibilities and build your own specialized AI assistant today!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

We welcome contributions to AI-Assistant-Builder! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

Please ensure your code adheres to our coding standards and includes appropriate tests. For major changes, please open an issue first to discuss what you would like to change.

Thank you for contributing!