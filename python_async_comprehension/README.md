# Python - Async Comprehension

This project contains tasks that demonstrate the use of async generators and async comprehensions in Python.

## Learning Objectives

- How to write an async generator
- How to use async comprehensions  
- How to type-annotate generators

## Tasks

### 0. Async Generator
Write a coroutine called `async_generator` that takes no arguments and yields random numbers.

### 1. Async Comprehensions  
Write a coroutine called `async_comprehension` that collects 10 random numbers using async comprehension.

### 2. Run time for four parallel comprehensions
Write a `measure_runtime` coroutine that measures the total runtime of executing `async_comprehension` four times in parallel.

## Requirements

- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9)
- All files should end with a new line
- First line of all files should be `#!/usr/bin/env python3`
- Code should use pycodestyle style (version 2.5.x)
- All modules and functions must have documentation
- All functions and coroutines must be type-annotated 