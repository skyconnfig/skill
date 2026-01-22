#!/bin/bash
# Repository Packaging Script for GitHub Releases
# Usage: ./package-release.sh [version] [output-dir]

set -e

# Get version from argument or use current date
VERSION=${1:-$(date +%Y.%m.%d-%H%M%S)}

# Get repository name from git or use current directory name
REPO_NAME=$(basename $(git rev-parse --show-toplevel 2>/dev/null || echo "project"))

# Output directory (default: ./releases)
OUTPUT_DIR=${2:-./releases}

echo "📦 Packaging repository for release..."
echo "   Repository: $REPO_NAME"
echo "   Version: $VERSION"
echo "   Output: $OUTPUT_DIR"

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Get git archive
echo "   Creating archives..."

# Create ZIP archive (Windows/macOS friendly)
git archive --format zip --output "$OUTPUT_DIR/${REPO_NAME}-${VERSION}.zip" HEAD
echo "   ✅ ${REPO_NAME}-${VERSION}.zip"

# Create TAR.GZ archive (Linux/Unix friendly)
git archive --format tar.gz --output "$OUTPUT_DIR/${REPO_NAME}-${VERSION}.tar.gz" HEAD
echo "   ✅ ${REPO_NAME}-${VERSION}.tar.gz"

# Create archives without .git folder (clean archives)
echo "   Creating clean archives (without .git)..."

# For clean archives, we need to exclude .git
git archive --format zip --output "$OUTPUT_DIR/${REPO_NAME}-${VERSION}-clean.zip" HEAD --prefix="${REPO_NAME}-${VERSION}/" -- '.gitignore' ':!.git'
git archive --format tar.gz --output "$OUTPUT_DIR/${REPO_NAME}-${VERSION}-clean.tar.gz" HEAD --prefix="${REPO_NAME}-${VERSION}/" -- '.gitignore' ':!.git'
echo "   ✅ ${REPO_NAME}-${VERSION}-clean.zip"
echo "   ✅ ${REPO_NAME}-${VERSION}-clean.tar.gz"

# List created files
echo ""
echo "📁 Created files in $OUTPUT_DIR:"
ls -lh "$OUTPUT_DIR"

# Calculate checksums
echo ""
echo "🔐 Generating SHA256 checksums..."
cd "$OUTPUT_DIR"
for file in *.zip *.tar.gz; do
    if [ -f "$file" ]; then
        sha256sum "$file" > "${file}.sha256"
        echo "   ✅ ${file}.sha256"
    fi
done

echo ""
echo "✨ Packaging complete!"
echo ""
echo "📖 Usage example:"
echo "   gh release create $VERSION --generate-notes"
echo "   gh release upload $VERSION ${REPO_NAME}-${VERSION}.zip"
echo "   gh release upload $VERSION ${REPO_NAME}-${VERSION}.tar.gz"
