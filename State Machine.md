I want rust enums.

But I want to be able to transition between enum variants while still keeping the associated data of the other enum variants.

I want to be able to access this state when we switch back a particular variant.

How do you express this in haskell?

It's kind of like state where you can only access a particular portion of depending on the current enum variant.


- associated data that must be provided when transitioning to the enum variant
- associated data that is provided when transitioning away from the state
- associated data accessable to many states
