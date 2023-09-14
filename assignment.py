
import hashlib
import random
import string

# Dictionary to store mappings between hashed and original URLs
url_mappings = {}

def generate_random_string(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def hash_url(url):
    """Hash a URL using SHA-256."""
    sha256 = hashlib.sha256()
    sha256.update(url.encode('utf-8'))
    return sha256.hexdigest()

def shorten_url(original_url):
    """Shorten a URL by hashing and storing it."""
    hashed_url = hash_url(original_url)
    token = generate_random_string()
    
    # Store the mapping between token and original URL
    url_mappings[token] = original_url
    short_url = "https://yourdomain.com/%s"%(token)
    
    return short_url

def resolve_url(token):
    """Resolve a hashed URL back to the original URL."""
    original_url = url_mappings.get(token)
    if original_url:
        return original_url
    else:
        return None

# Example usage:
original_url = os.getenv('ORG_URL')
shortened_url = shorten_url(original_url)
print(f"Shortened URL: {shortened_url}")

# Simulate a click on the shortened URL
resolved_url = resolve_url(shortened_url.split("/")[-1])
if resolved_url:
    print("Resolved URL: ",resolved_url)
else:
    print("URL not found.")
