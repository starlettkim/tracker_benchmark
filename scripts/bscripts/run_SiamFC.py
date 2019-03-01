from config import *
import subprocess

SIAMFC_PATH = '/Users/starlett/codes/repos/SiamFC-PyTorch'
SIAMFC_PATH = os.path.abspath(SIAMFC_PATH)

def run_SiamFC(seq, rp, bSaveImage):
    # Write config file
    tmp_config = os.path.join(SIAMFC_PATH, 'tmp_config.json')
    tmp_config_file = open(tmp_config, 'w')
    json.dump(seq, tmp_config_file, indent=2)
    tmp_config_file.close()

    # File to store result
    tmp_res = os.path.join(SIAMFC_PATH, 'tmp_res.json')

    # Run tracker
    os.chdir(os.path.join(SIAMFC_PATH, 'Tracking'))
    command = map(str, ['python', 'run_SiamFC.py', '-j', tmp_config, '-o', tmp_res])
    subprocess.call(command)

    os.chdir(SIAMFC_PATH)
    res = json.load(open(tmp_res, 'r'))

    # Collect garbage
    os.remove(tmp_config)
    os.remove(tmp_res)

    return res
