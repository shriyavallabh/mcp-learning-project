# Failure Scenarios and Counter-Strategies
## Learning System - Comprehensive Risk Analysis

**Date:** 2025-11-08
**Version:** 1.0

---

## Overview

This document identifies potential failure scenarios for the Learning System and provides detailed counter-strategies to prevent or mitigate each failure.

---

## Failure Scenario 1: Corrupted JSON Files

### Description
User accidentally edits `syllabus.json` or `progress.json` and introduces invalid JSON syntax (missing comma, unclosed bracket, etc.). This causes the system to crash when trying to load the files.

### Impact
- **Severity:** HIGH
- System becomes completely unusable
- User loses all progress if no backup
- Learning session cannot start

### Detection
```python
# Current detection in load_json():
except json.JSONDecodeError as e:
    print(f"❌ ERROR: Invalid JSON in {file_path}: {e}")
    sys.exit(1)
```

### Counter-Strategies

#### Strategy 1.1: Automatic Backup Before Every Write
```python
def save_json_with_backup(file_path: str, data: Dict) -> None:
    """
    Save JSON with automatic backup.

    Before writing new data:
    1. Create backup of current file
    2. Write new data
    3. Validate new data can be loaded
    4. If validation fails, restore backup
    """
    backup_path = file_path + ".backup"

    # Create backup if file exists
    if os.path.exists(file_path):
        import shutil
        shutil.copy2(file_path, backup_path)

    try:
        # Write new data
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        # Validate by loading
        with open(file_path, 'r', encoding='utf-8') as f:
            json.load(f)

        print(f"✅ Successfully saved: {file_path}")

    except Exception as e:
        print(f"❌ ERROR: Failed to save {file_path}: {e}")

        # Restore backup
        if os.path.exists(backup_path):
            shutil.copy2(backup_path, file_path)
            print(f"✅ Backup restored from: {backup_path}")

        sys.exit(1)
```

#### Strategy 1.2: JSON Schema Validation
```python
def validate_progress_json(data: Dict) -> bool:
    """
    Validate progress.json structure.

    Required fields:
    - metadata (dict)
    - progress (dict)
    - current_session (dict)
    - session_history (list)
    - statistics (dict)
    """
    required_keys = ["metadata", "progress", "current_session",
                     "session_history", "statistics", "preferences"]

    for key in required_keys:
        if key not in data:
            print(f"❌ Missing required key: {key}")
            return False

    return True
```

#### Strategy 1.3: Recovery Mode
```python
def recovery_mode():
    """
    Recovery mode to rebuild corrupted files.

    1. Check for backups
    2. Offer to restore from backup
    3. If no backup, create fresh files with defaults
    4. Preserve whatever data can be salvaged
    """
    print("🔧 RECOVERY MODE")
    print("="*80)

    # Check for backups
    backup_files = [
        (PROGRESS_PATH + ".backup", PROGRESS_PATH),
        (SYLLABUS_PATH + ".backup", SYLLABUS_PATH)
    ]

    for backup, original in backup_files:
        if os.path.exists(backup):
            response = input(f"Restore {original} from backup? (yes/no): ")
            if response.lower() in ['yes', 'y']:
                shutil.copy2(backup, original)
                print(f"✅ Restored: {original}")
```

**Implementation:** Add backup logic to `save_json()` function and recovery command.

---

## Failure Scenario 2: Internet Research Failure (New Topic Agent)

### Description
When adding a new topic, the system is supposed to research the topic online to gather information. However:
- No internet connection
- API rate limits exceeded
- Search service down
- Invalid search results

### Impact
- **Severity:** MEDIUM
- New Topic Agent cannot automatically gather information
- User must manually input all details
- Less intelligent topic placement

### Detection
```python
# During internet research:
try:
    # Internet research here
    search_results = web_search(topic_name)
except Exception as e:
    print(f"⚠️  Internet research failed: {e}")
    # Fall back to manual input
```

### Counter-Strategies

#### Strategy 2.1: Graceful Degradation with Manual Input
```python
def research_topic_with_fallback(topic_name: str) -> Dict:
    """
    Research topic with automatic fallback to manual input.

    1. Try internet research
    2. If fails, ask user for information
    3. Provide helpful prompts and examples
    """
    print(f"🔍 Researching topic: {topic_name}")

    try:
        # Attempt internet research
        from web_research import search_and_analyze
        research_data = search_and_analyze(topic_name)
        print("✅ Internet research successful!")
        return research_data

    except Exception as e:
        print(f"⚠️  Internet research failed: {e}")
        print("📝 Falling back to manual input...")
        print()

        # Manual input with helpful prompts
        return manual_topic_input(topic_name)

def manual_topic_input(topic_name: str) -> Dict:
    """
    Manually input topic details with helpful guidance.
    """
    print(f"Please provide details for: {topic_name}")
    print()
    print("💡 TIP: You can research this topic yourself and provide:")
    print("   - What concepts it covers")
    print("   - What you need to know before learning it")
    print("   - How long it might take to learn")
    print()

    # ... rest of manual input logic ...
```

#### Strategy 2.2: Cached Research Results
```python
def get_cached_research(topic_name: str) -> Optional[Dict]:
    """
    Check if we have cached research for similar topics.

    Benefits:
    - Faster topic addition
    - Works offline
    - Consistent results
    """
    cache_file = "learning_system/research_cache.json"

    if os.path.exists(cache_file):
        cache = load_json(cache_file)

        # Check for exact match
        if topic_name.lower() in cache:
            print(f"✅ Using cached research for: {topic_name}")
            return cache[topic_name.lower()]

        # Check for similar topics
        for cached_topic in cache.keys():
            similarity = calculate_similarity(topic_name, cached_topic)
            if similarity > 0.8:
                print(f"✅ Using cached research for similar topic: {cached_topic}")
                return cache[cached_topic]

    return None
```

#### Strategy 2.3: Community Database of Topics
```python
def download_community_syllabus():
    """
    Download pre-researched topics from community database.

    This provides:
    - Common topics (Python, Docker, etc.)
    - Pre-filled metadata
    - Curated subtopics and prerequisites
    """
    community_url = "https://learning-system.example.com/topics.json"

    try:
        response = requests.get(community_url, timeout=5)
        community_topics = response.json()

        # Merge with local syllabus
        merge_community_topics(community_topics)

        print(f"✅ Downloaded {len(community_topics)} community topics")

    except Exception as e:
        print(f"⚠️  Could not download community topics: {e}")
```

**Implementation:** Already implemented manual fallback. Add caching and community database.

---

## Failure Scenario 3: File Not Found (Topic References Missing File)

### Description
A topic in the syllabus references a file (e.g., `MCP_Complete_Tutorial_Chapter_1.md`) but:
- File was deleted
- File was moved to different location
- File path is incorrect
- User working on different computer without files

### Impact
- **Severity:** MEDIUM
- Cannot display file content
- Learning experience degraded
- User might get confused

### Detection
```python
# Current detection:
if topic["file_path"]:
    file_full_path = os.path.join(REPO_ROOT, topic["file_path"])
    if os.path.exists(file_full_path):
        # Read file
    else:
        print(f"⚠️  File not found: {file_full_path}")
```

### Counter-Strategies

#### Strategy 3.1: Smart File Search
```python
def find_file_smart(filename: str, search_paths: List[str]) -> Optional[str]:
    """
    Intelligently search for missing file.

    Search order:
    1. Original path
    2. Common locations (docs/, tutorials/, etc.)
    3. Recursive search from repo root
    4. Ask user for location
    """
    # Try common locations
    common_dirs = [
        "",
        "docs/",
        "tutorials/",
        "chapters/",
        "../",
    ]

    for dir_path in common_dirs:
        test_path = os.path.join(REPO_ROOT, dir_path, filename)
        if os.path.exists(test_path):
            print(f"✅ Found file at: {test_path}")
            return test_path

    # Recursive search
    for root, dirs, files in os.walk(REPO_ROOT):
        if filename in files:
            found_path = os.path.join(root, filename)
            print(f"✅ Found file at: {found_path}")
            return found_path

    # Ask user
    print(f"❓ Cannot find file: {filename}")
    user_path = input("   Enter correct path (or press Enter to skip): ")
    if user_path and os.path.exists(user_path):
        return user_path

    return None
```

#### Strategy 3.2: Download Missing Files
```python
def download_missing_file(filename: str) -> bool:
    """
    Download missing file from repository.

    If file is part of original tutorial, download from:
    - GitHub repository
    - Tutorial website
    - Backup server
    """
    download_sources = [
        f"https://raw.githubusercontent.com/user/repo/main/{filename}",
        f"https://tutorials.example.com/files/{filename}",
    ]

    for source_url in download_sources:
        try:
            response = requests.get(source_url, timeout=10)
            if response.status_code == 200:
                # Save file
                save_path = os.path.join(REPO_ROOT, filename)
                with open(save_path, 'w', encoding='utf-8') as f:
                    f.write(response.text)
                print(f"✅ Downloaded: {filename}")
                return True
        except Exception:
            continue

    return False
```

#### Strategy 3.3: Offline Learning Mode
```python
def enable_offline_mode():
    """
    Enable offline learning mode.

    Features:
    - Use cached file contents
    - Display topic metadata even without file
    - Provide alternative resources
    - Mark topics for later when files available
    """
    print("📴 OFFLINE MODE ENABLED")
    print()
    print("Features:")
    print("   • Learn from cached content")
    print("   • Topic overviews without files")
    print("   • Mark topics for later")
    print()
```

**Implementation:** Add smart file search and file repair functionality.

---

## Failure Scenario 4: Session Interruption (Unsaved Progress)

### Description
User starts a learning session but doesn't save before:
- Computer crashes
- Power outage
- Application forced quit
- User forgets to save

### Impact
- **Severity:** MEDIUM-HIGH
- Lost learning progress
- User frustration
- Time wasted
- Might discourage continued use

### Detection
```python
# Detect unsaved session on next start:
if progress["current_session"]["is_active"]:
    # Session was not properly saved
    print("⚠️  Unsaved session detected!")
```

### Counter-Strategies

#### Strategy 4.1: Auto-Save Every N Minutes
```python
def auto_save_session(progress_data: Dict, interval_minutes: int = 5):
    """
    Automatically save progress at regular intervals.

    Implementation:
    1. Background thread checks time since last save
    2. Auto-saves progress every N minutes
    3. Doesn't interrupt user
    4. Creates timestamped checkpoints
    """
    import threading
    import time

    def save_worker():
        while progress_data["current_session"]["is_active"]:
            time.sleep(interval_minutes * 60)

            # Create checkpoint
            checkpoint_file = f"{PROGRESS_PATH}.checkpoint"
            save_json(checkpoint_file, progress_data)
            print(f"💾 Auto-saved checkpoint at {datetime.now().strftime('%H:%M:%S')}")

    # Start background thread
    thread = threading.Thread(target=save_worker, daemon=True)
    thread.start()
```

#### Strategy 4.2: Session Recovery on Restart
```python
def recover_unsaved_session():
    """
    Recover unsaved session from previous run.

    1. Detect unsaved session
    2. Estimate progress from timestamps
    3. Offer to restore session
    4. Calculate partial time spent
    """
    progress = load_json(PROGRESS_PATH)

    if progress["current_session"]["is_active"]:
        print("="*80)
        print("⚠️  UNSAVED SESSION DETECTED")
        print("="*80)
        print()

        session_start = datetime.fromisoformat(progress["current_session"]["start_time"])
        elapsed = datetime.now() - session_start

        print(f"📅 Session started: {session_start.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"⏱️  Estimated duration: {format_duration(int(elapsed.total_seconds() / 60))}")
        print(f"📚 Topic: {progress['progress']['current_topic_id']}")
        print()

        response = input("Recover this session? (yes/no): ")
        if response.lower() in ['yes', 'y']:
            print("✅ Session recovered!")
            print("   Use 'python learning_agents.py save' to save progress.")
            return True
        else:
            # Clear session
            progress["current_session"]["is_active"] = False
            save_json(PROGRESS_PATH, progress)
            print("❌ Session discarded.")
            return False
```

#### Strategy 4.3: Exit Handler (Save on Exit)
```python
import atexit
import signal

def save_on_exit():
    """
    Automatically save progress when program exits.

    Handles:
    - Normal exit
    - Ctrl+C (SIGINT)
    - Kill signal (SIGTERM)
    """
    progress = load_json(PROGRESS_PATH)

    if progress["current_session"]["is_active"]:
        print("\n⚠️  Saving session before exit...")

        # Quick save without user input
        session_start = datetime.fromisoformat(progress["current_session"]["start_time"])
        duration = int((datetime.now() - session_start).total_seconds() / 60)

        progress["progress"]["total_time_spent_minutes"] += duration
        progress["current_session"]["is_active"] = False
        progress["current_session"]["notes"].append("Auto-saved on exit")

        save_json(PROGRESS_PATH, progress)
        print("✅ Session auto-saved!")

# Register exit handler
atexit.register(save_on_exit)

# Handle Ctrl+C
def signal_handler(sig, frame):
    save_on_exit()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)
```

**Implementation:** Add auto-save, recovery, and exit handlers.

---

## Failure Scenario 5: Prerequisite Loop (Circular Dependencies)

### Description
When adding new topics, user creates circular dependencies:
- Topic A requires Topic B
- Topic B requires Topic C
- Topic C requires Topic A

This creates an infinite loop where you can never complete any topic.

### Impact
- **Severity:** MEDIUM
- Syllabus becomes unusable
- Cannot determine learning order
- System might crash or hang
- User confusion

### Detection
```python
def detect_prerequisite_loop(syllabus: Dict, new_topic: Dict) -> bool:
    """
    Detect circular dependencies in prerequisites.

    Algorithm:
    1. Build dependency graph
    2. Check for cycles using DFS
    3. Return True if cycle found
    """
    # Build graph
    graph = {}
    for phase in syllabus["phases"]:
        for topic in phase["topics"]:
            graph[topic["topic_id"]] = topic["prerequisites"]

    # Add new topic
    graph[new_topic["topic_id"]] = new_topic["prerequisites"]

    # Check for cycles
    return has_cycle(graph)
```

### Counter-Strategies

#### Strategy 5.1: Cycle Detection Before Adding Topic
```python
def has_cycle(graph: Dict[int, List[int]]) -> bool:
    """
    Detect cycles in directed graph using DFS.

    Returns True if cycle exists, False otherwise.
    """
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {node: WHITE for node in graph}

    def dfs(node):
        if color[node] == GRAY:
            return True  # Cycle found
        if color[node] == BLACK:
            return False  # Already processed

        color[node] = GRAY
        for neighbor in graph.get(node, []):
            if dfs(neighbor):
                return True

        color[node] = BLACK
        return False

    for node in graph:
        if color[node] == WHITE:
            if dfs(node):
                return True

    return False

def validate_new_topic_prerequisites(syllabus: Dict, new_topic: Dict) -> bool:
    """
    Validate new topic doesn't create circular dependencies.
    """
    # Build temporary graph with new topic
    temp_syllabus = copy.deepcopy(syllabus)
    # Add new topic temporarily
    temp_syllabus["phases"][0]["topics"].append(new_topic)

    # Check for cycles
    if detect_prerequisite_loop(temp_syllabus, new_topic):
        print("❌ ERROR: Adding this topic creates circular dependencies!")
        print("   Please review prerequisite selection.")
        return False

    return True
```

#### Strategy 5.2: Prerequisite Path Visualization
```python
def visualize_prerequisite_path(syllabus: Dict, topic_id: int):
    """
    Visualize prerequisite chain for a topic.

    Shows:
    - Direct prerequisites
    - Indirect prerequisites (prerequisites of prerequisites)
    - Complete learning path
    """
    def get_all_prerequisites(tid, visited=None):
        if visited is None:
            visited = set()

        if tid in visited:
            return []  # Already seen

        visited.add(tid)
        topic = get_topic_by_id(syllabus, tid)

        prereqs = [tid]
        for prereq_id in topic["prerequisites"]:
            prereqs.extend(get_all_prerequisites(prereq_id, visited))

        return prereqs

    all_prereqs = get_all_prerequisites(topic_id)

    print(f"Prerequisite chain for Topic {topic_id}:")
    for i, prereq_id in enumerate(reversed(all_prereqs)):
        indent = "  " * i
        topic = get_topic_by_id(syllabus, prereq_id)
        print(f"{indent}└─ Topic {prereq_id}: {topic['title']}")
```

#### Strategy 5.3: Automatic Prerequisite Suggestion
```python
def suggest_prerequisites(syllabus: Dict, new_topic: Dict) -> List[int]:
    """
    Intelligently suggest prerequisites for new topic.

    Based on:
    - Topic difficulty
    - Topic phase
    - Similar topics
    - Common patterns
    """
    suggestions = []

    # For beginner topics, suggest Python basics
    if new_topic["difficulty"] == "beginner":
        suggestions.append(3)  # Python Basics

    # For infrastructure topics, suggest client-server
    if "infrastructure" in new_topic["title"].lower() or "docker" in new_topic["title"].lower():
        suggestions.append(2)  # Client-Server
        suggestions.append(7)  # Infrastructure Concepts

    # For agent topics, suggest MCP fundamentals
    if "agent" in new_topic["title"].lower():
        suggestions.extend([1, 4, 5, 6])  # MCP fundamentals

    print("💡 Suggested prerequisites based on topic:")
    for prereq_id in suggestions:
        topic = get_topic_by_id(syllabus, prereq_id)
        print(f"   • Topic {prereq_id}: {topic['title']}")

    return suggestions
```

**Implementation:** Add cycle detection before allowing topic addition.

---

## Additional Failure Scenarios (Brief)

### Scenario 6: Concurrent Access (Multiple Sessions)
**Problem:** User runs learning agents from two terminals simultaneously
**Solution:** File locking mechanism, detect active sessions, warn user

### Scenario 7: Encoding Issues
**Problem:** Non-UTF-8 characters in files cause read errors
**Solution:** Try multiple encodings, fallback to latin-1 or binary mode

### Scenario 8: Disk Space Full
**Problem:** Cannot save progress due to disk full
**Solution:** Check disk space before writes, cleanup old backups

### Scenario 9: Permission Errors
**Problem:** No write permissions for JSON files
**Solution:** Check permissions, suggest running with sudo or changing location

### Scenario 10: Version Incompatibility
**Problem:** Old progress.json format doesn't work with new version
**Solution:** Version migration scripts, backward compatibility

---

## Implementation Priority

### High Priority (Must implement)
1. ✅ Automatic backups (Scenario 1)
2. ✅ Manual fallback for research (Scenario 2)
3. ✅ Session recovery (Scenario 4)
4. ✅ Cycle detection (Scenario 5)

### Medium Priority (Should implement)
5. File search and repair (Scenario 3)
6. Auto-save (Scenario 4)
7. Prerequisite visualization (Scenario 5)

### Low Priority (Nice to have)
8. Concurrent access control (Scenario 6)
9. Community topics database (Scenario 2)
10. Version migration (Scenario 10)

---

## Testing Checklist

- [ ] Test with corrupted JSON files
- [ ] Test with no internet connection
- [ ] Test with missing files
- [ ] Test session interruption (Ctrl+C)
- [ ] Test circular prerequisites
- [ ] Test with different file encodings
- [ ] Test with low disk space
- [ ] Test with read-only files
- [ ] Test concurrent sessions
- [ ] Test version upgrades

---

## Monitoring and Logging

### Log Important Events
```python
import logging

logging.basicConfig(
    filename='learning_system/learning.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Log events
logging.info("Session started")
logging.warning("File not found: chapter1.md")
logging.error("JSON corrupted, using backup")
```

### Health Checks
```python
def system_health_check():
    """
    Perform health check before starting.

    Checks:
    - JSON files valid
    - Required files exist
    - Disk space available
    - Permissions OK
    """
    print("🏥 Running system health check...")

    checks = [
        check_json_validity(),
        check_file_permissions(),
        check_disk_space(),
        check_required_files(),
    ]

    if all(checks):
        print("✅ All systems healthy!")
        return True
    else:
        print("⚠️  Some issues detected. See above.")
        return False
```

---

## Conclusion

By implementing these counter-strategies, the learning system becomes:
- **Robust:** Handles errors gracefully
- **Reliable:** Data is protected with backups
- **Resilient:** Recovers from interruptions
- **User-friendly:** Clear error messages and guidance

The system should **fail gracefully** and **never lose user data**.

---

**Last Updated:** 2025-11-08
**Next Review:** After testing phase
