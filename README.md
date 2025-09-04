# NeuraSeek

NeuraSeek is a futuristic AI-powered domain search tool that leverages semantic search to find relevant domain-specific content on the public web. Built with Flask, TailwindCSS, and the Exa AI Search API.

## Features

- AI-driven semantic search for precise results
- Clean, responsive UI with modern Tailwind CSS
- Configurable number of results and domain filtering
- Deploys seamlessly on Vercel

## Requirements

- Python 3.8+
- Flask
- exa_py (Exa AI API client)
- TailwindCSS (via CDN)

## Setup

1. Clone the repository:

git clone https://github.com/your-github-username/custom-search-engine.git
cd custom-search-engine


2. Create and activate a virtual environment (recommended):

On Windows:
python -m venv venv
.\venv\Scripts\activate


On Mac/Linux:
python3 -m venv venv
source venv/bin/activate


3. Install dependencies:

pip install -r requirements.txt


4. Set your Exa API key as an environment variable:

- On Mac/Linux:
  ```
  export EXA_API_KEY="your_api_key_here"
  ```

- On Windows:
  ```
  set EXA_API_KEY=your_api_key_here
  ```

5. Run the Flask app:

python app.py


Open http://localhost:5000 in your browser to use the app.

## Deployment on Vercel

1. Ensure your `requirements.txt` and `vercel.json` are in the project root.

2. Push your code to GitHub.

3. Connect your GitHub repo on [Vercel](https://vercel.com/) dashboard.

4. For Build Command, use:

pip install -r requirements.txt


5. Leave the Output Directory blank.

6. Vercel will automatically run your Flask app using `vercel.json` configuration.

7. Deploy and get your live app URL.

## Project Structure

├── app.py # Main Flask app
├── templates/
│   └── index.html # HTML template
├── static/ # CSS, JS, images if any
├── requirements.txt # Python dependencies
└── vercel.json # Vercel deployment config

## Credits

- [Exa AI Search API](https://exa.ai)
- [Flask](https://flask.palletsprojects.com/)
- [TailwindCSS](https://tailwindcss.com/)
- Deployed on [Vercel](https://vercel.com/)

---

If you have any questions or want to contribute, feel free to open an issue or PR.

---

*Happy Searching!* 🚀