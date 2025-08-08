# Commands to solve picoCTF 'Mob psycho' challenge:

## Search for hex strings 16+ characters long
```bash
find mobpsycho -type f -exec strings {} \; | grep -oE '[0-9a-fA-F]{16,}'
```
**here:**
* **`-type`** - this is a find option for filtering by object type. `f` - "file" (regular file); other options: `-type d` (directories), `-type l` (symbolic links)
* **`-exec`** - execute command for each found file. Everything between `-exec` and `\;` is the command that will be executed:
  ```bash
  -exec command arguments \;
  ```
* **`strings {}`** - here `{}` is a placeholder that find replaces with the full path to the found file. For example:
  ```bash
  # find finds: mobpsycho/classes.dex
  # command becomes: strings mobpsycho/classes.dex
  ```
* **`\;`** - escapes `;` from bash shell and ends the command for `-exec`
* **`grep -oE '[0-9a-fA-F]{16,}'`** - find hex strings 16+ characters, `-E` - extended regular expressions, `-o` - print only lines that match the regular expression

## with sorting
```bash
find mobpsycho -type f -exec strings {} \; | grep -oE '[0-9a-fA-F]{16,}' | sort -u
```
**here:**
* **`sort`** - sorts lines, A→Z, 1→9 by default
* **`-u --unique`** - removes duplicates

## Search and decode potential flag
```bash
find mobpsycho -type f -exec strings {} \; | grep -oE '[0-9a-fA-F]{50,}' | while read hex; do
    echo "Hex: $hex"
    echo "Decoded: $(echo $hex | xxd -r -p 2>/dev/null || echo 'decode failed')"
    echo "---"
done
```

## additional method for simultaneous search and decoding
```bash
find mobpsycho -type f -exec strings {} \; | grep -oE '[0-9a-fA-F]{60,}' | xargs -I {} sh -c 'echo "Hex: {}"; echo "Decoded: $(echo {} | xxd -r -p)"; echo "---"'
```
**here:**
* **`find`** → finds files
* **`strings`** → extracts text from files  
* **`grep`** → filters only hex strings
* **`xargs`** → receives hex strings and PASSES THEM to script (`sh -c` cannot directly receive data from pipe)
* **`{}`** - placeholder/container for hex string variable
* **`sh -c`** - starts the script
* **`xxd -r -p`** - takes hex values in pairs, converts to raw bytes and then presents as plain text

## Data flow diagram:
```
📁 files → 📄 text → 🔢 hex-strings → 💾 arguments → 🔤 decoded text
    ↓        ↓           ↓              ↓             ↓
   find    strings     grep          xargs        xxd -r -p
```
