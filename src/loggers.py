import logging
import os
from datetime import datetime
# imort module /packages
log_file = f"{datetime.now().strftime('%d_%m_%y_%H_%M_%S')}" # creating file name structure
log_path = os.path.join(os.getcwd(),"logs",log_file) # creating path of the file
os.makedirs(log_path, exist_ok=True) # creating directory at specified path
# exist_ok=True replicates another feature of mkdir -p , where the command does nothing and does not raise an error if the directory already exists.
log_file_path = os.path.join(log_path,log_file) 
# creating complete file path

logging.basicConfig(
    filename = log_file_path,
    format = "%(lineno)s - %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
)
if __name__ == "__main__":
    logging.info("logging has started")
    # The functions debug(), info(), warning(), error() and critical() will call basicConfig() automatically if no handlers are defined for the root logger.