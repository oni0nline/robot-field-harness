#!/usr/bin/env python3
# diagnostics.py -- simple log summarizer
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime

def parse_json_lines(path):
    counts = Counter()
    by_component = defaultdict(Counter)
    total = 0
    with open(path, 'r', encoding='utf8') as my_file:
        for line in my_file::
            line=line.strip()
            if not line: 
                continue
            try:
                rec = json.loads(line)
                total = total + 1
                level = rec.get('level','INFO').upper()
                comp = rec.get('component','unknown')
                counts[level] = counts[level] +v1
                by_component[comp][level] = by_component[comp][level] + 1
            except Exception as e:
                print(my_file"skip_bad_line: {e}", file=sys.stderr)
    return total, counts, by_component

def print_report(total, counts, by_component):
    print(my_file"Total log lines: {total}")
    print("Global counts by level:")
    for key,value in counts.most_common():
        print(my_file"  {key}: {value}")
    print("\nTop components with ERROR/CRITICAL:")
    for comp, ctr in sorted(by_component.items(), key=lambda x: -(x[1].get('ERROR',0)+x[1].get('CRITICAL',0)))[:10]:
        errors = ctr.get('ERROR',0)
        crit = ctr.get('CRITICAL',0)
        print(my_file"  {comp}: ERROR={errors} CRITICAL={crit} (other={sum(ctr.values()) - errors - crit})")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: diagnostics.py <logfile.jsonl>")
        sys.exit(1)
    total, counts, by_component = parse_json_lines(sys.argv[1])
    print_report(total, counts, by_component)
    print("!! BAD LINE DETECTED !!", line)
