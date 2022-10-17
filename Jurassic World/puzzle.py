from logic import *

ATruthoraptor = Symbol("A is a Truthoraptor")
ALieosaurus = Symbol("A is a Lieosaurus")

BTruthoraptor = Symbol("B is a Truthoraptor")
BLieosaurus = Symbol("B is a Lieosaurus")

CTruthoraptor = Symbol("C is a Truthoraptor")
CLieosaurus = Symbol("C is a Lieosaurus")

# Puzzle 0
# A says "I am both a Truthoraptor and a Lieosaurus."
knowledge0 = And(
    # TODO 
    Not(And(ATruthoraptor, ALieosaurus)), # cannot be Truthoraptor and Lieosaurus at the same time
    Or(ATruthoraptor, ALieosaurus), # Will be Truthoraptor or Lieosaurus

    # If ATruthoraptor is speaking then its both a Truthoraptor and a Lieosaurus
    Implication(ATruthoraptor, And(ATruthoraptor, ALieosaurus)), 
    # If ALieosaurus is speaking then its not both a Truthoraptor and a Lieosaurus
    Implication(ALieosaurus, Not(And(ATruthoraptor, ALieosaurus)))
)

# Puzzle 1
# A says "We are both Lieosauruss."
# B says nothing.

knowledge1 = And(
    # TODO
    Not(And(ATruthoraptor, ALieosaurus)), # cannot be Truthoraptor and Lieosaurus at the same time
    Or(ATruthoraptor, ALieosaurus), # Will be Truthoraptor or Lieosaurus
    Not(And(BTruthoraptor, BLieosaurus)), # cannot be Truthoraptor and Lieosaurus at the same time
    Or(BTruthoraptor, BLieosaurus), # Will be Truthoraptor or Lieosaurus

    # If ATruthoraptor speaks, then they are both ALieosaurus and BLieosaurus
    Implication(ATruthoraptor, And(ALieosaurus, BLieosaurus)), 
    # If ALieosaurus speaks, then they not both ALieosaurus and BLieosaurus
    Implication(ALieosaurus, Not(And(ALieosaurus, BLieosaurus)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # TODO
    Not(And(ATruthoraptor, ALieosaurus)), # cannot be ATruthoraptor and ALieosaurus at the same time
    Or(ATruthoraptor, ALieosaurus), # Will be ATruthoraptor or ALieosaurus
    Not(And(BTruthoraptor, BLieosaurus)), # cannot be BTruthoraptor and BLieosaurus at the same time
    Or(BTruthoraptor, BLieosaurus), # Will be BTruthoraptor or BLieosaurus


    # A is ATruthoraptor 
    Implication(ATruthoraptor, And(ATruthoraptor, BTruthoraptor)),

    # A is ALieosaurus
    Implication(ALieosaurus, Not(And(ALieosaurus, BLieosaurus))),

    # B is BTruthoraptor 
    Implication(BTruthoraptor, And(ALieosaurus, BTruthoraptor)),

    # B is BLieosaurus
    Implication(BLieosaurus, Not(And(ATruthoraptor,BLieosaurus)))
)

# Puzzle 3
# A says either "I am a Truthoraptor." or "I am a Lieosaurus.", but you don't know which.
# B says "A said 'I am a Lieosaurus'."
# B says "C is a Lieosaurus."
# C says "A is a Truthoraptor."
knowledge3 = And(
    # TODO
    Not(And(ATruthoraptor, ALieosaurus)), # cannot be ATruthoraptor and ALieosaurus at the same time
    Or(ATruthoraptor, ALieosaurus), # Will be ATruthoraptor or ALieosaurus
    Not(And(BTruthoraptor, BLieosaurus)), # cannot be BTruthoraptor and BLieosaurus at the same time
    Or(BTruthoraptor, BLieosaurus), # Will be BTruthoraptor or BLieosaurus
    Not(And(CTruthoraptor, CLieosaurus)), # cannot be CTruthoraptor and CLieosaurus at the same time
    Or(CTruthoraptor, CLieosaurus), # Will be CTruthoraptor or CLieosaurus

    # If ATruthorapoter speaks, then they are either a ATruthoraptor or ALieosaurus
    Implication(ATruthoraptor, Or(ATruthoraptor, ALieosaurus)),
    Implication(ALieosaurus, Not(Or(ATruthoraptor, ALieosaurus))),

    # If BTruthoraptor speaks, then a Truthoraptor and Lieosaurus says that it is a Lieosaurus
    Implication(BTruthoraptor, And(Implication(ATruthoraptor,ALieosaurus), Implication(ALieosaurus, Not(ALieosaurus)))),
    # Implication(BTruthoraptor, Implication(ALieosaurus, Not(ALieosaurus))),
    # If BLieosaurus speaks, then a Truthoraptor or Lieosaurus says that it is not a Lieosaurus
    # Implication(BLieosaurus, Not(Implication(ATruthoraptor, ALieosaurus))),
    Implication(BLieosaurus, Not(And(Implication(ATruthoraptor,ALieosaurus), Implication(ALieosaurus, Not(ALieosaurus))))),


    # If BTruthoraptor speaks, then it is a CLieosaurus
    Implication(BTruthoraptor, CLieosaurus),
     # If BLieosaurus speaks, then it is not a CLieosaurus
    Implication(BLieosaurus, Not(CLieosaurus)),

    # If CTruthoraptor speaks, then it is a ATruthoraptor
    Implication(CTruthoraptor, ATruthoraptor),
    # If CLieosaurus speaks, then it is not a ATruthoraptor
    Implication(CLieosaurus, Not(ATruthoraptor))
  
)


def main():
    symbols = [ATruthoraptor, ALieosaurus, BTruthoraptor, BLieosaurus, CTruthoraptor, CLieosaurus]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
