"""
SESSION 06 - Question 3: Student Scores Tracker
Topics: Lists in CSV, data persistence, error handling

INSTRUCTIONS:
Complete the four functions below. Replace 'pass' with your code.
Run this file to test your implementation.
"""

def save_scores(scores, filename="scores.csv"):
     with open(filename, 'w') as file:
        file.write("name,scores\n")
        
        for name, score_list in scores.items():
           
            score = ",".join(map(str, score_list))
            line = f"{name},{score}\n"
            file.write(line)


def load_scores(filename="scores.csv"):
    scores= {}

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            
            for line in lines[1:]:
                parts = line.strip().split(",")
                
                name = parts[0]
                score_list = list(map(int, parts[1:]))
                
                scores[name] = score_list

    except FileNotFoundError:
        return{}
    return scores
    
  


def add_score(name, score, filename="scores.csv"):
    scores = load_scores(filename)

    if name not in scores:
        return False  

    scores[name].append(score)
    save_scores(scores, filename)
    
    return True 


def get_statistics(name, filename="scores.csv"):
     scores = load_scores(filename)
     if name not in scores:
        return None
     
     score_list = scores[name]
     if len(score_list) == 0:
        return None
     
     min_score = min(score_list)
     max_scoer = max(score_list)
     average = sum(score_list) / len(score_list)

     return {
        "min": min_score,
        "max": max_scoer,
        "average": average
    }
     
     

   


# =============================================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# =============================================================================

def test_scores_tracker():
    """Test all scores tracker functions"""
    import os

    print("="*60)
    print("TESTING STUDENT SCORES TRACKER")
    print("="*60)

    test_file = "test_scores.csv"

    # Test 1: Save scores
    print("\n[Test 1] Saving scores to CSV...")
    try:
        test_scores = {
            "Alice": [85, 92, 78, 88],
            "Bob": [90, 88, 95],
            "Charlie": [75, 80, 82]
        }

        save_scores(test_scores, test_file)

        if os.path.exists(test_file):
            with open(test_file, "r") as f:
                lines = f.readlines()

            # Check header
            if lines[0].strip() == "name,scores":
                print("✓ PASS: CSV header correct")
            else:
                print(f"✗ FAIL: Header incorrect: {lines[0].strip()}")

            # Check Alice's line
            alice_line = lines[1].strip()
            if "Alice" in alice_line and "85" in alice_line:
                print("✓ PASS: Scores format correct")
            else:
                print(f"✗ FAIL: Format incorrect: {alice_line}")

            if len(lines) == 4:  # Header + 3 students
                print(f"✓ PASS: {len(lines)-1} students saved")
            else:
                print(f"✗ FAIL: Expected 4 lines, got {len(lines)}")
        else:
            print("✗ FAIL: File not created")
    except Exception as e:
        print(f"✗ ERROR: {e}")

    # Test 2: Load scores
    print("\n[Test 2] Loading scores from CSV...")
    try:
        scores = load_scores(test_file)

        if len(scores) == 3:
            print(f"✓ PASS: Loaded {len(scores)} students")
        else:
            print(f"✗ FAIL: Expected 3 students, got {len(scores)}")

        # Check Alice's scores
        if "Alice" in scores:
            alice_scores = scores["Alice"]
            if alice_scores == [85, 92, 78, 88]:
                print("✓ PASS: Alice's scores correct")
            else:
                print(f"✗ FAIL: Alice's scores incorrect: {alice_scores}")

            # Check types
            if all(isinstance(score, int) for score in alice_scores):
                print("✓ PASS: Scores are integers (not strings)")
            else:
                print("✗ FAIL: Scores should be integers")
        else:
            print("✗ FAIL: Alice not found")
    except Exception as e:
        print(f"✗ ERROR: {e}")

    # Test 3: Add score
    print("\n[Test 3] Adding new score...")
    try:
        success = add_score("Alice", 95, test_file)

        if success:
            print("✓ PASS: Score added successfully")

            # Verify
            scores = load_scores(test_file)
            if len(scores["Alice"]) == 5 and scores["Alice"][-1] == 95:
                print("✓ PASS: Score correctly appended")
            else:
                print(f"✗ FAIL: Score not appended: {scores['Alice']}")
        else:
            print("✗ FAIL: add_score returned False")
    except Exception as e:
        print(f"✗ ERROR: {e}")

    # Test 4: Add to non-existent student
    print("\n[Test 4] Adding to non-existent student...")
    try:
        success = add_score("Diana", 90, test_file)

        if not success:
            print("✓ PASS: Correctly rejected non-existent student")
        else:
            print("✗ FAIL: Should reject non-existent student")
    except Exception as e:
        print(f"✗ ERROR: {e}")

    # Test 5: Get statistics
    print("\n[Test 5] Getting statistics...")
    try:
        stats = get_statistics("Alice", test_file)

        if stats:
            print(f"✓ PASS: Statistics calculated")
            print(f"  Min: {stats['min']}")
            print(f"  Max: {stats['max']}")
            print(f"  Average: {stats['average']:.2f}")

            # Check calculations
            scores = load_scores(test_file)
            alice_scores = scores["Alice"]
            expected_min = min(alice_scores)
            expected_max = max(alice_scores)
            expected_avg = sum(alice_scores) / len(alice_scores)

            if stats['min'] == expected_min and stats['max'] == expected_max:
                print("✓ PASS: Min and max correct")
            else:
                print(f"✗ FAIL: Stats incorrect")

            if abs(stats['average'] - expected_avg) < 0.01:
                print("✓ PASS: Average correct")
            else:
                print(f"✗ FAIL: Average incorrect")
        else:
            print("✗ FAIL: Statistics not calculated")
    except Exception as e:
        print(f"✗ ERROR: {e}")

    # Test 6: Stats for non-existent student
    print("\n[Test 6] Stats for non-existent student...")
    try:
        stats = get_statistics("Diana", test_file)

        if stats is None:
            print("✓ PASS: Returns None for non-existent student")
        else:
            print("✗ FAIL: Should return None")
    except Exception as e:
        print(f"✗ ERROR: {e}")

    # Test 7: Load non-existent file
    print("\n[Test 7] Loading non-existent file...")
    try:
        scores = load_scores("nonexistent_file.csv")

        if scores == {}:
            print("✓ PASS: Returns empty dict for missing file")
        else:
            print(f"✗ FAIL: Should return {{}}, got {scores}")
    except Exception as e:
        print(f"✗ ERROR: {e}")

    # Cleanup
    if os.path.exists(test_file):
        os.remove(test_file)
        print(f"\n✓ Test file '{test_file}' cleaned up")

    print("\n" + "="*60)
    print("TESTS COMPLETE")
    print("="*60)


def demo_scores_tracker():
    """Interactive demo of scores tracker"""
    print("\n" + "="*60)
    print("SCORES TRACKER DEMO")
    print("="*60)

    filename = "demo_scores.csv"

    # Create initial data
    print("\n1. Creating student records...")
    initial_scores = {
        "Alice": [85, 92, 78, 88],
        "Bob": [90, 88, 95],
        "Charlie": [75, 80, 82, 78, 85]
    }
    save_scores(initial_scores, filename)
    print("   ✓ 3 students with scores saved")

    # Display statistics for all
    print("\n2. Student Statistics:")
    print("   " + "-"*56)
    scores = load_scores(filename)
    for name in sorted(scores.keys()):
        stats = get_statistics(name, filename)
        print(f"   {name:10} Scores: {len(scores[name]):2}  "
              f"Min: {stats['min']:2}  Max: {stats['max']:2}  "
              f"Avg: {stats['average']:.1f}")
    print("   " + "-"*56)

    # Add new scores
    print("\n3. Adding new test scores...")
    add_score("Alice", 95, filename)
    add_score("Bob", 92, filename)
    print("   ✓ Scores added")

    # Show updated stats
    print("\n4. Updated Statistics:")
    print("   " + "-"*56)
    for name in ["Alice", "Bob"]:
        stats = get_statistics(name, filename)
        scores = load_scores(filename)
        print(f"   {name:10} Scores: {scores[name]}")
        print(f"              Stats: Min={stats['min']} "
              f"Max={stats['max']} Avg={stats['average']:.1f}")
    print("   " + "-"*56)

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
    test_scores_tracker()

    # Run demo (uncomment to see demo)
    # demo_scores_tracker()

    print("\n💡 TIP: Use map(int, parts[1:]) to convert score strings to ints!")
    print("💡 TIP: Use ','.join(map(str, scores)) to save scores list!")
