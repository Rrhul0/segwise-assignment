FROM python:3.10

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
  wget \
  unzip \
  curl \
  gnupg \
  && rm -rf /var/lib/apt/lists/*

RUN CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
   mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION && \
   curl -sS -o /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
   unzip -qq /tmp/chromedriver_linux64.zip -d /opt/chromedriver-$CHROMEDRIVER_VERSION && \
   rm /tmp/chromedriver_linux64.zip && \
   chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver && \
   ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver /usr/local/bin/chromedriver


# Install Google Chrome
RUN sh -c 'curl -fSsL https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor | tee /usr/share/keyrings/google-chrome.gpg >> /dev/null'
RUN sh -c 'echo deb [arch=amd64 signed-by=/ust/share/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main | tee /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install xvfb -y
RUN apt-get install google-chrome-stable -y

# Set display port to avoid errors when running Chrome
ENV DISPLAY=:99

# Set the working directory in the container
WORKDIR /app

# Copy the Python dependencies and install them
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the Flask application code into the container
COPY . .

# Expose the port the Flask app will run on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "-m", "flask", "run"]