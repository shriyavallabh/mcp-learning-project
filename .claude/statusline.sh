#!/bin/bash

# Read JSON input from stdin
input=$(cat)

# Parse key information using jq (or basic parsing if jq not available)
if command -v jq &> /dev/null; then
    # Using jq for robust parsing
    model=$(echo "$input" | jq -r '.session.model // "claude"')
    tokens=$(echo "$input" | jq -r '.session.totalTokens // 0')
    is_thinking=$(echo "$input" | jq -r '.session.isThinking // false')
else
    # Fallback: basic grep parsing
    tokens=$(echo "$input" | grep -o '"totalTokens":[0-9]*' | grep -o '[0-9]*' || echo "0")
    is_thinking="false"
fi

# Build status line with activity indicator
if [ "$is_thinking" = "true" ]; then
    # Show spinner when Claude is thinking
    status="⚡ WORKING"
else
    # Show ready when waiting for input
    status="✓ Ready"
fi

# Display: [Status] | Tokens: XXXX | Dir: current_dir
echo "$status | Tokens: $tokens | $(basename "$PWD")"
