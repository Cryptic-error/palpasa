import requests
from bs4 import BeautifulSoup
import csv

def make_request(page_index):
    url = 'https://www.bolpatra.gov.np/egp/searchBidDashboardHomePage'
    headers = {
        'Host': 'www.bolpatra.gov.np',
        'Cookie': 'JSESSIONID=3C0509D5F5EB8C18B290FA482FBA5885.node2',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://www.bolpatra.gov.np/egp/searchOpportunity',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Te': 'trailers',
        'Connection': 'keep-alive'
    }

    params = {
        'bidSearchTO.title': '',
        'bidSearchTO.ifbNO': '',
        'bidSearchTO.procurementCategory': '-1',
        'bidSearchTO.procurementMethod': '-1',
        'bidSearchTO.publicEntityTitle': '',
        'bidSearchTO.publicEntity': '0',
        'parentPE': '0',
        'null_widget': '',
        'bidSearchTO.childPEId': '-1',
        'bidSearchTO.NoticePubDateText': '',
        'bidSearchTO.lastBidSubmissionDateText': '',
        'bidSearchTO.contractType': '-1',
        'currentPageIndexInput': (page_index +1),
        'pageSizeInput': '30',
        'pageActionInput': 'goto',
        'tenderId': '',
        'addNewJV': 'false',
        'currentPageIndex': page_index,
        'pageSize': '30',
        'pageAction': '',
        'totalRecords': '133011',
        'startIndex': str((page_index - 1) * 30),
        'numberOfPages': '4434',
        'isNextAvailable': 'true',
        'isPreviousAvailable': 'true',
        '_': '1719166577952'
    }

    try:
        response = requests.get(url, headers=headers, params=params, verify=False)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the table with the id 'dashBoardBidResult'
        table = soup.find('table', {'id': 'dashBoardBidResult'})
        
        if table:
            # Extract the table headers
            headers = []
            for th in table.find_all('th'):
                headers.append(th.get_text(strip=True))
            
            # Extract the table rows
            rows = []
            for tr in table.find_all('tr')[1:]:  # Skip the header row
                cells = tr.find_all(['td', 'th'])
                row = [cell.get_text(strip=True) for cell in cells]
                rows.append(row)
            
            return headers, rows
        else:
            print(f"No table found on page {page_index}")
            return None, None
    except requests.exceptions.RequestException as e:
        print(f"Request failed for page {page_index}: {e}")
        return None, None

# Example usage: Fetch data for pages 1 to 10 and save to CSV
all_headers = []
all_rows = []

for page_index in range(1, 434):
    print(f"Fetching data for page {page_index}...")
    headers, rows = make_request(page_index)
    if headers and rows:
        if not all_headers:
            all_headers = headers  # Use headers from the first page
        all_rows.extend(rows)
# Write data to CSV file
csv_filename = 'bid_results.csv'
with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(all_headers)  # Write headers
    writer.writerows(all_rows)  # Write rows

print(f"Data has been written to {csv_filename}")

