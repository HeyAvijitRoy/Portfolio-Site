---
layout: default
title: "Saving Your Work Like a Pro: Git & GitHub for C++ Students"
description: "A complete, analogy-driven guide to version control for first-semester computer science students learning C++."
author: "Avijit Roy"
date: 2026-05-22
version: "1.0.0"
permalink: /
nav_order: 1
---

<!-- ============================================================
     SAVING YOUR WORK LIKE A PRO
     Git & GitHub for C++ Students
     
     Author  : Avijit Roy
     Course  : CSCI 271 / CSCI 272 — John Jay College of Criminal Justice
     Version : 1.0.0
     License : CC BY 4.0
     
     Reading time: ~90 minutes
     ============================================================ -->

# Saving Your Work Like a Pro
## Git & GitHub for C++ Students

**A Complete, Analogy-Driven Guide to Version Control**

---

*By Avijit Roy*<br>
*Substitute Lecturer, Computer Science — John Jay College of Criminal Justice, CUNY*<br>
*Adjunct Assistant Professor — Collins College of Professional Studies, St. John's University*<br>
*CSCI 271 / CSCI 272*

---

> "The best time to learn version control was before your first assignment.  
> The second best time is right now."

---

## About This Book

This guide is written for you — the student sitting in your first or second semester of CS, staring at a C++ file that used to work and now doesn't, with no idea what you changed or how to get back to where things were okay.

Every concept here is explained through analogy before it's explained through commands. You'll see real C++ code, real terminal sessions, and real workflows — not abstract diagrams that make sense only after you already know the material.

By the end, you will understand:

- What version control actually *is* and why professionals cannot work without it
- The difference between Git (the tool) and GitHub (the platform) — a distinction most beginners confuse
- Every command you'll need for a full semester of coursework
- How to collaborate on group projects without overwriting each other's code
- How to recover from mistakes — because mistakes are inevitable

**Prerequisites:** You know how to open a terminal, navigate directories with `cd` and `ls` (or `dir` on Windows), and you've written at least one C++ program.

---

## Table of Contents

1. [Why Version Control? The Problem It Solves](#chapter-1-why-version-control-the-problem-it-solves)
2. [The Time Machine Analogy — What Git Actually Does](#chapter-2-the-time-machine-analogy-what-git-actually-does)
3. [Git vs. GitHub — Two Different Things](#chapter-3-git-vs-github-two-different-things)
4. [Installing and Configuring Git](#chapter-4-installing-and-configuring-git)
5. [Your First Repository](#chapter-5-your-first-repository)
6. [The Three Zones — Working, Staging, History](#chapter-6-the-three-zones-working-staging-history)
7. [Making Commits — Saving Snapshots](#chapter-7-making-commits-saving-snapshots)
8. [Reading Your History](#chapter-8-reading-your-history)
9. [Going Back in Time — Undo and Restore](#chapter-9-going-back-in-time-undo-and-restore)
10. [Branches — Parallel Universes for Your Code](#chapter-10-branches-parallel-universes-for-your-code)
11. [GitHub — Taking Git Online](#chapter-11-github-taking-git-online)
12. [Cloning, Pushing, and Pulling](#chapter-12-cloning-pushing-and-pulling)
13. [Collaborating on Group Projects](#chapter-13-collaborating-on-group-projects)
14. [C++-Specific Patterns — What to Track and What to Ignore](#chapter-14-c-specific-patterns-what-to-track-and-what-to-ignore)
15. [When Things Go Wrong — Common Mistakes and Fixes](#chapter-15-when-things-go-wrong-common-mistakes-and-fixes)
16. [The Professional Workflow](#chapter-16-the-professional-workflow)
17. [Quick Reference — Every Command You Need](#chapter-17-quick-reference-every-command-you-need)

---

## Chapter 1: Why Version Control? The Problem It Solves

### The Midnight Disaster

It's 11:45 PM. Your C++ assignment is due at midnight. You've been working for four hours, and an hour ago, your program compiled perfectly and produced the right output for every test case.

Then you decided to make it "just a little cleaner." You reorganized a few functions, changed some variable names, maybe restructured a loop. Now `g++ main.cpp -o main` throws eleven errors, none of which make sense, and you have no idea what you actually changed in the last hour.

You hit Ctrl+Z. Again. Again. Your editor's undo history runs out. The code is still broken. You sit there wondering whether starting over is actually faster.

This scenario plays out for almost every programmer at least once. The ones who've learned from it don't let it happen again — because they use version control.

---

### What Version Control Actually Is

Version control is a system that records changes to files over time so that you can recall specific versions later. Think of it this way: your operating system's file system only knows about your files *right now*. Version control keeps a detailed journal of every meaningful state your files have ever been in.

More precisely, it tracks:
- **What** changed (which lines in which files)
- **When** it changed (exact timestamp)
- **Who** changed it (name and email)
- **Why** it changed (a message you write, called a *commit message*)

That last point matters more than people expect. Months from now, you might look at a change and genuinely not remember why you made it. The commit message is a note to your future self.

---

### The Filing Cabinet Analogy

Imagine you're working on a term paper and you're worried about losing your progress. A non-programmer's instinct is to do this:

```
term_paper.docx
term_paper_v2.docx
term_paper_FINAL.docx
term_paper_FINAL_actually.docx
term_paper_FINAL_v2_submitted.docx
```

Sound familiar? You've been doing version control manually — it's just *terrible* version control. You don't know what changed between versions without opening each one. You can't easily compare two versions. The filenames become increasingly desperate.

Version control automates this process and does it properly. Instead of saving five copies of your file with confusing names, you maintain one file and save *checkpoints* at meaningful moments. Each checkpoint has a clear label, a timestamp, and notes about what you did. You can return to any checkpoint instantly.

In the context of your C++ work, this looks like:

```
main.cpp    ← just one file, always
```

But inside your version control system, there's a hidden journal that reads:

```
Checkpoint 1 — "Initial skeleton, main() prints hello world"
Checkpoint 2 — "Add calculateGPA() function"
Checkpoint 3 — "Fix off-by-one error in GPA loop"
Checkpoint 4 — "Add input validation, handle negative credits"
```

At any moment, you can go back to Checkpoint 2 and see exactly what `main.cpp` looked like then.

---

### Why C++ Students Specifically Need This

C++ is unforgiving in ways that Python or JavaScript aren't. A missing semicolon, a pointer left dangling, a header file included in the wrong order — any of these can cascade into dozens of incomprehensible compiler errors. When you're debugging C++, you often need to *isolate* what changed and test whether that change introduced the bug.

Version control makes this trivial. You can:

- Compare the current (broken) file against the last (working) checkpoint line by line
- Revert to the working checkpoint in one command
- Create a separate copy to experiment with, without touching your working version
- Show your instructor exactly what your code looked like at every stage of development

Beyond debugging, version control is how *every* professional C++ codebase is managed — game engines, operating systems, compilers, embedded firmware. Learning it in your first semester means you're picking up a skill that will be immediately relevant in any technical role you pursue.

---

## Chapter 2: The Time Machine Analogy — What Git Actually Does

### Meet Git

**Git** is a free, open-source version control system. It was created in 2005 by Linus Torvalds — the same person who created Linux. He built it in about two weeks to manage the development of the Linux kernel, which is one of the largest and most complex software projects in the world. The fact that it's survived and become the universal standard says something about how well it was designed.

Git runs entirely on your computer. It's a command-line program — you interact with it by typing commands in your terminal, just like you use `g++` to compile your C++ code. It requires no internet connection. It costs nothing. It stores everything in a hidden folder called `.git` inside your project.

---

### The Time Machine

Here's the mental model that makes everything else click.

Git is a time machine for your code.

When you reach a meaningful point in your work — your function compiles, your tests pass, you've finished a logical chunk — you take a *snapshot*. Git saves a complete picture of every file in your project at that exact moment. This snapshot is called a **commit**.

Every commit has:

1. A unique fingerprint (a long hexadecimal ID like `3f4a1c2e8b...`) that identifies it forever
2. A pointer to the previous commit (so commits form a chain)
3. A timestamp
4. Your name and email
5. A message describing what this snapshot represents

The collection of all your commits — the full chain of snapshots — is your **repository** (or "repo"). The repository is stored inside the `.git` folder in your project directory.

---

### Snapshots, Not Differences

This is a subtlety worth understanding even though it won't affect how you use Git day to day.

Some older version control systems stored the *differences* between each version — "in version 3, line 12 changed from X to Y." Git does something different: it stores complete snapshots of your entire project at each commit. If a file didn't change between two commits, Git is smart enough to just reference the previous snapshot rather than duplicate it, so storage stays efficient.

What this means in practice: retrieving any historical version is fast, because Git doesn't have to reconstruct the file by replaying all the changes — it just loads the snapshot directly.

---

### The Photographer Analogy

Think of a photographer covering a sporting event. They don't film a continuous video — they take individual photographs at key moments. Each photo captures the complete scene at that instant: who's where, what the scoreboard says, how everyone is positioned.

When the game is over, the photographer has a collection of photographs that together tell the story of the game. They can go back to any moment, examine it in detail, compare two moments side by side, and understand exactly how things changed.

Your Git commits are those photographs. Each one is a complete, self-contained snapshot of your project. Your commit history is the photo album that tells the story of how your code evolved.

---

### What Git Tracks (and What It Doesn't)

Git tracks **text files** very well — source code, configuration files, documentation, anything written in plain text. It can detect changes down to individual characters.

Git also stores **binary files** (images, compiled executables, audio files), but it can't show you *what* changed between two binary versions — just that they're different. For this reason, there are conventions around which files to include in a Git repository and which to exclude. We'll cover this in detail in Chapter 14, specifically for C++ projects.

---

## Chapter 3: Git vs. GitHub — Two Different Things

This distinction trips up nearly every beginner, and the confusion is understandable — you'll often hear "push your code to GitHub" or "use Git" in the same breath, as if they're the same thing. They're not, and understanding the difference will save you from a lot of confusion.

---

### Git Is a Tool. GitHub Is a Service.

**Git** is a program installed on your computer. It lives in your terminal. It works without internet. It has nothing to do with any website.

**GitHub** is a website — `github.com`. It's a hosting platform that stores Git repositories in the cloud. When you "push" your code to GitHub, you're uploading a copy of your local Git repository to GitHub's servers.

The relationship is like this: Git is the filing system; GitHub is the filing cabinet stored in a cloud warehouse that other people can access.

---

### The Library Analogy

Imagine you're writing a book (your C++ project). 

**Git** is your personal notebook system — the way you organize your drafts, track your revisions, and maintain a history of everything you've written. It's physical, local, yours.

**GitHub** is the public library where you can submit a copy of your book so others can read it, where your study group can access it, and where a backup exists even if your notebook burns down.

You can write your book perfectly well without ever submitting it to the library. But submitting to the library makes your work accessible, shareable, and backed up. In a class with group projects, your teammates need the library.

---

### A Direct Comparison

| | Git | GitHub |
|---|---|---|
| **What it is** | Software on your machine | Website / cloud service |
| **Created by** | Linus Torvalds, 2005 | Tom Preston-Werner et al., 2008 |
| **Owned by** | Open source community | Microsoft (acquired 2018) |
| **Requires internet?** | No | Yes |
| **Requires an account?** | No | Yes (free) |
| **Main purpose** | Track changes locally | Host, share, collaborate |
| **Where data lives** | `.git` folder on your computer | GitHub's servers |
| **Can you use it alone?** | Yes, perfectly | No — GitHub hosts Git repos, so Git is required |
| **Alternatives** | (No real alternatives — Git dominates) | GitLab, Bitbucket, Gitea, Azure Repos |

---

### Why GitHub Specifically?

GitHub is the dominant platform because it has the largest community of developers. When you search for an open-source C++ library, the code almost certainly lives on GitHub. When you apply for a technical internship, you'll often be asked for your GitHub profile URL. When your instructor gives feedback on your assignments, they'll likely use GitHub's interface.

GitHub adds several features that go beyond simply hosting code:

**Pull Requests** are a formal way to propose changes and request review before merging them. In a group project, you wouldn't merge your teammates' code without checking it first. Pull requests are how you check it.

**Issues** are a built-in task tracker. You can file bug reports, feature requests, and discussion threads attached directly to the code.

**GitHub Actions** is an automation system. Every time you push code, it can automatically compile it, run your tests, check your formatting, and notify you if something breaks. This is how professional teams ensure code quality.

**GitHub Pages** hosts static websites directly from a repository. This book, in fact, can be served as a website using GitHub Pages.

---

### Other Platforms Worth Knowing

While GitHub is where you should start, you'll encounter others in your career:

**GitLab** is popular in enterprise environments and has stronger built-in CI/CD (automated testing and deployment) pipelines. Many companies self-host GitLab on their own servers.

**Bitbucket** integrates tightly with Jira (a project management tool made by Atlassian) and is common in companies that use that ecosystem.

**Gitea** is a lightweight, self-hosted option that teams run on their own infrastructure when they need full control over their data.

All of them use Git. The underlying version control is identical — only the web interface and collaboration features differ.

---

## Chapter 4: Installing and Configuring Git

### Installation

**macOS:** Git is often already installed. Open Terminal and type `git --version`. If it's not there, install the Xcode Command Line Tools:

```bash
xcode-select --install
```

Or install Git directly via Homebrew if you have it:

```bash
brew install git
```

**Windows:** Download the installer from [git-scm.com/downloads](https://git-scm.com/downloads). During installation, the defaults are fine for most students. This also installs **Git Bash**, a Unix-style terminal — use this instead of Command Prompt when running Git commands.

**Linux (Ubuntu/Debian):**

```bash
sudo apt update
sudo apt install git
```

**Verify your installation:**

```bash
git --version
# git version 2.44.0
```

Any version from 2.23 onward is fine for everything in this book.

---

### Configuration — The First Thing You Do

Before Git will let you make commits, it needs to know who you are. This information gets permanently attached to every commit you make, so it's traceable and accountable. Run these two commands once:

```bash
git config --global user.name "Your Full Name"
git config --global user.email "your.email@example.com"
```

Use your real name and your CUNY email address. The `--global` flag means this setting applies to every repository on your machine — you set it once and never again.

**Verify your configuration:**

```bash
git config --list
# user.name=Your Full Name
# user.email=your.email@example.com
```

---

### Setting Your Default Editor

When Git needs you to write something (like a detailed commit message), it opens a text editor. By default this is Vim, which has a notoriously steep learning curve — new users have gotten stuck in it. Set it to something more comfortable:

**VS Code:**
```bash
git config --global core.editor "code --wait"
```

**Nano (simple terminal editor):**
```bash
git config --global core.editor "nano"
```

---

### Setting the Default Branch Name

Modern Git uses `main` as the default branch name. Older installations default to `master`. Align yours:

```bash
git config --global init.defaultBranch main
```

This matters for consistency when you create new repositories and push them to GitHub, which also defaults to `main`.

---

### A Note on the Terminal

All Git commands are typed in your terminal. On macOS/Linux, this is Terminal or any shell (bash, zsh). On Windows, use **Git Bash** (installed with Git), not Command Prompt or PowerShell — Git Bash gives you a Unix-style environment that matches the examples in this book.

When you see lines starting with `$`, that's the terminal prompt. You type everything after it:

```bash
$ git status
```

Means: at your terminal prompt, type `git status` and press Enter. Don't type the `$`.

---

## Chapter 5: Your First Repository

### Creating a Project from Scratch

Let's create a real C++ project and track it with Git from the beginning.

```bash
# Create a project folder
mkdir csci271-project1
cd csci271-project1

# Initialize Git — this is what creates the .git folder
git init
```

You'll see something like:
```
Initialized empty Git repository in /Users/you/csci271-project1/.git/
```

That's it. Your project is now a Git repository. The `.git` folder contains the entire database of your project's history. You'll never need to touch it directly — Git manages it — but it's good to know it's there.

**Verify:**
```bash
ls -a
# .  ..  .git
```

The `-a` flag shows hidden files (ones starting with `.`). The `.git` folder is the only thing in your project right now.

---

### Your First C++ File

Create `main.cpp` in your project folder using VS Code or any editor:

```cpp
// main.cpp
// CSCI 271 — Project 1
// Author: Your Name

#include <iostream>

int main() {
    std::cout << "Hello, CSCI 271!" << std::endl;
    return 0;
}
```

Now check what Git sees:

```bash
git status
```

```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        main.cpp

nothing added to commit but untracked files present
```

Git is telling you: "I see a file called `main.cpp`, but I'm not tracking it yet. You haven't told me to include it." This is the *working directory* — your file exists, but Git doesn't have a record of it.

---

### The .gitignore File — What to Keep Out

Before making your first commit, create a `.gitignore` file. This tells Git which files to *never* track. For a C++ project, you never want to commit compiled binaries — they're generated files, they're large, and they vary by platform.

Create a file called `.gitignore` in your project root with these contents:

```gitignore
# Compiled output
*.o
*.out
*.exe
a.out
main

# IDE and editor files
.vscode/
.idea/
*.swp
*.swo
*~

# macOS junk
.DS_Store

# Windows junk
Thumbs.db
desktop.ini

# Build directories
build/
cmake-build-*/
```

Why does this matter? If you commit your compiled binary (e.g., the `main` executable), two things happen: the repository gets large unnecessarily, and Git can't meaningfully track what changed between two binary versions. Since the binary is always generated by compiling your `.cpp` files, there's no reason to store it — anyone with your source code can compile it themselves.

---

### Making Your First Commit

With `main.cpp` and `.gitignore` created, you're ready to make your first commit. This is a two-step process:

**Step 1: Stage the files** (tell Git which files to include in this commit)

```bash
git add main.cpp
git add .gitignore
```

Or, to add everything at once:

```bash
git add .
```

**Step 2: Commit** (create the snapshot with a description)

```bash
git commit -m "Initial commit: hello world C++ program with .gitignore"
```

Output:
```
[main (root-commit) a1b2c3d] Initial commit: hello world C++ program with .gitignore
 2 files changed, 20 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 main.cpp
```

Congratulations. You've just made your first Git commit. That `a1b2c3d` is the beginning of your commit's unique ID (the full ID is 40 characters; Git shows you the shortened version by default).

---

## Chapter 6: The Three Zones — Working, Staging, History

Understanding Git's three zones is the single most important thing in this book. Almost every beginner confusion — "why isn't my commit including my changes?", "why can't I switch branches?", "where did my file go?" — comes from not having a clear picture of these three zones.

---

### The Restaurant Kitchen Analogy

Imagine a restaurant kitchen.

The **dining room** is where guests place orders — this is your **working directory**. Things happen here. Changes are made. It's the live, messy environment where active work occurs.

The **pass** (the window between kitchen and dining room) is where dishes are placed before they go out — this is the **staging area**. Food doesn't go straight from the stove to the table. It gets inspected, plated, verified. The staging area is your inspection point.

The **ticket rail** (the record of every order that went out) is your **commit history**. Once an order goes out, it's recorded. You can always look at the record and see what was sent, when, and to whom.

---

### Zone 1: The Working Directory

This is simply the files you see when you open your project folder. It's where you edit code in your text editor or IDE. Changes here are **not tracked by Git yet** — they're just changes on your hard drive.

```bash
# You edit main.cpp, adding a new function
# Git sees this immediately
git status
```

```
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
        modified:   main.cpp
```

Git says the file is "modified" — it knows the file exists and is being tracked, and it can see that the content has changed since the last commit. But it hasn't saved anything yet.

---

### Zone 2: The Staging Area (Index)

The staging area is a preparation zone — a buffer between your edits and your permanent history. You move files from the working directory to the staging area using `git add`.

Why does this zone exist? Because you often make multiple related changes to several files but want to organize them into separate, logical commits. You might fix a bug in one file and add a new feature in another — two different commits, each telling a clear story.

```bash
# Stage main.cpp (move it to the staging area)
git add main.cpp

git status
```

```
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   main.cpp
```

The file is now "to be committed" — it's in the staging area, waiting for you to create the snapshot.

---

### Zone 3: The Commit History (Repository)

When you run `git commit`, Git takes everything in the staging area and permanently saves it as a new snapshot in the repository's history. This is the permanent record.

```bash
git commit -m "Add calculateGPA() function"
```

```
[main 7f3a2b1] Add calculateGPA() function
 1 file changed, 18 insertions(+), 1 deletion(-)
```

Once committed, this snapshot is immutable. The commit with ID `7f3a2b1` will always represent exactly what your files looked like at this moment. You can always return to it.

---

### Visualizing the Three Zones

```
┌─────────────────────┐   git add    ┌──────────────────┐   git commit  ┌──────────────────────┐
│   Working Directory │ ───────────▶ │   Staging Area   │ ────────────▶ │   Commit History     │
│                     │              │   (Index)        │               │   (Repository)       │
│  main.cpp  ← edit   │              │  main.cpp ✓      │               │  [a1c3d] Initial   │
│  utils.cpp ← edit   │              │                  │               │  [7f2b1] Add GPA   │
│  README.md          │              │                  │               │  [9d4c2] Fix bug   │
└─────────────────────┘              └──────────────────┘                └──────────────────────┘

      git restore <file>                git restore                      git checkout <id>
     ◀────────────────────              --staged <file>                    ◀──────────────────
                                       ◀──────────────────────
```

You can move files backward too:

- `git restore <file>` — discard changes in the working directory (dangerous: you lose your edits)
- `git restore --staged <file>` — move a file from staging back to working directory (safe: edits are kept)

---

### A Common Beginner Trap

Here is a scenario that confuses almost every new Git user at least once:

1. You edit `main.cpp`.
2. You run `git commit -m "My message"`.
3. Git says: `nothing to commit, working tree clean`.

What happened? You forgot `git add`. Your edited file is in the working directory. You didn't move it to the staging area. Git committed nothing because the staging area was empty.

The fix:
```bash
git add main.cpp
git commit -m "My message"
```

**Always check `git status` before committing.** It will tell you exactly what's staged, what's modified but not staged, and what's untracked.

---

## Chapter 7: Making Commits — Saving Snapshots

### The Commit Message — A Letter to Your Future Self

When you write `git commit -m "..."`, the message inside the quotes is permanent. It will appear in your history forever. It's the only way — six months from now — that you'll know why you made a particular change.

Bad commit messages are not just annoying; they're a liability. Consider these:

```
fix
asdf
stuff
work
finally
aaaaaa
```

These tell you absolutely nothing. Compare:

```
Fix off-by-one error in calculateGPA() when credit hours = 0
Add input validation for negative grade values in main()
Refactor parseInput() to use stringstream instead of scanf
```

These are commit messages that do actual work. They tell you what changed, where, and implicitly why.

---

### The Commit Message Convention

Professional developers follow a widely used convention:

**Use the imperative mood.** Write as if completing the sentence "If applied, this commit will..." So: "Add feature" not "Added feature." "Fix bug" not "Fixed bug."

**Keep the subject line under 72 characters.** This is a formatting convention from the days of email patches and is still respected because it keeps `git log` readable.

**For more detail, leave a blank line after the subject and add a body.** For a CS assignment, a one-line message is usually fine. For larger projects, a body adds context.

A detailed commit (using `git commit` without `-m`, which opens your editor):

```
Add GPA calculation with credit-hour weighting

The calculateGPA() function now accounts for courses with different
credit hours. Previously it treated all courses as equal weight,
which produced incorrect results for lab sections (1 credit) vs
lecture sections (3 credits).

Closes: #12
```

For homework, this level of detail is overkill. But understanding why it exists helps.

---

### How Often to Commit?

**Commit early, commit often.** This is not a phrase to take lightly.

A commit should represent one logical unit of work. Not a whole assignment — one meaningful step toward completing it. Here's what a realistic commit history for a CSCI 271 assignment might look like:

```
a1b2c3d  Initial project skeleton with main() and includes
7f3a2b1  Add struct definition for Student
9e5d4c2  Implement readStudentData() to parse input file
2c8a1f4  Add displayStudent() output function
b3f7e9d  Add calculateGPA() with credit-hour weighting
4d1a8c3  Fix: handle empty student name in input validation
e5b9f2a  Add error handling for missing input file
3c7d1a2  Final cleanup: remove debug cout statements
```

This is eight commits over the course of writing one assignment. Each commit is small enough to be easily understood, and together they tell the story of how the assignment was built.

**Why does this matter for you, specifically?**

1. If something breaks, you can pinpoint exactly which commit introduced the bug.
2. If you run out of time, you have a partially-complete, consistently-working version to submit rather than a broken mess.
3. Your instructor can see that you worked on it over several sessions, not in a panic the hour before the deadline.

---

### Building a C++ Program — Commit by Commit

Let's walk through a realistic example. You're building a student grade calculator in C++.

**Commit 1:** The skeleton

```cpp
// main.cpp
#include <iostream>
#include <string>
#include <vector>

int main() {
    // TODO: implement grade calculator
    std::cout << "Grade Calculator" << std::endl;
    return 0;
}
```

```bash
git add main.cpp
git commit -m "Add project skeleton with includes and empty main()"
```

**Commit 2:** Add the data structure

```cpp
// main.cpp
#include <iostream>
#include <string>
#include <vector>

struct Course {
    std::string name;
    double grade;   // 0.0 to 4.0
    int credits;
};

int main() {
    std::cout << "Grade Calculator" << std::endl;
    return 0;
}
```

```bash
git add main.cpp
git commit -m "Add Course struct with name, grade, and credits fields"
```

**Commit 3:** Implement the first function

```cpp
double calculateGPA(const std::vector<Course>& courses) {
    double totalPoints = 0.0;
    int totalCredits = 0;

    for (const auto& course : courses) {
        totalPoints += course.grade * course.credits;
        totalCredits += course.credits;
    }

    if (totalCredits == 0) return 0.0;
    return totalPoints / totalCredits;
}
```

```bash
git add main.cpp
git commit -m "Implement calculateGPA() with credit-hour weighting"
```

Notice: each commit is small, focused, and the program compiles correctly after each one (or at least doesn't get worse). This is the discipline that makes version control useful.

---

## Chapter 8: Reading Your History

### git log — The History Browser

```bash
git log
```

This shows every commit in your repository, most recent first:

```
commit 9e5d4c2f1a8b3d7e6f2c4a1b9e8d3c7a2f4b1e9  (HEAD -> main)
Author: Your Name <you@example.com>
Date:   Thu May 22 14:32:11 2026 -0400

    Implement calculateGPA() with credit-hour weighting

commit 7f3a2b1c8e9d4a5f2b6c3d1e7f4a8b2c9d3e4a5f
Author: Your Name <you@example.com>
Date:   Thu May 22 13:45:02 2026 -0400

    Add Course struct with name, grade, and credits fields

commit a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0
Author: Your Name <you@example.com>
Date:   Thu May 22 12:15:44 2026 -0400

    Add project skeleton with includes and empty main()
```

The full commit ID is that 40-character hexadecimal string. You rarely need the full thing — the first 7 characters usually uniquely identify a commit.

---

### The Compact View

For a project with many commits, the full log gets long. The one-line format is much more readable:

```bash
git log --oneline
```

```
9e5d4c2 (HEAD -> main) Implement calculateGPA() with credit-hour weighting
7f3a2b1 Add Course struct with name, grade, and credits fields
a1b2c3d Add project skeleton with includes and empty main()
```

This is usually the first thing you read when you return to a project after a few days away.

---

### HEAD — Where You Are Right Now

You'll see `HEAD` appear throughout Git's output. `HEAD` is simply a pointer to your current position in history. Normally, it points to the latest commit on your current branch. When you make a new commit, HEAD advances to point at it.

Think of `HEAD` like a bookmark. It says: "This is the page I'm currently reading." When you create new commits, the bookmark moves forward automatically.

---

### Viewing What Changed in a Commit

```bash
# See the changes introduced by the most recent commit
git show

# See the changes introduced by a specific commit
git show 7f3a2b1

# Compare your current files against the last commit (what you've changed but not yet staged)
git diff

# Compare the staging area against the last commit (what you've staged but not yet committed)
git diff --staged
```

The output of `git diff` uses a standard format: lines prefixed with `-` are removed, lines prefixed with `+` are added, and unchanged context lines have no prefix.

```diff
--- a/main.cpp
+++ b/main.cpp
@@ -8,6 +8,16 @@ struct Course {
     int credits;
 };
 
+double calculateGPA(const std::vector<Course>& courses) {
+    double totalPoints = 0.0;
+    int totalCredits = 0;
+
+    for (const auto& course : courses) {
+        totalPoints += course.grade * course.credits;
+        totalCredits += course.credits;
+    }
+
+    if (totalCredits == 0) return 0.0;
+    return totalPoints / totalCredits;
+}
+
 int main() {
```

Reading diffs is a skill. Practice it — being able to quickly read "what changed" is fundamental to debugging and code review.

---

## Chapter 9: Going Back in Time — Undo and Restore

One of Git's most valuable features is the ability to undo mistakes. There are several levels of "undo," and understanding which to use in which situation prevents data loss.

### Level 1: Discard Unsaved Changes (Most Dangerous)

You edited a file and realized the changes are wrong. You want the file to go back to exactly what it was at the last commit.

```bash
git restore main.cpp
```

**Warning:** This is permanent. Your unsaved edits are gone. Git doesn't keep a trash can for working directory changes — if you restore, the edits vanish. Only do this when you're certain you want to throw the changes away.

---

### Level 2: Unstage a File (Safe)

You ran `git add main.cpp` by mistake — maybe you wanted to commit two other files but not this one. Move it back to the working directory without losing your edits:

```bash
git restore --staged main.cpp
```

Your changes to `main.cpp` are still there in the working directory — you just took it out of the staging area.

---

### Level 3: Undo the Last Commit (Keeps Your Changes)

You made a commit and immediately realized the message was wrong, or you forgot to include a file. Undo the commit but keep all the changes in the staging area:

```bash
git reset --soft HEAD~1
```

`HEAD~1` means "one commit before HEAD." Your commit disappears from history, but your files are still staged and your code is intact. You can now fix whatever was wrong and commit again.

---

### Level 4: Undo the Last Commit (Moves Changes to Working Directory)

Same as above, but the files go back to the working directory instead of staying staged:

```bash
git reset HEAD~1
```

(Same as `git reset --mixed HEAD~1`, which is the default.)

---

### Level 5: View an Old Version Without Changing Anything

You want to see what your code looked like two commits ago — just to read it, not to change anything:

```bash
git checkout a1b2c3d
```

This puts you in a "detached HEAD" state — you're looking at a historical snapshot but not making any changes. To go back to your current state:

```bash
git switch main
```

---

### The Broken Code Emergency

This is the scenario that version control was made for. You've been editing for an hour, everything is broken, and you want to go back to the last working state:

```bash
# First, see what commit you want to go back to
git log --oneline

# Discard all changes since the last commit
git restore .
```

Or if you want to go back further — say, two commits:

```bash
git reset --hard HEAD~2
```

`--hard` is destructive: it discards both the commits and all file changes. Use it when you genuinely want to erase everything since that point. For anything important, make sure you have a backup first — or use `--soft` if you're uncertain.

---

## Chapter 10: Branches — Parallel Universes for Your Code

### The Parallel Universe Analogy

Imagine your C++ project is a universe. Right now, in the main timeline, you have a working grade calculator. Your professor announces extra credit for adding a graphical output.

You have two options:

1. Start editing your working program, hoping the graphical code doesn't break anything.
2. Create a **parallel universe** where you experiment with the graphical code. If it works, you merge it back into the main timeline. If it doesn't, you delete the parallel universe and the main timeline is completely unaffected.

Option 2 is branching.

A **branch** in Git is an independent line of development. You can create as many branches as you need, work on them independently, and merge them back together when you're ready. The `main` branch (your default) is just the first branch Git creates. It has no special properties beyond being the default.

---

### Why Branching Matters for Students

You might think: "I'm working alone on an assignment, why do I need branches?" Fair question. Here are situations where they save you:

**The experiment:** You want to try a completely different algorithm for a function — say, replacing bubble sort with quicksort. Make a branch, implement it, test it. If it's better, merge it. If it's worse, delete the branch. Your original code was never touched.

**The bug fix:** You're in the middle of adding a new feature when you notice a different bug. Create a branch from `main`, fix the bug, merge it back. Then return to your feature branch. The bug fix and the feature never interfere.

**Group projects:** Each teammate works on a separate branch. Code is merged together only after review. This prevents the most common group project disaster: two people editing the same file and overwriting each other's work.

---

### Creating and Switching Branches

```bash
# See all branches (the * marks the current one)
git branch
# * main

# Create a new branch
git branch feature/quicksort

# Switch to it
git switch feature/quicksort

# Or, do both in one command:
git switch -c feature/experimental-sort
```

After switching, any commits you make go onto this branch. Your `main` branch is untouched.

---

### A Real Example: Two Sorting Algorithms

Let's say your assignment requires sorting a list of students by GPA. You've implemented bubble sort. You want to try insertion sort and compare.

```bash
# You're on main, bubble sort is committed
git log --oneline
# a1b2c3d Implement bubble sort for student list
# 9e5d4c2 Add Student data structure

# Create a branch for insertion sort
git switch -c feature/insertion-sort

# Implement insertion sort in main.cpp
# ...

git add main.cpp
git commit -m "Replace bubble sort with insertion sort implementation"

# Now test both:
# On this branch: insertion sort
# Switch back to main for bubble sort
git switch main
# main.cpp still has bubble sort — the other branch is unaffected
```

---

### Merging

When your feature is ready and tested, you merge it back:

```bash
# Switch to the branch you want to merge INTO
git switch main

# Merge the feature branch
git merge feature/insertion-sort
```

```
Updating a1b2c3d..3b5f7e9
Fast-forward
 main.cpp | 24 ++++++++++++++----------
 1 file changed, 14 insertions(+), 10 deletions(-)
```

**Fast-forward** means the merge was simple — `main` hadn't changed since you branched, so Git just moves the pointer forward. No merge commit needed.

---

### Merge Conflicts — When Two Timelines Collide

A **merge conflict** happens when two branches both changed the same lines of the same file in different ways. Git can't decide automatically which version to keep — it needs you to decide.

```bash
git merge feature/new-parser
# Auto-merging main.cpp
# CONFLICT (content): Merge conflict in main.cpp
# Automatic merge failed; fix conflicts and then commit the result.
```

Open `main.cpp`. Git has marked the conflict:

```cpp
<<<<<<< HEAD
// This is the version from your main branch
void parseInput(std::string filename) {
    // original implementation using fstream
=======
// This is the version from feature/new-parser
void parseInput(std::string filename) {
    // new implementation using stringstream
>>>>>>> feature/new-parser
```

You manually edit the file to keep what you want (could be one version, the other, or a combination), then:

```bash
# Remove the conflict markers, save the file, then:
git add main.cpp
git commit -m "Merge feature/new-parser: use stringstream for input parsing"
```

Merge conflicts look scary the first time. They're actually straightforward once you understand what the markers mean — Git is just showing you the two competing versions and asking you to pick.

---

### Cleaning Up Branches

After merging, delete the branch to keep your repo tidy:

```bash
git branch -d feature/insertion-sort
# Deleted branch feature/insertion-sort (was 3b5f7e9).
```

`-d` (lowercase) is the safe delete — it refuses to delete a branch if it hasn't been merged. Use `-D` (uppercase) to force-delete an unmerged branch.

---

## Chapter 11: GitHub — Taking Git Online

### Creating a GitHub Account

Go to [github.com](https://github.com) and create a free account. Use your real name — this profile will be visible to future employers. If you're a student, go to [education.github.com](https://education.github.com) and verify your status to get the **GitHub Student Developer Pack**, which includes:

- GitHub Copilot (AI coding assistant) — free for students
- Private repositories (unlimited)
- Dozens of professional tools and services at no cost

---

### Creating a Repository on GitHub

1. Click the `+` icon in the top right → **New repository**
2. Name it (use the same name as your local folder, e.g., `csci271-project1`)
3. Leave it **Public** for class assignments (unless you have private repo access and prefer privacy)
4. **Do not** check "Add a README" — you already have files locally and this avoids a conflict
5. Click **Create repository**

GitHub will show you setup instructions. Since you already have a local repository, use the "push an existing repository" section.

---

### Connecting Your Local Repo to GitHub

After creating the GitHub repo:

```bash
# Add GitHub as the "remote" called "origin"
git remote add origin https://github.com/yourusername/csci271-project1.git

# Verify the remote was added
git remote -v
# origin  https://github.com/yourusername/csci271-project1.git (fetch)
# origin  https://github.com/yourusername/csci271-project1.git (push)

# Push your commits to GitHub
git push -u origin main
```

The `-u` flag sets the "upstream" — it tells Git that `origin/main` is the remote branch your local `main` should track. You only need `-u` the first time. After that, just `git push` is enough.

---

### Understanding "origin"

"origin" is just a name — a shorthand that refers to your GitHub remote URL. It's the default name Git uses, and you should stick with it. When you `git push origin main`, you're saying: "Push my local `main` branch to the remote named `origin`."

You can have multiple remotes with different names, but for most student work, you'll have exactly one remote called `origin`.

---

### Authentication — HTTPS vs. SSH

When you push for the first time, GitHub needs to verify that you're authorized to write to that repository. There are two methods:

**HTTPS with a Personal Access Token (PAT):** GitHub no longer accepts your account password over HTTPS. Instead, you create a token (Settings → Developer settings → Personal access tokens) and use it as your password when Git prompts you. GitHub's credential manager can cache this so you don't type it every push.

**SSH Keys (Recommended after initial setup):** You generate a cryptographic key pair — a private key that stays on your machine and a public key that you upload to GitHub. Once configured, you never type a password to push or pull. This is the setup professionals use.

Instructions for both: [docs.github.com/en/authentication](https://docs.github.com/en/authentication)

---

## Chapter 12: Cloning, Pushing, and Pulling

### Cloning — Getting a Repo onto Your Machine

If a repository already exists on GitHub (your own from another computer, a professor's starter code, or a teammate's fork), use `clone` to download it:

```bash
git clone https://github.com/username/repo-name.git
```

This does three things automatically:
1. Creates a folder named `repo-name` in your current directory
2. Downloads the entire repository history into it
3. Sets up `origin` to point back at the GitHub URL

After cloning, you have a complete, local copy of the repository. You can commit, create branches, and view history without any internet connection.

---

### Push and Pull — Staying Synchronized

**`git push`** uploads your local commits to GitHub:

```bash
git push origin main
```

After your first push with `-u`, you can shorten this to just `git push`.

**`git pull`** downloads commits from GitHub and applies them to your local branch:

```bash
git pull origin main
```

Think of push and pull like syncing a document with cloud storage, except Git tracks every change and can merge different versions intelligently.

**When do you pull?**

- When you work on multiple computers and need to sync
- When a teammate has pushed changes you need
- At the start of every work session on a shared project

**A safe habit:** Always pull before you push. This ensures you have the latest changes before adding yours. If you push when you're behind, GitHub will reject it:

```
! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/...'
hint: Updates were rejected because the remote contains work that you do not have locally.
```

The fix: `git pull` first, resolve any conflicts, then push.

---

### fetch vs. pull — The Subtle Difference

`git fetch` downloads changes from GitHub but doesn't apply them to your local branch. It updates your knowledge of what's on the remote without changing your files.

`git pull` is equivalent to `git fetch` + `git merge` — it downloads and immediately applies.

For most student workflows, `git pull` is what you want. `git fetch` is useful in team environments where you want to review changes before merging them.

---

## Chapter 13: Collaborating on Group Projects

### The Core Problem

Two people, working on the same codebase, simultaneously. This is simultaneously the most powerful and the most dangerous aspect of Git. Without discipline, two teammates can overwrite each other's work in minutes.

The solution is a workflow — a set of conventions that everyone on the team follows.

---

### The Feature Branch Workflow

This is the most widely used workflow for small teams and is what you'll use in a group programming assignment:

```
main branch  ─────────────────────────────────────────────────▶
                  ╲               ╱
                   ╲             ╱
                    ▶──────────▶           feature/teammate-a
                         ╲              ╱
                          ╲            ╱
                           ▶──────────▶  feature/teammate-b
```

**The rules:**
1. The `main` branch always contains working, tested code.
2. Nobody commits directly to `main`.
3. Every new feature or fix gets its own branch.
4. Branches are merged back to `main` through a **Pull Request** on GitHub.

---

### Step-by-Step: A Group Project Session

**Setup (everyone does this once):**

```bash
# One person creates the repo on GitHub and pushes initial code
# Everyone else clones it
git clone https://github.com/team/csci272-project.git
cd csci272-project
```

**Starting work:**

```bash
# Always pull first to get the latest changes
git pull origin main

# Create your branch (name it descriptively)
git switch -c feature/ali-input-parser
```

**Working:**

```bash
# Edit files, compile, test...
# Then commit your progress
git add parser.cpp parser.h
git commit -m "Implement CSV input parser for student records"
```

**Pushing your branch:**

```bash
git push origin feature/ali-input-parser
```

**Opening a Pull Request:**

Go to GitHub. You'll see a banner: "feature/ali-input-parser had recent pushes — compare and pull request." Click it. Write a description of what you did. Request a review from your teammate. They look at the changes, leave comments, and when everyone's satisfied, someone clicks **Merge pull request**.

**After the merge:**

```bash
# Everyone pulls the merged code
git pull origin main

# Delete the old branch locally
git branch -d feature/ali-input-parser
```

---

### The Golden Rules of Group Git

**Never force-push to main.** `git push --force` rewrites history on the remote. If your teammates have already pulled that history, their repositories are now out of sync in a way that's difficult to untangle. Force-push is sometimes necessary on feature branches you own alone — never on shared branches.

**Commit and push before going offline.** If you're working on a shared feature, your in-progress work on a pushed branch means your teammates can see your progress and won't duplicate it.

**Write useful commit messages.** Your teammates need to understand your changes. "fix" tells them nothing. "Fix null pointer in readStudent() when input file is empty" tells them exactly what you did and why.

**Pull before starting work, every time.** Every session starts with `git pull origin main`. This is not negotiable. You don't know what changed since you last worked.

---

### Handling the Conflict Your Teammate Caused

Suppose you and your teammate both edited the same section of `main.cpp`. You pull their changes, and:

```bash
git pull origin main
# CONFLICT (content): Merge conflict in main.cpp
```

Open the file. Find the conflict markers. Understand what each version does. The choices are:
1. Keep your version and delete theirs
2. Keep their version and delete yours
3. Combine both (often the right answer — each person's change might address a different concern)

After resolving:
```bash
git add main.cpp
git commit -m "Merge: resolve conflict in main(), keep both input validation approaches"
git push
```

Then tell your teammate what happened. Communication matters as much as the technical resolution.

---

## Chapter 14: C++-Specific Patterns — What to Track and What to Ignore

### The Compiled Binary Problem

C++ compilation produces files that should never be committed:

| File type | Extension(s) | Why exclude |
|---|---|---|
| Compiled binary | `a.out`, `main`, `*.exe` | Platform-specific, regenerated from source |
| Object files | `*.o`, `*.obj` | Intermediate build artifacts, large, binary |
| CMake cache | `CMakeCache.txt`, `cmake_build_*/` | Local configuration, regenerated on each machine |
| Makefile (generated) | `Makefile` (if auto-generated) | If using CMake — regenerated; if hand-written, commit it |
| Dependency files | `*.d` | Auto-generated by compiler, not source |

---

### The Complete C++ .gitignore

```gitignore
# ── Compiled output ───────────────────────────────
# Generic
*.o
*.a
*.so
*.so.*
*.dylib
*.dll
*.exe
*.out
a.out

# Named binaries (add your project names here)
main
grade_calculator
student_sorter

# ── Build systems ─────────────────────────────────
# CMake
CMakeCache.txt
CMakeFiles/
cmake_install.cmake
cmake_build_*/
build/
_build/
out/
install_manifest.txt

# Make
*.d

# Ninja
.ninja_deps
.ninja_log

# Autotools
Makefile.in
aclocal.m4
autom4te.cache/
configure
config.h.in

# ── IDE files ─────────────────────────────────────
# VS Code
.vscode/

# CLion / JetBrains
.idea/
*.iml
cmake-build-*/

# Visual Studio
*.vcxproj
*.vcxproj.filters
*.sln
x64/
Debug/
Release/

# Xcode
*.xcodeproj/
*.xcworkspace/
xcuserdata/

# ── Editor artifacts ──────────────────────────────
*.swp
*.swo
*~
\#*\#
.#*

# ── OS junk ───────────────────────────────────────
.DS_Store
.AppleDouble
.LSOverride
Thumbs.db
ehthumbs.db
desktop.ini

# ── Sanitizer / profiler output ───────────────────
*.profdata
*.profraw
*.gcda
*.gcno
gmon.out
callgrind.out.*
massif.out.*

# ── Testing ───────────────────────────────────────
Testing/
CTestTestfile.cmake
test_output/
```

Save this as `.gitignore` in your project root and commit it in your first commit. Once it's there, Git will silently ignore every matching file.

---

### What to Definitely Commit

- All `.cpp` and `.h` files you write by hand
- `CMakeLists.txt` or `Makefile` (if you wrote it, not auto-generated)
- `.gitignore`
- `README.md` — always write one
- Test files (`.cpp` test cases)
- Any data files your program needs as input (if they're small text files)

---

### Writing a README

Every repository deserves a README. It's the first thing anyone (your instructor, a future employer, you returning after three months) will read.

A minimal `README.md` for a student project:

````markdown
# CSCI 271 — Project 1: Grade Calculator

**Author:** Your Name  
**Course:** CSCI 271, Fall 2026  
**Instructor:** Prof. Roy

## Description

A C++ program that calculates a student's GPA given a list of courses,
grades, and credit hours. Accounts for credit-hour weighting.

## Compilation

```bash
g++ -std=c++17 -Wall main.cpp -o grade_calculator
```

## Usage

```bash
./grade_calculator input.txt
```

Input format: one course per line — `Course Name,Grade,Credits`

```
Mathematics,3.7,3
English Composition,4.0,3
Physics Lab,3.3,1
```

## Files

- `main.cpp` — main program and entry point
- `student.h` — Student struct definition
- `parser.cpp` / `parser.h` — CSV input parser
- `input.txt` — sample input file
````

A README like this takes ten minutes to write and communicates professionalism immediately.

---

## Chapter 15: When Things Go Wrong — Common Mistakes and Fixes

This chapter is a reference. Bookmark it. You will return here.

---

### "I committed to main when I should have committed to a branch"

```bash
# Move the last commit to a new branch
git switch -c feature/oops-branch

# Reset main to before the commit
git switch main
git reset --hard HEAD~1

# Your commit now lives on feature/oops-branch
# main is back where it was
```

---

### "I committed the compiled binary by accident"

```bash
# Remove it from Git's tracking but keep the file on disk
git rm --cached main
git rm --cached "*.o"

# Commit the removal
git commit -m "Remove accidentally committed binary files"

# Add entries to .gitignore so it doesn't happen again
echo "main" >> .gitignore
git add .gitignore
git commit -m "Add main binary to .gitignore"
```

---

### "I pushed a file with a password or API key in it"

This is a serious situation. Once you push to a public repository, the credentials are compromised — GitHub's search indexes quickly, and bots scan new public commits constantly.

**Immediate actions:**
1. Revoke the credential immediately (change the password, rotate the API key) — even before you fix the Git history.
2. Remove the sensitive file from Git history using `git filter-repo` (preferred over older `git filter-branch`).
3. Force-push the cleaned history.
4. Notify anyone who cloned the repo.

For future prevention: use environment variables or a `.env` file listed in `.gitignore`. Never hardcode credentials in source files.

---

### "My push was rejected because I'm behind"

```bash
# error: failed to push some refs
# hint: Updates were rejected because the remote contains work that you do not have locally.

# Solution: pull first
git pull origin main

# Resolve any merge conflicts, then push
git push origin main
```

---

### "I accidentally deleted a file and committed the deletion"

```bash
# See the commit that had the file
git log --oneline --all -- deleted_file.cpp

# Restore it from that commit
git checkout <commit-id>~1 -- deleted_file.cpp

# The file is back in your working directory and staging area
git commit -m "Restore accidentally deleted deleted_file.cpp"
```

---

### "git merge failed and I just want to cancel"

```bash
# Abort the merge entirely, return to pre-merge state
git merge --abort
```

---

### "I have uncommitted changes but need to switch branches"

Git won't let you switch branches if you have uncommitted changes that would be overwritten. Two options:

```bash
# Option 1: Stash the changes (temporarily shelve them)
git stash
git switch other-branch
# ... do your work ...
git switch back-to-original-branch
git stash pop   # restore your shelved changes

# Option 2: Commit them (make a WIP commit)
git commit -am "WIP: in-progress changes, will amend later"
git switch other-branch
```

**Stash** is like putting your work in a drawer temporarily — it's there when you come back, but it's out of the way.

---

### "I want to completely reset my repo to match GitHub"

Use this when your local repo is in a confused state and you trust GitHub has the correct version:

```bash
git fetch origin
git reset --hard origin/main
```

**This discards all local commits and file changes not on GitHub.** Only do this if you're certain you want to abandon your local changes.

---

## Chapter 16: The Professional Workflow

### What Industry Actually Looks Like

When you graduate and start working in a technical role, the Git workflow you'll encounter is more structured than what you need for coursework — but it's built from the same fundamentals. Understanding it now means you won't feel lost when you encounter it.

---

### The GitHub Flow

GitHub Flow is the workflow used by most modern software teams. It's simple and effective:

1. **`main` always deploys.** Whatever is on `main` is assumed to be production-ready. You never push broken code to `main`.

2. **Create a branch for any change.** Feature, bug fix, documentation improvement — everything gets a branch.

3. **Open a Pull Request early.** Even before the feature is done. This signals to teammates what you're working on and invites early feedback.

4. **Review and discuss in the Pull Request.** Teammates comment on specific lines, suggest changes, ask questions. This is how knowledge spreads in a team.

5. **Merge only when the PR is approved and tests pass.** Most professional teams have automated tests that run every time you push — if any test fails, you can't merge.

6. **Delete the branch after merging.** Keep the repository clean.

---

### Semantic Versioning and Tags

When you release a version of software, you tag a commit to mark it:

```bash
git tag -a v1.0.0 -m "Version 1.0.0 - initial release"
git push origin v1.0.0
```

Version numbers follow **Semantic Versioning** (semver): `MAJOR.MINOR.PATCH`.
- Increment PATCH for bug fixes: `1.0.1`
- Increment MINOR for new features that don't break anything: `1.1.0`
- Increment MAJOR for changes that break backward compatibility: `2.0.0`

You won't use tags in coursework, but you'll use them professionally and you'll see them in every open-source project's release history.

---

### Writing Good Commit History — The Resume Argument

Your GitHub profile is increasingly part of your resume. When a recruiter or hiring manager looks at your profile, the first thing they see is your repository list and your commit history. A repository with commits like:

```
stuff
fix
more stuff
aaa
done
ok
```

...tells them something about how you work. A repository with commits like:

```
Implement Red-Black tree insertion with rotations
Add unit tests for boundary conditions in RB tree
Fix: handle parent NULL case in right-rotate operation  
Optimize memory allocation in NodePool using slab allocator
Add README with complexity analysis and usage examples
```

...tells a very different story. The commits don't need to be impressive — they need to be clear, honest, and consistent.

---

### The .github Folder

Many repositories have a `.github` folder with files that configure GitHub-specific features:

```
.github/
├── PULL_REQUEST_TEMPLATE.md   ← Template that pre-fills every new PR description
├── ISSUE_TEMPLATE/
│   ├── bug_report.md          ← Template for bug reports
│   └── feature_request.md     ← Template for feature requests
└── workflows/
    └── build.yml              ← GitHub Actions workflow (auto-compile on push)
```

A simple GitHub Actions workflow that compiles your C++ code every time you push:

```yaml
# .github/workflows/build.yml
name: Build C++

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Compile
        run: g++ -std=c++17 -Wall -Wextra main.cpp -o main
      - name: Run basic test
        run: echo "Hello" | ./main
```

This is your first taste of CI/CD (Continuous Integration/Continuous Deployment) — automated validation that runs on every push. Once you set this up, you'll immediately know if your code compiles on a clean machine (not just yours).

---

## Chapter 17: Quick Reference — Every Command You Need

### Setup

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --global core.editor "code --wait"
```

### Starting a Repository

```bash
git init                                    # Initialize new repo in current folder
git clone <url>                             # Download repo from GitHub
git clone <url> my-folder-name             # Clone into a specific folder name
```

### Daily Workflow

```bash
git status                                  # Always start here
git diff                                    # What changed (not staged)
git diff --staged                           # What changed (staged)
git add <file>                              # Stage a specific file
git add .                                   # Stage all changed files
git commit -m "Your message"               # Commit staged changes
git push                                    # Push to GitHub (after first setup)
git push origin main                        # Explicit push
git pull                                    # Pull from GitHub
git pull origin main                        # Explicit pull
```

### History

```bash
git log                                     # Full history
git log --oneline                           # Compact history
git log --oneline --graph                   # History with branch visualization
git show <commit-id>                        # Details of a specific commit
git diff <commit-id>                        # Changes since a commit
git diff <id1> <id2>                        # Changes between two commits
```

### Undoing Things

```bash
git restore <file>                          # Discard working directory changes (irreversible)
git restore --staged <file>                 # Unstage a file (keeps changes)
git reset --soft HEAD~1                     # Undo last commit, keep changes staged
git reset HEAD~1                            # Undo last commit, move changes to working dir
git reset --hard HEAD~1                     # Undo last commit, discard changes (irreversible)
git revert <commit-id>                      # Create a new commit that undoes a past commit (safe)
```

### Branches

```bash
git branch                                  # List local branches
git branch -a                               # List all branches (including remote)
git branch feature/my-feature              # Create branch (don't switch)
git switch feature/my-feature              # Switch to branch
git switch -c feature/my-feature           # Create and switch in one step
git merge feature/my-feature               # Merge into current branch
git branch -d feature/my-feature           # Delete merged branch
git branch -D feature/my-feature           # Force-delete unmerged branch
git merge --abort                           # Cancel an in-progress merge
```

### Remote and GitHub

```bash
git remote -v                               # List configured remotes
git remote add origin <url>                 # Add GitHub remote
git push -u origin main                     # First push, sets upstream
git fetch origin                            # Download changes without applying
git pull origin main                        # Fetch and merge
```

### Useful Utilities

```bash
git stash                                   # Temporarily shelve changes
git stash pop                               # Restore shelved changes
git stash list                              # See all stashes
git rm --cached <file>                      # Stop tracking a file (keep on disk)
git tag -a v1.0.0 -m "message"             # Create an annotated tag
git blame <file>                            # See who wrote each line
git grep "search term"                      # Search through tracked files
```

---

## Closing Thoughts

Version control is not a feature you add to your workflow — it becomes the workflow. The commands in this book will feel mechanical at first. You'll check notes, look things up, occasionally get confused about whether you staged something or what HEAD means right now. That's expected. After a few weeks of consistent use, these commands become reflexes.

The habit that matters most, early on, is simply **committing frequently with meaningful messages**. Everything else — branches, pull requests, rebasing, tags — can wait until you have that habit locked in.

A repository with a clean, honest commit history is something to be proud of. It's a log of how you learned to think, how you approached a problem, where you got stuck, and how you got unstuck. That history is worth preserving.

---

## Appendix A: Glossary

**Branch** — An independent line of development; a movable pointer to a sequence of commits.

**Clone** — Download a complete copy of a remote repository to your local machine.

**Commit** — A permanent snapshot of your project at a point in time, stored in the repository.

**Conflict** — Occurs when two branches have changed the same lines in the same file and Git cannot automatically merge them.

**Fetch** — Download objects and references from a remote without merging.

**Fork** — A personal copy of someone else's repository on GitHub.

**HEAD** — A special pointer indicating your current position in the commit history.

**Index** — Another name for the staging area.

**Merge** — Combine the history of two branches into one.

**Origin** — The conventional name for your primary remote (usually GitHub).

**Pull** — Fetch from a remote and merge into the current branch.

**Pull Request (PR)** — A GitHub feature for proposing and reviewing changes before merging.

**Push** — Upload local commits to a remote repository.

**Rebase** — Move or combine commits onto a different base commit (advanced; avoid until comfortable with merge).

**Remote** — A version of your repository hosted somewhere other than your machine.

**Repository (Repo)** — The complete collection of files and the history of all changes to those files.

**Staging Area** — A zone between your working directory and the commit history where you prepare changes for committing.

**Stash** — Temporarily shelve uncommitted changes to work on something else.

**Tag** — A named pointer to a specific commit, typically used to mark release versions.

**Working Directory** — The files you actively edit; the non-`.git` contents of your project folder.

---

## Appendix B: Recommended Next Steps

After finishing this book and completing a semester of practice, these are the natural next steps:

**Learn interactive rebasing.** `git rebase -i` lets you rewrite your commit history — squash several commits into one, reorder them, or fix messages. Essential for keeping a clean PR history.

**Learn `git bisect`.** Binary search through your commit history to find exactly which commit introduced a bug. Invaluable for large projects.

**Set up SSH authentication.** Generate an SSH key pair and add the public key to GitHub. After this, you never type a password to push or pull.

**Explore GitHub Actions.** Write a workflow that automatically compiles and tests your C++ code on every push. This is the foundation of CI/CD and a skill employers look for.

**Read Pro Git.** Available free at [git-scm.com/book](https://git-scm.com/book). Chapters 1–3 cover everything in this book in more depth. Chapters 6–7 cover internals and advanced workflows.

---

## Appendix C: External Resources

| Resource | URL | What It Is |
|---|---|---|
| Official Git Documentation | [git-scm.com/doc](https://git-scm.com/doc) | Reference manual for every command |
| Pro Git Book (Free) | [git-scm.com/book](https://git-scm.com/book/en/v2) | The definitive Git textbook |
| GitHub Docs | [docs.github.com](https://docs.github.com) | GitHub-specific features and workflows |
| Learn Git Branching | [learngitbranching.js.org](https://learngitbranching.js.org) | Best interactive visual tutorial |
| GitHub Skills | [skills.github.com](https://skills.github.com) | Hands-on courses inside real repositories |
| Atlassian Git Tutorials | [atlassian.com/git/tutorials](https://www.atlassian.com/git/tutorials) | Excellent written tutorials |
| Git Cheat Sheet (PDF) | [education.github.com/git-cheat-sheet-education.pdf](https://education.github.com/git-cheat-sheet-education.pdf) | Printable quick reference |
| GitHub Student Pack | [education.github.com/pack](https://education.github.com/pack) | Free tools for verified students |
| Semantic Versioning | [semver.org](https://semver.org) | Version numbering convention |

---

*This book is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). You are free to share and adapt it with attribution.*

*Version 1.0.0 — May 2026*  
*Avijit Roy — John Jay College of Criminal Justice, CUNY*
