"""Implementation of stream sampling using tags and a heap."""
import random
import heapq

import stream_sampler


class SolutionTwo(stream_sampler.StreamSampler):
    """Stream sampler by storing tags in a heap."""

    def __init__(self, k):
        """Initialize the stream sampler, setting k, the sample size."""
        self.current_sample = []
        self.k = k

    def update(self, x):
        """Inform the sampler of the next stream element."""
        tag = random.random()
        if len(self.current_sample) < self.k:
            heapq.heappush(self.current_sample, (tag, x))
        elif tag > self.current_sample[0][0]:
            heapq.heapreplace(self.current_sample, (tag, x))

    def get_sample(self):
        """Ask the sampler for the sample."""
        if len(self.current_sample) < self.k:
            raise ValueError(
                (
                    "We were asked to sample {} numbers, but only given {} to"
                    "sample from."
                ).format(self.k, len(self.current_sample))
            )

        return [x for (tag, x) in self.current_sample]


if __name__ == "__main__":
    stream_sampler.test_sampler(SolutionTwo)
