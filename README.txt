* Collect all the test submissions in current directory.
* The filenames should end with '.c'. The case of the file doesn't matter.
* The correct test cases and results have to be set in "main.c".
* Run the script "python check.py".
* The results are available in 'results.json' in JSON format.

How it works?
* The script compiles all the submissions available one by one.
* For each submission, "main.c" returns the total_score.
* The corresponding data is maintained.
* At the end, results are written to "results.json".


Configuration Options:
* Test cases and results in "main.c".
* Timeout relaxation in "check.py".
