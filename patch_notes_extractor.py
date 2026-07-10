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
from bs4 import BeautifulSoup
import json


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
        except requests.exceptions.RequestException:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # Exponential backoff
                time.sleep(wait_time)
            else:
                pass
    return None


def extract_og_image(html_content):
    """
    Extracts the og:image meta tag from HTML content.

    Args:
        html_content (str): HTML content to parse

    Returns:
        str or None: og:image URL if found, None otherwise
    """
    if not html_content:
        return None

    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        og_image_tag = soup.find('meta', property='og:image')
        if og_image_tag and og_image_tag.get('content'):
            return og_image_tag['content']
    except Exception:
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
        except Exception:
            return None
    return None


def extract_sections(markdown_content, section_patterns=None):
    """
    Extracts specified sections from the Markdown content.

    Args:
        markdown_content (str): Markdown content to parse
        section_patterns (list): List of regex patterns to match section headers.
                                If None, defaults to item-related sections.

    Returns:
        dict: Dictionary with section names as keys and content as values
    """
    if not markdown_content:
        return {}

    # Default patterns for item-related sections
    if section_patterns is None:
        section_patterns = [
            r'^#+\s+\*{0,2}ITEMS\*{0,2}',
            r'^#+\s+\*{0,2}ITEM\s+ADJUSTMENTS?\*{0,2}',
            r'^#+\s+\*{0,2}ITEM\s+CHANGES?\*{0,2}',
            r'^#+\s+\*{0,2}ITEM\s+UPDATES?\*{0,2}',
            r'^#+\s+\*{0,2}ITEM\s+REWORKS?\*{0,2}'
        ]

    # Patterns to stop extraction (end of relevant sections)
    stop_patterns = [
        r'^#+\s+\*{0,2}Related\s+Articles\*{0,2}',
        r'^#+\s+\*{0,2}SKINS\*{0,2}',
        r'^#+\s+\*{0,2}CHAMPIONS?\*{0,2}',
        r'^#+\s+\*{0,2}RUNES?\*{0,2}',
        r'^#+\s+\*{0,2}SUMMONER\s+SPELLS?\*{0,2}'
    ]

    sections = {}
    current_section = None
    current_content = ""

    for line in markdown_content.splitlines():
        # Check if this line starts a new section we're interested in
        section_match = None
        for pattern in section_patterns:
            if re.match(pattern, line, re.IGNORECASE):
                section_match = line.strip()
                break

        if section_match:
            # Save previous section if exists
            if current_section and current_content.strip():
                sections[current_section] = current_content.strip()

            # Start new section
            current_section = section_match
            current_content = line + "\n"
            continue

        # Check if we should stop (reached a non-item section)
        if current_section:
            stop_match = any(re.match(pattern, line, re.IGNORECASE) for pattern in stop_patterns)
            if stop_match:
                # Save current section and stop
                if current_content.strip():
                    sections[current_section] = current_content.strip()
                break
            else:
                # Continue adding to current section
                current_content += line + "\n"

    # Save the last section if exists
    if current_section and current_content.strip():
        sections[current_section] = current_content.strip()

    return sections



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
        description="Extract item-related sections and og:image from Wild Rift patch notes webpage",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python patch_notes_extractor.py https://wildrift.leagueoflegends.com/en-us/news/game-updates/wild-rift-patch-notes-6-2e/
  python patch_notes_extractor.py --json https://wildrift.leagueoflegends.com/en-us/news/game-updates/wild-rift-patch-notes-6-2e/
  python patch_notes_extractor.py --all-sections https://wildrift.leagueoflegends.com/en-us/news/game-updates/wild-rift-patch-notes-6-2e/
  python patch_notes_extractor.py --all-sections --json https://wildrift.leagueoflegends.com/en-us/news/game-updates/wild-rift-patch-notes-6-2e/
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

    parser.add_argument(
        "--json",
        action="store_true",
        help="Output in JSON format with items and og:image"
    )

    args = parser.parse_args()

    # Validate URL format
    if not validate_url(args.url):
        sys.exit(1)

    # Validate retry count
    if args.retries < 1:
        sys.exit(1)

    # Get HTML content for both items extraction and og:image extraction
    html_content = get_html_content(args.url, args.retries)
    if not html_content:
        sys.exit(1)

    # Extract content
    markdown_content = convert_html_to_markdown(html_content)
    if not markdown_content:
        sys.exit(1)

    sections = extract_sections(markdown_content)
    if not sections:
        sys.exit(1)

    # Extract og:image
    og_image_url = extract_og_image(html_content)

    if args.json:
        print(json.dumps({"sections": sections, "og_image": og_image_url}, ensure_ascii=False, indent=2))
    else:
        for section_name, section_content in sections.items():
            print(f"=== {section_name} ===")
            print(section_content)
            print()


if __name__ == "__main__":
    main()
