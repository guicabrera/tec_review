# tec_review Project

This project is an Eel application that provides a simple web interface for interacting with Python code. Below are the details of the project structure and files.

## Project Structure

```
tec_review
├── 28-05-2025.ipynb          # Jupyter Notebook containing the main application logic
├── web                       # Directory containing web-related files
│   ├── index.html           # Main HTML file for the Eel application
│   ├── css                  # Directory for CSS files
│   │   └── style.css        # Styles for the HTML elements
│   ├── js                   # Directory for JavaScript files
│   │   └── main.js          # JavaScript code interacting with the Eel backend
│   └── assets               # Directory for static assets
│       └── favicon.ico      # Favicon for the web application
└── README.md                # Documentation for the project
```

## Setup Instructions

1. **Clone the Repository**: 
   Clone this repository to your local machine using:
   ```
   git clone <repository-url>
   ```

2. **Install Dependencies**: 
   Make sure you have Python installed. Then, install the required packages using:
   ```
   pip install eel pandas
   ```

3. **Run the Application**: 
   Execute the Jupyter Notebook `28-05-2025.ipynb` to start the Eel application. You can do this by running:
   ```
   jupyter notebook 28-05-2025.ipynb
   ```

## Usage Guidelines

- Open your browser and navigate to `http://localhost:8080` to access the application.
- The application allows you to interact with the backend Python functions through the web interface.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.