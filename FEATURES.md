# Features of `liforra_utils`

`liforra_utils` is a utility library providing easy-to-use logging and configuration management, along with some fun extras.

## Table of Contents

- [Package Information](#package-information)
- [Logging](#logging)
- [Configuration](#configuration)
- [Utilities](#utilities)
- [Deprecations](#deprecations)

---

## Package Information

- **Author**: Liforra
- **Website**: https://liforra.de
- **Recommended Import**: `import liforra_utils as lutils` (or just `import liforra_utils`)

---

## Logging

The library provides a wrapper around Python's logging module with support for colors (via `coloredlogs` or ANSI codes) and file output.

### Usage

The recommended way to log messages is using the method syntax on the `log` object.

```python
from liforra_utils import log, set_log_level, set_log_file

# Set the log level (default is "info")
# Levels: "debug", "info", "warn", "err", "fatal"
set_log_level("debug")

# Optional: Log to a file
set_log_file("app.log")

# Log messages
log.debug("This is a debug message")
log.info("System is running smoothly")
log.warn("Something might be wrong")
log.err("An error occurred")

# 'fatal' logs the message and raises an Exception
try:
    log.fatal("Critical failure!")
except Exception as e:
    print(f"Caught fatal error: {e}")
```

### Deprecated Logging Syntax

Calling `log` as a function is **deprecated** and will be removed in version 0.3.0.

```python
# DEPRECATED
log("info", "This is the old way")
```

### Colors

The `color` dictionary provides ANSI escape codes for styling text in terminals.

```python
from liforra_utils import color

print(f"{color['red']}This is red text{color['reset']}")
print(f"{color['bg_blue']}This has a blue background{color['reset']}")
```

---

## Configuration

The `config` object manages application settings using a persistent file. It supports **TOML**, **INI**, **JSON**, and **YAML** formats (autodetected in that order).

### Key Concepts

- **Dot Notation**: Keys are accessed using dot notation (e.g., `section.key`), which maps to nested dictionaries or INI sections.
- **Auto-Saving**: Setting a value automatically writes it to the config file.
- **Auto-Defaulting**: Getting a value that doesn't exist (but providing a default) will automatically create that entry in the config file.

### Usage

```python
from liforra_utils import config

# 1. Setup (Optional)
config.set_path("./config")   # Default: "./"
config.set_name("my_app")     # Default: "config"

# 2. Setting Defaults
# This creates the config file if it doesn't exist.
config.set_defaults({
    "app": {
        "name": "My App",
        "debug": True
    },
    "database": {
        "host": "localhost",
        "port": 5432
    }
})

# 3. Reading Values
host = config.get("database.host")
# OR using dictionary syntax
port = config["database.port"]

# Reading with a default (updates file if key is missing)
timeout = config.get("network.timeout", default=30) 

# 4. Writing Values
config.set("app.debug", False)
# OR using dictionary syntax
config["database.host"] = "127.0.0.1"

# 5. Iterating
for key in config:
    print(f"{key}: {config[key]}")
```

---

## Utilities

### Maybe

`Maybe` is a chaotic utility that randomly evaluates to `True` or `False`.

```python
from liforra_utils import Maybe

if Maybe:
    print("Luck is on your side!")
else:
    print("Not this time.")
```

---

## Deprecations

### `lutils` Package Alias

Importing the package as `lutils` (the module name, not the variable alias) is deprecated.

**Deprecated:**
```python
import lutils  # Warns user
lutils.log.info("Hello")
```

**Recommended:**
```python
import liforra_utils
liforra_utils.log.info("Hello")

# OR
import liforra_utils as lutils
lutils.log.info("Hello")
```

### `log()` Function Call

As mentioned in the Logging section, calling `log()` directly is deprecated.

**Deprecated:**
```python
log("info", "message")
```

**Recommended:**
```python
log.info("message")
```
