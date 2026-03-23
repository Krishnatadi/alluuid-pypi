![pypi Version](https://img.shields.io/pypi/v/alluuid)
![GitHub Issues](https://img.shields.io/github/issues/Krishnatadi/alluuid-pypi)

# AllUUID

**AllUUID** is a powerful Python package designed to generate various types of UUIDs (Universally Unique Identifiers), including UUID v1, v4, v7, GUIDs, and deterministic UUIDs based on email addresses. Perfect for use in databases, session tokens, distributed systems, and applications requiri
ng consistent, unique identifiers. This tool is ideal for developers looking to create unique identifiers for databases, session tokens, or any other use cases where uniqueness is critical.


This tool is ideal for developers looking to create unique identifiers for various applications, including:
- Databases
- Session tokens
- Resource identifiers
- Any other use cases where uniqueness is critical


## Installation
To install this package:

```bash
pip install alluuid
```

After installation, you'll have access to both the Python library and the `alluuid` command-line tool.


## Features

- **Multiple UUID Versions**: Generate UUIDs of version 1, 4, and 7.
- **GUID Generation**: Create standard GUIDs.
- **Batch Generation**: Generate multiple UUIDs in one call.
- **Custom UUID Generation**: Create UUIDs based on custom object details.
- **Consistent UUID for Emails**: Generate a consistent UUID for the same email address.
- **Nil UUID Generation**: Generate a UUID with all bits set to zero.



## Command-Line Interface (CLI)

AllUUID includes a powerful command-line interface that makes UUID generation incredibly easy. Simply install the package and use the `alluuid` command from your terminal!

### Quick Start

```bash
# Generate a random UUID v4
alluuid v4

# Generate a time-based UUID v1
alluuid v1

# Generate a timestamp-based UUID v7
alluuid v7

# Get help for any command
alluuid --help
```

### CLI Commands Overview

| Command | Description | Example |
|---------|-------------|---------|
| `alluuid v1` | Generate UUID v1 (time-based) | `alluuid v1` |
| `alluuid v4` | Generate UUID v4 (random) | `alluuid v4` |
| `alluuid v7` | Generate UUID v7 (timestamp-based) | `alluuid v7` |
| `alluuid nil` | Generate Nil UUID (all zeros) | `alluuid nil` |
| `alluuid guid` | Generate GUID (Microsoft format) | `alluuid guid` |
| `alluuid batch [--count N]` | Generate multiple UUIDs (2-50) | `alluuid batch --count 10` |
| `alluuid email EMAIL` | Generate UUID from email (deterministic) | `alluuid email user@example.com` |
| `alluuid validate UUID EMAIL` | Validate UUID matches email | `alluuid validate <uuid> user@example.com` |
| `alluuid custom PATTERN` | Generate custom UUID by pattern (x=hex, d=digit, others=literal) | `alluuid custom 'BANK-xxxx-dddd'` |
| `alluuid info` | Display CLI information | `alluuid info` |

### CLI Usage Examples

#### Basic UUID Generation
```bash
# Generate single UUIDs
$ alluuid v4
UUID v4: a3f5c2e1-9b3d-4k2m-n5p6-r7s8t9u0v1w2
Generated successfully

$ alluuid v1
UUID v1: 2a3b4c5d-6e7f-1a2b-3c4d-5e6f7a8b9c0d
Generated successfully

$ alluuid v7
UUID v7: f1a2b3c4-d5e6-7f8a-9b0c-1d2e3f4a5b6c
Generated successfully
```

#### Batch Generation
```bash
# Generate 10 UUIDs at once
$ alluuid batch --count 10
Generated 10 UUID v4s:
  1. a1b2c3d4-e5f6-4g7h-8i9j-0k1l2m3n4o5p
  2. q1r2s3t4-u5v6-4w7x-8y9z-0a1b2c3d4e5f
  ...
Batch generation successful

# Short form
$ alluuid batch -c 5
```

#### Email-Based UUID
```bash
# Generate a deterministic UUID from email
$ alluuid email john.doe@example.com
Email-based UUID: 7a3f5c2e-1b9d-4k2m-n5p6-r7s8t9u0v1w2
Email: john.doe@example.com
Generated successfully

# Useful for user identification - same email always produces same UUID!
```

#### Validate UUID
```bash
# Validate if UUID matches an email
$ alluuid validate 7a3f5c2e-1b9d-4k2m-n5p6-r7s8t9u0v1w2 john.doe@example.com
Valid: UUID matches email 'john.doe@example.com'

# Invalid case
$ alluuid validate wrong-uuid-1234 john.doe@example.com
Invalid: UUID does NOT match email 'john.doe@example.com'
```

#### Custom Pattern UUID
Custom UUIDs let you generate identifiers with your own format and structure. The pattern system is simple and flexible:

**Pattern Symbols:**
- `x` = hex digit (0-9, a-f)
- `d` = decimal digit (0-9)
- **Any other character** = literal text

This simple design means you can use UPPERCASE letters, numbers, and any separators freely as literals!

```bash
# Business-friendly format with prefix
$ alluuid custom 'BANK-xxxx-dddd'
Custom UUID: BANK-57c8-9233
Pattern: BANK-xxxx-dddd
Generated successfully

# Invoice ID with 6 hex characters
$ alluuid custom 'INV-xxxxxx'
Custom UUID: INV-a1340a
Pattern: INV-xxxxxx
Generated successfully

# User ID with underscore separators
$ alluuid custom 'ID_dddd_dddd'
Custom UUID: ID_7524_6407
Pattern: ID_dddd_dddd
Generated successfully

# Custom separators (dots, pipes, etc.)
$ alluuid custom 'REF.xxxx.dddd'
Custom UUID: REF.5a3c.1729
Pattern: REF.xxxx.dddd
Generated successfully

# Mostly literal, just one random part
$ alluuid custom 'USER-code-xxxx'
Custom UUID: USER-code-b482
Pattern: USER-code-xxxx
Generated successfully
```

**Pattern Design Benefits:**
- Use UPPERCASE letters freely as literals
- Any separators work naturally (-, _, ., |, etc.)
- No placeholder conflicts
- What you write is what you get (mostly)
- Easy to remember: just x and d

#### Information Command
```bash
$ alluuid info
AllUUID CLI Information

About:
  AllUUID is a comprehensive UUID generation library for Python.
  It supports multiple UUID versions: v1, v4, v7, GUID, and custom patterns.

Available Commands:
  v1              - Generate UUID v1 (time-based)
  v4              - Generate UUID v4 (random)
  v7              - Generate UUID v7 (timestamp-based)
  nil             - Generate Nil UUID (all zeros)
  guid            - Generate GUID
  batch [COUNT]   - Generate multiple UUIDs (2-50)
  email EMAIL     - Generate UUID from email
  validate UUID   - Validate UUID against email
  custom PATTERN  - Generate custom UUID by pattern
  info            - Show this information
```

### Integration with Scripts

The CLI is perfect for use in shell scripts and automation:

```bash
# Generate a UUID and store it in a variable
NEW_UUID=$(alluuid v4)
echo "Generated UUID: $NEW_UUID"

# Generate multiple UUIDs for batch operations
alluuid batch --count 100 > uuids.txt

# Generate an ID for a user
USER_EMAIL="newuser@company.com"
USER_ID=$(alluuid email "$USER_EMAIL" | grep "UUID" | awk '{print $3}')
echo "User ID created: $USER_ID"
```

### Developer-Friendly Options

All commands support helpful flags:

```bash
# Get help for any command
alluuid --help
alluuid v4 --help

# Display version
alluuid --version
```


## Functions Overview

| Function Name                          | Description                                                                                                           | Example Output                                        |
|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| `generate_uuid1()`                     | Generates a UUID based on the current timestamp and the MAC address of the machine.                                  | `'123e4567-e89b-12d3-a456-426614174000'`            |
| `generate_uuid4()`                     | Creates a random UUID using version 4, generated entirely randomly.                                                  | `'abcd1234-5678-90ef-ghij-klmnopqrstuv'`            |
| `generate_uuid7()`                     | Generates a time-based UUID using version 7, incorporating a timestamp with an increasing sequence number.           | `'f47ac10b-58cc-4372-a567-0e02b2c3d479'`            |
| `generate_nil_uuid()`                  | Produces a nil UUID, a special UUID consisting entirely of zeros.                                                    | `'00000000-0000-0000-0000-000000000000'`            |
| `generate_guid()`                      | Generates a GUID (Globally Unique Identifier), similar to a UUID but often used in Microsoft environments.           | `'6B29FC40-CA47-1067-B31D-00DD010662DA'`            |
| `generate_multiple_uuids(count, length)` | Generates a specified number of random UUID4s at once, returning them as a list.                                     | `['abcd1234-5678-90ef-ghij-klmnopqrstuv', ...]`    |
| `generate_uuid_for_email(email)`       | Generates a UUID based on a provided email address, ensuring uniqueness and consistency for that email.              | `'9f16c98b-e3b8-4a62-aeef-5f261f2ff1c3'`            |
| `validate_uuid_for_email(uuid, email)` | Validates whether a UUID matches the one that would be generated from the specified email address.                   | `True` or `False`                                   |
| `generate_custom_uuid(pattern)`        | Generates a custom UUID based on a pattern (x=hex, d=digit, others=literal). Perfect for business-specific formats.  | `'BANK-57c8-9233'`                                  |



## Examples
### 1. Generate UUID Version 1
This code snippet imports the uniqueIDGenerator from the alluuid package and calls the version1() method. Version 1 UUIDs are generated based on the current timestamp and the MAC address of the computer (or a random number if the MAC address cannot be determined). As a result, the generated UUID will be unique across space and time.
```python
uuid = generate_uuid1()
# Example output: '123e4567-e89b-12d3-a456-426614174000'
```

### 2. Generate UUID Version 4
This code generates a Version 4 UUID using random numbers. It utilizes a secure random number generator to produce a UUID that is statistically unique. This is ideal for cases where no specific ordering or source of the UUID is required, as the randomness ensures that each UUID generated will not repeat.
```python
uuid = generate_uuid4()
# Example output: 'abcd1234-5678-40ef-ghij-klmnopqrstuv'
```

### 3. Generate UUID Version 7
In this snippet, a Version 7 UUID is generated. This type of UUID is based on time but utilizes a different encoding scheme than Version 1. It is intended for applications where both a timestamp and a unique identifier are needed, allowing sorting and uniqueness based on time of creation.
```python
uuid = generate_uuid7()
# Example output: 'f47ac10b-58cc-7372-a567-0e02b2c3d479'
```

### 4. Generate Nil UUID
This code snippet demonstrates the generation of a Nil UUID, which is a standardized UUID that represents the absence of a value. It is often used in databases and APIs to signify a null or undefined state without ambiguity.
```python
nil_uuid = generate_nil_uuid()
# Example output: '00000000-0000-0000-0000-000000000000'
```

### 5. Generate GUID
This snippet generates a GUID (Globally Unique Identifier). GUIDs and UUIDs serve similar purposes, but GUIDs are often used in Microsoft environments. The generateGuid method utilizes randomization to create a unique identifier that can be used interchangeably with UUIDs in many applications.
```python
guid = generate_guid()
# Example output: '6B29FC40-CA47-1067-B31D-00DD010662DA'
```

### 6. Generate Multiple UUID4s
This code demonstrates how to generate multiple UUIDs in a single call. The generateMultipleUUIDs function takes two parameters: the UUID version (4 in this case) and the number of UUIDs to generate (5). It returns an array of randomly generated Version 4 UUIDs, which can be useful for bulk operations or initializing datasets with unique identifiers.
```python
uuids = generate_multiple_uuids(4, 5)
# Example output: 
# ['abcd1234-5678-90ef-ghij-klmnopqrstuv',
#  'defg5678-1234-90ef-ghij-klmnopqrstuv',
#  'hijk9012-3456-78ef-ghij-klmnopqrstuv',
#  'lmnop3456-7890-abcd-efgh-ijklmnopqrstuv']
```

### 7. Generate UUID for Email
In this example, a UUID is generated based on a specific email address. The generateUUIDForEmail function ensures that the same email will always produce the same UUID, which is particularly useful for scenarios where user identification needs to be consistent (e.g., user accounts). This function hashes the email to generate a UUID, thereby maintaining a unique identifier linked to that email.
```python
uuid = generate_uuid_for_email("test@example.com")
# Example output: '9f16c98b-e3b8-4a62-aeef-5f261f2ff1c3'
```


### 8. Validate UUID Generated from Email
This example validates whether a given UUID was generated from a specific email address. The validate_uuid_for_email function checks if the UUID matches the one that would be generated by hashing the email, helping verify consistent identity mappings.
```python
validation = validate_uuid_for_email(uuidGenerated, "test@example.com")
# Example output: True/False
```

### 9. Generate Custom UUID
Custom UUIDs allow you to create identifiers with your own format and structure. Use the simple pattern system with just two symbols:

#### Pattern Symbols

- **`x`**: Represents a random hexadecimal digit (0-9, a-f)
- **`d`**: Represents a random decimal digit (0-9)
- **Any other character**: Treated as literal text

This simple design avoids conflicts and lets you use UPPERCASE letters, numbers, and any separators freely!

#### Use Cases
Custom UUIDs are especially useful in scenarios where:
- You need to follow a specific formatting standard for your business
- You want to create user-friendly identifiers with company prefixes
- You require random yet structured identifiers for categorization
- You need consistent UUID formats across your applications

#### Examples

```python
from alluuid import generate_custom_uuid

# Generate UUID with a business prefix and hex digits
custom_uuid = generate_custom_uuid('BANK-xxxx-dddd')
# Output: 'BANK-57c8-9233'

# Invoice ID format
invoice_id = generate_custom_uuid('INV-xxxxxx')
# Output: 'INV-a1340a'

# User ID with underscore separators
user_id = generate_custom_uuid('ID_dddd_dddd')
# Output: 'ID_7524_6407'

# Custom separators
ref_id = generate_custom_uuid('REF.xxxx.dddd')
# Output: 'REF.5a3c.1729'

# Mostly literal text with just one random part
auth_code = generate_custom_uuid('USER-code-xxxx')
# Output: 'USER-code-b482'
```




## Community and Ecosystem

By using **ALLUUID**, you are joining a growing community of developers who are passionate about UUID's. We encourage you to share your experiences, ideas, and feedback on GitHub Discussions or any community platform of your choice.

We welcome contributions! If you’d like to contribute, Share use cases, submit an issue or a pull request on GitHub.

We'd love to hear from you and see how you're using **ALLUUID** in your projects!
Contributing


## Issues and Feedback
For issues, feedback, and feature requests, please open an issue on our [GitHub Issues page](http://github.com/krishnatadi/alluuid-pypi/issues). We actively monitor and respond to community feedback.









