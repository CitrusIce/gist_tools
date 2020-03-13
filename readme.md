# gist_tools

a python tools to upload file to github gist

## requirements

a github token having gists scope access

settings -> developer settings -> personal access token -> generate new token -> select gists and generate

copy the token and  

```bash
echo <token> > gist_token
```

## usage

```
usage: gist.py [-h] [-n N] [-b] filename

positional arguments:
  filename    filename to upload

optional arguments:
  -h, --help  show this help message and exit
  -n N        specify the filename to use
  -b          base64 encode
```