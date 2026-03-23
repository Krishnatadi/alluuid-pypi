"""
AllUUID CLI - Command-line interface for UUID generation.

This module provides a user-friendly CLI for generating various types of UUIDs.
Uses only built-in Python modules (argparse, sys) for maximum compatibility.
Users can generate UUIDs of different versions, batch generate, email-based UUIDs, and more.
"""

import argparse
import sys
from . import (
    generate_uuid1,
    generate_uuid4,
    generate_uuid7,
    generate_nil_uuid,
    generate_guid,
    generate_uuid_for_email,
    validate_uuid_for_email,
    generate_custom_uuid,
    generate_multiple_uuids,
)


class Colors:
    """ANSI color codes for terminal output."""
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    RESET = '\033[0m'


def colored_text(text, fg=None, bold=False):
    """Format text with ANSI color codes."""
    color = ''
    if fg == 'cyan':
        color = Colors.CYAN
    elif fg == 'green':
        color = Colors.GREEN
    elif fg == 'yellow':
        color = Colors.YELLOW
    elif fg == 'red':
        color = Colors.RED
    
    bold_code = Colors.BOLD if bold else ''
    return f"{bold_code}{color}{text}{Colors.RESET}"


def cmd_v1(args):
    """Generate a UUID v1 (time-based with MAC address)."""
    uuid = generate_uuid1()
    print(colored_text("UUID v1: ", fg='cyan', bold=True) + f"{uuid}")
    print(colored_text("Generated successfully", fg='green'))


def cmd_v4(args):
    """Generate a UUID v4 (random)."""
    uuid = generate_uuid4()
    print(colored_text("UUID v4: ", fg='cyan', bold=True) + f"{uuid}")
    print(colored_text("Generated successfully", fg='green'))


def cmd_v7(args):
    """Generate a UUID v7 (timestamp-based with sequence)."""
    uuid = generate_uuid7()
    print(colored_text("UUID v7: ", fg='cyan', bold=True) + f"{uuid}")
    print(colored_text("Generated successfully", fg='green'))


def cmd_nil(args):
    """Generate a Nil UUID (all zeros)."""
    uuid = generate_nil_uuid()
    print(colored_text("Nil UUID: ", fg='cyan', bold=True) + f"{uuid}")
    print(colored_text("Generated successfully", fg='green'))


def cmd_guid(args):
    """Generate a GUID (similar to UUID v4, Microsoft format)."""
    guid_val = generate_guid()
    print(colored_text("GUID: ", fg='cyan', bold=True) + f"{guid_val}")
    print(colored_text("Generated successfully", fg='green'))


def cmd_batch(args):
    """Generate multiple UUIDs at once."""
    count = args.count
    
    if count < 2 or count > 50:
        print(colored_text("Error: Count must be between 2 and 50", fg='red', bold=True))
        return
    
    try:
        uuids = generate_multiple_uuids(4, count)
        print(colored_text(f"Generated {count} UUID v4s:\n", fg='cyan', bold=True))
        for i, uuid in enumerate(uuids, 1):
            print(f"  {i}. {uuid}")
        print(colored_text("\nBatch generation successful", fg='green'))
    except Exception as e:
        print(colored_text(f"Error: {str(e)}", fg='red', bold=True))


def cmd_email(args):
    """Generate a UUID based on an email address (consistent and deterministic)."""
    email = args.email
    try:
        uuid = generate_uuid_for_email(email)
        print(colored_text("Email-based UUID: ", fg='cyan', bold=True) + f"{uuid}")
        print(colored_text("Email: ", fg='yellow') + f"{email}")
        print(colored_text("Generated successfully", fg='green'))
    except ValueError as e:
        print(colored_text(f"Error: {str(e)}", fg='red', bold=True))


def cmd_validate(args):
    """Validate if a UUID matches the given email address."""
    uuid = args.uuid
    email = args.email_addr
    
    try:
        result = validate_uuid_for_email(uuid, email)
        if result:
            print(colored_text("Valid: ", fg='green', bold=True) + 
                  f"UUID matches email '{email}'")
        else:
            print(colored_text("Invalid: ", fg='red', bold=True) + 
                  f"UUID does NOT match email '{email}'")
    except Exception as e:
        print(colored_text(f"Error: {str(e)}", fg='red', bold=True))


def cmd_custom(args):
    """
    Generate a custom UUID based on a flexible pattern.
    
    Pattern symbols (simple and clean):
    - 'x' = hex digit (0-9, a-f)
    - 'd' = decimal digit (0-9)
    - Any other character = literal text
    
    This design avoids conflicts - use UPPERCASE letters freely as literals!
    
    Examples:
    - 'BANK-xxxx-dddd' = BANK literal + hex + digits
    - 'USER-code-xxxx' = USER-code- all literal, only xxxx is random hex
    - 'ID_dddd_dddd' = ID_ literal + digits
    - 'REF-xxxxxx' = REF- literal + 6 hex chars
    """
    pattern = args.pattern
    
    try:
        uuid = generate_custom_uuid(pattern)
        print(colored_text("Custom UUID: ", fg='cyan', bold=True) + f"{uuid}")
        print(colored_text("Pattern: ", fg='yellow') + f"{pattern}")
        print(colored_text("Generated successfully", fg='green'))
    except Exception as e:
        print(colored_text(f"Error: {str(e)}", fg='red', bold=True))


def cmd_info(args):
    """Display information about AllUUID and available commands."""
    print(colored_text("\nAllUUID CLI Information\n", fg='cyan', bold=True))
    
    print(colored_text("About:", fg='yellow', bold=True))
    print("  AllUUID is a comprehensive UUID generation library for Python.")
    print("  It supports multiple UUID versions: v1, v4, v7, GUID, and custom patterns.\n")
    
    print(colored_text("Available Commands:", fg='yellow', bold=True))
    print("  v1              - Generate UUID v1 (time-based)")
    print("  v4              - Generate UUID v4 (random)")
    print("  v7              - Generate UUID v7 (timestamp-based)")
    print("  nil             - Generate Nil UUID (all zeros)")
    print("  guid            - Generate GUID")
    print("  batch [COUNT]   - Generate multiple UUIDs (2-50)")
    print("  email EMAIL     - Generate UUID from email")
    print("  validate UUID   - Validate UUID against email")
    print("  custom PATTERN  - Generate custom UUID by pattern")
    print("  info            - Show this information\n")
    
    print(colored_text("Examples:", fg='yellow', bold=True))
    print("  alluuid v4")
    print("  alluuid batch --count 10")
    print("  alluuid email user@example.com")
    print("  alluuid custom 'BANK-xxxx-dddd'")
    print("  alluuid validate <uuid> user@example.com")
    
    print(colored_text("\nPattern Symbols (custom command):", fg='yellow', bold=True))
    print("  x = hex digit (0-9, a-f)")
    print("  d = decimal digit (0-9)")
    print("  ALL OTHER CHARACTERS = literal text\n")
    
    print(colored_text("Custom Pattern Examples:", fg='yellow', bold=True))
    print("  alluuid custom 'BANK-xxxx-dddd'      # Uppercase literal + random chars")
    print("  alluuid custom 'INV-xxxxxx'         # Literal prefix + 6 hex digits")
    print("  alluuid custom 'ID_dddd_dddd'       # Literal underscore + digits")
    print("  alluuid custom 'USER-code-xxxx'     # Most literal, only xxxx random")
    print("  alluuid custom 'REF.xxxx.dddd.xxx'  # Custom separators + random\n")


def cli(args=None):
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        prog='alluuid',
        description='AllUUID - Powerful UUID Generation CLI Tool\n\nGenerate various types of UUIDs easily from the command line.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='\nExamples:\n  alluuid v4\n  alluuid batch --count 10\n  alluuid email user@example.com'
    )
    
    parser.add_argument('--version', action='version', version='%(prog)s 0.2.0')
    
    subparsers = parser.add_subparsers(title='commands', dest='command', help='Available commands')
    
    # v1 command
    subparsers.add_parser('v1', help='Generate UUID v1 (time-based with MAC address)')
    
    # v4 command
    subparsers.add_parser('v4', help='Generate UUID v4 (random)')
    
    # v7 command
    subparsers.add_parser('v7', help='Generate UUID v7 (timestamp-based with sequence)')
    
    # nil command
    subparsers.add_parser('nil', help='Generate Nil UUID (all zeros)')
    
    # guid command
    subparsers.add_parser('guid', help='Generate GUID (Microsoft format)')
    
    # batch command
    batch_parser = subparsers.add_parser('batch', help='Generate multiple UUIDs at once')
    batch_parser.add_argument('-c', '--count', type=int, default=5, 
                             help='Number of UUIDs to generate (2-50). Default: 5')
    
    # email command
    email_parser = subparsers.add_parser('email', help='Generate UUID from email address')
    email_parser.add_argument('email', help='Email address to generate UUID from')
    
    # validate command
    validate_parser = subparsers.add_parser('validate', help='Validate UUID against email')
    validate_parser.add_argument('uuid', help='UUID to validate')
    validate_parser.add_argument('email_addr', metavar='email', help='Email address to validate against')
    
    # custom command
    custom_parser = subparsers.add_parser('custom', help='Generate custom UUID by pattern')
    custom_parser.add_argument('pattern', help="Pattern: x=hex, d=digit, others=literal. Example: 'BANK-xxxx-dddd'")
    
    # info command
    subparsers.add_parser('info', help='Display information about AllUUID')
    
    # Parse arguments
    parsed_args = parser.parse_args(args)
    
    # Command mapping
    commands = {
        'v1': cmd_v1,
        'v4': cmd_v4,
        'v7': cmd_v7,
        'nil': cmd_nil,
        'guid': cmd_guid,
        'batch': cmd_batch,
        'email': cmd_email,
        'validate': cmd_validate,
        'custom': cmd_custom,
        'info': cmd_info,
    }
    
    # If no command provided, show help
    if parsed_args.command is None:
        parser.print_help()
        return
    
    # Execute command
    if parsed_args.command in commands:
        commands[parsed_args.command](parsed_args)
    else:
        parser.print_help()


if __name__ == '__main__':
    cli()

