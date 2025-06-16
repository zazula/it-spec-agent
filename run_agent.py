#!/usr/bin/env python3
"""
CLI entrypoint for the IT Spec Agent.
Usage:
  python run_agent.py [input_file] > output_file
  python run_agent.py -f json specs_req.md > specs.json
If no input_file is provided, reads from stdin.
"""
import sys
import argparse
import json
from agent.main import create_agent

def main():
    parser = argparse.ArgumentParser(
        description="Run the IT Spec Agent on a prompt or input file."
    )
    parser.add_argument(
        'input', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
        help='File containing the prompt (default: stdin)'
    )
    parser.add_argument(
        '-f', '--format', choices=['text', 'json'], default='text',
        help='Output format (text or json, default text)'
    )
    args = parser.parse_args()
    prompt = args.input.read()
    agent = create_agent()
    result = agent.run(prompt)
    if args.format == 'json':
        json.dump(result, sys.stdout, indent=2)
    else:
        # simple human-readable text
        out = []
        for name, content in result.items():
            out.append(f"## {name}\n{content}\n")
        sys.stdout.write("\n".join(out))

if __name__ == '__main__':  # pragma: no cover
    main()