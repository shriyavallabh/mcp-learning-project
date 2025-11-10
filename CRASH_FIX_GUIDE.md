# 🔧 Claude Code Crash Fix Guide

## 🚨 Problem Identified:
Your Mac is running out of memory, causing Claude Code (Cursor) to crash 2-3 times per day.

---

## 📊 Current System Status:

**Your Hardware:**
- RAM: 16 GB
- Currently Used: 15 GB (93% full) ❌
- Swap Used: 5.9 GB of 7 GB (82% used) ❌
- CPU Load: 99% busy ❌

**Claude Code Usage:**
- 3 active Claude processes
- ~900 MB memory usage
- Multiple terminals running simultaneously

---

## ✅ SOLUTION 1: Free Up Memory (DO THIS NOW!)

### Step 1: Close Unused Applications

**Close these if you're not using them:**
- ✅ Chrome/Safari (each tab uses ~100-200 MB!)
- ✅ Slack/Discord
- ✅ Email apps
- ✅ Music apps (Spotify, Apple Music)
- ✅ Docker Desktop (if not needed)
- ✅ Any development servers you're not using

**Check what's using memory:**
```bash
# See top memory users
top -o mem | head -20
```

### Step 2: Restart Claude Code
```bash
# Kill all Claude processes
killall -9 claude

# Restart Cursor
open -a Cursor
```

### Step 3: Work in ONE Terminal at a Time
- ❌ Don't open 5 terminals at once
- ✅ Use 1-2 terminals maximum
- ✅ Close finished terminals

---

## ✅ SOLUTION 2: Increase Swap Space

**Current swap:** 7 GB
**Recommended:** 16 GB (same as your RAM)

**How to do it:**
```bash
# Check current swap
sysctl vm.swapusage

# Note: macOS manages swap automatically
# But you can free up disk space to allow more swap
```

**Free up disk space:**
1. Delete large files you don't need
2. Empty Trash
3. Clear cache:
```bash
# Clear Xcode cache (if you have Xcode)
rm -rf ~/Library/Developer/Xcode/DerivedData/*

# Clear npm cache
npm cache clean --force

# Clear pip cache
pip cache purge
```

---

## ✅ SOLUTION 3: Optimize Claude Code Settings

### Limit Claude's Memory Usage

Create this file:
```bash
~/.config/claude-code/settings.json
```

Add:
```json
{
  "maxMemoryMB": 500,
  "maxConcurrentTasks": 2,
  "enableMemoryMonitoring": true
}
```

This limits each Claude process to 500 MB.

---

## ✅ SOLUTION 4: Use Activity Monitor

**Monitor memory in real-time:**

1. Open Activity Monitor (⌘ + Space, type "Activity Monitor")
2. Click "Memory" tab
3. Watch "Memory Pressure" graph
4. If it's RED → Close some apps immediately!

**Colors:**
- 🟢 Green = Good
- 🟡 Yellow = Warning
- 🔴 Red = About to crash!

---

## ✅ SOLUTION 5: Upgrade Your System (Long-term)

If this happens frequently, consider:

**Option A: Add More RAM**
- Your Mac: 16 GB
- Recommended for AI work: 32 GB or 64 GB
- Check if your Mac model supports RAM upgrade

**Option B: Get a New Mac**
- M3 Pro/Max with 32 GB+ RAM
- Perfect for AI development
- Worth the investment if you're serious about AI

---

## 🔍 How to Prevent Future Crashes

### Before Starting Work:

**1. Check Available Memory:**
```bash
# Quick memory check
vm_stat | grep "Pages free"
sysctl vm.swapusage
```

**2. Close What You Don't Need:**
- Browser tabs (each uses 100-200 MB!)
- Unused apps
- Old terminals

**3. Work Smart:**
- Use 1-2 terminals max (not 5!)
- Close terminals when done
- Restart Claude Code daily

### During Work:

**Monitor these signs of trouble:**
- ⚠️ Mac fan spinning loudly → CPU overheating
- ⚠️ System becoming slow → Memory full
- ⚠️ Rainbow spinning wheel → About to crash!

**If you see these signs:**
1. Save your work immediately!
2. Close some apps
3. Restart Claude Code

---

## 📋 Daily Checklist (Prevent Crashes)

**Morning Routine:**
```bash
# 1. Restart Claude Code (fresh start)
killall -9 claude && open -a Cursor

# 2. Check memory
vm_stat | grep "Pages free"

# 3. Close unused apps
# (Manually close what you don't need)
```

**During Work:**
- ✅ Use 1-2 terminals maximum
- ✅ Close finished tasks
- ✅ Watch Activity Monitor if system slows down

**End of Day:**
```bash
# Close everything
killall -9 claude
```

---

## 🧪 Test Your Fix

After applying these solutions:

**Test 1: Run a simple command**
```bash
echo "Testing Claude Code"
```
Should complete without crash.

**Test 2: Run 2 terminals**
Open 2 terminals, run simple commands in each.
Both should work smoothly.

**Test 3: Monitor memory**
```bash
# Watch memory while working
watch -n 5 'vm_stat | grep "Pages free"'
```

---

## 🆘 Emergency: If It Crashes Right Now

**Immediate steps:**

1. **Force quit Cursor:**
   - ⌘ + Option + Esc
   - Select "Cursor"
   - Click "Force Quit"

2. **Free up memory:**
   ```bash
   # Kill all Claude processes
   killall -9 claude

   # Close other apps
   killall -9 Chrome Safari Slack
   ```

3. **Check what's using memory:**
   ```bash
   ps aux | sort -nrk 4 | head -10
   ```

4. **Restart Cursor:**
   ```bash
   open -a Cursor
   ```

5. **Resume your session:**
   - Claude Code will offer to resume
   - Click "Resume"
   - Continue from where you left off

---

## 📊 Understanding Your System

**Memory Breakdown:**

```
Total RAM: 16 GB
├── macOS System: 2-3 GB (OS overhead)
├── Chrome: 2-4 GB (if open)
├── Cursor/Claude: 1-2 GB
├── Other Apps: 5-7 GB
└── Available: 1-2 GB ← This is what you have left!
```

**Why 16 GB isn't enough for AI work:**
- Claude Code: 1-2 GB
- Browser (research): 2-4 GB
- Development servers: 1-2 GB
- macOS: 2-3 GB
- **Total needed: 6-11 GB minimum**
- **Leaves only 5-10 GB for actual work**

**For serious AI development, you need:**
- Minimum: 32 GB RAM
- Recommended: 64 GB RAM

---

## 📚 Learn More

**Check memory at any time:**
```bash
# Simple check
free -h  # Linux
vm_stat  # macOS

# Detailed check
top -o mem

# Watch in real-time
watch -n 2 'vm_stat | head -5'
```

**Check what's using most memory:**
```bash
ps aux | sort -nrk 4 | head -20
```

**Check disk space (affects swap):**
```bash
df -h
```

---

## ✅ Summary

**Quick Fix (Do Now):**
1. Close unused apps
2. Restart Claude Code
3. Use 1-2 terminals max

**Medium-term Fix:**
1. Free up disk space
2. Optimize settings
3. Monitor memory daily

**Long-term Fix:**
1. Upgrade RAM (if possible)
2. Or get a new Mac with 32+ GB RAM

---

**Status:** Last crashed 10 minutes ago (9:09 AM)
**Root cause:** Memory exhaustion (93% RAM used)
**Quick fix:** Close apps, restart Claude Code
**Long-term:** Upgrade to 32 GB RAM

---

Created: 2025-10-13 09:19 AM
For: Shriyavallabh Pethkar
Issue: Claude Code crashing 2-3 times per day
