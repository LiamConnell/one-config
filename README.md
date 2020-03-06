# Config Object

## Use

Create a `.yaml` file in an appropriate place and add some parameters:
```yaml
# my_config.yaml
my:
  nested:
    - param1
    - param2
```
Then, at the entry-point(s) of your python package, initialize the `CONFIG` object with the path to the `.yaml` file:
```python
# run.py
from config import CONFIG
CONFIG.construct_config('path/to/my_config.yaml')
```
In any other module, you can import the `CONFIG` object and the parameters from the yaml file will be present.
```python
# my_module.py
from config import CONFIG
param1 = CONFIG.my.nested.param1
```
Notice how the nested parameters are accessed as nested attributes. 
 
## Motivation
It's common for ML projects to use a large configuration object with all parameters in one place. There are two broad requirements of a configuration object:
1. It should be able to easily represent the parameters of different runtime situations, such as `testing` and `production`.
2. It should be available for all modules 

In order to achieve the first requirement, the object should be somehow constructed (and done so only once in the codebase). 

In order to achieve the second requirement, we could have a `config.py` file with all configuration parameters as attributes. This could be imported into other modules and used ad hoc. 

However, in order to achieve *both requirements*, we would seemingly have to construct the config object once and inject the constructed `config` into all other objects in the codebase. This clutters the codebase. 

The `CONFIG` object in this module attempts to resolve this problem by using the (much ridiculed) singleton pattern. 

The `CONFIG` object is constructed *once and only once* by a method parametrized with the path to a yaml file. Once constructed, the object will contain all parameters *_even if imported by another module_*.

Although the code in `config.py` may be opaque to many readers (and others might disagree about how "pythonic" it is), its implementation should be straightforward and it should be very useful for maintaining clean code in any project.