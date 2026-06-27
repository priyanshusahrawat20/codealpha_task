# Email Extractor

import re

input_file = "input.txt"
output_file = "emails.txt"

# Read text from file
file = open(input_file, "r")
text = file.read()
file.close()

# Extract email addresses
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

# Save emails to another file
file = open(output_file, "w")

for email in emails:
    file.write(email + "\n")

file.close()

print("Email extraction completed!")
print("Total emails found:", len(emails))
print("Emails saved in", output_file)