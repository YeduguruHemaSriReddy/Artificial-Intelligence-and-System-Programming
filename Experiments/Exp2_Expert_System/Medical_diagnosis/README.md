# Medical Diagnosis Expert System

This Prolog-based expert system determines possible diseases based on a patient's symptoms.

## Facts
- `symptom(Person, Symptom)` defines which symptoms a person has.

## Rules
- `disease(Person, Disease)` deduces the disease based on symptoms.

## Sample Queries
```prolog
?- disease(john, Disease).
?- disease(mary, Disease).
?- disease(sam, Disease).
