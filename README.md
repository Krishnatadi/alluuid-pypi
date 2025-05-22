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


## Features

- **Multiple UUID Versions**: Generate UUIDs of version 1, 4, and 7.
- **GUID Generation**: Create standard GUIDs.
- **Batch Generation**: Generate multiple UUIDs in one call.
- **Custom UUID Generation**: Create UUIDs based on custom object details.
- **Consistent UUID for Emails**: Generate a consistent UUID for the same email address.
- **Nil UUID Generation**: Generate a UUID with all bits set to zero.



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
| `generate_custom_uuid()`               | Generates a custom UUID based on specified parameters, allowing for tailored UUID creation.                          | `'3a2d5c4b-0b47-4f3e-bfb8-1c41d8c7760e'`            |



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
#### Parameters

- **`pattern`** (str): Defines the format of the generated UUID. You can use:
  - `x`: Represents a random hexadecimal digit (0-9, a-f).
  - `d`: Represents a decimal digit (0-9).
  - Any other character will be treated as a literal part of the UUID.

- **`length`** (int): Specifies the length of each segment in the pattern. For example, if the pattern is `'xxxx-xxxx'` and the length is `4`, each segment will consist of 4 characters.

- **`prefix`** (str, optional): An optional prefix that can be added to the generated UUID. This can be useful for categorizing or identifying the source of the UUID.


#### Use Cases
Custom UUIDs are especially useful in scenarios where:
- You need to follow a specific formatting standard.
- You want to create user-friendly identifiers that include prefixes or specific structures.
- You require random yet structured identifiers for categorization or classification.


```python
# Basic custom UUID with a pattern of 'xxxx-xxxx'
basic_uuid = generate_custom_uuid('xxxx-xxxx', 4)
# Output: '88c7-2d9a'

# Custom UUID with a pattern 'abcd-dddd' and a prefix 'user'
prefixed_uuid = generate_custom_uuid('abcd-dddd', 4, 'user')
# Output: 'user-abc7-4494'

# Custom UUID with a complex pattern 'x-dx-x'
complex_uuid = generate_custom_uuid('x-dx-x', 3)
# Output: '262-0c3-b8c'
```




## Community and Ecosystem

By using **ALLUUID**, you are joining a growing community of developers who are passionate about UUID's. We encourage you to share your experiences, ideas, and feedback on GitHub Discussions or any community platform of your choice.

We welcome contributions! If you’d like to contribute, Share use cases, submit an issue or a pull request on GitHub.

We'd love to hear from you and see how you're using **ALLUUID** in your projects!
Contributing


## Issues and Feedback
For issues, feedback, and feature requests, please open an issue on our [GitHub Issues page](http://github.com/krishnatadi/alluuid-pypi/issues). We actively monitor and respond to community feedback.









