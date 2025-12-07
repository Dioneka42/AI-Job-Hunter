#!/usr/bin/env python3
"""
Job Search Tool using Anthropic API
Searches for jobs based on keywords and location using Claude's web search capabilities
"""

import os
import json
import sys
from pathlib import Path
import anthropic

# Configuration file path
CONFIG_DIR = Path.home() / ".job_search"
CONFIG_FILE = CONFIG_DIR / "config.json"


def ensure_config_dir():
    """Create config directory if it doesn't exist"""
    CONFIG_DIR.mkdir(exist_ok=True)


def save_api_key(api_key):
    """Save API key to config file"""
    ensure_config_dir()
    config = {"api_key": api_key}
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)
    print("✓ API key saved successfully!")


def load_api_key():
    """Load API key from config file"""
    if not CONFIG_FILE.exists():
        return None
    try:
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
        return config.get("api_key")
    except:
        return None


def remove_api_key():
    """Remove saved API key"""
    if CONFIG_FILE.exists():
        CONFIG_FILE.unlink()
        print("✓ API key removed successfully!")
    else:
        print("No API key found to remove.")


def get_api_key():
    """Get API key from config or prompt user"""
    api_key = load_api_key()
    if not api_key:
        print("\nNo API key found. Please enter your Anthropic API key.")
        print("(You can get one from https://console.anthropic.com/)")
        api_key = input("API Key: ").strip()
        if api_key:
            save_api_key(api_key)
    return api_key


def search_jobs(keywords, location, api_key):
    """Search for jobs using Anthropic API with web search"""
    print(f"\n🔍 Searching for '{keywords}' jobs near {location}...\n")
    
    try:
        client = anthropic.Anthropic(api_key=api_key)
        
        # Create the search query
        search_query = f"{keywords} jobs {location}"
        
        # Call Claude with web search tool
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4000,
            tools=[
                {
                    "type": "web_search_20250305",
                    "name": "web_search"
                }
            ],
            messages=[
                {
                    "role": "user",
                    "content": f"""Search for current job openings for '{keywords}' in or near '{location}'. 
                    
Please find recent job listings and provide:
1. Job title and company name
2. Location
3. Brief description or key requirements
4. Link to apply (if available)

Format the results in a clear, easy-to-read way. Focus on the most relevant and recent postings."""
                }
            ]
        )
        
        # Process the response
        full_response = []
        for block in message.content:
            if block.type == "text":
                full_response.append(block.text)
        
        result = "\n".join(full_response)
        
        if result:
            print("=" * 80)
            print(result)
            print("=" * 80)
        else:
            print("No results found. Try different keywords or location.")
            
    except anthropic.AuthenticationError:
        print("\n❌ Error: Invalid API key. Please check your API key and try again.")
        print("You can reset your API key with: python job_search.py --reset-key")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1)


def print_help():
    """Print help information"""
    help_text = """
Job Search Tool - Usage:
========================

Search for jobs:
    python job_search.py

Manage API key:
    --save-key          Save or update your Anthropic API key
    --reset-key         Remove saved API key
    --help              Show this help message

Examples:
    python job_search.py
    python job_search.py --save-key
    python job_search.py --reset-key
"""
    print(help_text)


def main():
    """Main program function"""
    # Check for command line arguments
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        
        if arg in ["--help", "-h"]:
            print_help()
            return
        elif arg == "--save-key":
            print("Enter your Anthropic API key:")
            api_key = input("API Key: ").strip()
            if api_key:
                save_api_key(api_key)
            else:
                print("No API key entered.")
            return
        elif arg == "--reset-key":
            remove_api_key()
            return
        else:
            print(f"Unknown argument: {arg}")
            print("Use --help to see available options.")
            return
    
    # Get API key
    api_key = get_api_key()
    if not api_key:
        print("API key is required to search for jobs.")
        sys.exit(1)
    
    print("\n" + "=" * 80)
    print("                        JOB SEARCH TOOL")
    print("=" * 80)
    
    # Get search parameters from user
    print("\nEnter job search details:")
    keywords = input("Job keywords (e.g., 'software engineer', 'data analyst'): ").strip()
    location = input("Location (e.g., 'San Francisco', 'Remote', 'New York'): ").strip()
    
    if not keywords or not location:
        print("Both keywords and location are required!")
        sys.exit(1)
    
    # Perform search
    search_jobs(keywords, location, api_key)
    
    # Ask if user wants to search again
    print("\n" + "=" * 80)
    again = input("\nSearch again? (y/n): ").strip().lower()
    if again == 'y':
        main()
    else:
        print("\nThank you for using Job Search Tool!")


if __name__ == "__main__":
    main()
