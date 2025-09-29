#!/usr/bin/env python3
"""
Validate that all configuration files have consistent tool versions.
This script checks that versions.py matches the generated configuration files.
"""

import re
import sys
from pathlib import Path

# Add the .devcontainer directory to Python path to import versions
sys.path.insert(0, str(Path(__file__).parent))

try:
    from versions import *
except ImportError:
    print("❌ Error: Could not import versions.py")
    sys.exit(1)


def check_file_versions():
    """Check that generated files match the version configuration."""
    project_root = Path(__file__).parent.parent
    errors = []
    
    # Check requirements.txt
    requirements_path = project_root / "requirements.txt"
    if requirements_path.exists():
        content = requirements_path.read_text()
        
        # Check Black version
        black_match = re.search(r'black==([^\s#]+)', content)
        if not black_match or black_match.group(1) != BLACK_VERSION:
            errors.append(f"requirements.txt: Black version mismatch (expected {BLACK_VERSION})")
        
        # Check Flake8 version
        flake8_match = re.search(r'flake8==([^\s#]+)', content)
        if not flake8_match or flake8_match.group(1) != FLAKE8_VERSION:
            errors.append(f"requirements.txt: Flake8 version mismatch (expected {FLAKE8_VERSION})")
    
    # Check .pre-commit-config.yaml
    precommit_path = project_root / ".pre-commit-config.yaml"
    if precommit_path.exists():
        content = precommit_path.read_text()
        
        # Extract all rev: lines
        rev_matches = re.findall(r'rev:\s+([^\s]+)', content)
        expected_versions = [BLACK_VERSION, ISORT_VERSION, FLAKE8_VERSION, BANDIT_VERSION, PRE_COMMIT_HOOKS_VERSION]
        
        if len(rev_matches) != len(expected_versions):
            errors.append(f".pre-commit-config.yaml: Expected {len(expected_versions)} rev entries, found {len(rev_matches)}")
        else:
            for i, (found, expected) in enumerate(zip(rev_matches, expected_versions)):
                if found != expected:
                    errors.append(f".pre-commit-config.yaml: Rev {i+1} version mismatch (found {found}, expected {expected})")
    
    return errors


def main():
    """Validate version consistency across all configuration files."""
    print("🔍 Validating version consistency...")
    
    errors = check_file_versions()
    
    if errors:
        print("❌ Version inconsistencies found:")
        for error in errors:
            print(f"  • {error}")
        print("\n💡 Run 'python .devcontainer/generate-configs.py' to fix inconsistencies")
        sys.exit(1)
    else:
        print("✅ All versions are consistent!")
        print("🎯 Configuration files match versions.py")


if __name__ == "__main__":
    main()