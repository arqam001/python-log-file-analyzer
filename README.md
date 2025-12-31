# Python Log File Analyzer

A lightweight Python command-line application that parses application log files, filters log entries by date, and generates clear summary statistics. This project focuses on clean Python fundamentals and practical log analysis using only the Python standard library.

---

## Overview

Application logs often contain large volumes of unstructured text, making it difficult to quickly understand system behavior. This tool reads log files line by line, extracts structured information such as timestamps and log levels, applies optional date-based filtering, and produces a concise summary report.

The project is intentionally kept simple to demonstrate readable, maintainable Python code without unnecessary frameworks or dependencies.

---

## Features

- Parse structured log entries from text files  
- Filter logs using start and end dates  
- Count log levels (`INFO`, `WARNING`, `ERROR`)  
- Extract and analyze response times (in milliseconds)  
- Generate a clean summary report in the terminal  
- Process large log files efficiently without loading them entirely into memory  

---

## Supported Log Format

Each log entry must follow this format:

YYYY-MM-DD HH:MM:SS LEVEL message

makefile
Copy code

Example:
2025-01-10 10:01:22 INFO Request completed in 245ms

yaml
Copy code

---

## Project Structure

python-log-file-analyzer/
│
├── analyzer/
│ ├── parser.py # Parses log lines into structured data
│ ├── date_filter.py # Filters logs by date range
│ ├── stats.py # Computes log statistics
│ ├── report.py # Prints summary output
│ └── init.py
│
├── sample_logs/
│ └── app.log
│
├── main.py # CLI entry point
├── README.md
├── requirements.txt
└── .gitignore

yaml
Copy code

---

## Usage

### Basic Run

```bash
python main.py sample_logs/app.log
Filter Logs by Date
bash
Copy code
python main.py sample_logs/app.log --start-date 2025-01-10 --end-date 2025-01-11
Example Output
pgsql
Copy code
Log Summary
--------------------
Total logs processed: 4
INFO: 2
WARNING: 1
ERROR: 1
Average response time: 245.00 ms
Technologies Used
Python 3

Python Standard Library (datetime, argparse, re)

No third-party dependencies are required.

Design Decisions
Uses only the Python standard library to keep the project lightweight and accessible

Reads log files line by line to support large files

Separates parsing, filtering, analysis, and reporting into clear modules

Omits timezone handling to keep the scope focused and beginner-friendly

