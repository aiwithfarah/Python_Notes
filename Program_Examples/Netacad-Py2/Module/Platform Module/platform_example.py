# you use Modules to write code, and you use Packages to organize those modules into a clean,
# navigable structure.

# lets you access the underlying platform's data, i.e., hardware, operating system, and interpreter version information.

from platform import machine, system, platform, processor, version, python_version, python_implementation

print(platform())  # Windows-10-10.0.19045-SP0
print(machine())  # AMD64
print(system())  # Windows
# Intel64 Family 6 Model 142 Stepping 10, GenuineIntel -->processor name
print(processor())
print(version())  # 10.0.19045 --> returns OS version
print(python_implementation())  # CPython
print(python_version())  # 3.13.1
