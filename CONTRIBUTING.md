# Contributing Guidelines 🤝

Thank you for your interest in contributing! This document outlines how to contribute to the Python Basics Learning Journey repository.

---

## Table of Contents

- [Code of Conduct](#-code-of-conduct)
- [Getting Started](#-getting-started)
- [Types of Contributions](#-types-of-contributions)
- [Contribution Process](#-contribution-process)
- [Code Guidelines](#-code-guidelines)
- [Commit Messages](#-commit-messages)
- [Pull Request Process](#-pull-request-process)
- [Reporting Issues](#-reporting-issues)
- [Recognition](#-recognition)

---

## 📋 Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for all contributors.

### Our Standards

**Be respectful:**
- Treat all community members with respect
- Accept constructive criticism gracefully
- Focus on the code, not the person

**Be inclusive:**
- Welcome contributors at all skill levels
- Encourage and support each other
- Celebrate diverse perspectives

**Be honest:**
- Report issues accurately
- Don't claim credit for others' work
- Acknowledge and give credit appropriately

### Enforcement

Violations of the Code of Conduct may result in:
- Warning
- Temporary ban
- Permanent removal from the project

Report violations to the maintainer directly.

---

## 🚀 Getting Started

### 1. Fork the Repository

```bash
# Click "Fork" on GitHub repository page
# This creates a copy under your account
```

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR-USERNAME/python-basics.git
cd python-basics
```

### 3. Add Upstream Remote

```bash
# Keep your fork synced with original
git remote add upstream https://github.com/vishal-kushwaha-9912/python-basics.git
git fetch upstream
```

### 4. Create Feature Branch

```bash
# Never work on main branch
git checkout -b feature/your-feature-name
```

### 5. Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate          # macOS/Linux
venv\Scripts\activate             # Windows

# Install development dependencies
pip install jupyter pylint black
```

---

## 📝 Types of Contributions

### 🐛 Bug Fixes

**Report bugs** through GitHub Issues with:
- Clear description of the problem
- Steps to reproduce
- Expected behavior
- Actual behavior
- Python version and OS

**Fix bugs** by:
1. Creating issue first
2. Assigning yourself
3. Making fix in feature branch
4. Adding test/verification
5. Submitting PR with issue reference

### 📚 Documentation Improvements

- Fix typos
- Clarify explanations
- Add examples
- Improve comments
- Add docstrings
- Update README sections

### ✨ New Features

- Add new concept files
- Create new practice problems
- Add mini-projects
- Improve existing code
- Add better examples

### 🎯 Practice Problems

- Add beginner problems
- Add intermediate challenges
- Add advanced problems
- Provide solutions and explanations

### 💡 Suggestions

- Propose new topics
- Suggest reorganization
- Recommend resources
- Improve learning paths

---

## 🔧 Contribution Process

### Step 1: Identify What to Work On

**Option A: Pick an Open Issue**
- Browse [Issues](https://github.com/vishal-kushwaha-9912/python-basics/issues)
- Comment: "I'd like to work on this"
- Wait for assignment

**Option B: Create New Issue**
1. Click "New Issue"
2. Describe your contribution
3. Wait for feedback
4. Get approval before starting

**Option C: Small Fixes**
- Typos, formatting, small improvements
- Can start directly

### Step 2: Make Your Changes

```bash
# Keep your branch updated
git fetch upstream
git rebase upstream/main

# Make changes
# Edit files, add code, improve docs

# Test thoroughly
python your_test.py
```

### Step 3: Commit Your Changes

```bash
git add .
git commit -m "Add: improved for-loop explanation with examples"
git push origin feature/your-feature-name
```

See [Commit Messages](#-commit-messages) section for guidelines.

### Step 4: Submit Pull Request

1. Go to your fork on GitHub
2. Click "Create Pull Request"
3. Fill in PR template
4. Link related issues (use `Closes #123`)
5. Submit PR

### Step 5: Address Feedback

- Respond to reviewer comments
- Make requested changes
- Push updates to same branch
- Maintain respectful dialogue

### Step 6: Merge

Once approved, your PR will be merged by maintainer.

---

## 📝 Code Guidelines

### Python Style

Follow [PEP 8](https://pep8.org/) with these specifics:

```python
# Good: Clear, readable, follows conventions
def calculate_average(numbers):
    """Calculate average of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Bad: Unclear naming, poor formatting
def calc(n):
    s=sum(n)
    l=len(n)
    return s/l if l else 0
```

### Formatting

```bash
# Use Black for formatting
black filename.py

# Use pylint for linting
pylint filename.py
```

### Comments

```python
# Use clear, helpful comments
# ✅ Good
# Calculate the average by summing all values and dividing by count
average = sum(values) / len(values)

# ❌ Bad
# Get avg
a = s / l  # Calculate average
```

### Naming Conventions

```python
# Variables: lowercase with underscores
user_name = "Vishal"
age = 20

# Constants: UPPERCASE
MAX_ATTEMPTS = 5
PI = 3.14159

# Functions: lowercase with underscores
def calculate_total():
    pass

# Classes: CamelCase (uppercase first letter)
class StudentProgress:
    pass
```

### File Organization

```python
"""
Module docstring at the top.
Brief description of what this file does.
"""

# Standard library imports
import os
import sys

# Third-party imports
import numpy as np

# Local imports
from utils import helper_function

# Constants
MAX_ITEMS = 100

# Classes
class MyClass:
    pass

# Functions
def my_function():
    pass

# Main
if __name__ == "__main__":
    pass
```

---

## 💬 Commit Messages

### Format

```
<type>: <subject>

<body (optional)>

<footer (optional)>
```

### Types

- **Add**: New feature, file, or concept
- **Fix**: Bug fix
- **Improve**: Enhancement to existing code
- **Refactor**: Code reorganization
- **Docs**: Documentation changes
- **Test**: Adding or fixing tests
- **Style**: Formatting, linting

### Examples

```bash
# Good commits
git commit -m "Add: detailed explanation of nested loops"
git commit -m "Fix: typo in list comprehension example"
git commit -m "Improve: make function examples more clear"
git commit -m "Docs: update README with new section"

# Bad commits (avoid)
git commit -m "updated stuff"
git commit -m "fix"
git commit -m "more changes"
```

### Tips

- Use imperative mood: "Add" not "Added"
- First line under 50 characters
- Reference issues: "Fixes #123"
- Be specific and clear

---

## 🔀 Pull Request Process

### PR Title Format

```
[Type] Description of changes
Examples:
[Add] New practice problems for loops
[Fix] Typo in function explanation
[Improve] Better comments in datatypes.py
[Docs] Update README setup instructions
```

### PR Description Template

```markdown
## Description
Brief description of what this PR does.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code improvement

## Related Issues
Closes #123

## Changes Made
- Change 1
- Change 2
- Change 3

## Testing
How was this tested?

## Checklist
- [ ] Code follows style guidelines
- [ ] Comments added for clarity
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Changes tested locally
```

### PR Review Process

1. **Automated Checks**
   - Code formatting validation
   - Basic syntax checks
   
2. **Manual Review**
   - Code quality assessment
   - Content accuracy check
   - Style compliance

3. **Feedback & Revision**
   - Address reviewer comments
   - Make requested changes
   - Request re-review

4. **Approval & Merge**
   - Maintainer approves
   - PR is merged to main
   - Branch is deleted

---

## 🐛 Reporting Issues

### Before Creating an Issue

1. Check existing issues (might be duplicate)
2. Check documentation and FAQ
3. Try troubleshooting steps

### Creating an Issue

Use appropriate template:

**For Bugs:**
```markdown
## Description
Clear description of the bug

## Reproduction Steps
1. Step 1
2. Step 2
3. Step 3

## Expected Behavior
What should happen

## Actual Behavior
What actually happened

## Environment
- Python version: 3.x.x
- OS: Windows/macOS/Linux
- Python file: filename.py

## Screenshots/Code
Include relevant code or screenshots
```

**For Feature Requests:**
```markdown
## Description
What feature would you like?

## Use Case
Why do you need this?

## Suggested Implementation
How might this be implemented?

## Alternatives Considered
Are there other ways to solve this?
```

---

## 🌟 Recognition

### Contributors

All contributors will be:
- ✅ Listed in CONTRIBUTORS.md
- ✅ Credited in commit history
- ✅ Mentioned in CHANGELOG.md
- ✅ Recognized in README

### Contribution Tiers

**🥇 Gold Contributor**
- 20+ contributions
- Significant impact on project

**🥈 Silver Contributor**
- 10+ contributions
- Regular improvements

**🥉 Bronze Contributor**
- 3+ contributions
- Helpful additions

**⭐ Community Member**
- 1+ contributions
- All contributors start here

---

## 📚 Resources

### Documentation
- [PEP 8 Style Guide](https://pep8.org/)
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)

### Tools
- [Black Code Formatter](https://github.com/psf/black)
- [Pylint Linter](https://www.pylint.org/)
- [Python Tutor Visualizer](https://pythontutor.com/)

---

## ❓ FAQ for Contributors

**Q: Do I need to sign a CLA?**  
A: No, just follow the Code of Conduct.

**Q: How long does review take?**  
A: Usually 2-7 days depending on complexity.

**Q: Can I work on multiple issues?**  
A: Yes, but complete or abandon one before starting another.

**Q: Can I modify after PR is submitted?**  
A: Yes, just push to your branch; PR updates automatically.

**Q: What if my PR is rejected?**  
A: That's okay! Get feedback and try again, or work on something else.

**Q: Can I contribute if I'm a beginner?**  
A: Absolutely! This is a learning repository; contributions help everyone.

---

## 🎯 Good First Issues

Looking to contribute? Start with issues tagged:
- `good-first-issue`
- `beginner-friendly`
- `documentation`
- `typo`

---

## 💪 Contribution Ideas

### Easy (1-2 hours)
- [ ] Fix typos and formatting
- [ ] Improve existing comments
- [ ] Add examples to files
- [ ] Update documentation
- [ ] Fix code formatting

### Medium (2-5 hours)
- [ ] Add new practice problems
- [ ] Improve explanations
- [ ] Create new concept guide
- [ ] Add more examples
- [ ] Write tutorial

### Hard (5+ hours)
- [ ] Create new mini-project
- [ ] Reorganize content
- [ ] Build automated tests
- [ ] Add interactive features
- [ ] Create learning path

---

## 🙏 Thank You!

Every contribution, no matter how small, makes this learning resource better for everyone.

We appreciate your time, effort, and passion for helping others learn Python!

---

_Last Updated: August 2026_

---

Have questions? Open an issue or reach out to the maintainer!

Happy contributing! 🚀
