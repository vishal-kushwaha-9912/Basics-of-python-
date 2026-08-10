
## Interview Questions

### Easy Level

**Q1: What's the difference between `remove()` and `discard()`?**

A: `remove()` raises a KeyError if the item doesn't exist, while `discard()` doesn't. Use `discard()` for safer removal.

```python
s = {1, 2, 3}
s.remove(2)      # Works, removes 2
s.discard(5)     # Works, does nothing (no error)
s.remove(5)      # Error! KeyError
```

**Q2: Why can't you put a list in a set?**

A: Lists are mutable (can change), but set items must be hashable (immutable). Hashing requires consistent values.

**Q3: What's the time complexity of checking if an item is in a set?**

A: O(1) - constant time, much faster than lists which are O(n).

**Q4: How do you create an empty set?**

A: Use `set()`, not `{}` (which creates an empty dict).

```python
empty_set = set()      # Correct
empty_dict = {}        # Wrong - this is a dict!
```

**Q5: Can you use the `in` operator with sets?**

A: Yes! It's one of the fastest operations in Python (O(1)).

```python
if item in my_set:
    print("Found!")
```

### Medium Level

**Q6: Explain how set hashing works and why it makes lookups fast.**

A: Sets use a hash function to convert items to positions in an internal hash table. This allows O(1) lookup instead of O(n) search through a list.

```
Item "apple" → Hash function → Position 12847
Check position 12847 → Found in one step!
```

**Q7: What are frozensets and when would you use them?**

A: Frozensets are immutable sets. Use them as dictionary keys or when you need a set that can't change.

```python
fs = frozenset([1, 2, 3])
d = {fs: "value"}  # Can use as key
```

**Q8: How do you safely modify a set while iterating through it?**

A: Loop through a copy of the set.

```python
for item in my_set.copy():
    if condition(item):
        my_set.remove(item)
```

**Q9: What's the difference between `union()` and `update()`?**

A: `union()` returns a new set, while `update()` modifies the original set.

```python
s1 = {1, 2}
s2 = {2, 3}

s3 = s1.union(s2)    # s1 unchanged, s3 = {1, 2, 3}
s1.update(s2)        # s1 now = {1, 2, 3}
```

**Q10: How would you find common elements between three sets?**

A: Use the intersection operator multiple times.

```python
s1 = {1, 2, 3, 4}
s2 = {2, 3, 4, 5}
s3 = {3, 4, 5, 6}

common = s1 & s2 & s3  # {3, 4}
# Or:
common = s1.intersection(s2, s3)
```

### Hard Level

**Q11: Implement a function that finds the intersection of multiple sets efficiently.**

```python
def find_intersection(*sets):
    """Find common elements in multiple sets"""
    if not sets:
        return set()
    
    # Start with smallest set for efficiency
    result = min(sets, key=len).copy()
    
    # Intersect with remaining sets
    for s in sets:
        if not result:  # Early exit if empty
            break
        result &= s  # Intersection assignment
    
    return result

# Test
print(find_intersection({1,2,3}, {2,3,4}, {3,4,5}))  # {3}
```

**Q12: Create a class that tracks unique visitors and finds patterns.**

```python
class VisitorTracker:
    def __init__(self):
        self.daily_visitors = {}  # date -> set of visitor_ids
    
    def add_visitor(self, date, visitor_id):
        if date not in self.daily_visitors:
            self.daily_visitors[date] = set()
        self.daily_visitors[date].add(visitor_id)
    
    def find_repeat_visitors(self, date1, date2):
        """Find visitors who came on both dates"""
        if date1 not in self.daily_visitors or date2 not in self.daily_visitors:
            return set()
        return self.daily_visitors[date1] & self.daily_visitors[date2]
    
    def find_weekly_regulars(self, dates):
        """Find visitors who came on all specified dates"""
        if not dates:
            return set()
        
        regulars = self.daily_visitors[dates[0]].copy()
        for date in dates[1:]:
            regulars &= self.daily_visitors.get(date, set())
        
        return regulars

# Usage
tracker = VisitorTracker()
tracker.add_visitor("2024-01-01", "user1")
tracker.add_visitor("2024-01-01", "user2")
tracker.add_visitor("2024-01-02", "user2")
tracker.add_visitor("2024-01-02", "user3")

print(tracker.find_repeat_visitors("2024-01-01", "2024-01-02"))  # {'user2'}
```

**Q13: Explain the trade-off between memory usage and speed in sets.**

A: Sets use extra memory to maintain hash tables, but this provides O(1) lookups. Lists use less memory but have O(n) lookups. Choose based on your needs.

**Q14: How would you efficiently find all duplicates in a list?**

```python
def find_all_duplicates(items):
    """Find all duplicate items efficiently"""
    seen = set()
    duplicates = set()
    
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return duplicates

# Time: O(n), Space: O(n)
# Much faster than nested loops O(n²)
```

**Q15: Implement a Set without using Python's built-in set.**

```python
class SimpleSet:
    """A simplified set implementation using dictionary"""
    def __init__(self, items=None):
        self._dict = {}
        if items:
            for item in items:
                self.add(item)
    
    def add(self, item):
        self._dict[item] = None
    
    def remove(self, item):
        if item not in self._dict:
            raise KeyError(item)
        del self._dict[item]
    
    def discard(self, item):
        self._dict.pop(item, None)
    
    def __contains__(self, item):
        return item in self._dict
    
    def __len__(self):
        return len(self._dict)
    
    def __iter__(self):
        return iter(self._dict)
    
    def __repr__(self):
        return f"SimpleSet({list(self._dict.keys())})"

# Usage
s = SimpleSet([1, 2, 3])
s.add(4)
print(len(s))  # 4
print(2 in s)  # True
```

---

## Multiple Choice Questions (MCQs)

### Question 1
What will be the output?
```python
s = {1, 2, 3}
s.add(2)
print(len(s))
```
A) 3  
B) 4  
C) Error  
D) None

**Answer: A** - Sets only store unique items, so adding 2 (already present) doesn't increase size.

---

### Question 2
Which data type cannot be stored in a set?
A) Tuple  
B) Integer  
C) String  
D) List

**Answer: D** - Lists are mutable and not hashable.

---

### Question 3
What's the time complexity of `item in my_set`?
A) O(n)  
B) O(1)  
C) O(log n)  
D) O(n log n)

**Answer: B** - Set membership test is constant time.

---

### Question 4
What does this code output?
```python
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 - s2)
```
A) {2, 3}  
B) {1}  
C) {4}  
D) {1, 2, 3, 4}

**Answer: B** - Difference operator returns elements in s1 but not s2.

---

### Question 5
How do you create an empty set?
A) `s = {}`  
B) `s = set()`  
C) `s = set([])`  
D) B and C

**Answer: D** - Both create empty sets. `{}` creates a dictionary.

---

### Question 6
What will happen?
```python
s = {1, 2, 3}
for x in s:
    s.add(x + 1)
```
A) Adds 2, 3, 4 successfully  
B) RuntimeError: Set changed size during iteration  
C) No change to set  
D) Infinite loop

**Answer: B** - Modifying set during iteration causes RuntimeError.

---

### Question 7
What's the output?
```python
s = frozenset([1, 2, 3])
s.add(4)
```
A) frozenset({1, 2, 3, 4})  
B) Error: 'frozenset' object has no attribute 'add'  
C) frozenset({1, 2, 3})  
D) None

**Answer: B** - Frozensets are immutable.

---

### Question 8
Which operation is the fastest on a large dataset?
A) Finding max in a list  
B) Checking if item in list  
C) Checking if item in set  
D) Sorting a list

**Answer: C** - Set membership is O(1).

---

### Question 9
What is the output?
```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 | s2)
```
A) {3}  
B) {1, 2}  
C) {1, 2, 3, 4, 5}  
D) Error

**Answer: C** - Union combines all items from both sets.

---

### Question 10
What does `isdisjoint()` check?
A) If sets are equal  
B) If one is subset of other  
C) If sets have NO common items  
D) If sets have common items

**Answer: C** - `isdisjoint()` returns True if sets have no common elements.

---

## Coding Exercises

### Easy Exercises

**Exercise 1: Remove Duplicates**
Write a function that removes duplicates from a list without changing order.

```python
def remove_duplicates(lst):
    """Remove duplicates while keeping order"""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Test
print(remove_duplicates([1, 2, 2, 3, 1, 4]))  # [1, 2, 3, 4]
```

**Exercise 2: Find Common Characters**
Find common characters in two strings.

```python
def common_chars(s1, s2):
    """Find characters present in both strings"""
    return set(s1) & set(s2)

# Test
print(common_chars("hello", "world"))  # {'l', 'o'}
```

**Exercise 3: Check Subset**
Write a function to check if one set is a subset of another.

```python
def is_subset(small, large):
    """Check if small is subset of large"""
    return small <= large  # or small.issubset(large)

# Test
print(is_subset({1, 2}, {1, 2, 3}))  # True
print(is_subset({1, 4}, {1, 2, 3}))  # False
```

---

### Medium Exercises

**Exercise 4: Unique Words in Multiple Documents**
Find unique words across multiple documents.

```python
def unique_words_in_docs(docs):
    """Get all unique words across documents"""
    all_words = set()
    for doc in docs:
        words = doc.lower().split()
        all_words.update(words)
    return all_words

# Test
docs = ["Hello world", "Python world", "Hello Python"]
print(unique_words_in_docs(docs))  # {'hello', 'world', 'python'}
```

**Exercise 5: Find Intersection of Multiple Lists**
Find common elements in multiple lists.

```python
def find_common_elements(lists):
    """Find elements common to all lists"""
    if not lists:
        return set()
    
    # Convert first list to set and intersect with others
    common = set(lists[0])
    for lst in lists[1:]:
        common &= set(lst)
    
    return common

# Test
print(find_common_elements([[1,2,3], [2,3,4], [3,4,5]]))  # {3}
```

**Exercise 6: Filter by Set Conditions**
Filter items based on multiple set conditions.

```python
def filter_by_tags(items, must_have, cannot_have):
    """Filter items by tags"""
    result = []
    for item in items:
        tags = set(item['tags'])
        if must_have <= tags and cannot_have & tags == set():
            result.append(item)
    return result

# Test
items = [
    {'name': 'Item1', 'tags': ['new', 'sale']},
    {'name': 'Item2', 'tags': ['new', 'broken']},
    {'name': 'Item3', 'tags': ['old', 'sale']},
]
result = filter_by_tags(items, {'new', 'sale'}, {'broken'})
# Returns [Item1]
```

---

### Hard Exercises

**Exercise 7: Implement Set Class**
Implement a simple custom set with basic operations.

```python
class SimpleSet:
    """A simplified set implementation"""
    def __init__(self, items=None):
        self.items = {}  # Using dict as hash table
        if items:
            for item in items:
                self.add(item)
    
    def add(self, item):
        """Add item to set"""
        self.items[item] = True
    
    def remove(self, item):
        """Remove item from set"""
        if item in self.items:
            del self.items[item]
        else:
            raise KeyError(item)
    
    def __contains__(self, item):
        """Check membership"""
        return item in self.items
    
    def __len__(self):
        """Get size"""
        return len(self.items)
    
    def union(self, other):
        """Union with another set"""
        result = SimpleSet(self.items.keys())
        for item in other.items.keys():
            result.add(item)
        return result

# Test
s = SimpleSet([1, 2, 3])
s.add(4)
print(len(s))  # 4
print(2 in s)  # True
```

**Exercise 8: Solve Set-Based Problem**
Find all unique pairs that sum to a target.

```python
def find_pairs_with_sum(numbers, target):
    """Find all unique pairs that sum to target"""
    seen = set()
    pairs = set()
    
    for num in numbers:
        complement = target - num
        if complement in seen:
            # Store as sorted tuple to avoid duplicates
            pair = tuple(sorted([num, complement]))
            pairs.add(pair)
        seen.add(num)
    
    return pairs

# Test
print(find_pairs_with_sum([1, 2, 3, 4, 5], 6))  # {(1, 5), (2, 4)}
```

**Exercise 9: Anagram Grouping**
Group words by their anagrams.

```python
def group_anagrams(words):
    """Group anagrams together"""
    groups = {}
    
    for word in words:
        # Sort letters to create key
        key = ''.join(sorted(word.lower()))
        
        if key not in groups:
            groups[key] = set()
        
        groups[key].add(word)
    
    return list(groups.values())

# Test
print(group_anagrams(['listen', 'silent', 'evil', 'vile', 'enlist']))
# [{'listen', 'silent', 'enlist'}, {'evil', 'vile'}]
```

---

## Mini Projects

### Project 1: Social Network Analysis

```python
class SocialNetwork:
    def __init__(self):
        self.users = {}  # user_id -> set of friends
    
    def add_user(self, user_id):
        if user_id not in self.users:
            self.users[user_id] = set()
    
    def add_friend(self, user1, user2):
        self.add_user(user1)
        self.add_user(user2)
        self.users[user1].add(user2)
        self.users[user2].add(user1)  # Mutual friendship
    
    def get_mutual_friends(self, user1, user2):
        """Get common friends"""
        return self.users[user1] & self.users[user2]
    
    def get_all_friends_of_friends(self, user):
        """Get friends of friends (excluding direct friends)"""
        friends = self.users.get(user, set())
        fof = set()
        for friend in friends:
            fof |= self.users[friend]
        fof -= friends  # Remove direct friends
        fof.discard(user)  # Remove self
        return fof
    
    def get_friend_suggestions(self, user, limit=5):
        """Suggest friends based on mutual connections"""
        suggestions = self.get_all_friends_of_friends(user)
        return list(suggestions)[:limit]

# Usage
network = SocialNetwork()
network.add_friend("Alice", "Bob")
network.add_friend("Alice", "Charlie")
network.add_friend("Bob", "Diana")
network.add_friend("Charlie", "Diana")

print(network.get_mutual_friends("Alice", "Charlie"))  # set()
print(network.get_friend_suggestions("Alice"))  # Suggests Diana
```

### Project 2: Duplicate File Finder

```python
import hashlib
from pathlib import Path

class DuplicateFileFinder:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.file_hashes = {}  # hash -> set of file paths
    
    def _get_file_hash(self, filepath):
        """Get SHA256 hash of file"""
        sha256_hash = hashlib.sha256()
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    
    def find_duplicates(self):
        """Find all duplicate files"""
        for filepath in Path(self.root_dir).rglob("*"):
            if filepath.is_file():
                try:
                    file_hash = self._get_file_hash(filepath)
                    if file_hash not in self.file_hashes:
                        self.file_hashes[file_hash] = set()
                    self.file_hashes[file_hash].add(str(filepath))
                except (IOError, OSError):
                    pass
        
        # Return only duplicates
        return {
            hash_val: paths for hash_val, paths in self.file_hashes.items()
            if len(paths) > 1
        }

# Usage
finder = DuplicateFileFinder(".")
duplicates = finder.find_duplicates()
for hash_val, files in duplicates.items():
    print(f"Duplicate files (hash: {hash_val[:8]}...):")
    for f in files:
        print(f"  - {f}")
```

### Project 3: Event RSVP System

```python
class EventRSVPSystem:
    def __init__(self):
        self.events = {}  # event_id -> {'attendees': set, 'capacity': int}
    
    def create_event(self, event_id, capacity):
        self.events[event_id] = {'attendees': set(), 'capacity': capacity}
    
    def add_attendee(self, event_id, user_id):
        """Add attendee to event"""
        if event_id not in self.events:
            return False
        
        event = self.events[event_id]
        if len(event['attendees']) >= event['capacity']:
            return False  # Event is full
        
        event['attendees'].add(user_id)
        return True
    
    def remove_attendee(self, event_id, user_id):
        """Remove attendee from event"""
        if event_id in self.events:
            self.events[event_id]['attendees'].discard(user_id)
    
    def get_attendees(self, event_id):
        """Get set of attendees"""
        return self.events.get(event_id, {}).get('attendees', set())
    
    def find_users_in_multiple_events(self, *event_ids):
        """Find users attending all specified events"""
        if not event_ids:
            return set()
        
        result = self.get_attendees(event_ids[0]).copy()
        for event_id in event_ids[1:]:
            result &= self.get_attendees(event_id)
        
        return result

# Usage
system = EventRSVPSystem()
system.create_event("PyCon", 100)
system.create_event("WebDev", 50)

system.add_attendee("PyCon", "Alice")
system.add_attendee("PyCon", "Bob")
system.add_attendee("WebDev", "Alice")
system.add_attendee("WebDev", "Charlie")

print(system.find_users_in_multiple_events("PyCon", "WebDev"))  # {'Alice'}
```

---

## Edge Cases You Should Know

### Edge Case 1: Empty Sets and Truthiness

```python
empty_set = set()

# Empty set is falsy
if empty_set:
    print("This won't print")

if not empty_set:
    print("Empty set is falsy!")  # Prints

# Difference with None
s = None
if s:
    print("Won't print")

# Better: explicit check
if len(my_set) == 0:
    print("Set is empty")
```

### Edge Case 2: Boolean True/False as 1/0

```python
s = {True, 1, 2, 3}
print(s)  # {True, 1, 2, 3} or {1, 2, 3}?
print(len(s))  # 3! True == 1 in hashing

s = {False, 0}
print(s)  # {False, 0} or {0}?
print(len(s))  # 1! False == 0 in hashing

# This can be surprising:
mixed = {1, True, 2, False, 0}
print(mixed)  # {False, 1, 2} - only 3 items!
```

### Edge Case 3: Float Precision Issues

```python
s = {0.1 + 0.2}
print(0.3 in s)  # False! (Due to floating-point precision)
print(0.1 + 0.2 in s)  # True

# The hash differs due to floating-point imprecision
print(0.1 + 0.2 == 0.3)  # False

# Better: use Decimal for precise comparisons
from decimal import Decimal
s = {Decimal('0.3')}
print(Decimal('0.1') + Decimal('0.2') in s)  # True
```

### Edge Case 4: Sets with Tuple Unpacking

```python
coords = {(1, 2), (3, 4), (5, 6)}

# This works:
for x, y in coords:
    print(f"({x}, {y})")

# Mixed tuples of different lengths cause issues:
mixed = {(1, 2), (1, 2, 3)}  # Different length tuples
for item in mixed:
    print(item)  # Works fine, but be careful

# Better: enforce consistent structure
```

### Edge Case 5: Large Sets and Memory

```python
# Creating a huge set
large_set = set(range(1_000_000))

# Memory usage can be substantial
import sys
print(sys.getsizeof(large_set))  # Much larger than expected

# Sets grow beyond their contents (hash table overhead)
# Typical load factor: ~2/3 full before expanding
```

### Edge Case 6: Mutating While Iterating (Revisited)

```python
s = {1, 2, 3, 4, 5}

# This is dangerous:
# for item in s:
#     s.remove(item)  # RuntimeError!

# This works:
for item in list(s):  # Convert to list first
    s.remove(item)

# Or use copy:
for item in s.copy():
    if item > 2:
        s.remove(item)

print(s)  # {1, 2}
```

### Edge Case 7: Set Operations with Empty Sets

```python
s = {1, 2, 3}
empty = set()

print(s | empty)      # {1, 2, 3}
print(s & empty)      # set() - empty!
print(s - empty)      # {1, 2, 3}
print(s ^ empty)      # {1, 2, 3}

# Be aware: operations with empty set always return specific results
```

### Edge Case 8: Unhashable Objects in Functions

```python
def process_data(*items):
    # Try to create set from arguments
    unique = set(items)  # Might fail!
    return unique

# This works:
process_data(1, 2, 3)

# This fails:
# process_data(1, [2, 3])  # TypeError: unhashable type

# Better: check or convert first
def safe_process(*items):
    try:
        unique = set(items)
    except TypeError:
        # One of the items isn't hashable
        unique = set()
    return unique
```

### Edge Case 9: Set of Tuples with Lists

```python
# This works - tuples are immutable:
s = {(1, 2, 3), (4, 5, 6)}

# This fails - lists inside tuples are still mutable:
# s = {([1, 2], 3)}  # TypeError!

# Fix: convert nested lists to tuples
s = {(tuple([1, 2]), 3), (tuple([4, 5]), 6)}
print(s)
```

### Edge Case 10: Dictionary Keys from Sets

```python
# You can't directly use a set as dict key
# dict = {{1, 2}: "value"}  # TypeError!

# But frozenset works:
d = {frozenset([1, 2]): "value"}
print(d[frozenset([2, 1])])  # "value" (order doesn't matter)
```

### Edge Case Summary Table

| Scenario | Result | Action |
|----------|--------|--------|
| True == 1 | {True, 1} → {1} | Be aware of bool-int equivalence |
| 0.1 + 0.2 | Precision issues | Use Decimal for precision |
| Empty set truthiness | Falsy | Use `len()` for explicit check |
| Mutate while iterating | RuntimeError | Loop over `.copy()` |
| Large sets | High memory | Monitor performance |
| Set operations with empty | Predictable results | Know the outcomes |

---