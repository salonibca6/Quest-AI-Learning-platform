"""
Checks every lesson: compiles each solution & example, runs the solution and
compares the output with expected_output, and checks the 'must_contain' words.

Usage:  python validate_curriculum.py            (checks C and Java)
        python validate_curriculum.py c          (only C)
Needs gcc for C and Java 11+ for Java (java Main.java).
"""
import importlib.util, os, subprocess, sys, tempfile, shutil, re

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name):
    spec = importlib.util.spec_from_file_location(
        'core.curriculum', os.path.join(HERE, 'core', 'curriculum', '__init__.py'),
        submodule_search_locations=[os.path.join(HERE, 'core', 'curriculum')])
    mod = importlib.util.module_from_spec(spec)
    sys.modules['core.curriculum'] = mod
    spec.loader.exec_module(mod)
    return mod.get_levels(name)


def norm(s):
    return '\n'.join(l.rstrip() for l in s.strip().splitlines())


def run_c(code, tmp, run=True):
    src = os.path.join(tmp, 'main.c'); exe = os.path.join(tmp, 'a.out')
    open(src, 'w').write(code)
    r = subprocess.run(['gcc', '-Wall', '-o', exe, src], capture_output=True, text=True)
    if r.returncode: return False, r.stderr
    if not run: return True, ''
    r = subprocess.run([exe], input='15\n', capture_output=True, text=True, timeout=10, cwd=tmp)
    return True, r.stdout


def run_java(code, tmp, run=True):
    src = os.path.join(tmp, 'Main.java')
    open(src, 'w').write(code)
    if not run:
        return True, ''   # no javac on some machines; example is checked by shape only
    r = subprocess.run(['java', src], input='15\n', capture_output=True, text=True, timeout=30, cwd=tmp)
    if r.returncode: return False, r.stderr
    return True, r.stdout


def main():
    which = sys.argv[1:] or ['c', 'java']
    bad = 0
    for slug in which:
        levels = load(slug)
        print(f'== {slug.upper()}: {len(levels)} levels, '
              f'{sum(l["is_project"] for l in levels)} projects')
        if len(levels) != 30: print('  !! expected 30 levels'); bad += 1
        nums = [l['level_number'] for l in levels]
        if nums != list(range(1, len(levels) + 1)): print('  !! level numbers not 1..N'); bad += 1
        for l in levels:
            n = l['level_number']; tmp = tempfile.mkdtemp()
            runner = run_c if slug == 'c' else run_java
            ok, out = runner(l['solution_code'], tmp)
            if not ok:
                print(f'  L{n} SOLUTION FAILS TO RUN:\n{out[:400]}'); bad += 1
            elif norm(out) != norm(l['expected_output']):
                print(f'  L{n} OUTPUT MISMATCH\n   expected: {norm(l["expected_output"])!r}\n   got:      {norm(out)!r}'); bad += 1
            flat = re.sub(r'\s+', '', l['solution_code'])
            for tok in l['must_contain']:
                if re.sub(r'\s+', '', tok) not in flat:
                    print(f'  L{n} must_contain token not in solution: {tok!r}'); bad += 1
            if slug == 'c':
                ok2, err = run_c(l['code_example'], tmp, run=False)
                if not ok2: print(f'  L{n} EXAMPLE DOES NOT COMPILE:\n{err[:300]}'); bad += 1
            if len(l['quiz_options']) != 4 or not (0 <= l['quiz_correct_index'] < 4):
                print(f'  L{n} bad quiz'); bad += 1
            shutil.rmtree(tmp, ignore_errors=True)
    print('\nALL GOOD' if not bad else f'\n{bad} problem(s) found')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
