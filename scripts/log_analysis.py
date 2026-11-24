from pathlib import Path

log_file = Path(__file__).resolve().parent.parent / "logs/sample.log"
failed_attempts = 0

with open(log_file, "r") as file:
    for line in file:
        if "Failed login" in line:
            print(line.strip())
            failed_attempts += 1

print(f"Total failed login attempts: {failed_attempts}")