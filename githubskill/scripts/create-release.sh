#!/bin/bash
# Automated GitHub Release Creation Script
# Usage: ./create-release.sh <version> [assets...]

set -e

VERSION=$1
REPO_OWNER=${2:-$(gh repo view --json owner -q .owner.login)}
REPO_NAME=${3:-$(gh repo view --json name -q .name)}

if [ -z "$VERSION" ]; then
    echo "Usage: $0 <version> [assets...]"
    echo "Example: $0 v1.0.0 ./dist.zip"
    exit 1
fi

shift  # Remove version from arguments

echo "🚀 Creating release $VERSION for $REPO_OWNER/$REPO_NAME..."

# Create release with auto-generated notes
echo "📝 Creating release with auto-generated notes..."
gh release create "$VERSION" --generate-notes --repo "$REPO_OWNER/$REPO_NAME"

# Upload assets if provided
if [ $# -gt 0 ]; then
    echo "📦 Uploading assets..."
    for asset in "$@"; do
        if [ -f "$asset" ]; then
            echo "  📤 Uploading: $asset"
            gh release upload "$VERSION" "$asset" --repo "$REPO_OWNER/$REPO_NAME"
        else
            echo "  ⚠️  File not found: $asset"
        fi
    done
fi

# Display release info
echo ""
echo "✅ Release $VERSION created successfully!"
echo ""
gh release view "$VERSION" --repo "$REPO_OWNER/$REPO_NAME"
