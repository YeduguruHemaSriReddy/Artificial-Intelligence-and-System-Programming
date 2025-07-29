# Animal Identification Expert System

This Prolog expert system identifies types of animals based on physical traits.

## Facts
- `has(Entity, Trait)` defines characteristics of entities.

## Rules
- `animal(Entity, Type)` classifies the animal based on its traits.

## Sample Queries
```prolog
?- animal(bat, Type).
?- animal(penguin, Type).