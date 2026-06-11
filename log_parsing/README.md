# Log Parsing

## Description

A Python script that reads log lines from stdin and computes running metrics.

## Input Format

```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

Lines that do not match this exact format are silently skipped.

## Output

Statistics are printed after every 10 valid lines and on keyboard interruption (CTRL+C):

```
File size: <total size>
<status code>: <count>
...
```

- **Total file size**: cumulative sum of all `<file size>` values seen so far.
- **Status codes** printed in ascending order: `200`, `301`, `400`, `401`, `403`, `404`, `405`, `500`. Codes with a count of zero are omitted.

## Usage

```bash
./0-generator.py | ./0-stats.py
```

## Files

| File | Description |
|------|-------------|
| `0-stats.py` | Main log parsing script |

## Requirements

- Python 3
- Reads from standard input
