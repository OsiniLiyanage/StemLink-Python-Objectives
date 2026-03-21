"""
SESSION 06 - Question 1: File Logger
Topics: Writing files, appending, reading files

INSTRUCTIONS:
Complete the three functions below. Replace 'pass' with your code.
Run this file to test your implementation.
"""

from datetime import datetime

def create_log_file(filename):
  
  with open(filename,'w') as file:
      file.write("=== Activity Log ===\n")

def add_log_entry(filename, message):
    
    with open(filename,'a') as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        enrty = f"[{timestamp}] {message}\n"
        f.write(enrty)


    # Hint: Use datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    


def read_recent_logs(filename, n=5):

    with open(filename,'r') as file:
        lines = file.readlines()

    entries = [line.strip() for line in lines[1:]]

    return entries[-n:]
   


# =============================================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# =============================================================================

def test_file_logger():
    """Test all file logger functions"""
    import os

    print("="*60)
    print("TESTING FILE LOGGER")
    print("="*60)

    test_file = "test_activity.log"

    # Test 1: Create log file
    print("\n[Test 1] Creating log file...")
    try:
        create_log_file(test_file)

        if os.path.exists(test_file):
            with open(test_file, "r") as f:
                content = f.read()
                if content == "=== Activity Log ===\n":
                    print("✓ PASS: Log file created with correct header")
                else:
                    print(f"✗ FAIL: Header incorrect. Got: {repr(content)}")
        else:
            print("✗ FAIL: File not created")
    except Exception as e:
        print(f"✗ ERROR: {e}")

    # Test 2: Add log entries
    print("\n[Test 2] Adding log entries...")
    try:
        add_log_entry(test_file, "User logged in")
        add_log_entry(test_file, "File uploaded")
        add_log_entry(test_file, "User logged out")

        with open(test_file, "r") as f:
            lines = f.readlines()

        # Check we have header + 3 entries
        if len(lines) == 4:
            print(f"✓ PASS: {len(lines)-1} entries added")

            # Check format
            entry = lines[1].strip()
            if entry.startswith("[") and "]" in entry:
                print("✓ PASS: Entry format correct")
            else:
                print(f"✗ FAIL: Entry format incorrect: {entry}")
        else:
            print(f"✗ FAIL: Expected 4 lines, got {len(lines)}")
    except Exception as e:
        print(f"✗ ERROR: {e}")

    # Test 3: Read recent logs
    print("\n[Test 3] Reading recent logs...")
    try:
        recent = read_recent_logs(test_file, 2)

        if len(recent) == 2:
            print(f"✓ PASS: Retrieved {len(recent)} recent entries")
            print(f"  Last entry: {recent[-1]}")
        else:
            print(f"✗ FAIL: Expected 2 entries, got {len(recent)}")
    except Exception as e:
        print(f"✗ ERROR: {e}")

    # Test 4: Read all logs
    print("\n[Test 4] Reading all logs...")
    try:
        all_logs = read_recent_logs(test_file, 10)  # More than available

        if len(all_logs) == 3:  # Header not included
            print(f"✓ PASS: Retrieved all {len(all_logs)} entries")
            for i, log in enumerate(all_logs, 1):
                print(f"  {i}. {log[:50]}...")
        else:
            print(f"✗ FAIL: Expected 3 entries, got {len(all_logs)}")
    except Exception as e:
        print(f"✗ ERROR: {e}")

    # Cleanup
    if os.path.exists(test_file):
        os.remove(test_file)
        print(f"\n✓ Test file '{test_file}' cleaned up")

    print("\n" + "="*60)
    print("TESTS COMPLETE")
    print("="*60)


def demo_file_logger():
    """Demo of file logger in action"""
    print("\n" + "="*60)
    print("FILE LOGGER DEMO")
    print("="*60)

    # Create a demo log
    print("\n1. Creating activity log...")
    create_log_file("demo.log")
    print("   ✓ Log file created")

    # Add some entries
    print("\n2. Adding log entries...")
    entries = [
        "Application started",
        "User Alice logged in",
        "File report.pdf generated",
        "Email sent to 5 recipients",
        "Database backup completed",
        "User Alice logged out"
    ]

    for entry in entries:
        add_log_entry("demo.log", entry)
        print(f"   ✓ Logged: {entry}")

    # Read recent
    print("\n3. Reading last 3 entries...")
    recent = read_recent_logs("demo.log", 3)
    for log in recent:
        print(f"   {log}")

    print("\n4. Full log file contents:")
    print("   " + "-"*56)
    with open("demo.log", "r") as f:
        for line in f:
            print(f"   {line.rstrip()}")
    print("   " + "-"*56)

    # Cleanup
    import os
    if os.path.exists("demo.log"):
        os.remove("demo.log")

    print("\n" + "="*60)


if __name__ == "__main__":
    # Run tests
    test_file_logger()

    # Run demo (uncomment to see demo)
    # demo_file_logger()

    print("\n💡 TIP: Implement all functions to pass all tests!")
    print("💡 TIP: Check that files are created in your directory!")
