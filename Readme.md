# test_synergyway

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/khaulinD/test_synergyway.git
    cd test_synergyway
    ```

2. **Set up a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    Make sure your `requirements.txt` file includes all the necessary packages

## Configuration

- **Environment Variables:**

    Set up necessary environment variables, especially for any external service like email services or payment gateways. You can use `python-dotrank==1.0.1` to manage environment variables through a `.env` file.

## Running the Application

1. **Start the Uvicorn server:**

    ```bash
    uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
    ```

    This command starts the application with live reloading enabled.

2. **Visit the application:**

    Open a browser and go to [http://localhost:8000/docs](http://localhost:8000/docs) to see the running application.


# Using Docker
1. **Start the docker:**

    ```bash
    docker-compose up --build
    ``` 
2. **Visit the application:**

    Open a browser and go to [http://localhost:8000/docs](http://localhost:8000/docs) to see the running application.

   - Flower - for celery task monitoring: http://localhost:5555
   - Adminer - for database review in browser: http://localhost:8080
