"""
SESSION 06 - Question 4: Configuration File Manager
Topics: Key-value pairs, file persistence, default values

INSTRUCTIONS:
Complete the four functions below. Replace 'pass' with your code.
Run this file to test your implementation.
"""

def load_config(filename="config.txt"):
    """
    Load configuration from file.
    Returns default config if file doesn't exist.

    Args:
        filename (str): Config file name

    Returns:
        dict: Configuration key-value pairs

    File Format:
        theme=dark
        font_size=14
        auto_save=True

    Default Config:
        {
            "theme": "light",
            "font_size": "12",
            "auto_save": "False",
            "language": "English"
        }

    Example:
        config = load_config()
        # {'theme': 'dark', 'font_size': '14', ...}
    """
    # TODO: Define default config dict
    # Try to open file in read mode
    # If FileNotFoundError:
    #   Return default config
    # For each line:
    #   Split by "=": key, value = line.strip().split("=")
    #   Add to config dict
    # Return config dict

    default_config = {
        "theme": "light",
        "font_size": "12",
        "auto_save": "False",
        "language": "English"
    }

    config={}

    try:
        with open(filename,'r') as file:
            for line in file:
                line=line.strip()

                if not line:
                    continue

                key,valie = line.split("=")
                config[key]= valie
    except FileNotFoundError:
        return default_config
    
    return config





def save_config(config, filename="config.txt"):
    with open(filename, 'w') as file:
        for key, value in config.items():
            file.write(f"{key}={value}\n")


def get_setting(key, filename="config.txt"):
   allconfig = load_config(filename)
   return allconfig.get(key)



def update_setting(key, value, filename="config.txt"):
   allconfig = load_config(filename)
   allconfig[key] = value
   save_config(allconfig,filename)


# =============================================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# =============================================================================

def test_config_manager():
    """Test all config manager functions"""
    import os

    print("="*60)
    print("TESTING CONFIGURATION MANAGER")
    print("="*60)

    test_file = "test_config.txt"

    # Test 1: Save config
    print("\n[Test 1] Saving configuration...")
    try:
        test_config = {
            "theme": "dark",
            "font_size": "14",
            "auto_save": "True",
            "language": "Python"
        }

        save_config(test_config, test_file)

        if os.path.exists(test_file):
            with open(test_file, "r") as f:
                content = f.read()

            if "theme=dark" in content and "font_size=14" in content:
                print("✓ PASS: Config saved correctly")
            else:
                print(f"✗ FAIL: Config format incorrect")

            lines = content.strip().split("\n")
            if len(lines) == 4:
                print(f"✓ PASS: All {len(lines)} settings saved")
            else:
                print(f"✗ FAIL: Expected 4 lines, got {len(lines)}")
        else:
            print("✗ FAIL: File not created")
    except Exception as e:
        print(f"✗ ERROR: {e}")

    # Test 2: Load config
    print("\n[Test 2] Loading configuration...")
    try:
        config = load_config(test_file)

        if len(config) == 4:
            print(f"✓ PASS: Loaded {len(config)} settings")
        else:
            print(f"✗ FAIL: Expected 4 settings, got {len(config)}")

        # Check specific values
        if config.get("theme") == "dark":
            print("✓ PASS: Theme value correct")
        else:
            print(f"✗ FAIL: Theme incorrect: {config.get('theme')}")

        if config.get("font_size") == "14":
            print("✓ PASS: Font size value correct")
        else:
            print(f"✗ FAIL: Font size incorrect: {config.get('font_size')}")
    except Exception as e:
        print(f"✗ ERROR: {e}")

    # Test 3: Get setting
    print("\n[Test 3] Getting individual settings...")
    try:
        theme = get_setting("theme", test_file)

        if theme == "dark":
            print(f"✓ PASS: Retrieved theme: {theme}")
        else:
            print(f"✗ FAIL: Expected 'dark', got {theme}")

        # Get non-existent setting
        result = get_setting("nonexistent", test_file)
        if result is None:
            print("✓ PASS: Returns None for non-existent setting")
        else:
            print(f"✗ FAIL: Should return None, got {result}")
    except Exception as e:
        print(f"✗ ERROR: {e}")

    # Test 4: Update setting
    print("\n[Test 4] Updating settings...")
    try:
        update_setting("theme", "light", test_file)

        # Verify update
        theme = get_setting("theme", test_file)
        if theme == "light":
            print("✓ PASS: Setting updated and saved")
        else:
            print(f"✗ FAIL: Update failed, theme is {theme}")

        # Add new setting
        update_setting("new_setting", "new_value", test_file)

        # Verify new setting
        value = get_setting("new_setting", test_file)
        if value == "new_value":
            print("✓ PASS: New setting added successfully")
        else:
            print(f"✗ FAIL: New setting not added")
    except Exception as e:
        print(f"✗ ERROR: {e}")

    # Test 5: Load non-existent file (default config)
    print("\n[Test 5] Loading with default config...")
    try:
        # Remove test file
        if os.path.exists(test_file):
            os.remove(test_file)

        config = load_config(test_file)

        if config:  # Should return default config
            print("✓ PASS: Default config returned for missing file")
            print(f"   Default config has {len(config)} settings")

            # Check if it's using defaults
            if "theme" in config:
                print(f"   Default theme: {config['theme']}")
        else:
            print("✗ FAIL: Should return default config")
    except Exception as e:
        print(f"✗ ERROR: {e}")

    # Test 6: Persistence
    print("\n[Test 6] Testing persistence...")
    try:
        # Create new config
        new_config = {
            "theme": "custom",
            "font_size": "16"
        }
        save_config(new_config, test_file)

        # Simulate program restart - load again
        loaded = load_config(test_file)

        if loaded["theme"] == "custom" and loaded["font_size"] == "16":
            print("✓ PASS: Config persists across 'restarts'")
        else:
            print("✗ FAIL: Config not persisted correctly")
    except Exception as e:
        print(f"✗ ERROR: {e}")

    # Cleanup
    if os.path.exists(test_file):
        os.remove(test_file)
        print(f"\n✓ Test file '{test_file}' cleaned up")

    print("\n" + "="*60)
    print("TESTS COMPLETE")
    print("="*60)


def demo_config_manager():
    """Interactive demo of config manager"""
    print("\n" + "="*60)
    print("CONFIGURATION MANAGER DEMO")
    print("="*60)

    filename = "demo_config.txt"

    # Initial setup
    print("\n1. First run - no config file exists...")
    config = load_config(filename)
    print("   ✓ Default config loaded:")
    for key, value in config.items():
        print(f"      {key}: {value}")

    # User makes changes
    print("\n2. User customizes settings...")
    update_setting("theme", "dark", filename)
    update_setting("font_size", "16", filename)
    update_setting("auto_save", "True", filename)
    print("   ✓ Settings updated")

    # Display current config
    print("\n3. Current configuration:")
    print("   " + "-"*56)
    config = load_config(filename)
    for key, value in config.items():
        print(f"   {key:15} = {value}")
    print("   " + "-"*56)

    # Simulate program restart
    print("\n4. Simulating program restart...")
    print("   (Loading config from file)")
    config = load_config(filename)
    print(f"   ✓ Config loaded: {len(config)} settings")
    print(f"   Theme: {get_setting('theme', filename)}")
    print(f"   Font Size: {get_setting('font_size', filename)}")

    # Show file contents
    print("\n5. Config file contents:")
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
    test_config_manager()

    # Run demo (uncomment to see demo)
    # demo_config_manager()

    print("\n💡 TIP: Provide default config when file doesn't exist!")
    print("💡 TIP: Use split('=') to parse key=value format!")
