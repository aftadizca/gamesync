import tarfile
import os


def create_gzip(source, filename):
    with tarfile.open(filename + ".tar.gz", "w:gz") as tar:
        tar.add(source, arcname="")


def extract_gzip(target, filename):
    if not os.path.isdir(target):
        os.mkdir(target)
    with tarfile.open(filename + ".tar.gz") as tar:
        tar.extractall(target)


if __name__ == "__main__":
    source = "/mnt/c/ProgramData/Orbit/420/Player/"
    target = "/mnt/c/ProgramData/Orbit/420/Player2/"

    create_gzip(source, "Farcry4")