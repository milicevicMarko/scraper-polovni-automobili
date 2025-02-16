import re


def read_and_split_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content.split()


def is_valid_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        # domain...
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None


def get_batch(file_path):
    try:
        urls = read_and_split_file(file_path)
        valid_urls = [url for url in urls if is_valid_url(url)]
        return valid_urls
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == '__main__':
    file_path = 'batch.txt'
    result = get_batch(file_path)
    print(result)
