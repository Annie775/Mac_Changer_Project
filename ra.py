import random

def generate_random_mac():
    # Generate a random MAC address in the format 00:XX:XX:XX:XX:XX
    mac = [0x00, random.randint(0x00, 0x7f),  # Ensure it's locally administered
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: f"{x:02x}", mac))

# Example usage
random_mac = generate_random_mac()
print("Generated Random MAC Address:", random_mac)
