# Lab 9: Logging

## Create directory structure

```bash
mkdir -p ~/python/labs/lab09
```

## Change to lab09 directory

```bash
cd ~/python/labs/lab09
```

## Create logging\_example.py

```bash
cat >> logging_example.py << EOF
import logging

# Configure logging
logging.basicConfig(
    filename="app.log",          # log file name
    filemode="w",                # overwrite on each run
    level=logging.DEBUG,         # log level
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Different log levels
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

print("Logs have been written to app.log")
EOF
```

## Run in venv

```bash
python3 -m venv myenv
source myenv/bin/activate
```

### Create requirements.txt if required and run it

(logging is built into Python, so no extra requirements needed)

## Run the Python script

```bash
python logging_example.py
```

**Expected Output (console):**

```
Logs have been written to app.log
```

**Expected app.log content:**

```
2025-09-05 13:30:00,123 - DEBUG - This is a debug message
2025-09-05 13:30:00,124 - INFO - This is an info message
2025-09-05 13:30:00,124 - WARNING - This is a warning message
2025-09-05 13:30:00,124 - ERROR - This is an error message
2025-09-05 13:30:00,124 - CRITICAL - This is a critical message
```

