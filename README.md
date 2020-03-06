# Config Object

## Motivation
It's common for ML projects to use a large configuration object with all parameters in one place. There are two broad requirements of a configuration object:
1. It should be able to easily represent the parameters of different runtime situations, such as `testing` and `production`.
2. It should be available for all modules 

In order to achieve the first requirement, the object should be somehow constructed (and done so only once in the codebase). 

In order to achieve the second requirement, we could have a `config.py` file with all configuration parameters as attributes. This could be imported into other modules and used ad hoc. 

However, in order to achieve *both requirements*, we would seemingly have to construct the config object once and inject the constructed `config` into all other objects in the codebase. This clutters the codebase. 

The `one_config` module attempts to resolve this problem by using the singleton pattern.

A `one_config` object is constructed *once and only once* by a method parametrized with the path to a yaml file. Once constructed, the object will contain all parameters *_even if accessed by another module_*.

Although the code in `config.py` may be opaque to many readers (and others might disagree about how "pythonic" it is), its implementation should be straightforward and it should be very useful for maintaining clean code in any project.

## How to use it

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
import one_config
one_config.build_config().from_yaml('path/to/my_config.yaml')
```
In any other module, you can import the `CONFIG` object and the parameters from the yaml file will be present.
```python
# my_module.py
import one_config
CONFIG = one_config.get_config()
param1 = CONFIG.my.nested.param1
```
Notice how the nested parameters are accessed as nested attributes. 
 
### Named configs
It is also possible to name a config in order to have multiple config environments simultaneously:  

```python
# run.py
import one_config
one_config.build_config('private').from_yaml('private_env.yaml')
```
```python
# my_module.py
import one_config
PRIVATE_ENV = one_config.get_config('private')
key = PRIVATE_ENV.my.super.secret.key
```
 
## A note on the Singleton Pattern

The singleton pattern is one of the more controversial design patterns. It is often ridiculed and seen as the "bad" pattern of the Gang of Four. On stack oveflow, the consensus seems to be that the singleton is either an anti-pattern or is useless in a language like python. 
 
In its original form, the Singleton might be all of those things. However, if we expand our definition of singleton to include any object whose state will be the same everywhere in the entire code base, we notice that we encounter singletons all the time in python. A python module is a singleton. 

Our singleton is simply an extension of the typical module singeton that allows us to easily add attributes based on an external file. 