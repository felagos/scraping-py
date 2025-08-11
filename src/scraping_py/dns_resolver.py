import socket
from urllib.parse import urlparse


def get_ip_from_url(url):
    """
    Given a URL, returns its IP address.

    Args:
        url (str): The URL to resolve (e.g., 'https://www.google.com' or 'google.com')

    Returns:
        str: The IP address of the URL

    Raises:
        socket.gaierror: If the hostname cannot be resolved
        ValueError: If the URL is invalid
    """
    try:
        # Parse the URL to extract the hostname
        parsed_url = urlparse(url)

        # If no scheme is provided, assume it's just a hostname
        if parsed_url.netloc:
            hostname = parsed_url.netloc
        elif parsed_url.path and not parsed_url.scheme:
            hostname = parsed_url.path
        else:
            raise ValueError("Invalid URL format")

        # Remove port number if present
        hostname = hostname.split(":")[0]

        # Resolve hostname to IP address
        ip_address = socket.gethostbyname(hostname)
        return ip_address

    except socket.gaierror as e:
        raise socket.gaierror(f"Failed to resolve hostname: {e}")
    except Exception as e:
        raise ValueError(f"Error processing URL: {e}")
