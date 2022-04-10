"""Implementation of stream sampling by storing the entire stream."""
import random

import stream_sampler


class SolutionOne(stream_sampler.StreamSampler):
    """Stream sampler by storing the whole stream."""

    def __init__(self, k):
        """Initialize the stream sampler, setting k, the sample size."""
        self.memory = []
        self.k = k

    def update(self, x):
        """Inform the sampler of the next stream element."""
        self.memory.append(x)

    def get_sample(self):
        """Ask the sampler for the sample."""
        if len(self.memory) < self.k:
            raise ValueError(
                (
                    "We were asked to sample {} numbers, but only given {} to"
                    " sample from."
                ).format(self.k, len(self.memory))
            )

        sample = []
        for _ in range(self.k):
            n = len(self.memory)
            i = random.randrange(n)
            sample.append(self.memory[i])
        return sample


if __name__ == "__main__":
    stream_sampler.test_sampler(SolutionOne)
