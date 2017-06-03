import sys

from themachine.core import publish

def main():
    """
    DEVELOPMENT SCRIPT
    Starts processing the github username given as the first argument
    (Publishes the username into the `github.start_user_process` topic.
    """

    publish('github.start_user_process', {
        'username': sys.argv[1]
    })

if __name__ == '__main__':
    main()
