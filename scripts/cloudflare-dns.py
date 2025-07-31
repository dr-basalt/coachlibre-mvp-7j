#!/usr/bin/env python3
import requests
import json
import sys
import argparse
import os
from typing import Dict, List, Optional

class CloudflareDNSManager:
    def __init__(self, api_token: str):
        self.api_token = api_token
        self.base_url = "https://api.cloudflare.com/client/v4"
        self.headers = {
            'Authorization': f'Bearer {api_token}',
            'Content-Type': 'application/json'
        }
    
    def get_zone_id(self, domain: str) -> str:
        """Get zone ID for a domain"""
        zone_name = '.'.join(domain.split('.')[-2:])
        
        response = requests.get(
            f'{self.base_url}/zones?name={zone_name}',
            headers=self.headers
        )
        
        if not response.ok:
            raise Exception(f"Failed to get zones: {response.text}")
        
        zones = response.json()['result']
        if not zones:
            raise Exception(f"Zone {zone_name} not found")
        
        return zones[0]['id']
    
    def create_dns_record(self, domain: str, ip: str, record_type: str = 'A', proxied: bool = True) -> Dict:
        """Create DNS record"""
        zone_id = self.get_zone_id(domain)
        
        dns_data = {
            'type': record_type,
            'name': domain,
            'content': ip,
            'ttl': 300,
            'proxied': proxied
        }
        
        response = requests.post(
            f'{self.base_url}/zones/{zone_id}/dns_records',
            headers=self.headers,
            json=dns_data
        )
        
        if response.ok:
            result = response.json()['result']
            print(f"✅ DNS record created: {domain} -> {ip}")
            return result
        else:
            print(f"❌ Failed to create DNS record: {response.text}")
            return None
    
    def delete_dns_record(self, domain: str) -> bool:
        """Delete DNS record"""
        zone_id = self.get_zone_id(domain)
        
        # First, find the record
        response = requests.get(
            f'{self.base_url}/zones/{zone_id}/dns_records?name={domain}',
            headers=self.headers
        )
        
        if not response.ok:
            print(f"❌ Failed to find DNS record: {response.text}")
            return False
        
        records = response.json()['result']
        if not records:
            print(f"⚠️ DNS record {domain} not found")
            return False
        
        # Delete the record
        record_id = records[0]['id']
        response = requests.delete(
            f'{self.base_url}/zones/{zone_id}/dns_records/{record_id}',
            headers=self.headers
        )
        
        if response.ok:
            print(f"✅ DNS record deleted: {domain}")
            return True
        else:
            print(f"❌ Failed to delete DNS record: {response.text}")
            return False
    
    def create_tenant_dns(self, tenant_domain: str, ip: str) -> List[Dict]:
        """Create all DNS records for a tenant"""
        records = []
        
        # Main domain
        records.append(self.create_dns_record(tenant_domain, ip, proxied=True))
        
        # API subdomain
        records.append(self.create_dns_record(f"api.{tenant_domain}", ip, proxied=True))
        
        # AI subdomain
        records.append(self.create_dns_record(f"ai.{tenant_domain}", ip, proxied=True))
        
        # Workflows subdomain
        records.append(self.create_dns_record(f"workflows.{tenant_domain}", ip, proxied=True))
        
        # Meeting subdomain (not proxied for WebRTC)
        records.append(self.create_dns_record(f"meet.{tenant_domain}", ip, proxied=False))
        
        return [r for r in records if r is not None]

def main():
    parser = argparse.ArgumentParser(description='Manage Cloudflare DNS records')
    parser.add_argument('--action', required=True, choices=['create', 'delete', 'create-tenant'])
    parser.add_argument('--domain', required=True, help='Domain name')
    parser.add_argument('--ip', help='IP address')
    parser.add_argument('--api-token', help='Cloudflare API token')
    
    args = parser.parse_args()
    
    # Get API token
    api_token = args.api_token or os.environ.get('CLOUDFLARE_API_TOKEN')
    if not api_token:
        raise Exception("CLOUDFLARE_API_TOKEN environment variable or --api-token required")
    
    dns_manager = CloudflareDNSManager(api_token)
    
    if args.action == 'create':
        if not args.ip:
            raise Exception("--ip required for create action")
        dns_manager.create_dns_record(args.domain, args.ip)
    
    elif args.action == 'delete':
        dns_manager.delete_dns_record(args.domain)
    
    elif args.action == 'create-tenant':
        if not args.ip:
            raise Exception("--ip required for create-tenant action")
        dns_manager.create_tenant_dns(args.domain, args.ip)

if __name__ == "__main__":
    main()
