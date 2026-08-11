import requests
import os,sys
import shutil
import logging
import subprocess

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

def update_github_hosts(url:str=r"https://raw.hellogithub.com/hosts",hosts_path:str=r"C:/Windows/System32/drivers/etc/hosts")->None:
    '''
    Updates the system's hosts file with the latest GitHub hosts.
    
    - `url`: The URL to download the latest GitHub hosts file. Default is "https://raw.hellogithub.com/hosts".
    - `hosts_path`: The path to the system's hosts file. Default is "C:/Windows/System32/drivers/etc/hosts".
    '''

    try:
        logging.info("Downloading the latest GitHub hosts file...")
        res=requests.get(url,timeout=10)
        res.raise_for_status()
        hosts=res.text
        logging.info("Downloading succeeded.")
        logging.info("Updating system hosts file...")

        with open(hosts_path,"w",encoding="utf-8") as file:
            file.write(hosts)
        logging.info("Updation succeeded.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
    except PermissionError:
        logging.error("No permission to write to the hosts file. Please run the script as an administrator.")
    except Exception as e:
        logging.error(f"Runtime Error: {e}")
    else:
        subprocess.run(r"ipconfig /flushdns")
        logging.info("Flushed DNS cache successfully.")

if __name__=="__main__":
    update_github_hosts()