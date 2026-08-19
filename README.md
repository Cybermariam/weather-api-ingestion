# Weather API Ingestion

A Python data ingestion script that fetches live weather data from the OpenWeatherMap REST API, cleans the response, handles errors, logs execution, and stores the cleaned data locally as JSON.

## Project Overview

This project demonstrates a basic data ingestion workflow using Python.

The script:

- Fetches live weather data from the OpenWeatherMap API
- Uses request timeouts to prevent requests from hanging
- Handles HTTP and network errors
- Extracts relevant fields from the raw API response
- Transforms the API response into a clean dataset
- Logs execution status and errors
- Saves the cleaned data as a formatted JSON file

## Data Extracted

The script extracts the following fields:

- City
- Country
- Temperature
- Feels-like temperature
- Humidity
- Weather description
- Wind speed

## Technologies Used

- Python
- Requests
- JSON
- Logging
- python-dotenv
- OpenWeatherMap REST API

## Project Structure

```text
weather-api-ingestion/
├── data/
├── src/
│   └── weather.py
├── tests/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Environment Variables

Create a `.env` file in the project root and add your OpenWeatherMap API key:

```text
OPENWEATHER_API_KEY=your_api_key_here
```

The `.env` file is excluded from Git using `.gitignore` and should never be committed to the repository.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Cybermariam/weather-api-ingestion.git
cd weather-api-ingestion
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the script

```bash
python src/weather.py
```

## Output

The script saves the cleaned weather data as a JSON file.

Example:

```json
{
    "city": "Lagos",
    "country": "NG",
    "wind_speed": 3.1,
    "temperature": 26.22,
    "feels_like": 26.22,
    "humidity": 80,
    "description": "overcast clouds"
}
```

Execution logs are also written to the configured log file.

## Error Handling

The script handles:

- Network/request errors
- HTTP errors
- Request timeouts

Python's `logging` module is used to record execution status and errors.

## Data Flow

```text
OpenWeatherMap API
        ↓
   HTTP Request
        ↓
   JSON Response
        ↓
 Data Extraction
        ↓
  Data Cleaning
        ↓
   JSON Output
```

## Future Improvements

- Store weather data in a database
- Support multiple cities
- Schedule automated data ingestion
- Add data validation
- Add automated tests
- Build an ETL pipeline
- Deploy the ingestion process to the cloud

## Author

Mariam