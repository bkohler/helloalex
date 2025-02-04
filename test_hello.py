import subprocess

def test_hello():
    # Compile the C program
    compile_result = subprocess.run(['make'], capture_output=True, text=True)
    if compile_result.returncode != 0:
        print("Compilation failed")
        print(compile_result.stderr)
        return

    # Run the compiled program
    run_result = subprocess.run(['./hello'], capture_output=True, text=True)
    if run_result.returncode != 0:
        print("Execution failed")
        print(run_result.stderr)
        return

    # Check the output
    expected_output = "Hello Alex\n"
    if run_result.stdout == expected_output:
        print("Test passed: Output is correct")
    else:
        print("Test failed: Output is incorrect")
        print(f"Expected: {expected_output}")
        print(f"Got: {run_result.stdout}")

if __name__ == "__main__":
    test_hello()
