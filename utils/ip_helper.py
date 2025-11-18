import ipaddress

def convert_range_to_cidr(start_ip: str, end_ip: str):
    start = ipaddress.ip_address(start_ip)
    end = ipaddress.ip_address(end_ip)

    if start > end:
        raise ValueError("Start IP cannot be greater than End IP")

    cidrs = ipaddress.summarize_address_range(start, end)
    return [str(c) for c in cidrs]
