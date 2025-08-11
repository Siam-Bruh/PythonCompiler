import CpythonEncoder

print("Available functions/objects in CpythonEncoder:")
print(dir(CpythonEncoder))

if hasattr(CpythonEncoder, "main"):
    CpythonEncoder.main()
elif hasattr(CpythonEncoder, "start"):
    CpythonEncoder.start()
else:
    print("No main/start function found.")
