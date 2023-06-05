import sys

message = f"Hello, {sys.argv[1]}!"

# Print the message to stdout, which Greengrass saves in a log file.
print(message)
