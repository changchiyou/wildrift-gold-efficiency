#!/usr/bin/env python3
"""
Patch Notes Extractor

A script to extract the ITEMS section from Wild Rift patch notes webpages.
Fetches a webpage and converts its content to Markdown, then extracts the items section.
"""

import argparse
import sys
import time
import requests
from markdownify import markdownify as md
import re
from urllib.parse import urlparse


def validate_url(url):
    """Validates if the provided URL is properly formatted."""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        return False


def get_html_content(url, max_retries=3):
    """
    Fetches the HTML content of a given URL with retry mechanism.

    Args:
        url (str): The URL to fetch
        max_retries (int): Maximum number of retry attempts

    Returns:
        str or None: HTML content if successful, None otherwise
    """
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()  # Raise an exception for bad status codes
            return response.text
        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # Exponential backoff
                time.sleep(wait_time)
            else:
                pass
    return None


def convert_html_to_markdown(html_content):
    """
    Converts HTML content to Markdown.

    Args:
        html_content (str): HTML content to convert

    Returns:
        str or None: Markdown content if successful, None otherwise
    """
    if html_content:
        try:
            markdown_output = md(html_content, heading_style="ATX")  # ATX style for headings (e.g., # Heading)
            return markdown_output
        except Exception as e:
            return None
    return None


def extract_items_section(markdown_content):
    """
    Extracts the items section from the Markdown content.

    Args:
        markdown_content (str): Markdown content to parse

    Returns:
        str: Items section content
    """
    if not markdown_content:
        return ""
    item_section = ""
    item_section_started = False
    for line in markdown_content.splitlines():
        if re.match(r'^#+\s+ITEMS', line, re.IGNORECASE):
            item_section_started = True
        if item_section_started and (
            re.match(r'^#+\s+Related\s+Articles', line, re.IGNORECASE) or
            re.match(r'^#+\s+SKINS', line, re.IGNORECASE)
        ):
            break
        if item_section_started:
            item_section += line + "\n"
    if item_section_started:
        pass
    else:
        pass
    return item_section


def webpage_to_markdown(url, max_retries=3):
    """
    Fetches a webpage and converts its content to Markdown.

    Args:
        url (str): The URL to fetch and convert
        max_retries (int): Maximum number of retry attempts

    Returns:
        str or None: Markdown content if successful, None otherwise
    """
    html_content = get_html_content(url, max_retries)
    if html_content:
        return convert_html_to_markdown(html_content)
    return None


def main():
    """Main function to handle command line arguments and execute the extraction."""
    parser = argparse.ArgumentParser(
        description="Extract ITEMS section from Wild Rift patch notes webpage",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python patch_notes_extractor.py https://wildrift.leagueoflegends.com/en-us/news/game-updates/wild-rift-patch-notes-6-2e/
        """
    )

    parser.add_argument(
        "url",
        help="URL of the patch notes webpage to extract items from"
    )
    
    parser.add_argument(
        "--retries",
        type=int,
        default=3,
        help="Number of retry attempts for failed requests (default: 3)"
    )

    args = parser.parse_args()

    # Validate URL format
    if not validate_url(args.url):
        sys.exit(1)

    # Validate retry count
    if args.retries < 1:
        sys.exit(1)

    # Extract items section
    markdown_content = webpage_to_markdown(args.url, args.retries)
    if markdown_content:
        items_section = extract_items_section(markdown_content)
        if items_section.strip():
            print(items_section)
        else:
            sys.exit(1)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
