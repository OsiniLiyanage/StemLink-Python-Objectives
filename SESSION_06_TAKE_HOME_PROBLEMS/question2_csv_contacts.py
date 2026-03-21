"""
SESSION 06 - Question 2: CSV Contact Book
Topics: CSV format, dictionaries, structured data

INSTRUCTIONS:
Complete the four functions below. Replace 'pass' with your code.
Run this file to test your implementation.
"""

def save_contacts(contacts, filename="contacts.csv"):
   
   with open(filename,'w') as f:
       f.write("name,phone,email\n")

       for name, info in contacts.items():
            line = f"{name},{info['phone']},{info['email']}\n"
            f.write(line)

       

def load_contacts(filename="contacts.csv"):
    

    contacts={}

    try:
        with open(filename,'r') as file:
            lines = file.readlines()
            for line in lines[1:]:
                name,phone,email = line.strip().split(",")

                contacts[name] = {"phone":phone, "email": email}

    except FileNotFoundError:
        return{}
    
    return contacts
    
    

def add_contact(name, phone, email, filename="contacts.csv"):
  
    contacts = load_contacts(filename)
    if name in contacts:
        return False
    contacts[name] = {"phone":phone, "email":email}

    save_contacts(contacts,filename)

    return True


def search_contact(name, filename="contacts.csv"):
    
    
    contacts = load_contacts(filename)
    if name in contacts:
        return contacts[name]
    else:
        return None


# =============================================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# =============================================================================

def test_csv_contacts():
    """Test all CSV contact functions"""
    import os

    print("="*60)
    print("TESTING CSV CONTACT BOOK")
    print("="*60)

    test_file = "test_contacts.csv"

    # Test 1: Save contacts
    print("\n[Test 1] Saving contacts to CSV...")
    try:
        test_contacts = {
            "Alice": {"phone": "555-1234", "email": "alice@email.com"},
            "Bob": {"phone": "555-5678", "email": "bob@email.com"}
        }

        save_contacts(test_contacts, test_file)

        if os.path.exists(test_file):
            with open(test_file, "r") as f:
                lines = f.readlines()

            # Check header
            if lines[0].strip() == "name,phone,email":
                print("✓ PASS: CSV header correct")
            else:
                print(f"✗ FAIL: Header incorrect: {lines[0].strip()}")

            # Check number of entries
            if len(lines) == 3:  # Header + 2 contacts
                print(f"✓ PASS: {len(lines)-1} contacts saved")
            else:
                print(f"✗ FAIL: Expected 3 lines, got {len(lines)}")
        else:
            print("✗ FAIL: File not created")
    except Exception as e:
        print(f"✗ ERROR: {e}")

    # Test 2: Load contacts
    print("\n[Test 2] Loading contacts from CSV...")
    try:
        contacts = load_contacts(test_file)

        if len(contacts) == 2:
            print(f"✓ PASS: Loaded {len(contacts)} contacts")
        else:
            print(f"✗ FAIL: Expected 2 contacts, got {len(contacts)}")

        # Check Alice's data
        if "Alice" in contacts:
            alice = contacts["Alice"]
            if alice["phone"] == "555-1234" and alice["email"] == "alice@email.com":
                print("✓ PASS: Alice's data correct")
            else:
                print(f"✗ FAIL: Alice's data incorrect: {alice}")
        else:
            print("✗ FAIL: Alice not found in contacts")
    except Exception as e:
        print(f"✗ ERROR: {e}")

    # Test 3: Add new contact
    print("\n[Test 3] Adding new contact...")
    try:
        success = add_contact("Charlie", "555-9012", "charlie@email.com", test_file)

        if success:
            print("✓ PASS: Contact added successfully")

            # Verify by loading
            contacts = load_contacts(test_file)
            if len(contacts) == 3 and "Charlie" in contacts:
                print("✓ PASS: Charlie found in loaded contacts")
            else:
                print(f"✗ FAIL: Charlie not properly saved")
        else:
            print("✗ FAIL: add_contact returned False")
    except Exception as e:
        print(f"✗ ERROR: {e}")

    # Test 4: Try adding duplicate
    print("\n[Test 4] Testing duplicate detection...")
    try:
        success = add_contact("Alice", "555-0000", "new@email.com", test_file)

        if not success:
            print("✓ PASS: Duplicate correctly rejected")
        else:
            print("✗ FAIL: Duplicate should be rejected")
    except Exception as e:
        print(f"✗ ERROR: {e}")

    # Test 5: Search contact
    print("\n[Test 5] Searching for contacts...")
    try:
        alice = search_contact("Alice", test_file)

        if alice:
            print(f"✓ PASS: Found Alice")
            print(f"  Phone: {alice['phone']}")
            print(f"  Email: {alice['email']}")
        else:
            print("✗ FAIL: Alice not found")

        # Search for non-existent
        result = search_contact("Diana", test_file)
        if result is None:
            print("✓ PASS: Non-existent contact returns None")
        else:
            print("✗ FAIL: Should return None for non-existent contact")
    except Exception as e:
        print(f"✗ ERROR: {e}")

    # Test 6: Load non-existent file
    print("\n[Test 6] Loading non-existent file...")
    try:
        contacts = load_contacts("nonexistent_file.csv")

        if contacts == {}:
            print("✓ PASS: Returns empty dict for missing file")
        else:
            print(f"✗ FAIL: Should return {{}}, got {contacts}")
    except Exception as e:
        print(f"✗ ERROR: {e}")

    # Cleanup
    if os.path.exists(test_file):
        os.remove(test_file)
        print(f"\n✓ Test file '{test_file}' cleaned up")

    print("\n" + "="*60)
    print("TESTS COMPLETE")
    print("="*60)


def demo_contact_book():
    """Interactive demo of contact book"""
    print("\n" + "="*60)
    print("CONTACT BOOK DEMO")
    print("="*60)

    filename = "demo_contacts.csv"

    # Add some contacts
    print("\n1. Adding contacts...")
    add_contact("Alice Smith", "555-1234", "alice@email.com", filename)
    add_contact("Bob Jones", "555-5678", "bob@email.com", filename)
    add_contact("Charlie Brown", "555-9012", "charlie@email.com", filename)
    print("   ✓ 3 contacts added")

    # Load and display
    print("\n2. Loading all contacts...")
    contacts = load_contacts(filename)
    print(f"   Found {len(contacts)} contacts:")
    for name, info in contacts.items():
        print(f"   - {name}: {info['phone']} | {info['email']}")

    # Search
    print("\n3. Searching for 'Bob Jones'...")
    contact = search_contact("Bob Jones", filename)
    if contact:
        print(f"   Found: {contact}")

    # Try duplicate
    print("\n4. Trying to add duplicate...")
    success = add_contact("Alice Smith", "555-0000", "new@email.com", filename)
    if not success:
        print("   ✓ Duplicate correctly rejected")

    # Show file contents
    print("\n5. CSV file contents:")
    print("   " + "-"*56)
    with open(filename, "r") as f:
        for line in f:
            print(f"   {line.rstrip()}")
    print("   " + "-"*56)

    # Cleanup
    import os
    if os.path.exists(filename):
        os.remove(filename)

    print("\n" + "="*60)


if __name__ == "__main__":
    # Run tests
    test_csv_contacts()

    # Run demo (uncomment to see demo)
    # demo_contact_book()

    print("\n💡 TIP: Use strip() before split() when parsing CSV!")
    print("💡 TIP: Handle FileNotFoundError when loading!")
