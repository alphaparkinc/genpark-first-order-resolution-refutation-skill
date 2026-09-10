from client import ResolutionProver

def main():
    print("=== Testing Resolution Refutation Automated Prover ===")
    prover = ResolutionProver()

    # KB: {p}, {not p or q}, {not q} -> Contradictory set
    kb = [{1}, {-1, 2}, {-2}]
    is_unsat = prover.prove_unsat(kb)

    print(f"Empty clause derived (Theorem proved via contradiction): {is_unsat}")
    assert is_unsat is True
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
