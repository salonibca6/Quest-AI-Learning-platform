"""
Curriculum data for the Quest learning platform.
30 levels for C and 30 levels for Java, written in simple words.
Levels marked project=True are Mini Projects (real small programs).
"""


def L(n, title, summary, diff, xp, concept, example, ctitle, cdesc, starter,
      expected, must, hint, solution, q, opts, ans, why, project=False):
    return {
        'level_number': n, 'title': title, 'summary': summary,
        'difficulty': diff, 'xp_reward': xp, 'is_project': project,
        'concept_content': concept.strip(), 'code_example': example.strip(),
        'challenge_title': ctitle, 'challenge_description': cdesc,
        'starter_code': starter.strip(), 'expected_output': expected.strip(),
        'must_contain': must, 'solution_hint': hint,
        'solution_code': solution.strip(),
        'quiz_question': q, 'quiz_options': opts,
        'quiz_correct_index': ans, 'quiz_explanation': why,
    }


def get_levels(slug):
    if slug == 'c':
        from .c_part1 import LEVELS as a
        from .c_part2 import LEVELS as b
    else:
        from .java_part1 import LEVELS as a
        from .java_part2 import LEVELS as b
    return a + b
