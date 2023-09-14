# jidtidy
A *tidy* wrapper for [JIDT](https://github.com/jlizier/jidt) (Java Information Dynamics Toolbox) to streamline its use in Python.

This implementation is the first try and will have to be extended to support more calculators and more handy features. 

To use a calculator, you need to `activate` JIDT and then initialise it with a selection of estimator before you run it with data, e.g.:
```python
cal = ITCalculators()
cal.activate()
cal.te_init('Kraskov')
r = cal.te_calc(s, t) # just the result from source s to target t
r, pvalue, surrogate_dist = cal.te_calc(s, t, surrogates=100) # result, p-value, and surrogate distribution
```

Depends on `infodynamics.jar` file available from [JIDT GitHub](https://github.com/jlizier/jidt/wiki/Downloads)
