# Commands to solve picoCTF 'Mob psycho' challenge

## Basic hex string search

### Find hex strings 16+ characters long
```bash
find mobpsycho -type f -exec strings {} \; | grep -oE '[0-9a-fA-F]{16,}'
```

**Explanation:**
- **`-type f`** - filter by file type (`f` = regular files, `d` = directories, `l` = symbolic links)
- **`-exec`** - execute command for each found file. Everything between `-exec` and `\;` is the command:
  ```bash
  -exec command arguments \;
  ```
- **`strings {}`** - `{}` is a placeholder that find replaces with the full path to found file:
  ```bash
  # find finds: mobpsycho/classes.dex
  # command becomes: strings mobpsycho/classes.dex
  ```
- **`\;`** - escapes `;` from bash shell and ends the `-exec` command
- **`grep -oE '[0-9a-fA-F]{16,}'`** - find hex strings 16+ characters:
  - `-E` - extended regular expressions
  - `-o` - print only matching strings

## With sorting and deduplication

```bash
find mobpsycho -type f -exec strings {} \; | grep -oE '[0-9a-fA-F]{16,}' | sort -u
```

**Additional options:**
- **`sort`** - sorts lines (A→Z, 1→9 by default)  
- **`-u` / `--unique`** - removes duplicates after sorting

## Search and decode potential flags

### Using while loop
```bash
find mobpsycho -type f -exec strings {} \; | grep -oE '[0-9a-fA-F]{50,}' | while read hex; do
    echo "Hex: $hex"
    echo "Decoded: $(echo $hex | xxd -r -p 2>/dev/null || echo 'decode failed')"
    echo "---"
done
```

### Using xargs (one-liner)
```bash
find mobpsycho -type f -exec strings {} \; | grep -oE '[0-9a-fA-F]{60,}' | xargs -I {} sh -c 'echo "Hex: {}"; echo "Decoded: $(echo {} | xxd -r -p)"; echo "---"'
```

## How the pipeline works

```
📁 files → 📄 text → 🔢 hex-strings → 💾 arguments → 🔤 decoded text
    ↓        ↓           ↓              ↓             ↓
   find    strings     grep          xargs        xxd -r -p
```

**Step by step:**
1. **`find`** → finds files
2. **`strings`** → extracts text from files  
3. **`grep`** → filters only hex strings
4. **`xargs`** → receives hex strings and PASSES THEM to script (`sh -c` cannot directly receive data from pipe)
5. **`{}`** - placeholder/container for hex string variable
6. **`sh -c`** - starts the script
7. **`xxd -r -p`** - takes hex values in pairs, converts to raw bytes and presents as plain text

## Tools explanation

### `xargs` purpose
- **Problem:** `sh -c` cannot directly receive pipe data
- **Solution:** `xargs` converts pipe input → command arguments
- **`-I {}`** - replacement string (placeholder that gets substituted)

### `xxd -r -p` decoding process
1. **Hex pairing:** `7069636f4354467b...` → `70 69 63 6f 43 54 46 7b...`
2. **Hex → Raw bytes:** `70` → byte 0x70, `69` → byte 0x69, etc.
3. **Raw bytes → Plain text:** `0x70` → ASCII 'p', `0x69` → ASCII 'i', etc.
4. **Result:** `picoCTF{...}`

## Quick reference

| Command | Purpose |
|---------|---------|
| `find -type f` | Find regular files |
| `strings` | Extract text from binary files |
| `grep -oE` | Filter with regex, output only matches |
| `sort -u` | Sort and remove duplicates |
| `xargs -I {}` | Convert pipe input to command arguments |
| `xxd -r -p` | Decode hex to text |

## Alternative approaches

### Simple hex search
```bash
find mobpsycho -name "*.dex" -exec strings {} \; | grep -i "picoCTF"
```

### Direct file analysis
```bash
strings mobpsycho/classes.dex | grep -oE '[0-9a-fA-F]{32,}'
```

### Using binwalk for file analysis  
```bash
binwalk mobpsycho/classes.dex
```

---

> 💡 **Tip:** APK files are just ZIP archives. You can `unzip` them to explore their contents!
