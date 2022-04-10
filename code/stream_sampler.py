"""Abstract class for stream sampling."""
import abc
import random
from collections import Counter
import tracemalloc
import time


class StreamSampler(metaclass=abc.ABCMeta):
    """The stream sampler."""

    @abc.abstractmethod
    def __init__(self, k):
        """Initialize the stream sampler, setting k, the sample size."""
        pass

    @abc.abstractmethod
    def update(self, x):
        """Inform the sampler of the next stream element."""
        pass

    @abc.abstractmethod
    def get_sample(self):
        """Ask the sampler for the sample."""
        pass

    def sample_stream(self, stream):
        """Run the sampler on a stream and get a sample at the end."""
        for x in stream:
            self.update(x)

        return self.get_sample()


def test_sampler_stream(Sampler, stream_fn, k):
    """Test the sampler on the stream returned by stream_fn."""
    numbers = list(stream_fn())

    sample_counter = Counter({number: 0 for number in numbers})

    num_samples = 1000

    tracemalloc.start()
    start = time.time()

    for _ in range(num_samples):
        sampler = Sampler(k)
        sample = sampler.sample_stream(stream_fn())
        sample_counter += Counter(sample)

    snapshot = tracemalloc.take_snapshot()
    end = time.time()
    tracemalloc.stop()

    total_time = end - start
    total_mem = sum(stat.size for stat in snapshot.statistics("lineno"))

    return (k, numbers, num_samples, sample_counter, total_time, total_mem)


def print_trial_results(k, numbers, num_samples, sample_counter, total_time, total_mem):
    """Print out the results of a trial."""
    print("Sample:")
    scale = 200 / k / num_samples
    for number in set(numbers):
        num_pounds = int(sample_counter[number] * scale)
        pounds = "#" * num_pounds
        print("{:>2}: {}".format(number, pounds))

    print("Took {:.3f} seconds".format(total_time))
    print("Total allocated memory: {:.1f} MiB".format(total_mem / 1000))


def numbers_stream():
    """Emit a stream containing the first 10 numbers."""
    return (random.randrange(20) for _ in range(1_000))


def big_stream():
    """Emit a really long random stream."""
    return (i % 20 for i in range(10000))


def test_sampler_k(sampler, k):
    """Test a smapler on both streams."""
    for stream_name, stream in [("numbers", numbers_stream), ("big", big_stream)]:
        print("===Testing on {} stream===".format(stream_name))
        trial = test_sampler_stream(sampler, stream, k)
        print_trial_results(*trial)
        print()


def test_sampler(sampler):
    """Test a sampler on both streams at k=1 and k=5."""
    for k in [1, 5]:
        print("***Testing with k={}***".format(k))
        test_sampler_k(sampler, k)
        print()
