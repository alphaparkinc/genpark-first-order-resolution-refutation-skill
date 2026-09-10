class ResolutionProver:
    """
    Propositional / Ground Resolution Refutation.
    Derives empty clause [] to prove unsatisfiability.
    """
    def resolve_clauses(self, c1, c2):
        resolvents = []
        for lit in c1:
            if -lit in c2:
                res = (set(c1) | set(c2)) - {lit, -lit}
                resolvents.append(tuple(sorted(res)))
        return resolvents

    def prove_unsat(self, clauses):
        clause_set = set(tuple(sorted(c)) for c in clauses)
        while True:
            new_clauses = set()
            c_list = list(clause_set)
            for i in range(len(c_list)):
                for j in range(i + 1, len(c_list)):
                    for r in self.resolve_clauses(c_list[i], c_list[j]):
                        if not r:
                            return True
                        if r not in clause_set:
                            new_clauses.add(r)
            if not new_clauses:
                return False
            clause_set.update(new_clauses)
