import socket
import requests

def device_info(ip):
  # Create a dictionary to store the results
  results = {}

  # Try to send an HTTP request to the device
  try:
    r = requests.get("http://" + ip)

    # If the request is successful, get the device's operating system and software versions
    results["Operating System"] = r.headers["Server"]
    results["Software"] = r.headers["X-Powered-By"]
  except:
    # If the request fails, set the operating system and software to "Unknown"
    results["Operating System"] = "Unknown"
    results["Software"] = "Unknown"

  # Create a socket object
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # Set a timeout for the socket
  s.settimeout(5)

  # Try to connect to the device on each of the common ports
  for port in [21, 22, 23, 25, 80, 443, 3389]:
    try:
      s.connect((ip, port))

      # If the connection is successful, add the open port to the results
      results[port] = "Open"
    except:
      # If the connection fails, move on to the next port
      continue

  # Close the socket
  s.close()

  # Return the results
  return results

# Get the IP address from the user
ip = input("Enter an IP address: ")

# Call the device_info function to gather information about the device
results = device_info(ip)

# Print the results
for key, value in results.items():
  print(key + ": " + value)
