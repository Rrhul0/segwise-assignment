### Segwise Assignment to create personalised connection message for LinkedIn user

This assignment/project is create personalised connection message for linkedin user by fetching/scraping the data like posts and user profile of user from linkedin.

## Setup and Run

To set up and run this application, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Rrhul0/Segwise-Assignment.git
    cd Segwise-Assignment
    ```

2. **Create and activate a virtual environment**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Get huggingface access token from**

    https://huggingface.co/settings/tokens
    and make sure you have set the nessesary permissions to the access token

5. **Set up environment variables**:
   Create a `.env` file in the root directory and add the necessary environment variables:

    ```
    LINKEDIN_USERNAME=your_linkedin_username
    LINKEDIN_PASSWORD=your_linkedin_password
    HUGGINGFACE_API_KEY=hf_***************
    ```

6. **Run the application**:

    ```bash
    python3 -m flask run
    ```

7. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:5000` to access the application.

## How to use

1. Open your web browser and navigate to `http://127.0.0.1:5000`.
2. Enter the LinkedIn profile URL in the provided text input field and click the submit button.
3. Wait while the application scrapes the LinkedIn pages and generates a personalized welcome message.
4. Once the scraping is complete, you will see the scraped data along with the result from the Hugging Face text completion API.

## Technologies used

1. Selenium:
   Selenium is an open-source tool that is used for automating web browsers. It provides a suite of tools for browser automation, including:

    - **Selenium WebDriver**: A collection of language-specific bindings to drive a browser. It supports multiple programming languages such as Java, C#, Python, and JavaScript.
    - **Selenium IDE**: A Chrome and Firefox plugin that allows you to record and playback browser interactions.
    - **Selenium Grid**: A tool that allows you to run tests on different machines against different browsers in parallel.

    Selenium is widely used for web application testing, web scraping, and automating repetitive web-based tasks. It supports all major browsers and operating systems, making it a versatile choice for developers and testers.

2. Beautiful Soup:
   Beautiful Soup is a Python library used for parsing HTML and XML documents. It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping. Key features include:

    - **Easy to use**: Beautiful Soup provides Pythonic idioms for iterating, searching, and modifying the parse tree.
    - **NavigableString**: Allows you to navigate the parse tree and extract text.
    - **Tag**: Represents an HTML or XML tag in the parse tree.
    - **Support for different parsers**: Beautiful Soup can work with different parsers like lxml and html.parser.

    Beautiful Soup is often used in conjunction with requests to fetch web pages and then parse the HTML content to extract the required information.

3. Flask:
   Flask is a lightweight WSGI web application framework in Python. It is designed with simplicity and flexibility in mind, making it easy to get started with web development. Key features include:

    - **Micro-framework**: Flask is minimalistic and does not include many built-in features, allowing developers to choose the components they need.
    - **Routing**: Flask provides a simple and intuitive way to define URL routes and handle HTTP requests.
    - **Templating**: Flask uses Jinja2 as its templating engine, enabling the creation of dynamic HTML pages.
    - **Extensible**: Flask supports extensions that can add functionality to the core framework, such as database integration, form handling, and authentication.

    Flask is commonly used for developing small to medium-sized web applications and APIs. Its simplicity and flexibility make it a popular choice for developers who want to build web applications quickly and efficiently.

4. Huggingface_hub:
   Huggingface_hub is a library that allows you to interact with the Hugging Face Hub, a platform for sharing and using pre-trained machine learning models. Key features include:

    - **Model Repository**: Access thousands of pre-trained models for various tasks such as natural language processing, computer vision, and more.
    - **Model Upload**: Easily upload your own models to the Hugging Face Hub for sharing and collaboration.
    - **Inference API**: Use the hosted inference API to run predictions using models from the Hub without needing to set up your own infrastructure.
    - **Versioning**: Keep track of different versions of your models and datasets.

    Huggingface_hub is widely used in the machine learning community for sharing and utilizing state-of-the-art models, making it easier to build and deploy machine learning applications.
