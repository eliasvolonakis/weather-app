# Weather App

This is a web application that provides weather forecasts based on user input. It uses Django for the backend and React for the frontend. Using the web application, a user may input any city of their choice and will then see the current day's weather, in addition to the forecasts for the next 5 days. The weather data is in a tabular format and uses icons to represent weather conditions. All weather data is obtained by the API: https://api.open-meteo.com. 

### Prerequisites

Before getting started, ensure you have the following installed:

- [Python](https://www.python.org/) (3.6 or higher)
- [Django](https://www.djangoproject.com/)
- [Node.js](https://nodejs.org/) (for the frontend)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/eliasvolonakis/weather_app.git
   ```

2. Change into the project directory:

   ```bash
   cd weather_app
   ```

3. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

4. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Change into the `weather` directory:

   ```bash
   cd weather
   ```

6. Make and apply the database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

8. Open a new terminal and change into the project's frontend directory:

   ```bash
   cd frontend
   ```

9. Install Node.js dependencies for the frontend:

   ```bash
   npm install
   ```

10. Start the frontend development server:

    ```bash
    npm start
    ```

11. You can now access the Weather App at [http://localhost:3000](http://localhost:3000).

## Usage

1. Open the Weather App in your web browser.

2. Enter a city in the input field and click the "Generate Forecast" button.

3. The app will fetch weather data and display it in a table with icons representing the weather conditions.
