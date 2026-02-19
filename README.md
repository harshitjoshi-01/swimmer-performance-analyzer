# Swimmer Performance Analyzer

A Python-based data analysis project that processes swimmer timing data from text files and calculates performance statistics such as average time and formatted results.

This project demonstrates file handling, data parsing, time conversion, and statistical analysis using Python.

---

## Features

- Reads swimmer data from text files
- Extracts swimmer information (name, age, distance, stroke)
- Converts time values into hundredths of seconds
- Calculates average swim time using Python statistics module
- Converts average time back into readable minute:second format
- Uses clean and modular code with functions

---

## Example Input File

File name:
Abi-10-50m-Back.txt

File content:
39.01,37.45,38.22,37.98

---

## Example Output

Swimmer: Abi  
Age: 10  
Distance: 50m  
Stroke: Back  
Average Time: 0:38.17  

---

## How It Works

The program performs the following steps:

1. Reads swimmer data file
2. Extracts swimmer details from filename
3. Reads swim times from file
4. Converts times into hundredths of seconds
5. Calculates average performance using statistics module
6. Converts result back into readable time format

---

## Technologies Used

- Python
- File Handling
- Functions
- statistics module
- String manipulation

---

## Project Structure

swimmer-performance-analyzer/

├── swimdata/  
│   └── Abi-10-50m-Back.txt  

├── main.py  

└── README.md  

---

## Skills Demonstrated

- Python programming
- Data processing
- File handling
- Problem solving
- Statistical analysis
- Clean code structure

---

## Author

Harshit Joshi

---

## Future Improvements

- Support multiple swimmers
- Add leaderboard ranking
- Detect fastest swimmer
- Add graphical visualization
- Add user interface
