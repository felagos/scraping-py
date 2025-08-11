import requests
from urllib.parse import urlparse
from .dns_resolver import get_ip_from_url


def make_ip_based_request(url: str) -> requests.Response:
    try:
        ip_address = get_ip_from_url(url)

        parsed_url = urlparse(url)

        ip_based_url = f"{parsed_url.scheme}://{ip_address}{parsed_url.path}"
        if parsed_url.query:
            ip_based_url += f"?{parsed_url.query}"
        if parsed_url.fragment:
            ip_based_url += f"#{parsed_url.fragment}"

        headers = {
            "Host": parsed_url.netloc,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        }

        print(f"Making IP-based request: {url} -> {ip_based_url}")
        print(f"Host header: {headers['Host']}")

        response = requests.get(ip_based_url, headers=headers)
        return response

    except Exception as e:
        print(f"IP-based request failed for {url}: {e}")
        print(f"Falling back to regular URL request")
        return requests.get(url)
