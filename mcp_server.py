import sys
import json
from client import ResolutionProver

prover = ResolutionProver()

def handle_call(name, arguments):
    if name == "prove":
        cls = [set(c) for c in arguments["clauses"]]
        return {"unsat_proved": prover.prove_unsat(cls)}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
