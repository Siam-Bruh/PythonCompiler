import PythonCompiler

print("Functions in PythonCompiler:")
print(dir(PythonCompiler))

if hasattr(PythonCompiler, "main"):
    PythonCompiler.main()
elif hasattr(PythonCompiler, "start"):
    PythonCompiler.start()
else:
    print("No main/start function found.")
