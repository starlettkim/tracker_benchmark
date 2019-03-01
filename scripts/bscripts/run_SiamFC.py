from config import *
import subprocess

SIAMFC_PATH = '/home/jihunkim/SiamFC-PyTorch'
SIAMFC_PATH = os.path.abspath(SIAMFC_PATH)

def run_SiamFC(seq, rp, bSaveImage):
    # Config
    seq_config = dict()
    seq_config['s_frames'] = seq.s_frames
    seq_config['init_rect'] = seq.init_rect

    # Write on config file
    tmp_config = os.path.join(SIAMFC_PATH, 'tmp_config.json')
    tmp_config_file = open(tmp_config, 'w')
    json.dump(seq_config, tmp_config_file, indent=2)
    tmp_config_file.close()

    # File to store result
    tmp_res = os.path.join(SIAMFC_PATH, 'tmp_res.json')

    # Run tracker
    curdir = os.path.abspath(os.getcwd())
    os.chdir(os.path.join(SIAMFC_PATH, 'Tracking'))
    command = map(str, ['python', 'run_SiamFC.py', '-j', tmp_config, '-o', tmp_res])
    subprocess.call(command)
    os.chdir(curdir)

    # Load results
    res = json.load(open(tmp_res, 'r'))

    # Collect garbage
    os.remove(tmp_config)

    return res
