import PythonCompiler

print("Available functions/objects in PythonCompiler:")
print(dir(PythonCompiler))

if hasattr(PythonCompiler, "main"):
    PythonCompiler.main()

elif hasattr(PythonCompiler, "start"):
    PythonCompiler.start()
