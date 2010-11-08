
import sys, os
from subprocess import check_call


def main():
    
    ROOT = '/'.join(os.path.abspath(__file__).split('/')[:-2])
    
    scriptCmd = sys.argv[1:]
    scriptCmd[0] = '%s/%s' % (ROOT, scriptCmd[0])
    scriptCmd = ['python'] + scriptCmd
    
    PYTHON_PATHS = [
        ROOT,
    ]
    
    cmd = ['env',
                'APP=%s' % os.environ['APP'],
                'PYTHONPATH=%s' % ':'.join(list(sys.path) + PYTHON_PATHS),
                'DJANGO_SETTINGS_MODULE=dev_deployment.settings',
                ] + scriptCmd
    
    check_call(cmd)


if __name__ == '__main__':
    main()
