"""
SESSION 05 - QUESTION 3: CONTACT BOOK
======================================

Topics Covered: Dictionaries (creating, accessing, modifying, looping)

TASK:
Complete the five functions below to build a contact book using dictionaries.
All the printing and formatting is handled for you - just implement the logic!

DO NOT modify the test code at the bottom.
"""

def create_contact(name, phone, email):
    return{"name":name,"phone":phone,"email":email}


def get_contact_info(contact, key):
  return contact.get(key,"Not found")


def update_contact(contact, key, new_value):
    contact[key] = new_value


def count_contacts(contacts):
   return{"total":len(contacts)}


def find_all_names(contacts):
   return[contact["name"] for contact in contacts]


# ============================================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================================

def test_contact_book():
    """Test function with formatted output"""
    print("=" * 60)
    print("SESSION 05 - QUESTION 3: CONTACT BOOK")
    print("=" * 60)
    print()

    # Test 1: Create contact
    print("TEST 1: Create a contact dictionary")
    print("-" * 40)
    contact = create_contact("Alice", "555-1234", "alice@email.com")
    print(f"Result: {contact}")
    expected = {"name": "Alice", "phone": "555-1234", "email": "alice@email.com"}
    print(f"Expected: {expected}")
    print(f"Status: {'✓ PASS' if contact == expected else '✗ FAIL'}")
    print()

    # Test 2: Get contact info (existing key)
    print("TEST 2: Get existing contact information")
    print("-" * 40)
    name = get_contact_info(contact, "name")
    phone = get_contact_info(contact, "phone")
    print(f"Name: {name}")
    print(f"Phone: {phone}")
    print(f"Status: {'✓ PASS' if name == 'Alice' and phone == '555-1234' else '✗ FAIL'}")
    print()

    # Test 3: Get contact info (missing key)
    print("TEST 3: Get missing contact information (should return 'Not found')")
    print("-" * 40)
    address = get_contact_info(contact, "address")
    print(f"Address: {address}")
    print(f"Status: {'✓ PASS' if address == 'Not found' else '✗ FAIL'}")
    print()

    # Test 4: Update contact
    print("TEST 4: Update contact information")
    print("-" * 40)
    print(f"Before: {contact}")
    update_contact(contact, "phone", "555-9999")
    print(f"After: {contact}")
    print(f"Status: {'✓ PASS' if contact['phone'] == '555-9999' else '✗ FAIL'}")
    print()

    # Test 5: Count contacts
    print("TEST 5: Count total contacts")
    print("-" * 40)
    contacts = [
        {"name": "Alice", "phone": "555-1111"},
        {"name": "Bob", "phone": "555-2222"},
        {"name": "Charlie", "phone": "555-3333"}
    ]
    summary = count_contacts(contacts)
    print(f"Contacts: {len(contacts)} people")
    print(f"Result: {summary}")
    print(f"Expected: {{'total': 3}}")
    print(f"Status: {'✓ PASS' if summary == {'total': 3} else '✗ FAIL'}")
    print()

    # Test 6: Find all names
    print("TEST 6: Extract all names from contacts")
    print("-" * 40)
    names = find_all_names(contacts)
    print(f"Result: {names}")
    print(f"Expected: ['Alice', 'Bob', 'Charlie']")
    print(f"Status: {'✓ PASS' if names == ['Alice', 'Bob', 'Charlie'] else '✗ FAIL'}")
    print()

    # Complete demonstration
    print("=" * 60)
    print("COMPLETE CONTACT BOOK DEMO")
    print("=" * 60)
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']}: {contact['phone']}")
    print()
    print("=" * 60)


if __name__ == "__main__":
    test_contact_book()
