# MalFoyle - Malicious File Detection System

MalFoyle is an open-source Command Line Interface (CLI) tool developed in Python for detecting malicious files using hash-based queries against a popular malware database. It provides key information about the file, including vendor verdicts and YARA rules, allowing users to identify potentially harmful files quickly and efficiently.

## Features

- Calculate and retrieve SHA256 hash of a given file.
- Query a file hash against a well-known malware database.
- Display detailed information about the file, including vendor verdicts and YARA rules.
- Option to output the results to a text file.
- Easy global installation using the provided installer script.

## Installation

Before installing MalFoyle, make sure you have Python 3 and pip3 installed on your system.

1. Download the repository from GitHub:

   ```bash
   git clone https://github.com/thevgavini/MalFoyle.git
   cd MalFoyle
   sudo bash installer.sh`
This will install the required dependencies, make the script executable, and create a symbolic link for easy access.

## Usage

To use MalFoyle, simply open your terminal and type `malfoyle` followed by the desired options.

### Command Line Options

-   `-h`, `--help`: Display help message and exit.
-   `-f PATH`, `--path PATH`: Specify the file path to be analyzed.
-   `-s SIGNATURE`, `--signature SIGNATURE`: Enter the file hash directly.
-   `-o OUTPUT`, `--output OUTPUT`: Save the analysis results to a text file.

### Examples

1.  Analyze a file using its path:
	`malfoyle -f /path/to/your/file` 

2.  Analyze a file using its hash:
	`malfoyle -s <file_hash>` 

3.  Analyze a file and save results to a text file:
	`malfoyle -f /path/to/your/file -o analysis_results`
    `malfoyle -s <file_hash> -o analysis_result`
	
	 

## Future Scope and Applications

MalFoyle, though currently a standalone CLI tool, holds significant potential for integration into more complex systems. Here are a few potential future directions and applications:

-   **Security Automation:** MalFoyle could be integrated into automated security pipelines to scan files as part of continuous integration (CI) and continuous deployment (CD) processes.
-   **Threat Intelligence Platforms:** MalFoyle's capabilities could be leveraged within larger threat intelligence platforms, enhancing their ability to detect and respond to new malware samples.
-   **Endpoint Security Solutions:** Integration with endpoint security solutions could enhance their file scanning capabilities, providing an additional layer of defense against malware.
-   **Incident Response:** MalFoyle could be used as a quick and reliable tool during incident response scenarios, aiding in the rapid assessment of potentially malicious files.

## Acknowledgments

MalFoyle was created by [Vivekananda Gavini](http://github.com/thevgavini) as an open-source project. If you find this tool helpful, consider leaving a star on the GitHub repository or contributing to its development.

## Disclaimer

MalFoyle is provided for educational and informational purposes only. The effectiveness of this tool may vary, and it should not be solely relied upon for critical security decisions. Always exercise caution and use additional security measures when handling potentially malicious files.

## License

MalFoyle is released under the [MIT License](https://github.com/thevgavini/MalFoyle/blob/main/LICENSE).