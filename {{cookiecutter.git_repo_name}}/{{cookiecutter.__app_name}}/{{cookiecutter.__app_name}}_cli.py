"""
CLI for {{cookiecutter.__app_name}}
"""
from argparse import ArgumentParser
import uvicorn


def cli() -> None:
    """Function to run the command line
    :rtype: None
    :returns: Nothing it is the CLI
    """
    arg_parser = ArgumentParser(description='{{cookiecutter.git_repo_name}}-cli')
    subparsers = arg_parser.add_subparsers(title='commands', description='Valid commands: a single command is required',
                                           help='CLI Help', dest='a single command please see the -h option')
    subparsers.required = True

    # This is the sub parser to print start
    arg_parser_start = subparsers.add_parser('start', help='Start FastAPI')
    arg_parser_start.set_defaults(which_sub='start')
    arg_parser_start.add_argument('-p', '--port', help='TCP Port')
    arg_parser_start.add_argument('-r', '--reload', action='store_true', help='Allow Auto Reload')

    args = arg_parser.parse_args()

    try:
        if args.which_sub == 'start':
            uvicorn.run('{{cookiecutter.__app_name}}:web_app', reload=args.reload,
                        host='0.0.0.0', port=int(args.port))

    except AttributeError as error:
        print(f'\n !!! {error} !!! \n')
        arg_parser.print_help()

    except FileNotFoundError as error:
        print(f'\n !!! {error} !!! \n')
        arg_parser.print_help()

    except FileExistsError as error:
        print(f'\n !!! {error} !!! \n')
        arg_parser.print_help()

    except Exception as error:  # pylint: disable=broad-exception-caught
        print(f'\n !!! {error} !!! \n')
        arg_parser.print_help()
