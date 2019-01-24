## 1. Task scheduling

You are given a collection of tasks numbered {0, . . . , N − 1}. Each
task t has an integral duration d t > 0. Each task t may depend on zero
or more tasks p ∈ P t ⊆ {0, . . . , N − 1}; each of these tasks must be
completed before task t begins.

#### Subproblems

1. Implement an algorithm that computes a feasible single-processor schedule:
   given N , {d t }, and {P t }, compute a feasible ordering of tasks (t 1 , .
   . . , t N ) with t i ∈ {0, . . . , N −1}. Determine the starting
   time for each task s t such that two consecutive tasks do not overlap, s t
   i+1 ≥ s t i + d t i .

1. Implement an algorithm that computes a feasible multi-processor schedule:
   given N , {d t }, {P t }, and the number of processors K, determine an
   assignment of tasks to processors A k = (t k,1 , . . . , t k,n k ), where n
   k is the number of tasks assigned to processor k, such that {A k } is a
   partition of {0, . . . , N − 1} (i.e., the A k are disjoint and their union
   forms the set of all tasks).  Determine the starting time s t for
   each task t; the starting times must be chosen such that two consecutive
   tasks on the same processor do not overlap, s t k,i+1 ≥ s t k,i + d t k,i
   for each k and i. You can assume that the results computed by one processor
   are immediately visible to all other processors, i.e., a shared memory
   architecture.

The primary criterion of evaluation is whether the returned schedule is
valid: each task is assigned to exactly one processor, the tasks
assigned to the same processor do not overlap, and the tasks obey the
dependencies: s t ≥ s p + d p for each t and p ∈ P t . The secondary
evaluation is the total duration of the schedule, s t N + d t N or max k
s t k,nk + d t k,nk for the first and the second version of the problem,
respectively.  We also evaluate the clarity and efficiency of the
code. For N = 1000 and K = 50, your program should run in under a
second.

#### Input / output format

Your program should read the problem specification from standard input
and write the solution to standard output. Please provide only one
program, covering both of the above subproblems.

**Input** consists of N + 1 lines. The first line consists of two
space-separated integers N and K.  Each of the following N lines
specifies the duration d t of task t (ordered sequentially) and its
dependencies P t as 1 + |P t | space-separated integers.

**Output** consists of K lines, specifying the tasks assigned to each
processor and their start times.  Each line specifies 2n k
space-separated integers t k,1 s t k,1 . . . t k,n k s t k,nk .
Alternatively, if the input problem is not feasible, the output consists
of a single line with string infeasible.

Please pay special attention to the format of the output (e.g., no
debugging information, no extra spaces at the end of the line,
no additional lines at the end). The correctness and the
optimality of your solution will be evaluated programmatically, and we
may reject solutions that do not conform to this specification. Use
stderr for any debugging output. You can assume that the input is valid.
