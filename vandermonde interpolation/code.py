# Интерполировать функцию методом Вандермонда.

import numpy
import matplotlib.pyplot as plot

Xs = numpy.array([2., 3., 4., 5., 6.])
Ys = numpy.array([2., 6., 5., 5., 6.])

V = numpy.vander(Xs, len(Xs))
policoefficients = numpy.linalg.solve(V, Ys)

samples = numpy.linspace(min(Xs), max(Xs))
something = numpy.polyval(policoefficients, samples)

plot.plot(samples, something, '-', Xs, Ys, 'ro')
plot.axis([min(samples)-0.1, max(samples)+0.1,
           min(samples)-0.1, max(samples)+0.1]);

plot.title('Vandermonde interpolation')
plot.ylabel('Y axis')
plot.xlabel('X axis')
plot.show()
