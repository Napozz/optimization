from Resolution import Probleme
import sys, signal

def signal_handler(signum, frame):
    raise Exception("Timed out")

if __name__ == '__main__':
    if len(sys.argv)!=4:
        print("Usage : python3 main.py temps input.txt output.txt")
        sys.exit(0)
    time = sys.argv[1]
    instance = sys.argv[2]
    output = sys.argv[3]

    #signal.signal(signal.SIGALRM, signal_handler)
    #signal.alarm(time)

    try:
        probleme = Probleme()
    except:
        print("Time out")
    if not probleme.load(instance):
        print(f"Impossible de charger {instance}")
        sys.exit(0)
    print(probleme)
    with open(output, "w") as f:
        f.write(probleme)