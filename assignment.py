
import hashlib
import random
import string

# Dictionary to store mappings between hashed and original URLs
url_mappings = {}

def generate_random_string(length=8):
    """Generate a random string of alphanumeric characters."""
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
    
    # Generate a unique token for the shortened URL (for privacy and security)
    token = generate_random_string()
    
    # Store the mapping between token and original URL
    url_mappings[token] = original_url
    
    return f"https://yourdomain.com/{token}"

def resolve_url(token):
    """Resolve a hashed URL back to the original URL."""
    original_url = url_mappings.get(token)
    if original_url:
        # Implement click tracking logic here
        # Log the click, update stats, etc.
        return original_url
    else:
        return None

# Example usage:
original_url = "https://www.youtube.com/watch?v=Ep_aoYCMhxM&t=15s"
# original_url="https://www.google.com/search?q=url+hashing+system&rlz=1C1GCEA_enIN1030IN1030&oq=url+hasing+&aqs=chrome.1.69i57j0i13i512j0i22i30l3j0i15i22i30j0i22i30l4.4907j0j15&sourceid=chrome&ie=UTF-8"
shortened_url = shorten_url(original_url)
print(f"Shortened URL: {shortened_url}")

# Simulate a click on the shortened URL
resolved_url = resolve_url(shortened_url.split("/")[-1])
if resolved_url:
    print(f"Resolved URL: {resolved_url}")
else:
    print("URL not found.")
