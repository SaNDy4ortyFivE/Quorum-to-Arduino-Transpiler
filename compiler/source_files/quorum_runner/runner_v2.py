import subprocess, sys, asyncio, time
import fileHandler

def compile(user_file):
    led = "libs/LED.quorum"
    ired = "libs/IRED.quorum"
    usonic = "libs/USONIC.quorum"
    button = "libs/BUTTON.quorum"
    lmtemp = "libs/LMTEMP.quorum"
    error = []
    file_loc = "quorum_user_code/" + user_file
    try:
        ##compile
        print("compiling {}".format(user_file))
        start_time = time.perf_counter()
        cmd = "java -jar ../quorum/Quorum.jar" + \
         " -library ../quorum/Library" + \
         " -compile " + file_loc + \
         " " + led + " " + ired + " " + usonic + \
         " " + button + " " + lmtemp
        print(cmd)
        completed = subprocess.run(
            [cmd],
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except subprocess.CalledProcessError as err:
        print('ERROR:Cannot call subprocess....')
        print(err)
        error = [err]
    else:
        end_time = time.perf_counter()
        if completed.returncode == 0:
            print("process was called sucessfully and exited with return code 0....")
            ##get console output
            op = completed.stdout.decode("utf-8")
            ##print(op)
            lines = op.strip().split("\n")
            if lines[1] == "Build Successful":
                print("{} was compiled sucessfully...".format(user_file))
                ##compilation Successful
                error = ["Build Successful"]
                ##delete class files after sucessfull compilation
            else:
                print("{} has errors in it...".format(user_file))
                for line in lines[3:]:
                    skip = line.find("Line")
                    error.append(line[skip:])
            error.append("Compile time:{0:.5f} seconds...".format(end_time-start_time))
            ##clean files here
        else:
            ##system errors
            ##the process did not exit with status code 0
            print("Process exited with return code:{}...".format(completed.returncode))
            err = completed.stderr.decode("utf-8").split("\n")
            ##print("Error:")
            for e in err:
                if e.find("Traceback") != -1 or e.find("traceback") != -1:
                    break
                ##print(e)
                error.append(e)
    finally:
        '''for number, line in enumerate(error):
            print("{}:{}".format(number, line))'''
        print(error)
        return error


'''async def main():
    user_file = sys.argv[1]
    compile_result = await compile(user_file)

asyncio.run(main())'''
