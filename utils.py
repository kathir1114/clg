def generate_file(data, filename):
    with open(filename, 'w') as f:
        for key, value in data.items():
            f.write(f"{key}: {value}\n")
    return filename
