# Flask Data Retrieval and Processing Application

## Setup instructions
1. Git clone the repository to created folder.
   mkdir flask-data-retrieval
   cd flask-data-retrieval
   git clone https://github.com/saikrishna-hub/vervoe-task-data-retrieval.gi
2. Create venv for local specific environment setup
   Python3 -m venv venv
   source venv/bib/activate
3. Install project dependencies:
   pip install -r requirements.txt
4. Run Flask application python app.py
   Python app.py

This project handles three API endpoints for data fetching, processing and retrieving.
GET /fetch-data: Fetches mock data.
POST /process-data: Processes the data (e.g., converts to uppercase).
GET /get-processed-data: Retrieves processed data from memory.

