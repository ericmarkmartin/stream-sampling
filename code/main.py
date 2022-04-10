import stream_sampler
from solution1 import SolutionOne
from solution2 import SolutionTwo
from solution3 import SolutionThree


if __name__ == "__main__":
    solutions = [SolutionOne, SolutionTwo, SolutionThree]
    solution_names = ["solution 1", "solution 2", "solution 3"]
    ks = [1, 5, 10, 20]
    times = []
    memory_usages = []

    for solution, solution_name in zip(solutions, solution_names):
        print("Using {}".format(solution_name))
        time_row = []
        memory_row = []
        for k in ks:
            print("Running on k={}".format(k))
            (*_, total_time, total_mem) = stream_sampler.test_sampler_stream(
                solution, stream_sampler.big_stream, k
            )

            time_row.append("{:.2f}s".format(total_time))
            memory_row.append("{:.1f} KiB".format(total_mem))

        times.append(time_row)
        memory_usages.append(memory_row)

    print("TIME")
    print("{:<15} {:<20} {:<20} {:<20} {:<20}".format("k", *ks))
    for solution_name, time_row in zip(solution_names, times):
        print("{:<15} {:<20} {:<20} {:<20} {:<20}".format(solution_name, *time_row))

    print("SPACE")
    print("{:<15} {:<20} {:<20} {:<20} {:<20}".format("k", *ks))
    for solution_name, space_row in zip(solution_names, memory_usages):
        print("{:<15} {:<20} {:<20} {:<20} {:<20}".format(solution_name, *space_row))
