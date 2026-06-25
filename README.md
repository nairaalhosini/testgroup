# Sonar Duplication and Smells Demo

Repo intentionally designed for SonarQube experiments:

- Security target: 0 findings as much as possible; no obvious SQL injection, command execution, hardcoded secrets, unsafe deserialization, weak crypto, or path traversal patterns.
- Duplication target: very high, around 70%+ depending on SonarQube version/settings.
- Code Smells: intentionally many smells: long functions, repeated branches, too many parameters, unused variables, magic numbers, complex conditionals, commented-out code, duplicate literals, dead-looking helper code, excessive nesting, and poor naming.
- Includes `coverage.xml` with roughly 50% line-rate metadata.

Run locally:

```bash
sonar-scanner
```
