# CZ Review

`CZ Review` is a decision-support skill inspired by the themes of *CZ_币安人生* and CZ's publicly observable decision style.

It is not a roleplay bot. It is a high-level judgment assistant with a CZ-like bias toward:

- user trust first
- downside awareness
- speed with control
- long-term compounding
- reducing unnecessary complexity

## What it does

For each decision, it follows one fixed flow:

1. Restate the decision
2. Identify the objective function
3. Break down key variables
4. Deliver a CZ-style judgment
5. Give next actions
6. Show what could invalidate the conclusion

Default output sections:

- `CZ Conclusion`
- `Why`
- `What to do now`
- `What would invalidate this`

## Best-fit scenarios

- founder / CEO decisions
- investing / trading judgments
- career opportunity choices
- major personal choices

## Boundary

This version is based on:

- the themes of the book
- public CZ-like patterns

It is not:

- a line-by-line reconstruction of the PDF
- a fake private-facts simulator
- a quote generator pretending to cite unverified book lines

## Install

```bash
mkdir -p .claude/skills
cp -R /path/to/cz-skill .claude/skills/cz-review
```

## Verify

```bash
python3 -m unittest discover -s tests -v
```
