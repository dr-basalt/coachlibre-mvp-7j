#!/usr/bin/env python3
import requests
import json
import sys
import argparse

def create_dns_record(domain, ip, api_token):
    """Create DNS A record in Cloudflare"""
    
    # Get zone ID
    zone_name = '.'.join(domain.split('.')[-2:])
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json'
    }
    
    zones_response = requests.get(
        f'https://api.cloudflare.com/client/v4/zones?name={zone_name}',
        headers=headers
    )
    
    if not zones_response.ok:
        raise Exception(f"Failed to get zones: {zones_response.text}")
    
    zones = zones_response.json()['result']
    if not zones:
        raise Exception(f"Zone {zone_name} not found")
    
    zone_id = zones[0]['id']
    
    # Create DNS record
    dns_data = {
        'type': 'A',
        'name': domain,
        'content': ip,
        'ttl': 300
    }
    
    response = requests.post(
        f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records',
        headers=headers,
        json=dns_data
    )
    
    if response.ok:
        print(f"✅ DNS record created: {domain} -> {ip}")
    else:
        print(f"❌ Failed to create DNS record: {response.text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--action', required=True, choices=['create', 'delete'])
    parser.add_argument('--domain', required=True)
    parser.add_argument('--ip', required=True)
    args = parser.parse_args()
    
    api_token = os.environ.get('CLOUDFLARE_API_TOKEN')
    if not api_token:
        raise Exception("CLOUDFLARE_API_TOKEN environment variable required")
    
    if args.action == 'create':
        create_dns_record(args.domain, args.ip, api_token)
