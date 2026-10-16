import re


def get_widget_groups(widget_file):
    group = None
    for line in widget_file:
        if line.startswith('WIDGET'):
            if group:
                yield group
            group = {}
        else:
            key, value = re.split(r'\s*=\s*', line)
            group[key] = value
    yield group


def main():
    with open('widgets.txt') as widget_file:
        for group in get_widget_groups(widget_file):
            print(group[4])


if __name__ == '__main__':
    main()
