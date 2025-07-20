# Flask Todo App for AWS Elastic Beanstalk

This repository contains a simple Flask-based Todo application designed for deployment on AWS Elastic Beanstalk.

## Features

- Add, view, and delete tasks with priorities
- Uses SQLite for data storage
- Ready for deployment on Elastic Beanstalk

## Getting Started

### Prerequisites

- Python 3.x

### Local Development

1. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    python application.py
    ```

### Deploying to Elastic Beanstalk

1. Zip your project files, including `.ebextensions`, `application.py`, `requirements.txt`, and the `templates` folder.

2. Upload the zip file using the AWS Elastic Beanstalk web console.

3. Follow the prompts in the AWS portal to create and launch your environment.

### Notes

- Configuration files for Elastic Beanstalk should be placed in the `.ebextensions` directory.
- The entry point for Elastic Beanstalk is set as `WSGIPath: application:app` in `.ebextensions/flask.config`.

## Project Structure

```
.
├── application.py
├── requirements.txt
├── templates/
│   ├── index.html
│   └── tasks.html
├── .ebextensions/
│   └── flask.config
└── README.md
```