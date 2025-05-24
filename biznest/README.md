# BizNest

BizNest is a next-gen AI-powered business management app designed to streamline operations using intelligent agents.

## Current Status

This is a very early development version of BizNest. The current functionality is minimal and serves as a basic proof-of-concept for the agent interaction model.

## Project Structure

The project is organized into the following main directories:

-   `frontend/`: Contains the user interface elements. Currently, this includes a simple HTML page to interact with the backend.
-   `backend/`: Houses the server-side logic. This includes the Flask API that receives commands and communicates with the agents.
-   `agents/`: Contains the definitions for the AI agents. `base_agent.py` provides the fundamental agent class.
-   `docs/`: Intended for project documentation (currently empty).

## How to Run

Follow these steps to run the current version of BizNest:

1.  **Start the Backend:**

    Open your terminal and navigate to the `backend` directory:
    ```bash
    cd biznest/backend
    ```
    Ensure you have Flask installed. If not, you can install it using pip:
    ```bash
    # If you are using a virtual environment, activate it first.
    # pip install Flask
    ```
    Then, run the Flask application:
    ```bash
    python app.py
    ```
    The backend server will start and listen on `http://127.0.0.1:5000`.

2.  **Open the Frontend:**

    Navigate to the `biznest/frontend/` directory in your file explorer. Open the `index.html` file using your preferred web browser (e.g., by double-clicking it or using "Open with..." from the right-click menu).

3.  **Interact:**
    Once the frontend is open in your browser:
    -   You will see an input field and a button labeled "Send Command to Alex".
    -   Type any command (e.g., "file my taxes" or "hello") into the input field.
    -   Click the "Send Command to Alex" button.
    -   The response from Alex (the Accountant agent) will be displayed below the button.

    For example, if you type "summarize expenses", you should see a reply like "Alex says: Agent Alex received command: summarize expenses".
