# Programming Languages are Syntax Sugar for State Machines

I found this blog post by Russ Cox preparing to introduce pull iterators into the go programming language
[Storing Data in Control Flow](https://research.swtch.com/pcdata).

The thesis is that every program written as a state machine can be better expressed in control flow.

He goes through a step by step transformation of a state machine (written in c) to a "idiomatic" c style control flow code.

While I don't agree that control flow is always better than an explicit state machine,
I found the article very thought provoking.

There is an isomorphism between programming languages and state machines.

> Unless you need to reify the application state, there's no strong reason to explicitly encode the program state as an automaton. In most cases, expressing control flow using structured programming (loops, conditionals) and functions is much clearer, and much easier to debug. In the context of parsers, this amounts to writing a recursive-descent parser instead of writing an LL(k) state transition table by hand. In concurrent programming, this amounts to writing code with async/await and letting the compiler transform it into a state machine, rather than writing an event loop by hand.

*Comment on an auto deleted stackexchange question*.

The hacker news thread on Russ' article was a good read,
in particular this comment [https://news.ycombinator.com/item?id=36687736](https://news.ycombinator.com/item?id=36687736)
> What's really unfortunate is that compilers already perform this "control flow -> state machine" transformation, but almost none of them expose it to the user for direct manipulation - instead, they tightly couple it to a bunch of unrelated abstractions like event loop runtimes, async executors, managed stacks, etc. I'd kill for a compiler that can properly:

What if we had a programming language where the fundamental building block and composable unit were state machines?
Syntax sugar could be layered on top.

The C programming language doesn't abstract out the underlying Von-Neumann Architecture, and most modern programming languages are just an artifact of c.
Haskell is one of the few languages that truly abstracts out Von-Neumann.
Maybe a state machine programming language could also properly abstract way Von-Neumann,
and be less of a toy language than Haskell is.

