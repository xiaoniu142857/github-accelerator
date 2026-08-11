# GitHub Accelerator

`github-accelerator` is a small Windows utility that downloads the latest GitHub hosts mapping from `raw.hellogithub.com`, writes it to the system hosts file, and flushes DNS.

## What it does

- Downloads the current hosts content from the upstream source
- Replaces `C:\Windows\System32\drivers\etc\hosts`
- Flushes the local DNS cache with `ipconfig /flushdns`

## Requirements

- Windows
- Python 3
- Administrator privileges
- `requests`

Install the dependency:

```bash
pip install requests
```

## Usage

Run the script from an elevated terminal:

```bash
python main.py
```

## Notes

- This script overwrites your hosts file.
- If the write fails, rerun the terminal as Administrator.
- The upstream hosts source is `https://raw.hellogithub.com/hosts`.

