# llm-coder

llm-coder is a web application that leverages a Large Language Model (LLM) such as OpenAI's GPT-3.5 Turbo to generate code snippets based on user inputs. 

## Getting Started

### Requirements

- Docker
- OpenAI API Key

### Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/llm-coder.git
    ```

2. Navigate to the project directory:

    ```bash
    cd llm-coder
    ```

3. Create a `.env` file in the root directory and add your OpenAI API key:

    ```plaintext
    OPENAI_API_KEY=your_api_key_here
    ```

4. Build the Docker image:

    ```bash
    docker build -t llm-coder .
    ```

5. Run the Docker container:

    ```bash
    docker run -d -p 8003:8003 llm-coder
    ```

6. Access the application at [http://localhost:8003/static/index.html](http://localhost:8003/static/index.html) in your web browser.

7. Alternatively, you can access the Swagger documentation at [http://localhost:8003/docs](http://localhost:8003/docs) for API endpoints.

## API Endpoints

- `/get_answer`: POST endpoint to send a prompt to the language model and get a code snippet response.
- `/feedback`: POST endpoint to submit feedback on the generated code snippets.

## Customization

- You can customize the application by modifying the FastAPI endpoints and the logic in the `main.py` file to suit your specific use case.
- Adjust the Dockerfile and Docker container settings as needed for your deployment environment.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for any bug fixes, feature requests, or improvements.

## License

This project is licensed under the [MIT License](LICENSE).
