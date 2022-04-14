"""Implementation of stream sampling using probabilities."""
import random

import stream_sampler


class SolutionThree(stream_sampler.StreamSampler):
    """Stream sampler without tags."""

    def __init__(self, k):
        """Initialize the stream sampler, setting k, the sample size."""
        self.current_sample = [None] * k
        self.k = k
        self.i = 1

    def update(self, x):
        """Inform the sampler of the next stream element."""
        i = self.i
        k = self.k
        if i <= k:
            self.current_sample[i - 1] = x
        elif random.random() * i < k:
            replace_idx = random.randrange(k)
            self.current_sample[replace_idx] = x
        self.i = i + 1

    def get_sample(self):
        """Ask the sampler for the sample."""
        if len(self.current_sample) < self.k:
            raise ValueError(
                (
                    "We were asked to sample {} numbers, but only given {} to"
                    "sample from."
                ).format(self.k, len(self.current_sample))
            )

        return self.current_sample


if __name__ == "__main__":
    stream_sampler.test_sampler(SolutionThree)
