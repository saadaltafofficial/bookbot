# BookBot

A Python text analysis tool that generates comprehensive statistics for books and text files.

## Features

- **Word Count**: Counts total words in the text
- **Character Frequency**: Analyzes alphabetic character frequency with sorted results
- **Command Line Interface**: Easy-to-use CLI with proper error handling

## Usage

```bash
python3 main.py <path_to_book>
```

### Examples

```bash
python3 main.py books/frankenstein.txt
python3 main.py books/mobydick.txt
```

## Requirements

- Python 3.x
- Text files to analyze

## Project Structure

- `main.py` - Main application entry point
- `stats.py` - Text analysis functions
- `books/` - Directory for text files (not included)

## Output

The tool provides:
- Total word count
- Character frequency analysis (alphabetic characters only)
- Results sorted by frequency in descending order
