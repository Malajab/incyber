# This Code write by Malek Aldossary
import requests
import socket
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import ipaddress

# List of IPs or CIDR ranges to scan
with open('ips.txt', 'r') as file:
    ips = [line.strip() for line in file]

# Convert CIDR ranges to list of IPs
ip_list = []
for ip in ips:
    if "/" in ip:
        ip_list += [str(ip) for ip in ipaddress.IPv4Network(ip)]
    else:
        ip_list.append(ip)

# Function to check if port is open
def check_port(ip, port, timeout):
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.shutdown(socket.SHUT_RDWR)
        return True
    except:
        return False

# List of open IPs
open_ips = []

# Scan each IP for open ports
for ip in ip_list:
    print(f"Scanning {ip}...")
    open_ports = []
    for port in [80, 443]:
        if check_port(ip, port, timeout=2):
            open_ports.append(port)

    if open_ports:
        open_ips.append((ip, open_ports))
        print(f"{ip} is open on ports {open_ports}")
    else:
        print(f"{ip} has no open ports")

# List of IPs with "index of" in the title
index_of_ips = []

# Check if each open IP has "index of" in the title
for ip, ports in open_ips:
    print(f"Checking {ip}...")
    for port in ports:
        url = f"http://{ip}:{port}/"
        try:
            response = requests.get(url, timeout=2)
            soup = BeautifulSoup(response.text, "html.parser")
            if "index of" in soup.title.string.lower():
                index_of_ips.append(ip)
                print(f"{ip} has 'index of' in the title")
                break
        except:
            print(f"Could not connect to {ip}:{port}")

# Set up headless Chrome driver
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=chrome_options)

# Take screenshot of each IP with "index of" in the title
for ip in index_of_ips:
    print(f"Taking screenshot of {ip}...")
    try:
        driver.get(f"http://{ip}")
        driver.save_screenshot(f"{ip}.png")
        print(f"Screenshot saved as {ip}.png")
    except:
        print(f"Could not connect to {ip}")

# Quit Chrome driver
driver.quit()
