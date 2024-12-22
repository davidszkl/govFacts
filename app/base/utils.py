def read_secret(secret_name):
    secret_path = f"/run/secrets/{secret_name}"
    try:
        with open(secret_path) as f:
            return f.read().strip()
    except FileNotFoundError:
        return None
    