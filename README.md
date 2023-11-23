# aisay
aisay means AI Say

## Description
This tool generates speech from text using OpenAI's speech API and plays it back.

## Installation

```bash
git clone https://github.com/vaderyang/aisay
```

To install the required dependencies, run:
```bash
pip install -r requirements.txt
```

## Usage
Run the script with the following command:
Setup your openai key
```bash
export OPENAI_API_KEY=sk-***********  
```
You may alternatively modify aisay.py direclty to put your openai key in client = OpenAI(api_key="sk-****") in a safe machine environment.

```bash
python3 aisay.py [arguments]
```

Arguments:
- string: Text to say
- `-v/--voice`: Voice model to use (default: onyx)
- `-f/--file`: Text file to read input from
- `-o/--output`: Output file path for the generated speech
- `-r/--rate`: Playback speed of the generated speech (0.25 to 4.0)

## Example
```bash
python3 aisay.py Hello World
```

```bash
python3 aisay.py -v echo -o helloworld.mp3 Hello Again!
```
## Extra Installation Options
If you want to make it as a system command for easier access, run:
```bash
sudo cp aisay.py /usr/local/bin/aisay
aisay Hello World
```
if this doesn't work, find out the right path to save your aisay file by 
```bash
echo $PATH
```

## NOTICE
You may need proxy to connect to the OpenAI API server through export https_proxy environment variable.

## License
BSD 2-Clause 
