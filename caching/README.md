Caching Algorithms

Background Context
In this project, you will learn about different caching algorithms.

Resources
Reading and Watching Materials:
Cache replacement policies: FIFO
Cache replacement policies: LIFO
Cache replacement policies: LRU
Cache replacement policies: MRU
Cache replacement policies: LFU
Learning Objectives
By the end of this project, you should be able to explain, without external help:

General Concepts
What a caching system is
The meaning of FIFO, LIFO, LRU, MRU, LFU
The purpose of a caching system
The limitations of a caching system
Requirements
Python Scripts
Compatible with Ubuntu 18.04 LTS using python3 (version 3.7)
All files must end with a new line
The first line of all files should be #!/usr/bin/env python3
Must include a README.md file at the project's root
Adhere to pycodestyle style (version 2.5)
All files must be executable
File length tested using wc
Documentation required for all modules, classes, and functions
Documentation must consist of sentences explaining the purpose of the module, class, or method
More Information
Parent Class BaseCaching
All your classes must inherit from BaseCaching defined as follows:

python
Copy code
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - data storage (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key """
        raise NotImplementedError("get must be implemented in your cache class")
