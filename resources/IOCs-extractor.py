# This code coocked By Malek Aldossary
import PyPDF2
import re

# Open the PDF file in read-binary mode
with open('threat_intelligence_report.pdf', 'rb') as f:
    # Create a PyPDF2 reader object
    pdf_reader = PyPDF2.PdfReader(f)

    # Extract text from all pages in the PDF
    report = ''
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        report += page.extract_text()

    # Extract IP addresses
    ip_addresses_obfuscated = re.findall(r'\b(?:\d{1,3}\[?\.\]?){3}\d{1,3}\b', report)
    ip_addresses_obfuscated = [ip.replace('[.]', '.') for ip in ip_addresses_obfuscated]

    ip_addresses_normal = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', report)

    ip_addresses = list(set(ip_addresses_normal + ip_addresses_obfuscated))

    # Extract domains
    domains_obfuscated = re.findall(r'[a-zA-Z0-9\-]+\[.\][a-zA-Z]{2,}', report)
    domains_obfuscated = [domain.replace('[.]', '.') for domain in domains_obfuscated]

    domains_normal = re.findall(r'[a-zA-Z0-9\-]+\.[a-zA-Z]{2,}', report)

    domains = list(set(domains_normal + domains_obfuscated))

    # Extract hashes
    hashes_md5 = re.findall(r'\b(?:[a-fA-F\d]{32})\b', report)
    hashes_sha1 = re.findall(r'\b(?:[a-fA-F\d]{40})\b', report)
    hashes_sha256 = re.findall(r'\b(?:[a-fA-F\d]{64})\b', report)
    hashes_sha512 = re.findall(r'\b(?:[a-fA-F\d]{128})\b', report)

    hashes = list(set(hashes_md5 + hashes_sha1 + hashes_sha256 + hashes_sha512))

    # Print the results
    if ip_addresses:
        print('IP addresses:', ip_addresses)
    else:
        print('No IP addresses found.')

    if domains:
        print('Domains:', domains)
    else:
        print('No domains found.')

    if hashes:
        print('Hashes:', hashes)
    else:
        print('No hashes found.')
