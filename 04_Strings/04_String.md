# Python Strings — Reference Guide

A complete cheat sheet for Python `str` — written for someone coming from Java/JavaScript.

---

## 1. Strings Are Immutable

Once created, a string can't be changed in place. Every "modifying" method returns a **new** string.

```python
s = "hello"
s[0] = "H"          # ❌ TypeError
s = "H" + s[1:]      # ✅ new string
```

---

## 2. Creating Strings

```python
s1 = 'single quotes'
s2 = "double quotes"        # no functional difference
s3 = '''triple
quotes'''                    # multi-line
s4 = str(42)                 # "42" — convert other types
```

Use `"..."` when the string contains `'` (e.g. `"don't"`), and vice versa, to avoid escaping.

---

## 3. Escape Characters & Raw Strings

```python
"line1\nline2"     # newline
"tab\there"          # tab
"back\\slash"        # literal backslash
"\u00e9"             # unicode: é
```

**Raw strings** turn off escape processing — use for regex & Windows paths:

```python
path = r"C:\Users\new_folder"
regex = r"\d+\.\d+"
```

---

## 4. Indexing & Slicing

Zero-indexed. Negative indices count from the end. Slicing never raises `IndexError`, even out of range.

```python
s = "Programming"

s[0]        # 'P'
s[-1]       # 'g'  (last char)

s[start:stop:step]

s[0:4]      # 'Prog'   (stop exclusive)
s[:4]       # 'Prog'   (start defaults to 0)
s[4:]       # 'ramming' (stop defaults to end)
s[-3:]      # 'ing'
s[::2]      # every 2nd char
s[::-1]     # reversed string — classic trick
```

---

## 5. Concatenation & Repetition

```python
"foo" + "bar"      # 'foobar'
"ab" * 3             # 'ababab'
"foo" "bar"          # 'foobar' — adjacent literals auto-concat
```

⚠️ **Don't build strings with `+` in a loop** — O(n²). Use `.join()` instead:

```python
# bad
result = ""
for word in words:
    result += word + " "

# good
result = " ".join(words)
```

---

## 6. String Formatting

### f-strings — default choice (3.6+)
```python
name, age = "MIIKE", 25
f"{name} is {age} years old"
f"{age * 2}"                 # expressions inline
f"{age:.2f}"                 # 2 decimal places
f"{name!r}"                  # repr(): 'MIIKE'
f"{price:,.2f}"               # 1,234.56
f"{value:>10}"                # right-align width 10
f"{value:<10}"                # left-align
f"{value:^10}"                # center
f"{num:08d}"                  # zero-padded: 00000042
f"{x = }"                      # debug shorthand (3.8+)
```

### `.format()` — older, still common
```python
"{} is {}".format(name, age)
"{0} is {1}, {0} again".format(name, age)   # positional reuse
"{n} is {a}".format(n=name, a=age)           # keyword
```

### `%` formatting — legacy, C-style
```python
"%s is %d years old" % (name, age)
```

---

## 7. Essential Methods

**Case**
```python
s.upper(); s.lower(); s.title(); s.capitalize(); s.swapcase()
```

**Whitespace**
```python
s.strip()          # trim both ends
s.lstrip(); s.rstrip()
s.strip("xy")        # strip specific chars
```

**Search & Check**
```python
s.find("py")         # index or -1 (never throws)
s.index("py")         # index or raises ValueError
s.count("a")
"py" in s              # prefer this for existence checks
s.startswith("Py"); s.endswith("on")
```

**Predicates**
```python
s.isdigit(); s.isalpha(); s.isalnum(); s.isspace(); s.isupper(); s.islower()
```

**Split & Join**
```python
"a,b,c".split(",")            # ['a', 'b', 'c']
"a  b   c".split()               # splits on any whitespace, drops empties
"a,b,c".rsplit(",", 1)         # ['a,b', 'c'] — from the right
"line1\nline2".splitlines()     # ['line1', 'line2']
",".join(["a", "b", "c"])       # 'a,b,c'
```

**Replace**
```python
s.replace("old", "new")
s.replace("old", "new", 1)      # only first occurrence
```

**Padding / Alignment**
```python
s.zfill(5)           # '00042'
s.ljust(10, "-")
s.rjust(10, "-")
s.center(10, "*")
```

---

## 8. Membership, Length, Iteration

```python
len(s)
"a" in "cat"          # True — substring check
for ch in "abc":       # strings are directly iterable
    print(ch)
list("abc")            # ['a', 'b', 'c']
```

---

## 9. Comparison

Lexicographic, like Java/JS:

```python
"apple" < "banana"     # True
"Apple" < "apple"       # True — uppercase has lower ASCII value
```

---

## 10. Multiline / Implicit Joining

```python
sql = (
    "SELECT * "
    "FROM users "
    "WHERE id = 1"
)   # implicit concatenation inside parens
```

---

## 11. Encoding

```python
s.encode("utf-8")        # str -> bytes
b = b"hello"
b.decode("utf-8")          # bytes -> str
```

Python 3 strings are Unicode by default — no `char` vs `String` split like Java, no surrogate-pair mess like JS.

---

## 12. Performance Notes

- Immutable strings → `+` in a loop is O(n²). Use `.join()`.
- `in` for substrings is O(n) but implemented in optimized C.
- f-strings compile to efficient bytecode — faster than `.format()` or `%` at runtime.

---

## 13. Handy One-Liners

```python
# Reverse a string
s[::-1]

# Palindrome check (case-insensitive)
s.lower() == s.lower()[::-1]

# Remove all vowels
"".join(c for c in s if c not in "aeiouAEIOU")

# Word frequency count
from collections import Counter
Counter("the cat sat on the mat".split())

# Multiline f-string template
name = "MIIKE"
msg = f"""
Hello {name},
Welcome!
"""

# Chained methods
"  Hello World  ".strip().lower().replace(" ", "_")   # 'hello_world'
```

---

## Quick Reference Table

| Task | Method |
|---|---|
| Change case | `.upper()`, `.lower()`, `.title()` |
| Trim whitespace | `.strip()`, `.lstrip()`, `.rstrip()` |
| Find substring | `.find()`, `.index()`, `in` |
| Split into list | `.split()`, `.rsplit()`, `.splitlines()` |
| Join list into string | `"sep".join(list)` |
| Replace text | `.replace(old, new)` |
| Check content type | `.isdigit()`, `.isalpha()`, `.isalnum()` |
| Pad / align | `.zfill()`, `.ljust()`, `.rjust()`, `.center()` |
| Reverse | `s[::-1]` |
| Format values into text | f-strings `f"{x}"` |