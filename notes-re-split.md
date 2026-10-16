# Python `re.split()` - Self Study Notes

## Learning Goal

By the end of these notes, you should be able to confidently answer:

- What does `re.split()` do?
- How is it different from `str.split()`?
- What do the parameters mean?
- When should I use it?
- Why do capturing groups behave differently?
- How can I mentally visualize what is happening?

---

# Function Signature

```python
re.split(pattern, string, maxsplit=0, flags=0)
```

---

# Core Idea

Think of `re.split()` as a pair of scissors.

It does **not** look for the text you want to keep.

Instead, it looks for the text that should act as a **cutting point**.

The regex pattern tells Python:

> "Whenever you find this pattern, cut the string here."

After all cuts are made, Python returns the remaining pieces.

---

# Visual Model

Suppose we have:

```python
import re

text = "apple12banana345orange"

re.split(r"\d+", text)
```

Pattern:

```python
\d+
```

Meaning:

```text
One or more digits
```

String:

```text
apple12banana345orange
     ^^      ^^^
      |        |
     cut      cut
```

Result:

```python
['apple', 'banana', 'orange']
```

Notice that the matched digits disappear.

Python returns only the pieces between the cuts.

---

# Relationship to str.split()

Before learning `re.split()`, remember ordinary splitting.

## Using str.split()

```python
text = "apple,banana,orange"

text.split(",")
```

Output:

```python
['apple', 'banana', 'orange']
```

The comma is the separator.

---

## Limitation of str.split()

Suppose the separators vary:

```python
apple,banana;orange
```

Now there are:

- commas
- semicolons

Using ordinary `split()` becomes awkward.

---

# Enter re.split()

```python
import re

text = "apple,banana;orange"

re.split(r"[,;]", text)
```

Output:

```python
['apple', 'banana', 'orange']
```

Pattern:

```python
[,;]
```

Meaning:

```text
Match either ',' or ';'
```

Visualization:

```text
apple , banana ; orange
      ↑        ↑
     cut      cut
```

---

# Understanding Each Parameter

## Parameter 1: pattern

The regex that specifies where to cut.

Example:

```python
re.split(r"\s+", "one   two    three")
```

Pattern:

```python
\s+
```

Meaning:

```text
One or more whitespace characters
```

Visualization:

```text
one   two    three
   ↑↑↑    ↑↑↑↑
    cut     cut
```

Result:

```python
['one', 'two', 'three']
```

---

## Parameter 2: string

The text to split.

Example:

```python
re.split(r"\s+", "one two three")
```

Here:

```python
pattern = r"\s+"
string = "one two three"
```

Python searches the string for matches and cuts wherever the pattern appears.

---

## Parameter 3: maxsplit

Controls how many cuts are allowed.

### Default

```python
re.split(r",", "a,b,c,d")
```

Output:

```python
['a', 'b', 'c', 'd']
```

Every possible cut is made.

---

### maxsplit=1

```python
re.split(r",", "a,b,c,d", maxsplit=1)
```

Output:

```python
['a', 'b,c,d']
```

Visualization:

```text
a,b,c,d
 ↑
cut only once
```

---

### maxsplit=2

```python
re.split(r",", "a,b,c,d", maxsplit=2)
```

Output:

```python
['a', 'b', 'c,d']
```

Visualization:

```text
a,b,c,d
 ↑ ↑
two cuts
```

After the allowed splits are used, Python stops cutting.

---

## Parameter 4: flags

Flags modify how pattern matching behaves.

A common example is:

```python
re.IGNORECASE
```

---

### Without IGNORECASE

```python
re.split(r"a", "A-b-a")
```

Output:

```python
['A-b-', '']
```

Only lowercase `a` is matched.

---

### With IGNORECASE

```python
re.split(r"a", "A-b-a", flags=re.IGNORECASE)
```

Output:

```python
['', '-b-', '']
```

Now both:

```text
A
a
```

are treated as matches.

---

# Common Real-World Examples

## Example 1: Multiple Separators

Input:

```python
text = "red,blue;green|yellow"
```

Split on:

- comma
- semicolon
- pipe

```python
re.split(r"[,;|]", text)
```

Output:

```python
['red', 'blue', 'green', 'yellow']
```

---

## Example 2: Multiple Spaces

Input:

```python
text = "Python     Java   C++"
```

Pattern:

```python
\s+
```

Meaning:

```text
One or more spaces/tabs/newlines
```

```python
re.split(r"\s+", text)
```

Output:

```python
['Python', 'Java', 'C++']
```

---

## Example 3: Split on Numbers

Input:

```python
text = "cat12dog34bird567fish"
```

```python
re.split(r"\d+", text)
```

Output:

```python
['cat', 'dog', 'bird', 'fish']
```

Numbers become the cutting points.

---

## Example 4: Splitting a Sentence Into Words

```python
text = "Hello, world! How are you?"
```

```python
re.split(r"[ ,!?]+", text)
```

Output:

```python
['Hello', 'world', 'How', 'are', 'you', '']
```

---

# Why Is There an Empty String?

A common beginner question:

```python
['Hello', 'world', 'How', 'are', 'you', '']
```

Why is there a final empty string?

Because the string ends with a matching separator.

Visualization:

```text
Hello, world! How are you?
                          ↑
                        cut
```

After the final cut, nothing remains.

Therefore Python returns:

```python
''
```

as the final piece.

---

# Important Rule: Matched Text Is Removed

Consider:

```python
re.split(r"\d+", "apple12banana345orange")
```

Matched text:

```text
12
345
```

These are removed.

Output:

```python
['apple', 'banana', 'orange']
```

This leads to a useful mental model:

> Find the matches, remove them, and keep everything between them.

---

# Capturing Groups Change the Behavior

This is one of the most important things beginners miss.

---

## Without Capturing Group

```python
re.split(r"[,;]", "a,b;c")
```

Output:

```python
['a', 'b', 'c']
```

Separators disappear.

---

## With Capturing Group

```python
re.split(r"([,;])", "a,b;c")
```

Output:

```python
['a', ',', 'b', ';', 'c']
```

Notice:

```python
','
';'
```

are now included.

---

# Why?

Because parentheses create a **capturing group**.

```python
([,;])
```

The parentheses tell Python:

> "Keep what was matched."

Visualization:

```text
a , b ; c
  ↑   ↑
keep these
```

Result:

```python
['a', ',', 'b', ';', 'c']
```

---

# Most Useful Mental Shortcut

Whenever you see:

```python
re.split(pattern, text)
```

Think:

```text
1. Find every regex match.
2. Treat each match as scissors.
3. Cut at each match.
4. Remove the matched text.
5. Return the remaining pieces.
```

---

# Comparing Important Regex Functions

## re.search()

Question:

```text
Does a match exist?
```

Example:

```python
re.search(r"\d+", "abc123")
```

Result:

```python
Match object
```

Returns the first match.

---

## re.findall()

Question:

```text
What was matched?
```

Example:

```python
re.findall(r"\d+", "abc123xyz45")
```

Output:

```python
['123', '45']
```

Returns the matches themselves.

---

## re.split()

Question:

```text
What exists between the matches?
```

Example:

```python
re.split(r"\d+", "abc123xyz45")
```

Output:

```python
['abc', 'xyz', '']
```

Returns the pieces between matches.

---

# Quick Cheat Sheet

## Split on comma

```python
re.split(r",", text)
```

---

## Split on comma or semicolon

```python
re.split(r"[,;]", text)
```

---

## Split on one or more spaces

```python
re.split(r"\s+", text)
```

---

## Split on numbers

```python
re.split(r"\d+", text)
```

---

## Limit to one split

```python
re.split(r",", text, maxsplit=1)
```

---

## Ignore case

```python
re.split(
    r"a",
    text,
    flags=re.IGNORECASE
)
```

---

## Keep separators in output

```python
re.split(r"([,;])", text)
```

---

# Final Intuition

Imagine a regex match is a pair of scissors:

```text
Text
 ↓
Find pattern
 ↓
Cut wherever pattern matches
 ↓
Throw away the matched separators
 ↓
Return all remaining pieces
```

One-sentence definition:

> `re.split()` finds every occurrence of a regex pattern, cuts the string at those locations, and returns the pieces between the cuts.
