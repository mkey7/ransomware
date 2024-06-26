cd /home/ransomwatch
data >> /home/ransom.log
python3 ransomwatch.py scrape >> /home/ransom.log
python3 ransomwatch.py parse >> /home/ransom.log
python3 get-country.py >> /home/ransom.log
