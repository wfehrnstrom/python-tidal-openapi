import subprocess

result = subprocess.run(["openapi-generator-cli", "generate",
                         "-g", "python",
                         "-i", "tidal-api-oas.json",
                         "-t", "./templates",
                         "--package-name", "tidal",
                         "--model-package", "models",
                         "--api-package", "api",
                         "--additional-properties=disallowAdditionalPropertiesIfNotPresent=false,useOneOfDiscriminatorLookup=true"])

if result.returncode == 0:
    print("OpenAPI Tidal Client Generation complete.")
else:
    print("OpenAPI Tidal Client Generation returned an error.")
    print(f"Exit Code: {result.returncode}")
    print(f"Client Generation Output: {result.stdout}")
    print(f"Std Error: {result.stderr}")