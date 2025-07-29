% ---------- FACTS ----------
% Parent relationships
parent(john, mary).
parent(john, tom).
parent(susan, mary).
parent(susan, tom).
parent(mary, alice).
parent(mary, bob).
parent(paul, alice).
parent(paul, bob).
% Gender information
male(john).
male(tom).
male(bob).
male(paul).
female(susan).
female(mary).
female(alice).
% ---------- RULES ----------
% Rule: X is the mother of Y if X is a parent of Y and X is female.
mother(X, Y) :- parent(X, Y), female(X).
% Rule: X is the father of Y if X is a parent of Y and X is male.
father(X, Y) :- parent(X, Y), male(X).
% Rule: X and Y are siblings if they share a parent and are not the same person.
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
% Rule: X is a grandfather of Y if X is a parent of Z and Z is a parent of Y and X is
male.
grandfather(X, Y) :- parent(X, Z), parent(Z, Y), male(X).
% Rule: X is a grandmother of Y if X is a parent of Z and Z is a parent of Y and X is
female.
grandmother(X, Y) :- parent(X, Z), parent(Z, Y), female(X).
