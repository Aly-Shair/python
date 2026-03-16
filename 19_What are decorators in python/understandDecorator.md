Absolutely! Here's the **clean, well-formatted Markdown content** that you can copy and save as a `.md` file (e.g., `decorator_cache_explanation.md`):

---

````markdown
# Understanding Why `print(f"cache_value: {cache_value}")` Runs Only Once in a Python Decorator

## 📌 Objective

This document explains **why the line**:

```python
print(f"cache_value: {cache_value}")
````

runs **only once** even when the decorated function is called multiple times.

---

## 🧪 Code Example

```python
import time

def cache(func):
    cache_value = {}
    print(f"cache_value: {cache_value}")
    
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        
        result = func(*args)
        cache_value[args] = result
        return result

    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b

print(long_running_function(2, 3))
print(long_running_function(2, 3))
print(long_running_function(4, 3))
print(long_running_function(4, 3))
print(long_running_function(6, 3))
```

---

## ⚙️ Explanation

### 1. **Decorator Execution Time**

When Python sees the `@cache` decorator, it **calls the `cache()` function immediately**, at **definition time**, not at runtime.

This line:

```python
@cache
def long_running_function(a, b):
```

is equivalent to:

```python
long_running_function = cache(long_running_function)
```

So the `cache()` function is called **once**, and it returns the `wrapper` function which will handle actual calls.

---

### 2. **Why `print(f"cache_value: {cache_value}")` Runs Only Once**

The print statement is located **inside the `cache()` function**, but **outside** the `wrapper()` function.

That means it only executes **once** — when the decorator is evaluated and applied. It is not part of the logic that runs when you call `long_running_function(...)`.

---

### 3. **How to Print the Cache on Each Call**

If you want to observe the cache **every time the function is called**, move the `print()` line **inside** the `wrapper` function:

```python
def wrapper(*args):
    print(f"Current cache: {cache_value}")
    if args in cache_value:
        return cache_value[args]
    
    result = func(*args)
    cache_value[args] = result
    return result
```

This will show the cache on each invocation of the decorated function.

---

## ✅ Summary

* The line `print(f"cache_value: {cache_value}")` runs only **once**, because it’s part of the decorator setup, not the actual function logic.
* Decorators are evaluated at **function definition time**, not during function calls.
* To print the cache during each call, place the `print()` inside the `wrapper()` function.

---

```

You can save this as `decorator_cache_explanation.md` for easy reading in any Markdown viewer.
```
