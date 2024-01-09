<br>Caching Algorithms

<br>Background Context
<br>In this project, you will learn about different caching algorithms.

<br>Resources
<br>Reading and Watching Materials:
<br>Cache replacement policies: FIFO
<br>Cache replacement policies: LIFO
<br>Cache replacement policies: LRU
<br>Cache replacement policies: MRU
<br>Cache replacement policies: LFU
Learning Objectives
<br>By the end of this project, you should be able to explain, without external help:

<br>General Concepts
<br>What a caching system is
<br>The meaning of FIFO, LIFO, LRU, MRU, LFU
<br>The purpose of a caching system
<br>The limitations of a caching system


<br>Requirements
<br>Python Scripts Compatible with Ubuntu 18.04 LTS using python3 (version 3.7)
<br>All files must end with a new line
<br>The first line of all files should be #!/usr/bin/env python3
<br>Must include a README.md file at the project's root
<br>Adhere to pycodestyle style (version 2.5)
<br>All files must be executable
<br>File length tested using wc
<br>Documentation required for all modules, classes, and functions
<br>Documentation must consist of sentences explaining the purpose of the module, class, or method
<br>More Information
<br>Parent Class BaseCaching
<br>All your classes must inherit from BaseCaching defined as follows:

<br>More Info
<br>Parent class BaseCaching
<br>All your classes must inherit from BaseCaching defined below:

$ cat base_caching.py
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
