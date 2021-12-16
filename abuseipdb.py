import requests
import os
import json

# Relevance in Days
days = '30'

# IP list Defined in file called 'nobueno.ip'
f = open('nobueno.ip', 'r')
ips = f.readlines()

for i in ips:
    headers = {
        'Key': '{YOUR API KEY HERE}',
        'Accept': 'application/json',
    }
    params = {
        'maxAgeInDays': days,
        'ipAddress': i.strip(),
        'verbose': ''
    }

    r = requests.get('https://api.abuseipdb.com/api/v2/check',
                     headers=headers, params=params)
    response = r.json()
    print("IP: " + i.strip())
    print("Total Reports: " + str(response['data']['totalReports']))
    print("Abuse Confidence: " +
          str(response['data']['abuseConfidenceScore']) + "%")
    print("Country: " + str(response['data']['countryName']))
    print("ISP: " + str(response['data']['isp']))
    print("Domain: " + str(response['data']['domain']))
    print()
