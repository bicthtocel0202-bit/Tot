#!/usr/bin/env python3
"""
Utility script to process video IDs from links_id_only.txt
"""

import os
import sys

# Validation constants
MIN_VIDEO_ID_LENGTH = 5


def read_video_ids(filename='links_id_only.txt'):
    """
    Read video IDs from the specified file.
    
    Args:
        filename: Name of the file containing video IDs
        
    Returns:
        List of video IDs
    """
    if not os.path.exists(filename):
        print(f"Error: {filename} not found!")
        return []
    
    with open(filename, 'r', encoding='utf-8') as f:
        ids = [line.strip() for line in f if line.strip()]
    
    return ids


def display_ids(ids):
    """Display the video IDs with numbering."""
    print(f"\nFound {len(ids)} video IDs:")
    print("-" * 40)
    for idx, video_id in enumerate(ids, 1):
        print(f"{idx}. {video_id}")
    print("-" * 40)


def validate_ids(ids):
    """
    Validate video ID format.
    
    Args:
        ids: List of video IDs to validate
        
    Returns:
        List of tuples (id, is_valid, message)
    """
    results = []
    for video_id in ids:
        if not video_id:
            results.append((video_id, False, "Empty ID"))
        elif len(video_id) < MIN_VIDEO_ID_LENGTH:
            results.append((video_id, False, f"ID too short (minimum {MIN_VIDEO_ID_LENGTH} characters)"))
        # Video IDs in this collection follow a pattern ending with a digit
        elif not video_id[-1].isdigit():
            results.append((video_id, False, "ID should end with a digit"))
        else:
            results.append((video_id, True, "Valid"))
    
    return results


def main():
    """Main function to process video IDs."""
    print("=" * 40)
    print("Video ID Processor")
    print("=" * 40)
    
    # Read IDs from file
    ids = read_video_ids()
    
    if not ids:
        print("No video IDs found!")
        sys.exit(1)
    
    # Display IDs
    display_ids(ids)
    
    # Validate IDs
    print("\nValidation Results:")
    print("-" * 40)
    validation_results = validate_ids(ids)
    
    all_valid = True
    for video_id, is_valid, message in validation_results:
        status = "✓" if is_valid else "✗"
        print(f"{status} {video_id}: {message}")
        if not is_valid:
            all_valid = False
    
    print("-" * 40)
    
    if all_valid:
        print("\n✓ All video IDs are valid!")
    else:
        print("\n✗ Some video IDs have issues.")
    
    return 0 if all_valid else 1


if __name__ == "__main__":
    sys.exit(main())
