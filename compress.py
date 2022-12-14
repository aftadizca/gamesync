import tarfile
import os


def create_gzip(source, filename):
    with tarfile.open(filename + ".tar.gz", "w:gz") as tar:
        tar.add(source, arcname="")


def extract_gzip(target, filename):
    if not os.path.isdir(target):
        os.mkdir(target)
    with tarfile.open(filename + ".tar.gz") as tar:
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(tar, target)


if __name__ == "__main__":
    source = "/mnt/c/ProgramData/Orbit/420/Player/"
    target = "/mnt/c/ProgramData/Orbit/420/Player2/"

    create_gzip(source, "Farcry4")