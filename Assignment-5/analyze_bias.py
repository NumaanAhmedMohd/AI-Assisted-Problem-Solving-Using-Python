"""analyze_bias.py

Performs static checks on example loan approval implementations to flag
use of protected attributes (gender, name, ethnicity, marital status) in
decision logic. Runs basic dynamic checks by importing modules and
inspecting source when possible.
"""

import ast
import importlib.util
import os
import re
import sys

BASE = os.path.dirname(__file__)
FILES = [
    os.path.join(BASE, 'biased_loan.py'),
    os.path.join(BASE, 'neutral_loan.py'),
]

PROTECTED_TERMS = ['gender', 'sex', 'race', 'ethnicity', 'name', 'nationality', 'married']

def read(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception:
        return ''

def static_ast_checks(src):
    findings = []
    try:
        tree = ast.parse(src)
    except Exception as e:
        findings.append(f'AST parse error: {e}')
        return findings
    # Walk AST to find comparisons or dictionary key usages involving protected terms
    class Visitor(ast.NodeVisitor):
        def visit_Compare(self, node):
            # look for comparisons where left or comparators use subscript or attribute of protected terms
            for child in ast.walk(node):
                if isinstance(child, ast.Subscript):
                    if hasattr(child.value, 'id') and child.value.id in ('applicant',):
                        # check for string literal key
                        if isinstance(child.slice, ast.Index) and isinstance(child.slice.value, ast.Constant):
                            key = str(child.slice.value.value)
                            if key.lower() in PROTECTED_TERMS:
                                findings.append(f'Comparison uses protected key: {key}')
                if isinstance(child, ast.Attribute):
                    if child.attr.lower() in PROTECTED_TERMS:
                        findings.append(f'Attribute access uses protected term: {child.attr}')
            self.generic_visit(node)

        def visit_Subscript(self, node):
            # check dictionary style applicant['gender']
            if isinstance(node.value, ast.Name) and node.value.id == 'applicant':
                # get slice value
                sl = node.slice
                key = None
                if isinstance(sl, ast.Index):
                    v = sl.value
                    if isinstance(v, ast.Constant) and isinstance(v.value, str):
                        key = v.value
                if key and key.lower() in PROTECTED_TERMS:
                    findings.append(f"Subscript access to protected key: {key}")
            self.generic_visit(node)

        def visit_Call(self, node):
            # detect use of .get('gender') patterns: applicant.get('gender')
            if isinstance(node.func, ast.Attribute):
                if isinstance(node.func.value, ast.Name) and node.func.value.id == 'applicant':
                    if node.func.attr == 'get' and node.args:
                        a0 = node.args[0]
                        if isinstance(a0, ast.Constant) and isinstance(a0.value, str):
                            if a0.value.lower() in PROTECTED_TERMS:
                                findings.append(f"Uses applicant.get('{a0.value}') — protected key access")
            self.generic_visit(node)

    Visitor().visit(tree)
    # simple regex checks for direct string membership checks like "in ('john','jane')"
    if re.search(r"in\s*\([^)]+(john|jane|michael|robert|ali)", src, re.I):
        findings.append('Detected name-based heuristic (string membership checks)')
    return findings

def dynamic_checks(path):
    findings = []
    name = os.path.splitext(os.path.basename(path))[0]
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except Exception as e:
        findings.append(f'Import failed: {e}')
        return findings
    # Try to inspect approve_loan source if present
    if hasattr(mod, 'approve_loan'):
        import inspect
        src = inspect.getsource(mod.approve_loan)
        # simple heuristics similar to static
        for term in PROTECTED_TERMS:
            if re.search(rf"\b{term}\b", src, re.I):
                findings.append(f"approve_loan uses protected term '{term}' in source")
    return findings

def analyze():
    results = {}
    for p in FILES:
        src = read(p)
        stat = static_ast_checks(src)
        dyn = dynamic_checks(p)
        results[os.path.basename(p)] = {'static': stat, 'dynamic': dyn}
    return results

def report(results):
    print('\nBias analysis report:')
    for fname, res in results.items():
        print('\n- ' + fname)
        if not res['static'] and not res['dynamic']:
            print('  No protected-attribute usage detected.')
            continue
        for s in res['static']:
            print('  [STATIC] ' + s)
        for d in res['dynamic']:
            print('  [DYNAMIC] ' + d)

if __name__ == '__main__':
    results = analyze()
    report(results)
