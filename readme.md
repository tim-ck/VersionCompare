# VersionCompare

## Overview

`VersionCompare` is a Python script designed to compare two Java files, format them by removing comments and whitespace, and then generate a unified diff output. This tool is useful for identifying differences in code while ignoring formatting discrepancies.

## Features

- **Remove Comments**: Strips out both single-line (`//`) and multi-line (`/* ... */`) comments.
- **Normalize Whitespace**: Removes all whitespace to ensure that only meaningful differences are highlighted.
- **Insert Line Breaks**: Adds line breaks after specific characters (`;`, `{`, `}`) to improve readability.
- **Generate Diff**: Uses `difflib` to create a unified diff of the formatted files.

## Usage

1. **Prepare Your Files**: Place the Java files you want to compare in the appropriate directories (e.g., `Local` and `ShareDrive`).

2. **Run the Script**: Execute the script to compare the files.
    ```sh
    python versioncompare.py
    ```

3. **View the Output**: The differences will be saved in `output.txt`.

## Example

### Input Files

**Local/Test.java**
```java
public class Test {
    public static void main(String[] args) {//see how different in the format does not treat as a different?
        System.out.println("Hello, World!smallchange");
    }
}
```

**ShareDrive/Test.java**
```java
public class Test 
{
    public static void main(String[] args) 
    {
        //see how different in the format does not treat as a different?
        System.out.println(
            "Hello, World!");
    }
}
```

### Output

**output.txt**
```plaintext
--- Local/Test.java
+++ ShareDrive/Test.java
@@ -1,5 +1,5 @@
 publicclassTest{
 publicstaticvoidmain(String[]args){
-System.out.println("Hello,World!");
+System.out.println("Hello,World!smalltinychange");
 }
 }
```

## Requirements

- Python 3.x

## Installation

Clone the repository and navigate to the directory:
```sh
git clone https://github.com/yourusername/VersionCompare.git
cd VersionCompare
```

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

