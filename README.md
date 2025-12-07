# Job Search Tool

A Python command-line tool that uses the Anthropic API (Claude) with web search to find job listings based on keywords and location.

## Features

- 🔍 Search for jobs by keywords and location
- 💾 Securely save your API key locally
- 🔄 Easy API key management (save/remove)
- 🤖 Powered by Claude with real-time web search
- 📋 Get detailed job listings with descriptions and links

## Installation

1. Install Python 3.7 or higher (if not already installed)

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

Or install directly:
```bash
pip install anthropic
```

3. Get your Anthropic API key from: https://console.anthropic.com/

## Usage

### First Time Setup

Run the program and it will prompt you for your API key:
```bash
python job_search.py
```

Or save your API key first:
```bash
python job_search.py --save-key
```

### Searching for Jobs

Simply run:
```bash
python job_search.py
```

You'll be prompted to enter:
- **Job keywords**: e.g., "software engineer", "data analyst", "marketing manager"
- **Location**: e.g., "San Francisco", "Remote", "New York, NY"

### Managing Your API Key

**Save or update your API key:**
```bash
python job_search.py --save-key
```

**Remove your saved API key:**
```bash
python job_search.py --reset-key
```

**Show help:**
```bash
python job_search.py --help
```

## Examples

Example search queries:
- Keywords: "python developer" | Location: "Austin, TX"
- Keywords: "remote software engineer" | Location: "United States"
- Keywords: "data scientist" | Location: "San Francisco Bay Area"
- Keywords: "marketing manager" | Location: "Remote"

## Security Note

Your API key is stored locally in `~/.job_search/config.json`. Keep this file secure and never share it. You can remove it anytime using the `--reset-key` option.

## How It Works

The tool uses Claude (via Anthropic API) with web search capabilities to:
1. Search the web for current job listings matching your criteria
2. Parse and format the results
3. Present you with job titles, companies, locations, and application links

## Troubleshooting

**"Invalid API key" error:**
- Make sure you copied your API key correctly
- Reset and re-enter your key: `python job_search.py --reset-key` then run again

**No results found:**
- Try broader keywords
- Try different location formats
- Check your internet connection

**Module not found error:**
- Make sure you installed the requirements: `pip install anthropic`

## Requirements

- Python 3.7+
- anthropic library (>=0.40.0)
- Internet connection
- Valid Anthropic API key

## License

Free to use and modify as needed.
