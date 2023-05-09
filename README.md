# Weather Forecast and Rain Alert

This code snippet retrieves weather forecast data from the WeatherAPI service and sends a rain alert message to a specified phone number using the Twilio API.

## Prerequisites

Before running the code, make sure you have the following:

- An account SID for your Twilio account.
- An authentication token for your Twilio account.
- An API key for the WeatherAPI service.
- A valid mobile phone number to receive the rain alert.

## Installation

To use this code, please follow these steps:

1. Install the required packages by running the following command:

```bash
pip install requests twilio
```

2. Set the environment variables for the following values:

- `AUTH_TOKEN`: Your Twilio account authentication token.
- `OWM_API_KEY`: Your WeatherAPI API key.
- `PH_NO`: The phone number to which you want to send the rain alert.

## Usage

Open the Python file and provide the necessary values for the following variables:

- `account_sid`: Your Twilio account SID.
- `API_KEY`: Your WeatherAPI API key.
- `END_POINT`: The URL endpoint for the WeatherAPI service.
- `parameters`: The parameters for the weather forecast request, including the location and forecast duration.

Save the file and run it. If rain is forecasted in the next 12 hours, the code will send a rain alert message to the specified phone number using the Twilio API.

**Note:** Ensure that you have a working internet connection while running the code.

## License

This code is licensed under the [MIT License](LICENSE).

Feel free to modify and enhance this code according to your requirements.
