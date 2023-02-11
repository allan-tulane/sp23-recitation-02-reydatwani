"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
###


def simple_work_calc(n, a, b):
  if (n == 1):
    return n
  else:
    return a * simple_work_calc(n // b, a, b) + n


pass


def test_simple_work():
  """ done. """
  assert work_calc(10, 2, 2) == 36
  assert work_calc(20, 3, 2) == 230
  assert work_calc(30, 4, 2) == 650


def work_calc(n, a, b, f):
  if (n == 1):
    return n
  else:
    return n * work_calc(n // b, a, b, f) + f(n)


pass


def span_calc(n, a, b, f):
  """Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
  # TODO
  pass


def test_work():
  """ done. """
  assert work_calc(10, 2, 2, lambda n: 1) == 36
  assert work_calc(20, 1, 2, lambda n: n * n) == 760
  assert work_calc(30, 3, 2, lambda n: n) == 300


def compare_work(work_fn1,
                 work_fn2,
                 sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
  """
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
  result = []
  for n in input_sizes:
    # compute W(n) using current a, b, f
    result.append((n, work_fn1(n), work_fn2(n)))
  return result


def print_results(results):
  """ done """
  print(
    tabulate.tabulate(results,
                      headers=['n', 'W_1', 'W_2'],
                      floatfmt=".3f",
                      tablefmt="github"))


def test_compare_work():
  work_fn1 = 1
  work_fn2 = 1
  work_fn1 = lambda n: 2 * work_fn1(n // 2) + work_fn1(n)
  work_fn1 = lambda n: 2 * work_fn2(n // 2) + work_fn1(n * n)
  res = compare_work(work_fn1, work_fn2)
  print(res)


def test_compare_span():
  assert span_calc(10, 2, 2, lambda n: 1) == 15
  assert span_calc(20, 1, 2, lambda n: n * n) == 426
  assert span_calc(30, 3, 2, lambda n: n) == 60
