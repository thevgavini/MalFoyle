#!/usr/bin/env python3
import pyfiglet
import requests
import hashlib
import argparse
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich import box

console=Console()

def banner():
    pyfiglet.print_figlet("MalFoyle")
    print("Malicious file detection system.")
    print("\n")
    print("#> by Vivekananda Gavini (@thevgavini)")
    print("#> http://github.com/thevgavini")
    print("-"*40)
    print("\n")

def error():
    err_text=Text("An error has occured. Please refer to the help below:  ", style="bold red")
    console.print(err_text)
    print("\n")
    help()

def help():
    
    help = """usage: malfoyle.py [-h] [-f PATH] [-s SIGNATURE] [-o OUTPUT]

MalFoyle - Malicious file detection system

options:
  -h, --help            show this help message and exit
  -f PATH, --path PATH  Enter the file path.
  -s SIGNATURE, --signature SIGNATURE
                        Enter the file signature.
  -o OUTPUT, --output OUTPUT
                        Output to a file.
    """
    print(help)

try:

    def output(f_name, data):
        file_name=f"{f_name}.txt"
        try:
            with open(file_name, "w") as f:
                f.write(data)
        except:
            error()

    def get_verdicts(json_data):
        js = json_data
        verdicts=dict()
        output_str=""
        console = Console()
        header = Text("Verdicts (Vendor, Verdict): ", style="yellow")
        console.print(header)
        table = Table(show_header=False, box=box.SIMPLE)
        table.add_column(style="bold cyan")
        table.add_column(style="bright_red")

        for i in js["data"]:
            for j in i["vendor_intel"]:
                k=i["vendor_intel"][j]
                if type(k) == dict and "verdict" in k:
                    verdicts[j]=k["verdict"]
                if type(k) == dict and "detection" in k:
                    verdicts[j]=k["detection"]           
                if type(k) == list:
                    for l in k:
                        if "verdict" in l:
                            verdicts[j]=l["verdict"]
                        elif "detection" in l:
                            verdicts[j]=l["detection"]
        for i in verdicts:
            output_str+=f"{i.capitalize()}: {str(verdicts[i]).capitalize()}\n"
            table.add_row(i.capitalize(), str(verdicts[i]).capitalize())
            output_str+=""
        output_str+="\n"
        console.print(table)
        return output_str

    def get_yara(json_data):
        js=json_data
        yara=list()
        output_str=""
        console = Console()
        header = Text("Yara Rules: ", style="yellow")
        console.print(header)

        table = Table(show_header=False, box=box.SIMPLE)
        table.add_column(style="bold cyan")
        table.add_column(style="bright_white")
        for i in js["data"]:
            for j in i["yara_rules"]:
                yara.append(j)
        for i in yara:
            for s in i:
                output_str+=f"{s.capitalize()}: {i[s]}\n"
                table.add_row(s.capitalize(), str(i[s]))
                output_str+=""
            table.add_row("", "")
            output_str+="\n"
        console.print(table)
        return output_str

    def file_info(json_data):
        js = json_data
        info=list()
        output_str=""
        console = Console()
        header = Text("Info: ", style="yellow")
        console.print(header)
        table = Table(show_header=False, box=box.SIMPLE)
        table.add_column(style="bold cyan")
        table.add_column(style="bright_white")

        for i in js["data"]:
            info.append(i)
            break
        for i in info:
            for s in i:
                if s!="file_information":
                    output_str+=f"{s.capitalize()}: {i[s]}\n"
                    table.add_row(s.capitalize(), str(i[s]))
                    output_str+=""
                else:
                    break
            break
        console.print(table)    
        return output_str

    def handle_response(response, o):
        js = response
        if js["query_status"] == "ok":
            console = Console()
            heading = Text("Malware Detected!", style="bold red")
            console.print(heading)
            print("\n")
            output_str=""
            output_str+="Malware detected!\n"
            output_str+=f"{file_info(js)}\n"
            output_str+=f"{get_verdicts(js)}\n"
            output_str+=f"{get_yara(js)}\n"
            if o:
                output(o, output_str)
        else:
            console = Console()
            heading = Text("No malware detected. This file is likely safe.\n", style="bold green")
            console.print(heading)

    def make_post_request(url,data, o):
        response = requests.post(url, data=data)

        if response.status_code == 200:
            response=response.json()
            handle_response(response, o)

        else:
            print(f"POST request failed with status code: {response.status_code}")
            print("Response:")
            print(response.text)

    def calculate_file_hash(file_path, hash_algorithm='sha256', chunk_size=8192):

        hash_obj = hashlib.new(hash_algorithm)
        
        with open(file_path, 'rb') as f:
            while True:
                data = f.read(chunk_size)
                if not data:
                    break
                hash_obj.update(data)

        return hash_obj.hexdigest()

    def parse():

        parser=argparse.ArgumentParser(description="MalFoyle - Malicious file detection system")
        parser.add_argument("-f", "--path", nargs=1, help="Enter the file path.")
        parser.add_argument("-s", "--signature", nargs=1, help="Enter the file signature. ")
        parser.add_argument("-o", "--output", nargs=1, help="Output to a file.")
        args=parser.parse_args()
        f=args.path[0] if args.path else False
        o=args.output[0] if args.output else False
        s=args.signature[0] if args.signature else False
        return f,o,s

    def main():
        banner()
        f,o,s=parse()
        if f!=False or s!=False:
            if f:
                hash_value = calculate_file_hash(f)
            elif s:
                hash_value = s
                table = Table(show_header=False, box=box.SIMPLE)
                table.add_column(style="bold cyan")
                table.add_column(style="bright_white")
                table.add_row("Hash Entered", hash_value)
                console.print(table)
            url = 'https://mb-api.abuse.ch/api/v1/'
            data = {'query': 'get_info', 'hash': ''}
            data['hash'] = hash_value
            make_post_request(url, data, o)
        else:
            error()

except Exception as e:
    error()

main()