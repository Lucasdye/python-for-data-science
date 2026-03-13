#Template for testig 42 projects

#Every test has an expected output that follows those rules :
#1)No exception should be caught by the tester.
#2)All outputs should match the expected result.
#3)Norminette (flake8) shouldn't output anything.

#Here are the three possible evaluations outcomes:
#1) ✅: Succes, no crash expected output
#2)❌: Fail, output mismatch.
#3)❌⚠️: Fail, uncaught exception.

from __future__ import annotations  as annotations
import  os                          as os
import  json                        as json
import  contextlib                  as ctxlib
import  io                          as io
import  sys                         as sys
import traceback                    as tb

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = #os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))
CASE_PATH = os.path.join(CURRENT_DIR, "cases.json")
OUTPUT_PATH = os.path.join(CURRENT_DIR, "output.txt")
sys.path.insert(0, ROOT_DIR)
# add module/script/program as a module

def test_sain_args(data: json, output_file:TextIO):
    cases = data["sain_cases"]["args"]
    expected = data["sain_cases"]["expected_outputs"]

    output_file.write(f"{'=' * 15}SAIN CASES{'=' * 15}\n")
    for arg, exp in zip(cases, expected):
        caught_exception = None
        exception_msg = ""
        responsible_file = ""

        captured_output = io.StringIO()
        with ctxlib.redirect_stdout(captured_output):
            try:
                #func_to_test(arg[0], arg[1], ...)
                pass
            except Exception as e:
                caught_exception = e
                pass

        captured_str = str(captured_output.getvalue())
        if not caught_exception and captured_str.strip() == exp:
            result = "✅"
        elif not caught_exception:
            result = "❌"
        else:
            result = "❌⚠️"
            exception_msg = str(caught_exception)
            last_frame = tb.extract_tb(caught_exception.__traceback__)[-1]
            filename = str(last_frame.filename)
            responsible_file = filename[filename.rfind("/") + 1:]

        if result == "✅" or result == "❌":
            output_file.write(str(
                f"\tTESTED:" + f"{' ' * 26}" + f"{result}\n"
                f"{arg}" + "\n\n"
                f"\tOUTPUT:\n"
                f"{captured_str}\n\n"
                f"\tEXPECTED:"
                f"\n{exp}\n"
                f"{'-' * 39}" + "\n"))
        else:
            output_file.write(str(
                f"\tTESTED:" + f"{' ' * 26}" + f"{result}\n"
                f"{arg}" + "\n\n"
                f"\tOUTPUTS:\n"
                f"STDOUT: {captured_str}\nEXCEPTION:'{exception_msg}' from '{responsible_file}'\n"
                f"{'-' * 39}" + "\n"))
            output_file.flush()
    return


def test_faulty_args(data: json, output_file:TextIO):
    cases = data["faulty_cases"]["args"]
    output_file.write(f"{'=' * 15}FAULTY CASES{'=' * 15}\n")
    
    for arg in cases:
        caught_exception = None
        exception_msg = ""
        responsible_file = ""
        
        captured_output = io.StringIO()
        with ctxlib.redirect_stdout(captured_output):
            with ctxlib.redirect_stderr(sys.stdout):
                try:
                    #func_to_test(arg[0], arg[1], ...)
                    pass
                except Exception as e:
                    caught_exception = e
                    pass
            
            captured_str = str(captured_output.getvalue())
            if not caught_exception:
                result = "✅"
            else:
                result = "⚠️"
                exception_msg = str(caught_exception)
                last_frame = tb.extract_tb(caught_exception.__traceback__)[-1]
                filename = str(last_frame.filename)
                responsible_file = filename[filename.rfind("/") + 1:]
            output_file.write(str(
                f"\tTESTED:" + f"{' ' * 26}" + f"{result}\n"
                f"{arg}" + "\n\n"
                f"\tOUTPUTS:\n"
                f"STDOUT: {captured_str}\nEXCEPTION:'{exception_msg}' from '{responsible_file}'\n"
                f"{'-' * 39}" + "\n"))
            output_file.flush()
    return


def main():

    output_file = open(OUTPUT_PATH, "w")
    output_file.truncate(0)

    with open(CASE_PATH, "r") as f:
        data = json.load(f)

    test_sain_args(data=data, output_file=output_file)
    output_file = open(OUTPUT_PATH, "a")
    test_faulty_args(data=data, output_file=output_file)
    return

if __name__ == "__main__":
    main()