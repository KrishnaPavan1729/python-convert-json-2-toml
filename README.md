# JSON to TOML Converter

## Project Overview

This project is a personal endeavor to create a robust and efficient tool for converting JSON files to TOML format. It serves as a demonstration of my programming skills, particularly in Python, and my ability to work with different data formats and implement efficient file processing techniques.

## Key Features

- Converts JSON files to TOML format with high accuracy
- Implements input validation for both JSON and TOML to ensure data integrity
- Utilizes advanced logging techniques for comprehensive error tracking and debugging
- Incorporates performance metrics to measure execution time and file size changes
- Demonstrates proper project structure and modular design in Python

## Technical Highlights

- **Modular Architecture**: The project is structured into separate modules (`config.py`, `converter.py`, `logging_setup.py`, `utils.py`, `main.py`) to demonstrate clean code organization and separation of concerns.
- **Configuration Management**: Utilizes a `config.ini` file for easy customization of runtime parameters.
- **Error Handling**: Implements comprehensive error handling and logging to ensure robustness.
- **Performance Optimization**: Incorporates file size calculation and execution time measurement to showcase performance awareness.

## Project Structure

```
json2toml/
├── src/
│   └── json2toml/
│       ├── __init__.py
│       ├── config.py
│       ├── converter.py
│       ├── logging_setup.py
│       ├── utils.py
│       └── main.py
├── tests/
│   └── test_json2toml.py
├── config.ini
├── README.md
├── requirements.txt
└── setup.py
```

## Setup and Usage

1. Clone the repository:
   ```
   git clone https://github.com/KrishnaPavan1729/python-convert-json-2-toml.git
   cd json2toml
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Configure the `config.ini` file with desired settings.

4. Run the main script:
   ```
   python -m src.json2toml.main
   ```

5. Follow the prompts to enter the JSON file path or use the default from the config file.

## Future Enhancements

- Implement a command-line interface for easier usage
- Add support for batch processing of multiple files
- Develop a simple GUI for non-technical users

## About the Author

I am a passionate programmer with a keen interest in data processing and software architecture. This project showcases my ability to create efficient, well-structured Python applications. Feel free to reach out to me for any questions or professional opportunities.

- GitHub: https://github.com/KrishnaPavan1729
- LinkedIn: Saikrishna Pavan
- Email: saikrishnapavan1729@gmail.com

