
# Google Analytics Custom Dimensions Creator

This Flask application authenticates with Google OAuth and creates custom dimensions for specified Google Analytics properties.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Python installed on your machine. Also, ensure you have `pip` available for installing dependencies.

### Installing

Clone this repository to your local machine:

```bash
git clone https://github.com/yasinabdulr/GA4-custom_dimension
```

Install the required packages:

```bash
pip install -r requirements.txt
```

### Setting Up

You need to set up a project in the Google API Console and get your client ID and client secret. Replace the placeholders in the script with your actual client ID and client secret.

### Running the Application

Run the application using:

```bash
python app.py
```

Navigate to `http://127.0.0.1:5000/` in your web browser to start the authentication process.

### Application Workflow

1. The user is presented with a link to authenticate with Google.
2. After authentication, the user is redirected to a callback URL.
3. The application then creates custom dimensions for each specified Google Analytics property.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
